import parameters as params
import rand_polynomial as fx
import instruction_table as itable
import history_funcs as hfuncs
import pseudo_rand_func as G


# Checks the given password and features are correct credentials or not
def is_login_success(pwd, features):
    global instruction_table
    # Check for error corrections on enabling the flag
    error_correction = map(lambda x: x < params.t, features)
    login_attempts = 0
    while 1:
        points = []
        # For each feature get (xi, yi)
        for i in range(1, params.m + 1):
            if error_correction[i - 1]:
                alpha = instruction_table[0][i - 1]
                x_i = 2 * i
                y_i = alpha - G.prf(params.r, pwd, str(2 * i))
                points.append((x_i, y_i))
            elif i <= params.m:
                beta = instruction_table[1][i - 1]
                x_i = 2 * i + 1
                y_i = beta - G.prf(params.r, pwd, str(2 * i + 1))
                points.append((x_i, y_i))
            i += 1

        # Calculate the lagrange interpolation with points (xi, yi)
        f = fx.lagrange_interpolation(points)

        # Get hardened password = f(0)
        hpwd = f(0)

        # Check if the hardened password is valid or not
        if hfuncs.is_success(hpwd):
            # Update the parameters for next iteration
            params.r_generator()
            rpoly = fx.rand_poly(params.m)
            hfuncs.update_file(hpwd, features, rpoly[0])

            instruction_table = itable.create_table(rpoly, pwd, hfuncs.read_file(rpoly[0]))
            return params.LOGIN_SUCCESS
        else:
            # If not enabled return as failed
            if not params.ENABLE_ERROR_CORRECTION:
                return params.LOGIN_FAILED
            # If attempts reach the max features length then return as failed
            if login_attempts == params.m:
                break
            # If enabled error correction then iterate for each feature by negating the condition.
            if login_attempts > 0:
                error_correction[login_attempts - 1] = not error_correction[login_attempts - 1]
            error_correction[login_attempts] = not error_correction[login_attempts]
            login_attempts += 1

    return params.LOGIN_FAILED


if __name__ == '__main__':
    # Read input test cases from file input.txt
    f = open(params.in_file, 'r')
    data = f.read().splitlines()
    pwd = data[0]
    n = len(data) / 2

    # Generate a random r
    params.r_generator()

    # Get the number of feature values
    params.m = len(pwd) - 1

    # Generate random polynomial
    poly = fx.rand_poly(params.m)

    # Create initial instruction table
    instruction_table = itable.initial_table(poly, pwd)

    # Create initial history file
    hfuncs.write_file(poly[0])

    # Check if login is success or not for each entry
    success = 0
    out_log = open(params.out_file, 'w')
    for i in xrange(0, n):
        pwd = data[2 * i]
        features = map(int, data[2 * i + 1].split(','))
        if len(features) != params.m:
            print 'Insufficient features'
        else:
            success = is_login_success(pwd, features)
            out_log.write(str(success) + '\n')

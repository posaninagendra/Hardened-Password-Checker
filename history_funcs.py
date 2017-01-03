import math
import crypto_funcs as crypt
import parameters as params


# Read encrypted history file and decrypt with key as hardened password
def read_file(hpwd):
    file_content = crypt.decrypt(hpwd).strip().splitlines()[1:]
    data = map(get_list, file_content)
    data = zip(*data)
    return data


# Write to the with encrypted feature values with key as hardened password
def write_file(hpwd, file_lines=()):
    # Constant file length calculation
    f_len = (params.m * 5 + 1) * params.h + len(params.h_text)
    f_len = int(math.ceil(f_len / 16) * 16)

    # Initial file text used to test whether encryption is success or not.
    file_content = params.h_text
    for i in file_lines:
        file_content += i + "\n"
    # Padding the file content to get constant file size
    file_content = file_content.ljust(f_len, ' ')
    # Encrypting the file content and writing it to the history file
    cipher = crypt.encrypt(hpwd, file_content)
    f = open(params.h_file, 'w')
    f.write(cipher)
    f.close()


# Test function to check whether login is success or not.
def is_success(hpwd):
    # Check if the decrypted history file content has the initial text as 'HF'
    if crypt.decrypt(hpwd).startswith(params.h_text):
        return True
    else:
        return False


# Update the history file with new feature values and adjust to have the last h success values
def update_file(hpwd, feature, pwd):
    # Decrypt file content with hardened password
    # Update it with last h success feature values
    file_content = crypt.decrypt(hpwd).strip().splitlines()[1:]
    if len(file_content) == params.h:
        file_content = file_content[1:]
    file_content.append(','.join(map(str, feature)))
    write_file(pwd, file_content)


# Helper function
def get_list(list):
    return map(int, list.split(','))




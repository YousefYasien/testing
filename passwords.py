import hashlib
import time
import logging

def convert_to_sha256(text):
    return hashlib.sha256(text.encode()).hexdigest()

def find_password_in_file(file_path, target_sha256):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file.readlines()):
                if convert_to_sha256(line.strip()) == target_sha256:
                    return line, line_num + 1
    except FileNotFoundError:
        logging.error(f"File {file_path} not found.")
        return None, None

def main():
    user_sha256 = input('Enter SHA256: ').strip().lower()
    password, line_num = find_password_in_file('./passwords_2.txt', user_sha256)
    if password:
        print(f"Found password: {password} on line: {line_num}")
    else:
        print("Password not found.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR)
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = round(end_time - start_time, 2)
    print(f"Time taken: {elapsed_time} seconds")
import hashlib
import argparse
import pyfiglet
import time
import itertools
import string

# Banner
banner = pyfiglet.figlet_format("Password Cracker")
print(banner)
print("By karthithehacker\n")

# Argument Parsing
parser = argparse.ArgumentParser(description="Advanced Password Cracker")
parser.add_argument("-hash", "--hash", required=True, help="Hashed password to crack")
parser.add_argument("-algo", "--algorithm", default="md5", choices=["md5", "sha1", "sha256", "sha512"], help="Hashing algorithm (default: md5)")
parser.add_argument("-file", "--file", help="Password dictionary file")
parser.add_argument("-bruteforce", action="store_true", help="Enable brute-force attack mode")
parser.add_argument("-min", type=int, default=4, help="Minimum length for brute-force (default: 4)")
parser.add_argument("-max", type=int, default=8, help="Maximum length for brute-force (default: 8)")
parser.add_argument("-charset", type=str, default=string.ascii_letters + string.digits, help="Character set for brute-force attack")
parser.add_argument("-output", help="Save cracked passwords to a file")
args = parser.parse_args()

# Start Time
start_time = time.time()
pass_found = False

# Function to hash words
def hash_word(word, algorithm):
    encoded_word = word.encode('utf-8')
    if algorithm == "md5":
        return hashlib.md5(encoded_word).hexdigest()
    elif algorithm == "sha1":
        return hashlib.sha1(encoded_word).hexdigest()
    elif algorithm == "sha256":
        return hashlib.sha256(encoded_word).hexdigest()
    elif algorithm == "sha512":
        return hashlib.sha512(encoded_word).hexdigest()
    return None

# Dictionary Attack
if args.file:
    try:
        with open(args.file, 'r', encoding="utf-8", errors="ignore") as pass_file:
            print(f"🔍 Attempting dictionary attack using {args.file}\n")
            for word in pass_file:
                word = word.strip()
                if hash_word(word, args.algorithm) == args.hash:
                    print(f"✅ Password Found: {word}")
                    pass_found = True
                    if args.output:
                        with open(args.output, "a") as out_file:
                            out_file.write(f"{word}\n")
                    break
    except FileNotFoundError:
        print(f"❌ Error: {args.file} not found. Please check the file path.")

# Brute Force Attack
if not pass_found and args.bruteforce:
    print(f"🔍 Attempting brute-force attack (charset: {args.charset}, length: {args.min}-{args.max})\n")
    for length in range(args.min, args.max + 1):
        for guess in itertools.product(args.charset, repeat=length):
            password = ''.join(guess)
            if hash_word(password, args.algorithm) == args.hash:
                print(f"✅ Password Found: {password}")
                pass_found = True
                if args.output:
                    with open(args.output, "a") as out_file:
                        out_file.write(f"{password}\n")
                break
        if pass_found:
            break

# End Time
end_time = time.time()
elapsed_time = round(end_time - start_time, 2)

if not pass_found:
    print("❌ Password not found.")
print(f"⏳ Time Taken: {elapsed_time} seconds")

![Logo](https://github.com/karthi-the-hacker/webintellect/blob/main/images/logo.png)

# Password Cracker

A simple and efficient password cracking tool for security testing and penetration testing.

## Tech Stack

- **Language:** Python
- **Libraries:** hashlib, itertools, argparse

## Features

- Supports multiple hash algorithms (MD5, SHA-1, SHA-256, etc.)
- Dictionary-based attack
- Brute-force attack with customizable character sets
- Supports custom wordlists
- Multi-threading for faster cracking
- Save cracked passwords to a file
- Simple CLI usage

## Installation

Clone the repository:

```bash
  git clone https://github.com/karthi-the-hacker/passwordcracker.git
```

Go to the project directory:

```bash
  cd Password-cracker
```

Install dependencies:

```bash
  pip install -r requirements.txt
```

## Usage

### Dictionary Attack

```bash
python password_cracker.py -hash <hash_value> -file <wordlist.txt>
```

### Brute Force Attack

```bash
python password_cracker.py -hash <hash_value> -bruteforce -min 4 -max 8 -charset abc123
```

### Save Cracked Passwords

```bash
python password_cracker.py -hash <hash_value> -file <wordlist.txt> -output cracked.txt
```

## Roadmap

- Add GPU acceleration using Hashcat
- Implement a hybrid attack mode (dictionary + brute force)
- Support more hash types (bcrypt, NTLM, etc.)
- Improve performance optimizations

## API Reference

Coming soon...

## Author

- [@karthithehacker](https://github.com/karthi-the-hacker)

## 🚀 About Me

I'm a Cyber Security Researcher passionate about penetration testing and security automation.


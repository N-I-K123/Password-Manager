import random
import string

def generator():
    length=16

    letters = string.ascii_letters
    digits = string.digits
    symbols = "!@#$%^&*()-_=+[]{}<>?/\\|"

    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    all_chars = letters + digits + symbols
    password += random.choices(all_chars, k=length - len(password))

    random.shuffle(password)

    return ''.join(password)

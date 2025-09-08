
def encrypt(text, key):
    result = bytearray()
    text_bytes = text.encode("utf-8")
    for i, byte in enumerate(text_bytes):
        shift = ord(key[i % len(key)])
        result.append((byte + shift) % 256)
    return result.hex()

def decrypt(cryptedText, key):
    text_bytes = bytes.fromhex(cryptedText)
    result = bytearray()
    for i, byte in enumerate(text_bytes):
        shift = ord(key[i % len(key)])
        result.append((byte - shift) % 256)
    return result.decode("utf-8")

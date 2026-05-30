def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord ('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)
message = "Hello, Asmaul * JUBAIR"
encrypted = encrypt(message, 3)
decrypted = decrypt(encrypted, 3)

print(f"Original message: {message}")
print(f"Encrypted message: {encrypted}")
print(f"Decrypted message: {decrypted}")
    

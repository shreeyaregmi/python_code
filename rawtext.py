def main():
    n = int(input("Enter value for n: "))
    m = int(input("Enter value for m: "))

    # Full path to your file (use raw string or double backslashes)
    file_path = r"C:\Users\This PC\Documents\CDU ASSIGNMENTS\Software Now\raw_text.txt"
    # Replace 'YourUsername' with your actual Windows username

    # Read original text from file
    with open(file_path, "r") as file:
        original_text = file.read()

    # Encrypt the text
    encrypted = encrypt_recursive(original_text, n, m)

    # Save encrypted text (in the same folder or current folder)
    with open("encrypted_text.txt", "w") as file:
        file.write(encrypted)

    # Decrypt the encrypted text
    decrypted = decrypt_recursive(encrypted, n, m)

    # Check if decrypted text matches original
    if decrypted == original_text:
        print("Success! Decrypted text matches the original.")
    else:
        print("Decryption failed. Text does not match.")

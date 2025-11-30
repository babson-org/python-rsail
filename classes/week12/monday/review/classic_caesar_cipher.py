def caesar_cipher():
    # Ask user for encrypt or decrypt
    choice = input("Encrypt or Decrypt? (e/d): ").strip().lower()
    while choice not in ("e", "d"):
        choice = input("Please enter 'e' to encrypt or 'd' to decrypt: ").strip().lower()

    # Shift amount
    shift = int(input("Enter shift amount (e.g., 3): "))

    # Decrypt means shifting backwards
    if choice == "d":
        shift = -shift

    text = input("Enter your message: ")

    result = ""

    # Caesar shift logic
    for ch in text:
        if 'A' <= ch <= 'Z':
            result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        elif 'a' <= ch <= 'z':
            result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += ch  # leave punctuation, spaces unchanged

    print("\nResult:", result)

caesar_cipher()
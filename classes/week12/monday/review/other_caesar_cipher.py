def caesar_cipher():
    import string

    choice = input("Encrypt or Decrypt? (e/d): ").strip().lower()
    while choice not in ("e", "d"):
        choice = input("Please enter 'e' to encrypt or 'd' to decrypt: ").strip().lower()

    # Shift amount
    shift = int(input("Enter shift amount (e.g., 3): "))

    letters = list(string.ascii_uppercase) 
    encrypted_letters  = [""] * 26  # why do we do this?
    for idx in range(26):
        new_idx = (idx - shift) % 26
        encrypted_letters[new_idx] = letters[idx]

    #print(letters)
    #print(encrypted_letters)
    
    text = input("Enter your message: ").upper()   

    result = ""

    if choice == 'e':
        for t in text:
            idx = letters.index(t)
            result += encrypted_letters[idx]
    else:
        for t in text:
            idx = encrypted_letters.index(t)
            result += letters[idx]
    
    print(result)
    
caesar_cipher()
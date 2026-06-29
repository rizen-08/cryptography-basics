# Import the SHA-256 algorithm from the pycryptodome library
from Crypto.Hash import SHA256

def main():
    # 1. Define the message you want to hash
    # The 'b' before the string converts it into bytes, which the algorithm requires.
    original_message = b"Cryptography is fascinating!"
    
    # 2. Create a new SHA-256 hash object
    hasher = SHA256.new()
    
    # 3. Feed your message into the hasher
    hasher.update(original_message)
    
    # 4. Generate the final hash string in hexadecimal format
    # Hexadecimal uses numbers 0-9 and letters a-f.
    final_hash = hasher.hexdigest()
    
    # Print the results to the screen
    print("--- SHA-256 Hashing ---")
    print(f"Original Message: {original_message.decode('utf-8')}")
    print(f"Resulting Hash:   {final_hash}")
    
    # Optional: Demonstrate the 'Avalanche Effect'
    # Changing just one letter changes the ENTIRE hash
    slightly_changed_message = b"cryptography is fascinating!" # Lowercase 'c'
    hasher2 = SHA256.new()
    hasher2.update(slightly_changed_message)
    print(f"\nChanged Message:  {slightly_changed_message.decode('utf-8')}")
    print(f"Resulting Hash:   {hasher2.hexdigest()}")

if __name__ == "__main__":
    main()
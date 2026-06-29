# Cryptography Fundamentals in Python 🔐

This repository contains practical Python implementations of three foundational cryptographic algorithms: **SHA-256**, **AES-256**, and **RSA-2048**. 

This project was built to explore the core pillars of modern digital security: data integrity, symmetric encryption, and asymmetric encryption.

# Algorithms Implemented

1. **Hashing (SHA-256)**
   * **File:** `hash_test.py`
   * **Concept:** One-way cryptographic hashing. Demonstrates the "Avalanche Effect" where a tiny change in input drastically changes the output. Used for data integrity and secure password storage.

2. **Symmetric Encryption (AES-256)**
   * **File:** `aes_test.py`
   * **Concept:** Reversible encryption using a single shared secret key. Implemented using Cipher Block Chaining (CBC) mode with dynamic Initialization Vectors (IV) and PKCS7 padding. Best for bulk data encryption.

3. **Asymmetric Encryption (RSA-2048)**
   * **File:** `rsa_test.py`
   * **Concept:** Public/Private key pair infrastructure using PKCS1_OAEP padding. Demonstrates how a public key encrypts data that only the private key can decrypt. Best for secure key exchange and digital signatures.

# Prerequisites

This project uses the modern `pycryptodome` library (a secure drop-in replacement for the deprecated `PyCrypto`).

To install the required dependencies, run:
```bash
pip install pycryptodome

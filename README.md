Rail Fence Cipher

Overview

This repository contains two Python scripts, encryption.py and decryption.py, for performing Rail Fence Cipher encryption and decryption. The Rail Fence Cipher is a form of transposition cipher that involves writing the plaintext in a zigzag pattern across multiple "rails" and then reading off each rail sequentially to produce the ciphertext.

Files
encryption.py: This script encrypts a given plaintext using the Rail Fence Cipher.
decryption.py: This script decrypts a given ciphertext that was encrypted using the Rail Fence Cipher, including handling multiple rounds of encryption as specified by the key.
Getting Started
Prerequisites
Python 3.x must be installed on your machine.
No additional libraries are required for these scripts.

Installation
   
   1)Clone the repository to your local machine
   
   2)Navigate to the repository directory
   
Usage:

Encrypting a Message

To encrypt a message using the Rail Fence Cipher, run the encryption.py script.

Example usage:

python encryption.py "Your message here" 4 5

Decrypting a Message

To decrypt a message that was encrypted using the Rail Fence Cipher, run the decryption.py script.

Example usage:

python decryption.py "Encrypted message here" 4 5

# Caesar Cipher using command line argument key


A [caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher) encoder in  C language.


![caesar](https://github.com/user-attachments/assets/38abceac-ad28-4454-aa90-0191966007df)



Supposedly, Caesar (yes, that Caesar) used to “encrypt” (i.e., conceal in a reversible way) confidential messages by shifting each letter therein by some number of places. For instance, he might write A as B, B as C, C as D, …, and, wrapping around alphabetically, Z as A. And so, to say HELLO to someone, Caesar might write IFMMP instead. Upon receiving such messages from Caesar, recipients would have to “decrypt” them by shifting letters in the opposite direction by the same number of places.
The secrecy of this “cryptosystem” relied on only Caesar and the recipients knowing a secret, the number of places by which Caesar had shifted his letters (e.g., 1). Not particularly secure by modern standards, but, hey, if you’re perhaps the first in the world to do it, pretty secure!
Unencrypted text is generally called plaintext. Encrypted text is generally called ciphertext. And the secret used is called a key.

To be clear, then, here’s how encrypting HELLO with a key of yields IFMMP:


example :- plaintext "H E L L O" + key(1)	= ciphertext "I F M M P"  here the key is 1.



<img width="951" alt="Screenshot 2024-08-05 at 2 15 46 PM" src="https://github.com/user-attachments/assets/b3b8da28-9b7e-4db8-a6fd-a77f44c06d3b">









## Usage

 Caution :- made with cs50 library (may not work in local device)

1) open vs code
2) copy and paste the .c file
3) run it
4) follow the next steps





# How to use command line argument ??? #

## Command line argument


In the below prompt it asks user for  plain text as the key  ./caesar "positive int"(in above example 1) 

```
./caesar 1
```

If any of the characters of the command-line argument is not a decimal digit, our program  prints the message Usage: ./caesar key and return from main a value of 1.

```
./caesar HELLO
```

# Made from cs50 problem set 
https://cs50.harvard.edu/x/2024/psets/2/caesar/





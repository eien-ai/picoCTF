# Easy Peasy
**Category**: Cryptography \
**Points**: 40

## Problem Statement
> A one-time pad is unbreakable, but can you manage to recover the flag? (Wrap with picoCTF{}) 
`nc mercury.picoctf.net 20266` (See __otp.py__)

## Hints
1. > Maybe there's a way to make this a 2x pad.

## Solution
Observe that in __otp.py__ the encryption key is presumed to have length 50000 (`KEY_LEN`), and that the algorithm reuses the same key once it hits the end. If we can get the program to re-encrypt the encrypted flag with the same part of the key then we will actually decrypt the flag (`ord(p) ^ k ^ k = ord(p)`).

1. The ciphertext is outputted as hexidecimal values. We can first convert it back into ascii as we need to feed this back into the program (call this `ascii_ciphertext`).
2. Next we build the input text in two parts:
    * `'0' * (KEY_LEN - len(ascii_ciphertext)) + chr(10) ` is used to use up the rest of the key so that the the algorithm starts reusing the same same key. The `chr(10)` is the "ENTER" key used to break up the input into two parts due to 50000 length restriction.
    * `ascii_ciphertext + '0'` where the `'0'` is added at the end to prevent `str.rstrip()` from removing the whitespace characters within the ciphertext.
3. Running __decrypt_otp.py__ will perform steps 1 & 2, and will output the input texts into the file __input.txt__.
4. We can pipe __input.txt__ as input to the program from the WebShell: 
    ```
    cat input.txt | nc mercury.picoctf.net 20266
    ```
5. Convert the last line of hexidecimal output back into ascii, and remove the last character. What is left is the decrypted flag.


## Flag
```
picoCTF{99072996e6f7d397f6ea0128b4517c23}
```

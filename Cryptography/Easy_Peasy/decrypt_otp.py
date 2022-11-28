KEY_LEN = 50000

flag_ciphertext = '5b1e564b6e415c0e394e0401384b08553a4e5c597b6d4a5c5a684d50013d6e4b'

ascii_ciphertext = ''.join([chr(int(flag_ciphertext[i:i+2], base=16)) for i in range(0, len(flag_ciphertext), 2)])
len_plaintext = len(ascii_ciphertext)

print(ascii_ciphertext)
print(len_plaintext)

trick_text = '0' * (KEY_LEN - len_plaintext) + chr(10) + ascii_ciphertext + '0'
# print(trick_text)
print(len(trick_text))

decrypted = '393930373239393665366637643339376636656130313238623435313763323351'
# print(decrypted[len(decrypted)-64:])
ascii_decrypted = ''.join([chr(int(decrypted[i:i+2], base=16)) for i in range(0, 2 * len_plaintext, 2)])
print(len(ascii_decrypted))
print(ascii_decrypted)

f = open('input.txt', 'w')
f.write(trick_text)

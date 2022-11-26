def rot13(plaintext):
    ciphertext = []
    for ch in plaintext:
        if str.isalpha(ch):
            base = 'A' if str.isupper(ch) else 'a'
            ciphertext.append(chr((ord(ch) - ord(base) + 13) % 26 + ord(base)))
        else:
            ciphertext.append(ch)
    return "".join(ciphertext)


def main():
    inp = input()
    print(rot13(inp))


main()

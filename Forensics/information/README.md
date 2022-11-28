# information
**Category**: Forensics \
**Points**: 10

## Problem Statement
Files can always be changed in a secret way. Can you find the flag? __cat.jpg__

## Hints
1. > Look at the details of the file
2. > Make sure to submit the flag as picoCTF{XXXXX}

## Solution
1. Looking at the details of the file by dumping all the strings with: `$ strings cat.jpg`. As part of the image meta data notice that there is a value that looks out of place:
    ```
    rdf:resource='cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9'
    ```
2. This value looks like it could be base64 encoded, and decoding this in python gives us the flag:
    ```
    >>> import base64
    >>> base64.b64decode('cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9')
    b'picoCTF{the_m3tadata_1s_modified}'

    ```

## Flag
```
picoCTF{the_m3tadata_1s_modified}
```
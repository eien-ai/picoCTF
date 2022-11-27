# Matryoshka doll
**Category**: Forensics \
**Points**: 30

## Problem Statement
Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: __dolls.jpg__

## Hints
1. > Wait, you can hide files inside files? But how do you find them?
2. > Make sure to submit the flag as picoCTF{XXXXX}

## Solution
Refer to __resources/Forensics/steganography.pdf__.

The __dolls.jpg__ image can be recursively unzipped to reveal more hidden files, until we eventual reach the __flag.txt__ file containing the flag.

## Flag
```
picoCTF{336cf6d51c9d9774fd37196c1d7320ff}
```

from string import ascii_uppercase


def decrypt(input_ciphertext):
    for refChar in ascii_uppercase:
        i = 1 + ord(refChar) - ord('A')
        output = []
        for ch in input_ciphertext:
            if ch == ' ':
                output.append(' ')
            else: 
                if ord(ch) + i > ord('Z'):
                    wrapped_ch = ord('A') + (ord(ch) + i - ord('Z')) - 1
                    output.append(chr(wrapped_ch))
                else:
                    output.append(chr((ord(ch) + i)))
        

        print(f"(key: +{i}) - result: {''.join(output)}")

        
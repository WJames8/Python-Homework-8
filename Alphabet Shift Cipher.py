def make_alphabet(keyword):
    alphabet = ""

    for char in keyword.upper() + "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if char.isalpha() and char not in alphabet:
            alphabet += char

    return alphabet


def encode(message, keyword):
    alphabet = make_alphabet(keyword)
    result = ""

    for char in message.upper():
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            result += alphabet[ord(char) - ord('A')]
        else:
            result += char

    return result


def decode(message, keyword):
    alphabet = make_alphabet(keyword)
    result = ""

    for char in message.upper():
        if char in alphabet:
            result += chr(alphabet.index(char) + ord('A'))
        else:
            result += char

    return result


def main():
    keyword = input("Enter a keyword: ")
    message = input("Enter a message to encode: ")

    encrypted = encode(message, keyword)
    decrypted = decode(encrypted, keyword)

    print("Cipher alphabet:", make_alphabet(keyword))
    print("Encoded message:", encrypted)
    print("Decoded message:", decrypted)


if __name__ == "__main__":
    main()
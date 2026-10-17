def encode(message, date):
    shifts = "".join(date.split("/"))
    result = ""
    index = 0

    for char in message.upper():
        if char.isalpha():
            shift = int(shifts[index % len(shifts)])
            letter = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result += letter
            index += 1

    return result


def decode(message, date):
    shifts = "".join(date.split("/"))
    result = ""
    index = 0

    for char in message.upper():
        if char.isalpha():
            shift = int(shifts[index % len(shifts)])
            letter = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            result += letter
            index += 1

    return result


def main():
    message = input("Enter a message (letters only): ")
    date = input("Enter the agreed date (M/D/YY): ")

    encrypted = encode(message, date)
    decrypted = decode(encrypted, date)

    print("Encoded message:", encrypted)
    print("Decoded message:", decrypted)


if __name__ == "__main__":
    main()
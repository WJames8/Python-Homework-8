def locate_letter(board, letter):
    letter = letter.upper()

    if letter == "Z":
        letter = "Y"

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == letter:
                return row, col

    return None


def encrypt(message, board):
    result = []

    for char in message.upper():
        if char.isalpha():
            if char == "Z":
                char = "Y"

            position = locate_letter(board, char)

            if position is not None:
                row, col = position
                result.append(str(row) + str(col))

    return " ".join(result)


def decrypt(ciphertext, board):
    result = ""
    digits = ciphertext.split()

    for pair in digits:
        row = int(pair[0])
        col = int(pair[1])
        result += board[row][col]

    return result


def main():
    board = [
        ["A", "B", "C", "D", "E"],
        ["F", "G", "H", "I", "J"],
        ["K", "L", "M", "N", "O"],
        ["P", "Q", "R", "S", "T"],
        ["U", "V", "W", "X", "Y"]
    ]

    message = input("Enter a message to encrypt: ")

    encrypted = encrypt(message, board)
    decrypted = decrypt(encrypted, board)

    print("Encrypted message:", encrypted)
    print("Decrypted message:", decrypted)


if __name__ == "__main__":
    main()
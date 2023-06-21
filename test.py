import os
from split_image import split_image


def addToClipBoard(text):
    command = "echo " + text.strip() + "| clip"
    os.system(command)


# Starts the program
def start():
    # emoji_command = input("What do you want to type for your emoji to appear? ")
    # value_of_squares = int(input("How many rows do you want the emoji to be? "))

    value_of_squares = 3

    split_image(
        "test/kappa.png",
        value_of_squares,
        value_of_squares,
        True,
        False,
        "/test/kappa/",
    )

    output = ""

    print(output)

    with open("test/output.txt", "w") as f:
        f.write(output)

    addToClipBoard(output)


start()

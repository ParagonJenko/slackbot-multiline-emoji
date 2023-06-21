import os


def addToClipBoard(text):
    command = "echo " + text.strip() + "| clip"
    os.system(command)


# Initalies the dictionary grid
def getGridDictionary(chosen_grid):
    grid = {
        "topleft": "",
        "topmiddle": "",
        "topright": "",
        "bottomleft": "",
        "bottommiddle": "",
        "bottomright": "",
    }

    if chosen_grid == 2:
        del grid["topmiddle"]
        del grid["bottommiddle"]

    return grid


# Gets the string emojis as inputs from users
def getEmojiStringInput(emoji_grid, location):
    for key in emoji_grid:
        match key:
            case "topleft":
                location = "top left"
            case "topmiddle":
                location = "top middle"
            case "topright":
                location = "top right"
            case "bottomleft":
                location = "bottom left"
            case "bottommiddle":
                location = "bottom middle"
            case "bottomright":
                location = "bottom right"

        emoji_grid[key] = input(
            "Please enter the "
            + location
            + " emoji name (for example: EMOJI_0_0 or EMOJI-topleft) "
        )

    return emoji_grid


# Creates the string
def createString(grid, emoji_grid, emoji_command):
    match grid:
        case 2:
            slackbot_string = (
                "`"
                + emoji_command
                + "` \\n :"
                + emoji_grid["topleft"]
                + ": :"
                + emoji_grid["topright"]
                + ":\\n :"
                + emoji_grid["bottomleft"]
                + ": :"
                + emoji_grid["bottomright"]
                + ": \\n"
            )
        case 3:
            slackbot_string = (
                "`"
                + emoji_command
                + "` \\n :"
                + emoji_grid["topleft"]
                + ": :"
                + emoji_grid["topmiddle"]
                + ": :"
                + emoji_grid["topright"]
                + ":\\n :"
                + emoji_grid["middleleft"]
                + ": :"
                + emoji_grid["middlemiddle"]
                + ": :"
                + emoji_grid["middlelright"]
                + ":\\n :"
                + emoji_grid["bottomleft"]
                + ": :"
                + emoji_grid["bottommiddle"]
                + ": :"
                + emoji_grid["bottomright"]
                + ": \\n"
            )
        case _:
            slackbot_string = "Error: Not valid grid value for getTemplate"

    return slackbot_string


# TestGrid data
def testDataGrid(grid):
    if int(grid) == 2:
        emoji_grid = {
            "topleft": "turtle_0_0",
            "topmiddle": "",
            "topright": "turtle_1_0",
            "bottomleft": "turtle_0_1",
            "bottommiddle": "",
            "bottomright": "turtle_1_1",
        }
    elif int(grid) == 3:
        emoji_grid = {
            "topleft": "kappa_0_0",
            "topmiddle": "kappa_1_0",
            "topright": "kappa_2_0",
            "middleleft": "kappa_0_1",
            "middlemiddle": "kappa_1_1",
            "middlelright": "kappa_2_1",
            "bottomleft": "kappa_0_2",
            "bottommiddle": "kappa_1_2",
            "bottomright": "kappa_2_2",
        }
    else:
        return 0

    return emoji_grid


# Starts the program
def start():
    emoji_command = input("What do you want to type for your emoji to appear? ")
    value_of_squares = input("Is it a 3x3 or a 2x2 emoji? ")

    # Testing data
    # emoji_command = "testing"
    # value_of_squares = "3"
    # test_grid = testDataGrid(value_of_squares)

    match value_of_squares:
        case "3" | "3x3" | 3:
            print("Chosen: 3x3")
            chosen_grid = 3

        case "2" | "2x2" | 2:
            print("Chosen: 2x2")
            chosen_grid = 2
        case _:
            print("Invalid input for the size of the emoji.")
            start()

    grid = getGridDictionary(chosen_grid)
    output = createString(
        chosen_grid, getEmojiStringInput(grid, emoji_command), emoji_command
    )

    # Testing function
    # output = createString(chosen_grid, test_grid, emoji_command)t

    print(output)

    with open("output.txt", "w") as f:
        f.write(output)

    addToClipBoard(output)


start()

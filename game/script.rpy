# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:
    "Opening narration"

label nightOne:
    "Who are you visiting tonight?"
    menu:
        "Partner":
            jump parterRouteScene1
        "Child":
            jump nightTwo

label nightTwo:

    "Night two XD"

    return

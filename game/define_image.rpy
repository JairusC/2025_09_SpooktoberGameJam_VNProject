# background
transform couch:
    center
    scale(4.0)

image bg apartment cold = "cold_apartment_bg.png"
image bg bedroom = "bedroom.jpg"
image bg couch warm:
    At("couch_warm_bg.png", couch)
image bg couch cold:
    At("couch_bg.png", couch)

# character
init python:
    def set_focus(speaker_name, speaker_expr="normal", other_name="", other_expr="normal"):
        renpy.show(speaker_name + " " + speaker_expr)
        Dissolve()
        if (other_name != ""):
            renpy.show(other_name + " " + other_expr + " dark")
            Dissolve()

    def darken(speaker_name, speaker_expr="normal", other_name="", other_expr="normal"):
        renpy.show(speaker_name + " " + speaker_expr + " dark")
        Dissolve()
        if (other_name != ""):
            renpy.show(other_name + " " + other_expr + " dark")
            Dissolve()

    def brighten(speaker_name, speaker_expr="normal", other_name="", other_expr="normal"):
        renpy.show(speaker_name + " " + speaker_expr)
        Dissolve()
        if (other_name != ""):
            renpy.show(other_name + " " + other_expr)
            Dissolve()

transform leftPortrait:
    left
    scale(0.2)
    ypos 600

transform leftPortraitDark:
    left
    scale(0.2)
    ypos 600
    matrixcolor BrightnessMatrix(-0.2)

transform rightPortrait:
    right
    scale(0.2)
    ypos 600
    xzoom -1.0

transform rightPortraitDark:
    right
    scale(0.2)
    ypos 600
    xzoom -1.0
    matrixcolor BrightnessMatrix(-0.2)

image lee normal:
    At("lee_normal.png", leftPortrait)
image lee normal dark:
    At("lee_normal.png", leftPortraitDark)
image lee smile:
    At("lee_happy.png", leftPortrait)
image lee smile dark:
    At("lee_happy.png", leftPortraitDark)
image lee sad:
    At("lee_sad.png", leftPortrait)
image lee sad dark:
    At("lee_sad.png", leftPortraitDark)
image lee pray:
    At("lee_pray.png", leftPortrait)

image tommy normal:
    At("tommy_normal.png", rightPortrait)
image tommy normal dark:
    At("tommy_normal.png", rightPortraitDark)
image tommy smile:
    At("tommy_happy.png", rightPortrait)
image tommy smile dark:
    At("tommy_happy.png", rightPortraitDark)
image tommy sad:
    At("tommy_sad.png", rightPortrait)
image tommy sad dark:
    At("tommy_sad.png", rightPortraitDark)
image cred = Text(credits_s, text_align=0.5)
image theend = Text("{size=80}The end", text_align=0.5)
image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5)

label credits:
    play music menu_music volume 0.3 fadein 1.0 fadeout 1.0
    $ credits_speed = 25
    scene black
    with dissolve
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide theend
    with dissolve
    with Pause(credits_speed - 3)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(1.5)
    hide thanks
    return

init python:
    credits = [
        ('', 'Our Last Second'),
        ('Played too much Hades II', 'Vincent'),
        ('Played too much Silk Song', 'Ria'),
        ('Played too much Sekiro', 'Tommy'),
        ('Should be studying for mid terms', 'Justin'),
        ('Did a lot of running', 'Jairus'),
        ('Special Thanks', 'Tam and the discord channel'),
        ('With love', '\nTo our families and friends,'),
        ('With love', 'No matter how long we\'ve had together,'),
        ('With love', 'every moment means the world.'),
        ('With love', 'Thank you.'),
    ]
    credits_s = "{size=80}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=25}" + c[0] + "\n"
        credits_s += "{size=30}" + c[1] + "\n"
        c1=c[0]
    
    credits_s += "\n\n\n\n{size=25}A game made for the 2025 Spooktober Game Jam"
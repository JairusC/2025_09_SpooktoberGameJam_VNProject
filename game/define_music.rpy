define menu_music = "audio/music/MenuLoop.mp3"
define door_opening = "audio/sfx/DoorOpening.mp3"
define thud = "audio/sfx/SittingOnBed.mp3"
define wedding_song = "audio/music/WeddingSong.mp3"
define wedding_song_end = "audio/music/WeddingSong End.mp3"

init python:
    def adapt_wedding_song():
        renpy.notify(("Function tested"))
        try:
            if (renpy.music.is_playing("music")):
                renpy.notify("music is playing")
                duration = 200
                pos = renpy.music.get_pos("music")
                renpy.notify("Duration: " + str(duration) + ", Position: " + str(pos))
                if duration is not None and pos is not None:
                    time_remaining = duration - pos
                    if time_remaining > 33.0:
                        renpy.music.stop(channel="music", fadeout=2.0)
                        renpy.say(None, "We dance quietly for a little longer.")
                        renpy.music.play(
                            "audio/music/WeddingSong End.mp3",
                            channel="music",
                            fadein=2.0,
                            loop=False,
                        )
                else:
                    renpy.notify("Music error: no duration")
        except Exception as e:
            renpy.notify("Music error: " + str(e))
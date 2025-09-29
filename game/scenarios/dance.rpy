label dance:
    $ brighten("lee", "sad", "tommy", "normal")
    show bg couch warm with fade
    play music wedding_song volume 0.3 fadein 1.0 fadeout 1.0

    pause 1.0

    "Then I hear a song playing. I raise my head and see Tommy, kneeling before me with his hand out."

    "He raises me up and leads me into a little dance. I know the steps well."

    "We'd only ever learned one dance."
    
    "The one for our wedding."

    pause 1.0

    $ set_focus("tommy", "normal", "lee", "sad")
    t "Your story doesn't end here."

    "We pace around the room a little. He brings me closer and whispers."

    t "The food I make will remind me of you, because we spent so many nights figuring out how to make our favorite recipes."

    t "All those plants you got for us even though I said we already had too many? I'll keep them alive."

    t "I listen to all the punk bands that you love, because you got us tickets to every concert and made me love them too."

    t "Our friends and family will always remember you, because you left an irreplaceable mark in our hearts."

    t "I'll visit all the places we said we would travel to."

    $ set_focus("tommy", "smile", "lee", "sad")
    t "And… I'll even keep wearing that scarf you made for me."

    $ set_focus("lee", "normal", "tommy", "smile")
    "Oh, but he hates that thing!"

    $ set_focus("tommy", "smile", "lee", "normal")
    t "Even without trying, you'll be by my side."
    t "Every minute of you mattered."

    # <She embraces him. Her sobs from earlier have been replaced with light chuckles.>

    "..."

    $ set_focus("lee", "normal", "tommy", "smile")
    l "You don't have to wear that stupid scarf."

    $ set_focus("tommy", "smile", "lee", "normal")
    t "I will, and I am going to tell everyone that you made it."

    $ set_focus("lee", "smile", "tommy", "smile")
    l "Ha!"

    $ set_focus("lee", "normal", "tommy", "smile")
    l "Please do..."

    $ adapt_wedding_song()

    "The song is about to end."

    "..."

    $ set_focus("lee", "sad", "tommy", "smile")

    "I hold his face still, taking one last look. He looks back with those gentle eyes of his and a fragile smile." 

    "An expression that shows silent resignation."
    
    "We both know that we've done and said everything."
    
    "There is so much love but it is time to let go."

    "But if there's a part of me that will live on through him…"
    
    "Maybe that's good enough for me."

    $ set_focus("tommy", "normal", "lee", "normal")

    t "If I put on another song, do we get to keep on dancing?"

    $ set_focus("lee", "smile", "tommy", "normal")

    l "Ha! You're so greedy."

    $ set_focus("lee", "normal", "tommy", "normal")

    "We keep dancing regardless."

    "For however much longer we have..."
    
    "...down to our last second."

    call credits
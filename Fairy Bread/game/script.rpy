# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg space = "space.jpg"
image bg ship = "ship.jpg"
image bg office = "office.jpg"
image alien a = "alien.png"
# Declare characters used by this game.
define b = Character('Boris:', color="#1A28C7")
define e = Character('Editor:', color="#F22727")
define n = Character('Narrator:', color="#FFFFFF")
define c = Character('Computer:', color ="#07A336")

# The game starts here.
label start:
    scene bg space

    n "At some point in the vast history of the universe, there was a repository of all knowledge."
    n "Of course, most of the knowledge was false, as a good 99\% of the inhabitants of said universe were not made of pure knowledge."
    n "This is the story of one of the rare beings of pure knowledge, or BOPK. This BOPK was called Boris, as it sounded faintly similar to BOPK."
    n "He was sitting in his room, when he decided to verify the accuracy of the article on \"How To Extract Temporal Information From Some Fairy Bread\""
    
    scene bg ship
    b "Computer, how do I extract temporal information from a peice of fairy bread?"
    play sound "dial.ogg"
    pause 3
    c "some highly technachal stuff"
    b "Darn. I should probably go fix that."
menu:
    "Maybe later...":
        jump end
    "Let's go! There's no time to wait!":
        jump go
label end:
    n "And so Boris procrastinated forever more, leaving the page unchanged for the next 25.6 years."
    ".:. Procrastination Ending"
    return
label go:
    scene bg office
    show alien a at right
    n "Boris went to the Infinite Publishing Houses of Betelgeuse III, and found the editor in question."
    n "The argument between them went something like this..."
    b "No, you use a tri-vector manipulator to re-smash the hundreds and thousands! There is no way a quad-vector equivalent could do the job to a high level of precision, despite the dimension jump!"
    e "Assuming we live in a 4-dimensional universe, then low-quality 4D imagery is superior to high-quality 3D imagery!"
menu:
    "I suppose you're right...":
        jump give
    "But even if it were 4D, we perceive it in 3D, so the extra dimension is useless!":
        jump book
    "I'll take this up with the Hall of Information!":
        jump hall
label give:
    e "Thank you, I knew I was right."
    scene bg space
    n "And so Boris gave up, with the mis-information there for the next 25.6 years."
    ".:. Defeat Ending"
    return
label book:
    e "So?"
    n "And so on and so forth."
    n "Eventually Boris realised that it was pointless to continue and went home to fix it."
    scene bg ship
    b "What! The page is locked? Greedy person, some people need that information!"
    scene bg space
    n "And, unlike most other universes where this event took place, the page, with the same content, was destroyed with the rest of the Infinite Publishing Houses of Betelgeuse III when the Physician's revolt happened, destroying as many books marketed to the common folk as possible."
    ".:. True Ending"
    return
label hall:
    e "Fine! It won't do anything!"
    scene bg space
    n "When Boris went home, he communicated with the Hall of Information, and 25.6 minutes after he ended the argument, the information was fixed."
    ".:. Good Ending"
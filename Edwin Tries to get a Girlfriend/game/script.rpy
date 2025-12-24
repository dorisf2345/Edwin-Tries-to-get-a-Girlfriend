# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Edwin")
define o = Character("Olivia")
define k = Character("Kelly")
define s = Character("Sophie")
define l = Character("Lily")
define t = Character("Teacher")

image Edwin = "Edwin.png"

image Olivia happy = "olivia/happy."
image Olivia uncomfortable = "olivia/uncomfortable"
image Olivia angry = "olivia/angry."
image Olivia blush = "olivia/blush."
image Olivia laugh = "olivia/laugh."
image Olivia shocked = "olivia/shocked."

image Kelly happy = "kelly/happy."
image Kelly angry = "kelly/angry."
image Kelly blush = "kelly/blush."
image Kelly laugh = "kelly/laugh."
image Kelly shocked = "kelly/shocked."

image Sophie happy = "sophie/happy."
image Sophie angry = "sophie/angry."
image Sophie blush = "sophie/blush."
image Sophie laugh = "sophie/laugh."
image Sophie shocked = "sophie/shocked."

image Teacher = "teacher."

default points = 0

# The game starts here.

label start:
    $ points = 0

    # add a file (named either "bg locker.png" or "bg locker.jpg") to the
    # images directory to show it.
    # plsplspslsplspls ask for more renpy time and make it unlimited

    pause 2.0
    scene bg locker with dissolve
    pause 1.0
    show Edwin

    # These display lines of dialogue.

    e "{i}shucks im at the locker room wow{i}"

    e "{i}shucks im so lonely like i want a gf sooo bad bro{i}"

    scene phone screen with dissolve

    e "{i}wow im left on delivered looks like all these girls are {b}so{b} busy like{i}"
    e "{i}shucks i gotta like lock in yk and focus on one girl{i}"

    menu:
        "Olivia":
            jump first route
        
        "Kelly":
            jump second route

        "Sophie":
            jump third route

    label first route
        pause 2.0
        scene chemistry room with dissolve
        $ points = 0
        pause 1.0
        show Teacher

        t "alright class lets do some retrieval practice... lets start by writing the chemical equation for combining hydrochloric acid with sodium hydroxide"
        
        show Edwin

        e "{i}oh crikey idk what to do uhmmm{i}"

        menu:
            "ask the person beside you":
                jump o first encounter1

            "suck it up and get the answer wrong":
                jump o first encounter2

        label o first encounter1
            scene chemistry room
            $ points += 2
            pause 1.0
            show Olivia happy

            e "hey uh dyk how to do this im dumb"

            show Olivia laugh

            o "yeah i can help you if u want"

            show Olivia happy

            o "first start by writing down the reactants chemical formulas, and then you do this and blablablablabal"

            pause 0.5
            e "wow tysm like wow ur so smart and cool"

        label o first encounter2
            scene chemistry room
            pause 1.0
            show Teacher with fade 

            t "alright folks times up. lets seee here"

            e "{i}please please dont choose me holy yikes{i}"

            pause 1.0

            t "..."

            t "edwin what did you get?"

            e "{i}shoot uhm make something up{i}"

            e "uhhhhhh insert wrong answer"

            pause 0.5

            t "...."   

            t "ok so you may need some extra practice ask the person next to you for help next time"

            show Olivia uncomfortable

            o "here take a look at what i did"

            e "wow tysm..."

            e "{i} really need to catch up- wow shes so pretty omg{i}"

            show Olivia happy 

            o "ur welcome! if u need more help u can ask next time, i dont bite"

                

    # This ends the game.

    return

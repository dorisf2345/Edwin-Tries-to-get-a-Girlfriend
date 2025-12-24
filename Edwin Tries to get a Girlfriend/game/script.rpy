# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Edwin")
define o = Character("Olivia")
define k = Character("Kelly")
define s = Character("Sophie")
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
image Sophie uncomfortable = "sophie/uncomfortable."
image Sophie angry = "sophie/angry."
image Sophie blush = "sophie/blush."
image Sophie laugh = "sophie/laugh."
image Sophie shocked = "sophie/shocked."

image chemTeacher = "chemteacher."
image mathTeacher = "mathTeacher."

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
        show chemTeacher

        t "alright class lets do some retrieval practice... lets start by writing the chemical equation for combining hydrochloric acid with sodium hydroxide"
        
        hide chemTeacher with fade

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

            menu:
                "wow tysm like wow ur so smart and cool thx ggs":
                    jump o first encounter1a
                
                "thanks ig":
                    jump o first encounter1b

                "do u think u could tutor me for chem":
                    jump o first encounter1c

            label o first encounter1a
                scene chemistry room
                $ points += 5
                pause 1.0
                show Olivia laugh with fade
                show e

                o "youre welcome heh! if u want i can help u out in future lessons"

                show Olivia happy

                o "dw im sure youll the hang of it eventually tho once u understand the basics"

                e "tysm yes beo pls helpme out"

                show chemTeacher with fade

                t "times up folks and the right answer isssss blablablablabalab and to find it u do this this this"

                e "ohhhhh thats how u get there"

                show Olivia laugh

                o "i just showed u that idiot- sorry"

                e "heh oops its fine guys trust i got goldfish memory"

                t "there goes the bell get tf out of my classroom u brats ahh"

                show Olivia happy

                e "uhm k bye"

                o "bye"

                jump o second encounter

            label o first encounter1b
                scene chemistry room
                $ points -= 2
                pause 1.0
                show Olivia uncomfortable with fade
                show e

                o "ur welcome."

                e "{i}shucks now i sound like a jerk blabalbalbal{i}"

                show chemTeacher with fade

                t "ok folks heres the answer- oh there goes the bell and boom shakalaka get tf out of my class"

                e "hey wait-"

                hide Olivia uncomfortable with fade

                e "shucks"

                jump o second encounter

            label o first encounter1c

        label o first encounter2
            scene chemistry room
            $ points += 2
            pause 1.0
            show chemTeacher with fade 

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

            t "alright folks theres the bell leave my classroom get tf out"

            hide chemTeacher with fade

            o "welp ill see u around ig"

            e "yeah"

            jump o second encounter
        
        label o secound encounter
            if points >= 
            



    label second route
        pause 1.0
        scene fitness room with dissolve
        $ points = 0
        show e

        e "{i}shucks that was my last rep ykyk"

    label third route
        pause 1.0
        scene math room with dissolve
        $ points = 0
        show mathTeacher with fade

        t "blablala math stuff"

        e "{i}ts is so easy guys like allaalal{i}"

        t "alright guys theres the bell yall can go"

        e "{i}betbetbetebt maybe if i walk quickly i can actually find a seat in the caf{i}"

        t "oh shucks just a moment edwin i need to speak with u"

        e "{i}shucks am i in trouble like what is this{i}"

        e "ofc teach give me a second"

        t "alright son do u think u can carry some supplies i bought to the art room? i made a deal with ms pigeon and ended up having to buy her class extra things.... a lot of extra things"

        e "yikes is that actually allowed"

        t "probably not but alas what can u do. so are u up to the task? it is quite heavy"

        e "u bet i can do this lalalalalalaa"

        t "ty bro i appreciate it. dyk where it is"

        pause 0.5

        e "uhhhhhhhhhh"

        t "haha its ok, its second floor room 204"

        e "betbebtbetbe i will get it done teach"

        t "tyty just tell ms pigeon that i sent u"

        e "perf have a good day"

        scene lifting box1 with fade

        e "{i}shucks what in the world did teach have to buy this is crazy{i}"

        scene lifting box2 with fade

        e "{i}almost there... 1,2,3 lalalallaalalal just another three flights of stairs{i}"
        




                

    # This ends the game.

    return

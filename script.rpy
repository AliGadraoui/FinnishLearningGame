#Script_For_Finnish_Learning_Game 
#Author and Founder: Ali Gadraoui 
#Date: 2024-10-07
#Version: 1.0

#Description: This script is designed to create a simple text-based learning game for foreigners who seek to learn Finnish.
#Gamification of Education

# Global Variables
default player_name = "Player"  # Default name for the protagonist
default country = "Unknown"  # Default country

# Define characters in the game
define p = Character("[player_name]")  # Define the protagonist dynamically
define h = Character("Hockey Player")  # Friendly local who helps at the airport
define t = Character("Train Conductor")  # Conductor on the VR train
define u = Character("Tutor")  # Player's guide in Kokkola

# Background images
image bg airport = "images/Airpoirt terminal background.png"  # Airport background
image bg train_station = "images/train_rail_road.jpg"  # Train station background
image bg train_interior = "images/inside_Train.jpg"  # Train interior background
image bg kokkola_station = "images/Kokkola_Train_station.jfif"  # Kokkola station background

# Character sprites
image hockey_player_idle = "images/Hockey_player_OpenMouth.png"  # Hockey player standing
image train_conductor_idle = "images/Conductor_OpenMouth.png"  # Train conductor
image tutor_idle = "images/Tutor_normal_pose_OpenMouth.png"  # Tutor character

# Airport Scene
label start:
    # Scene: Airport background with airplane landing sound
    play sound "audio/airplane_landing.mp3"  # Airplane landing sound
    scene bg airport with fade  # Airport background fades in
    
    # Airport ambiance starts after landing
    play music "audio/airport_ambience.mp3" loop  # Background ambiance loops

    # Player's inner monologue
    p "The airplane has landed. I’m finally here... Finland."
    p "But now, what do I do? This airport is so big, and I have no idea where to go."
    p "I look around, hoping to find someone who can help..."

    # Player notices someone nearby
    p "There’s a guy standing near the arrivals board. He looks approachable."
    p "Alright, just go for it. Don’t overthink it."

    # Show the stranger (hockey player)
    show hockey_player_idle with dissolve

    # Player approaches and starts the conversation
    p "Excuse me, do you speak English?"

    # Stranger responds in Finnish
    h "Hei! Tarvitsetko apua?"  # "Hi! Do you need help?"
    p "Great, now what? He’s speaking Finnish. Fantastic..."
    p "Okay, maybe if I try again, he’ll get the point."

    # Dialogue continues
    menu:
        "Try again in English, slower this time.":
            p "Sorry... Do. You. Speak. English?"
            h "Ah, yes, I do! Sorry about that. How can I help you?"
            p "Wait... You spoke Finnish just now. I don’t understand a word!"
            h "Oh, that? Haha, I have a habit of messing with people who ask me things in English. It’s my way of making new friends. Welcome to Finland!"
        "Just gesture helplessly.":
            p "I just shrug and point at myself, looking as lost as possible."
            h "Haha, sorry! I didn’t mean to confuse you. I do speak English! I just like to mess with travelers—it’s a Finnish icebreaker, you could say!"

    # Stranger tries to help
    p "Relieved, I take a deep breath and explain."
    p "I need to find the train station. Can you point me in the right direction?"
    h "Of course! The train station is just outside the terminal. But wait..."
    h "Are you visiting Finland? You don’t seem local."

    # Stranger asks for the player’s name
    h "By the way, what’s your name?"
    $ player_name = renpy.input("Type your name:")  # Prompt for user input
    $ player_name = player_name.strip()  # Clean up extra spaces

    # Assign default name if none entered
    if player_name == "":
        $ player_name = "Traveler"

    p "I’m [player_name]."
    h "Nice to meet you, [player_name]! I’m Eetu."

    # Stranger asks where the player is from
    h "So, [player_name], where are you from?"
    $ country = renpy.input("Type your country name:")  # Prompt for user input
    $ country = country.strip()  # Clean up extra spaces

    p "I’m from [country]."
    h "Ah, [country]! That’s great. Finland is a bit colder, but you’ll get used to it."

    # Conversation concludes
    h "Follow me. I’ll walk you to the train station. It’s just ahead."
    p "I follow Eetu, feeling a bit more confident now. This trip might not be so bad after all."

    # Transition to the next scene
    stop music fadeout 3.0  # Fade out airport ambiance
    call train_scene  # Call the next scene

    return

# Train Scene
label train_scene:
    # Scene: Train interior with ambiance
    play music "audio/train_ambience.mp3" loop  # Train ambiance
    scene bg train_interior with fade  # Show the train interior background
    
    # Player's inner monologue
    p "The train is surprisingly quiet. Outside, I can see the snow-covered fields passing by."
    p "I hope I’m on the right train. I don’t even know how to ask if I’m headed to Kokkola."

    # Train conductor enters
    show train_conductor_idle with dissolve
    
    # Train conductor speaks in Finnish
    t "Lippunne, olkaa hyvä!"  # "Your ticket, please!"
    p "Oh no, they’re asking for something... Is it my ticket?"
    
    # Player's choices
    menu:
        "Try to hand over your ticket silently":
            p "I hand over my ticket nervously, hoping it’s what they’re asking for."
            t "Ah, kyllä! Hyvä. Oletko menossa Kokkolaan, eikö niin?"
            p "They said something about Kokkola! I nod quickly."
        "Ask in English: 'Is this my ticket?'":
            p "Is this my ticket?"
            t "Yes, that’s it! You’re headed to Kokkola?"
            p "I nod quickly, relieved that they speak some English."
    
    # Train conductor continues
    t "Hyvä. Tämä on oikein."  # "Good. This is correct."
    p "I think that means everything is okay. Phew!"

    # Train ambiance continues as conductor moves on
    t "Have a nice trip!"  # In English
    p "I relax a little, but I realize I really need to learn more Finnish for situations like this."

    # Fade out the train scene
    stop music fadeout 3.0
    hide train_conductor_idle
    call tutor_scene  # Transition to the tutor scene

    return

# Tutor Scene
label tutor_scene:
    # Scene: Arrival at Kokkola station
    play sound "audio/train_arrival.mp3" loop  # Train arrival sound
    scene bg kokkola_station with fade  # Show the Kokkola station background
    
    # Player's inner monologue
    p "Finally, the train comes to a stop. I step out into the cold, fresh air of Kokkola."
    p "Now, I just need to find my tutor. Hopefully, they’re friendly."
    # Tutor enters
    show tutor_idle with dissolve
    u "Hei! Tervetuloa !!"  # "Hi! Welcome to Kokkola!"
    p "I hear someone speaking with a warm, cheerful tone. Could this be my tutor?"

    # Player's choices
    menu:
        "Smile and nod nervously.":
            p "I smile nervously, unsure how to respond. Should I say something?"
            u "Are you [player_name]? You look like a bit of a traveler!"  # Tutor switches to English.
        "Ask in English: 'Are you my tutor?'":
            p "Excuse me, are you my tutor?"
            u "Yes, I am! Welcome to Kokkola, [player_name]. You must be freezing after your trip!"

    # Tutor continues
    u "I’m Elina, your tutor. It’s great to finally meet you in person!"
    p "Elina seems friendly, and her smile puts me at ease."
    u "So, [player_name], how was your journey here? Was it confusing, or did you find your way alright?"
    
    # Player responds
    menu:
        "It was fine, but the Finnish is a bit overwhelming.":
            p "It was fine, but... honestly, the Finnish language is a bit overwhelming."
            u "Haha, I understand! Finnish can sound like an alien language at first, but don’t worry. We’ll take it step by step."
        "I got lost, but a friendly guy helped me at the airport.":
            p "I got a bit lost, but a friendly guy helped me out at the airport."
            u "Oh, that’s classic Finland for you. People can be quiet, but they’re very helpful once you talk to them!"

    # Tutor switches to teaching mode
    u "Speaking of Finnish, let’s start with a little lesson right now. What do you say?"
    p "Right now? Sure, I guess..."
    u "Okay, let’s start with something simple. Here’s how to say 'Hello' in Finnish: 'Hei'. Try it!"
    menu:
        "Say 'Hei' confidently.":
            p "Hei!"  # Player confidently says hello.
            u "Great! See? You’re already sounding like a local."
        "Mumble 'Hei' awkwardly.":
            p "H-Hei..."  # Player says hello nervously.
            u "Haha, don’t worry. It’ll get easier with practice!"

    # Tutor continues teaching
    u "Now, let’s add a little more. If you want to say 'Thank you,' you say 'Kiitos.' Can you try that?"
    menu:
        "Say 'Kiitos'.":
            p "Kiitos!"
            u "Perfect! You’re already making progress."
        "Struggle with 'Kiitos'.":
            p "Ki-Kiitos?"
            u "Haha, almost there! You’ll get it with time."

    # Tutor reassures the player
    u "See? Finnish isn’t so scary when you break it down. And don’t worry, I’ll be here to guide you every step of the way."
    u "By the end of your journey here, you’ll be speaking Finnish like a pro—or at least enough to order coffee and find your way around!"

    # Player feels reassured
    p "I can’t help but smile. Elina’s energy is contagious, and I’m starting to feel a little more confident about this adventure."

    # Transition to the next part
    u "Alright, let’s get going. The learning center isn’t far from here. We’ll get you settled in and start your Finnish journey properly!"
    p "I follow Elina, feeling a mix of excitement and nervousness. This is going to be a unique adventure."
    
    # Fade out the scene and end the introductory level
    hide tutor_idle
    stop sound fadeout 3.0
    scene bg black with fade
    p "End of the introductory level. Thank you for playing!"

    return

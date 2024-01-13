from time import sleep
import pyttsx3


subtitle = ["\n", ":::       ::: ::::::::::: :::        :::::::::      :::    ::: :::    ::: ::::    ::: :::::::::::", ":+:       :+:     :+:     :+:        :+:    :+:     :+:    :+: :+:    :+: :+:+:   :+:     :+:", "+:+       +:+     +:+     +:+        +:+    +:+     +:+    +:+ +:+    +:+ :+:+:+  +:+     +:+", "+#+  +:+  +#+     +#+     +#+        +#+    +:+     +#++:++#++ +#+    +:+ +#+ +:+ +#+     +#+", "+#+ +#+#+ +#+     +#+     +#+        +#+    +#+     +#+    +#+ +#+    +#+ +#+  +#+#+#     +#+", " #+#+# #+#+#      #+#     #+#        #+#    #+#     #+#    #+# #+#    #+# #+#   #+#+#     #+#", "  ###   ###   ########### ########## #########      ###    ###  ########  ###    ####     ###"]

for i in subtitle:
    print(i)
    sleep(0.5)

def voice(message, voice_index=1, rate=170):
    engine = pyttsx3.init()

    try:
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[voice_index].id)
        engine.setProperty('rate', rate)

        print(f'{message}')
        engine.say(message)
        engine.runAndWait()

    except pyttsx3.EngineError as e:
        print(f'Error initializing the text-to-speech engine: {e}')
    except Exception as e:
        print(f'Error speaking the message: {e}')


def credits():
    sleep(2)
    print("\nBased on the game: The Witcher 3")
    sleep(2)
    print("By: CD Projekt Red")
    sleep(2)
    print("I present an RPG adventure developed entirely in text, \nDeveloped by a fan.")


def intro():
    sleep(5)
    voice("\nA war is happening between nations...")
    voice("\nAnd a girl carrying a mystery is fleeing from hunters. \nThe only person who can give her a clue continues to evade.")
    sleep(2)
    voice("\nIn the present day\n")
    voice("You arrive at a battlefield where warriors had clashed a few days ago.")
    voice("You find traces of the person you've been searching for, \nconcluding that she kept running in the direction she was heading, as if something were following her.")
    sleep(2)
    voice("\nWelcome to this story.")
    voice("You will experience the events of this world through the eyes of Geralt of Rivia.")
    voice("You can decide the course of events. \nEnjoy this journey...\n")

    sleep(4)
    voice("You and Master Vesemir decide to rest for the night.")
    voice("While sleeping, you dream of times at Kaer Morhen...\n")
    sleep(2)

    print("Yennefer of Vengerberg:")
    voice("   -You promised Ciri that you would train her.")
    voice("   Go, before Vesemir bores her to death with those drawings.\n")
    print("Geralt of Rivia:")
    voice("   -I thought Ciri could wait a little longer.\n", voice_index=2)
    print("Yennefer of Vengerberg:")
    voice("   -Nothing instructive. Not to mention it's irrational.")

    while True:
        print("\nEnter a option:")
        options = int(input("[ 1 ] I want to stay with you a little longer. \n[ 2 ] Let's be irrational. \n[ 3 ] You're right. I should go see Ciri. \nOption: "))
        if options == 1:
            print("Geralt of Rivia:")
            voice("   -I want to spend a bit more time with you.", voice_index=2)
            break
        elif options == 2:
            print("Geralt of Rivia:")
            voice("I don't want to be rational.", voice_index=2)
            break
        elif options == 3:
            print("Geralt of Rivia:") 
            voice("You're right. I should go see Ciri.", voice_index=2)
            break

    print("\nYennefer of Vengerberg:")
    voice("   -Aha! So that's the way the wind blows!")
    voice("   Go and train with her. Then come back. That will give me a chance to get ready.")
    print("\nGeralt of Rivia:")
    voice("   -Of all the women I know, you're the only one who does this before...", voice_index=2)
    print("\nYennefer of Vengerberg:")
    voice("   -You know many?")
    print("\nGeralt of Rivia:")
    voice("   -What's the problem? I've always thought of you.", voice_index=2)
    sleep(2)

def main():
    credits()
    intro()

if __name__ == "__main__":
    main()
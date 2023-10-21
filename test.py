def run_bojack_quiz():
    print("Welcome to my BoJack Horseman quiz!! :D")

    playing = input("Would you like to participate? ")

    if playing.lower() != "yes":
        quit()

    print("Great, let's begin! :)")

    questions = [
        {
            "question": "What is the name of BoJack Horseman's autobiography, which he struggles to write throughout the series?",
            "answers": {
                "a": "The Horse's Mouth",
                "b": "Horsin' Around: My Life in Hollywoo",
                "c": "BoJack Unleashed",
                "d": "Tales from the Stable"
            },
            "correct": "b"
        },
        {
            "question": "What's Mr. Peanutbutter's signature catchphrase?",
            "answers": {
                "a": "What's the deal with airline food?",
                "b": "Oh no, what is this? A crossover episode?",
                "c": "It's a doggy-dog world!",
                "d": "I'm not a regular dog, I'm a cool dog."
            },
            "correct": "b"
        },
        {
            "question": "Princess Carolyn is known for juggling multiple tasks simultaneously. What's her favorite metaphor for multitasking?",
            "answers": {
                "a": "I'm like a cat in a yarn store.",
                "b": "I'm like a fish riding a bicycle.",
                "c": "I'm like a squirrel on an espresso binge.",
                "d": "I'm like a pizza delivery guy on roller skates."
            },
            "correct": "b"
        },
        {
            "question": "What is the name of the parody version of 'Hollywood' in the BoJack Horseman universe?",
            "answers": {
                "a": "Hollywoo",
                "b": "Hollyrock",
                "c": "Hollyweird",
                "d": "Hollyweed"
            },
            "correct": "a"
        },
        {
            "question": "Todd Chavez's accidental business 'WhatTimeIsItRightNow.com' was so brilliant that even an owl couldn't keep up. What does the website actually do?",
            "answers": {
                "a": "Tells you the time, but in rhymes",
                "b": "Shows you random celebrity wristwatches",
                "c": "Simply displays the current time",
                "d": "Gives you pointless facts about time, like how long you've been wasting it"
            },
            "correct": "c"
        },
        {
            "question": "The legendary actor and method acting enthusiast BoJack once partied with is a bigger deal than a Hollywood blockbuster. Who is it?",
            "answers": {
                "a": "Character Actress Margo Martindale",
                "b": "Daniel Radcliffe",
                "c": "Zach Galifianakis",
                "d": "Method Man"
            },
            "correct": "b"
        },
        {
            "question": "What is the name of the seahorse character who serves as a lawyer in the BoJack Horseman world?",
            "answers": {
                "a": "Stephen Seahorseberg",
                "b": "Lawyer Larry the Seahorse",
                "c": "Gloria the Galloping Seahorse",
                "d": "Judge Jaws"
            },
            "correct": "a"
        },
        {
            "question": "What's the name of the reality TV show that Princess Carolyn becomes briefly obsessed with, featuring squids and their drama-filled lives?",
            "answers": {
                "a": "Squid Dynasty",
                "b": "Squidwives of the Deep",
                "c": "Squidzillionaire Matchmaker",
                "d": "Squid Game of Thrones"
            },
            "correct": "a"
        },
        {
            "question": "BoJack's favorite drink is 'The BoJack,' a cocktail more potent than a breakup. What's in it?",
            "answers": {
                "a": "Whiskey, regret, and a dash of lemon",
                "b": "Vodka, self-loathing, and a twist of lime",
                "c": "Rum, nostalgia, and a cherry on top",
                "d": "Tequila, poor life choices, and a sombrero"
            },
            "correct": "b"
        },
        {
            "question": "What is the name of the '90s sitcom that made BoJack Horseman famous and was a recurring theme throughout the series?",
            "answers": {
                "a": "Family Ties but with more horseplay",
                "b": "Horsin' Around for both kids and adults",
                "c": "Hollywood Squares starring animals",
                "d": "BoJack's Backyard Adventures with a hint of animal mischief"
            },
            "correct": "b"
        }
    ]

    for question_data in questions:
        print(question_data["question"])
        answers = question_data["answers"]
        correct_answer = question_data["correct"]

        for key, value in answers.items():
            print(f"{key}) {value}")

        chances = 3

        while chances > 0:
            answer = input("You have 3 chances! Good luck: ").lower()

            if answer in answers and answers[answer] == answers[correct_answer]:
                print(f"Correct! '{answers[correct_answer]}' is the right answer.")
                break
            else:
                print("Sorry, that's not the correct answer.")
                chances -= 1

        if chances == 0:
            print("You've used all your chances. Game over.")

    print("Congratulations! You've completed my first quiz!")

run_bojack_quiz()

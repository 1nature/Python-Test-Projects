def guess_number():
    try:
        import random
        condition = False
        lower_choice = int(input("Enter the lower bound number: "))
        upper_choice = int(input("Enter the upper bound number: "))
        system_choice = random.randint(lower_choice, upper_choice)
        print(f"system_choice is: {system_choice}")
        counter = 0
        attempts = 7
        while not condition:
            counter += 1
            user_guess = int(input("Make a guess: "))
            if user_guess == system_choice:
                print(f"Guess {counter}: {user_guess} → Correct!")
                condition = True
                if condition == True or counter == attempts:
                    break
            elif user_guess > system_choice:
                print(f"Guess {counter}: {user_guess} → Too high")
            else:
                print(f"Guess {counter}: {user_guess} → Too low")
    except Exception as e:

        print("An exception occurred.")




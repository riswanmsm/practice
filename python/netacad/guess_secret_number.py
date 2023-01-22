def guess_secret_number():
    
    secret_number = 777

    print(
    """
    +================================+
    | Welcome to my game, muggle!    |
    | Enter an integer number        |
    | and guess what number I've     |
    | picked for you.                |
    | So, what is the secret number? |
    +================================+
    """)
    
    # take input from user
    guessed_number = int(input("Enter your guessed number: "))
    
    # loop while the guess is not equl to secret
    while guessed_number != secret_number:
        
        # if the user stacked in the loop display a message
        print("Ha ha! You're stuck in my loop!")
        # if the guessed number is not equal to secret number, ask again
        guessed_number = int(input("Enter your guessed number: "))
    
    # If the number guessed matches the secret number display secret number and a message
    print("The secret number was:", secret_number)
    print("Well done, muggle! You are free now.")

guess_secret_number()

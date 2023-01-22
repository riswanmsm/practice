def madlib():
    print("""
+================================+
| Welcome to Madlib game!        |
| Enter an adjective             |
| and a noun once asked and get  |
| what the phrase picked for you.|
| So, Lets get started!          |
+================================+
    """)

    # stories = [
    #     {"phrase": "There is more than one way to _(VERB)_ a/an _(NOUN)_", "missing": ["VERB", "NOUN"]}
    # ]

    # print(stories[0])

    # get a word for verb from user
    verb = input('Enter a verb: ')
    # get a word for noun from user
    noun = input('Enter a noun: ')

    # combine user input with the story and display
    print("There is more than one way to", verb, noun)

madlib()
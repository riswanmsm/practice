def odd_even_counter():
    # take a number as user input
    number = int(input('Enter a number to continue or 0 to exit: '))
    # initialize odd and even counters with 0
    odd_counter = even_counter = 0
    # loop and take number until user enters 0
    while number:
        
        if number % 2:
            # if the number is odd increase odd counter by one
            odd_counter += 1
        else:
            # if the number is even increase even counter by one
            even_counter += 1
        
        # take a number as user input
        number = int(input('Enter a number to continue or 0 to exit: '))
    
    # print the odd counter and even counter
    print("Number of odd numbers entered: ", odd_counter, "\n", "Number of even numbers entered: ", even_counter, sep="") 

odd_even_counter()
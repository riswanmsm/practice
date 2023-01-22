import time

def counter(times):
    # Write a for loop that counts to five.
    for count in range(1,times + 1):
        # Body of the loop - print the loop iteration number and the word "Mississippi".
        print(count, 'Mississippi')
        # Body of the loop - use: time.sleep(1)
        time.sleep(1)

    # Write a print function with the final message.
    print("Ready or not, here I come!")

def game(times = 3):
    # take the times need to say mississippi and say it in console 
    # take one second to pronounce one mississippi
    for i in range(times):    
        for char in "Mississippi":
            print(char)
            time.sleep(0.091)
        print(i + 1, 'seconds gone')
    # print a message after count finish
    print("Ready or not, here I come!")

counter(5)
game(5)
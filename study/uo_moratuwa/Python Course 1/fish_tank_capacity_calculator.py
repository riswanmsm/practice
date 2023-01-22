"""
A program which can calculate the water capacity of a fish tank
inputs: length, width and height of the tank
outputs: the volume of water the tank can hold
"""

def display_instructions():
    print("\n\n\t\t#########################################################################")
    print("\t\t#                                                                       #")
    print("\t\t# This program calculates the volume of water a fish tank can hold.     #")
    print("\t\t#                                                                       #")
    print("\t\t# Enter the length, width and height of the tank in metres / cm / feet. #")
    print("\t\t#                                                                       #")
    print("\t\t# The volume will be displayed in litres.                               #")
    print("\t\t#                                                                       #")
    print("\t\t#########################################################################\n\n")

def calculate_volume(length, width, height, unit):
    if unit == "m":
        volume = length * width * height * 1000
    elif unit == "cm":
        volume = (length / 10) * (width / 10) * (height / 10)
    elif unit == "ft":
        volume = length * width * height / 0.035315
    else:
        print("Invalid unit of measurement.")
        volume = 0
    return volume

def main():
    # get the length, width and height of the tank
    unit = input("Enter the unit of measurement (m, cm, ft): ")
    length = float(input("Enter the length of the tank: "))
    width = float(input("Enter the width of the tank: "))
    height = float(input("Enter the height of the tank: "))

    # calculate the volume of water the tank can hold
    volume = calculate_volume(length, width, height, unit)

    # display the volume
    print("\t\t#########################################################################")
    print("\t\t#                                                                       #")
    print(f"\t\t#\t The volume of water the tank can hold is: {volume:.5f} litres.  #")
    print("\t\t#                                                                       #")
    print("\t\t#########################################################################")

if __name__ == "__main__":
    display_instructions()
    main()
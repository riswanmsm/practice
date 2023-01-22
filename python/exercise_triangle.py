
def two_sided_triangle(width_of_triangle):
    for x in range(width_of_triangle):
        stars = ''
        for y in range(x+1):
            spaces = ''
            for z in range(width_of_triangle-x):
                spaces += ' '
            stars += '* '
        print(spaces + stars)
    for x in range(width_of_triangle):
        stars = ''
        for y in range(width_of_triangle-(x+1)):
            spaces = ''
            for z in range(x+1):
                spaces += ' '
            stars += ' *'
        print(spaces + stars)

def left_sided_triangle(width_of_triangle):
    for x in range(width_of_triangle):
        stars = ''
        for y in range(x+1):
            stars += '* '
        print(stars)

def right_sided_triangle(width_of_triangle):
    for x in range(width_of_triangle):
        stars = ''
        for y in range(width_of_triangle):
            if y >= width_of_triangle - (x+1):
                stars += ' *'
            else:
                stars += '  '
        print(stars)

def find_largest(list):
    if list:
        largest = list[0]
        for element in list:
            if element > largest:
                largest = element
        print(f'the largest element in {list} is: {largest}')
    else:
        print('list is empty...')


find_largest([1,2,3,20,4,-90,0.5])


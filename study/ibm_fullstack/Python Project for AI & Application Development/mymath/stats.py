def mean(numbers):
    """
    This function returns the mean of the given list of numbers
    """
    total = 0
    num_of_elements = 0

    for number in numbers: 
        total += number
        num_of_elements += 1
    
    return total / num_of_elements

def median(numbers):
    """
    This function returns median of the given list of numbers
    """
    num_of_elements = len(numbers)
    center_position = num_of_elements // 2
    if num_of_elements % 2: # odd numbers
        return numbers[center_position]
    else:
        sum_of_two_mids = numbers[center_position - 1] + numbers[center_position]
        return sum_of_two_mids / 2 
        

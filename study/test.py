def mysplit(strng):
    
    temp_str = strng.strip()
    space_index = temp_str.find(' ')
    result = []

    while space_index != -1:
        result.append(temp_str[:space_index])
        temp_str = temp_str[space_index + 1:]

        space_index = temp_str.find(' ')

    if temp_str != "":
        result.append(temp_str)

    return result


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
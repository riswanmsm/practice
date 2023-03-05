import urllib.request

# url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
# filename = 'Example1.txt'
# # it will download the file from the given url
# urllib.request.urlretrieve(url, filename)

example_file_name = "Example1.txt"
# Open file using with


def open_file_normally():

    # Read the Example1.txt
    file1 = open(example_file_name, "r")
    file_content = file1.read()

    # It is very important that the file is closed in the end. This frees up resources and ensures consistency across different python versions.
    file1.close()

    print(file_content)

    print(file1.name)  # it will give the name of the file opened
    print(file1.mode)  # it will show the mode in which the file opened
    # type of the file content it will be string for all normally
    print(type(file_content))


def open_file_properly(example_file_name):
    with open(example_file_name, "r") as file1:
        fileContent = file1.read()

    print(fileContent)

    # The file automatically closed if open using with. We can verify if by running below which will show True
    print(file1.closed)


def read_portion_eachline():
    """
    it will read portion of the length provided in the file
    """
    file_content = []
    with open(example_file_name, "r") as file:
        file_content.append(file.read(4))  # Reads first 4 charactors
        file_content.append(file.read(4))  # Reads next 4 charactors

    print(file_content)


# read_portion_eachline()

# Read one line
def read_oneline():
    with open(example_file_name, "r") as file1:
        print(file1.readline())

# We can also pass an argument to  readline()  to specify the number of charecters we want to read. However, unlike  read(),  readline() can only read one line at most.


def read_number_of_chars_in_one_line():
    with open(example_file_name, "r") as file1:
        # does not read past the end of line if chars are less than 20 then it reads only available chars and stop
        print(file1.readline(20))
        print(file1.read(20))  # Returns the next 20 chars

# Iterate through the lines


def iterate_reading():
    with open(example_file_name, "r") as file1:
        i = 0
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1

# Read all lines and save as a list


def get_file_to_list():
    with open(example_file_name, "r") as file1:
        FileasList = file1.readlines()

    print(FileasList)  # it will print a list containing all the lines


# write line to file
def write_file():
    '''
    if no file then it will create 
    if file exist previous content will be deleted and new content will be written
    '''
    exmp2 = 'Example2.txt'
    with open(exmp2, 'w') as writefile:  # if no file in such name it will create one and write
        writefile.write("This is line A")


# write_file()
# open_file_properly('Example2.txt')
# with open('Example2.txt', 'a') as testwritefile:
#     testwritefile.write("This is line C\n")
#     testwritefile.write("This is line D\n")
#     testwritefile.write("This is line E\n")

with open('Example2.txt', 'r+') as testwritefile:
    print(testwritefile.tell())
    data = testwritefile.readlines()
    print(data)
    print(testwritefile.tell())
    testwritefile.seek(0, 0)  # write at beginning of file

    testwritefile.write("Line 111" + "\n")
    testwritefile.write("Line 112" + "\n")
    testwritefile.write("Line 113" + "\n")
    # testwritefile.write("finished\n")
    # Uncomment the line below
    # testwritefile.truncate()
    testwritefile.seek(0, 0)
    print(testwritefile.read())

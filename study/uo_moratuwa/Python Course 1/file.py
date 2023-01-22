fhandle = open("file1.txt")
line_1 = fhandle.readline()
line_2 = fhandle.readline()
fhandle.close()

fhandle = open("file2.txt", "w")
fhandle.write(line_1 +  line_2)

fhandle = open("file2.txt")
fcontent = fhandle.read()
print(fcontent)
fhandle.close()

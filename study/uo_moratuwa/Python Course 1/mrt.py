val = int(input())
for x in range (0, val):
    for y in range(0, val):
        print('*',end='')
    print()



i = int(input())
j = 2 # fix the code (1) 
while (j <= (i/j)):
    if not(i%j): 
        print("not a prime")
        break # fix the code (2)
    j = j + 1 # fix the code (3)
if (j > i/j): 
    print ("prime")

def sqr(n):
    return n ** 2

# File handling /////
fhandle = open("file1.txt")
line_1 = fhandle.readline()
line_2 = fhandle.readline()
fhandle.close()

fhandle = open("file2.txt", "w")
fhandle.write(line_1 + line_2)

fhandle = open("file2.txt")
fcontent = fhandle.read()
fhandle.close()

print(fcontent)

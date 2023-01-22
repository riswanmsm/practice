# hotel consisting of three buildings, 15 floors each. There are 20 rooms on each floor
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

# check if there are any vacancies on the 15th floor of the third building: 

vacancy = 0

for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1
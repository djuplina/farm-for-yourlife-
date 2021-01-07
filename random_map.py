import random

#reset map data
open('map-test.txt', 'w').close()
#set map index
index = 15
#loop and generate a map


while index > 0:
    f = open('map-test.txt', "a")
    f.write(str(random.randint(0,1)))
    f.write(str(random.randint(0,1)))
    f.write(str(random.randint(0,1)))
    f.write(str(random.randint(0,1)))
    f.write(str(random.randint(0,1)))
    f.write(str(random.randint(0,1)))
    f.write(str(random.randint(0,1)))
    f.write(str(random.randint(0,1)))
    f.write(str(random.randint(0,1)))
    f.write(str(random.randint(0,1)))
    index -= 1
    f.write('\n')
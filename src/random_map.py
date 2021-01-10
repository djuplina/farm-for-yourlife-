import random
import os

# curr_path = os.path.dirname(__file__)
# assets_path = os.path.join(curr_path, "assets")
# map_path = os.path.join(f"{assets_path}", "map.txt")

def main():

    #reset map data
    # open(f"{map_path}", 'w').close()
    #set map index
    i1 = 10
    seed = ""
    #loop and generate a map


    while i1 > 0:
        i2 = 8
        while i2 > 0:
            seed += (str(random.randint(1,2)))
            i2 -= 1
        i1 -= 1
        seed += "\n"
    return seed
        # f = open(f"{map_path}", "a")
        # f.write(str(random.randint(1,2)))
        # f.write(str(random.randint(1,2)))
        # f.write(str(random.randint(1,2)))
        # f.write(str(random.randint(1,2)))
        # f.write(str(random.randint(1,2)))
        # f.write(str(random.randint(1,2)))
        # f.write(str(random.randint(1,2)))
        # f.write(str(random.randint(1,2)))
        # index -= 1
        # f.write('\n')


main()
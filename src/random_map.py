import random
import os

curr_path = os.path.dirname(__file__)
assets_path = os.path.join(curr_path, "assets")
map_path = os.path.join(f"{assets_path}", "map.txt")

def main():

    #reset map data
    open(f"{map_path}", 'w').close()
    #set map index
    index = 10
    #loop and generate a map


    while index > 0:
        f = open(f"{map_path}", "a")
        f.write(str(random.randint(1,3)))
        f.write(str(random.randint(1,3)))
        f.write(str(random.randint(1,3)))
        f.write(str(random.randint(1,3)))
        f.write(str(random.randint(1,3)))
        f.write(str(random.randint(1,3)))
        f.write(str(random.randint(1,3)))
        f.write(str(random.randint(1,3)))
        index -= 1
        f.write('\n')

main()
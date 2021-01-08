import random
import os

curr_path = os.path.dirname(__file__)  # Where your .py file is located
assets_path = os.path.join(curr_path, "assets")  # The assets folder path
map_path = os.path.join(f"{assets_path}", "map.txt")

def main():

    #reset map data
    open(f"{map_path}", 'w').close()
    #set map index
    index = 18
    #loop and generate a map


    while index > 0:
        f = open(f"{map_path}", "a")
        f.write(str(random.randint(0,3)))
        f.write(str(random.randint(0,3)))
        f.write(str(random.randint(0,3)))
        f.write(str(random.randint(0,3)))
        f.write(str(random.randint(0,3)))
        f.write(str(random.randint(0,3)))
        f.write(str(random.randint(0,3)))
        f.write(str(random.randint(0,3)))
        f.write(str(random.randint(0,3)))
        f.write(str(random.randint(0,3)))
        f.write(str(random.randint(0,3)))
        f.write(str(random.randint(0,3)))
        f.write(str(random.randint(0,3)))
        f.write(str(random.randint(0,3)))
        f.write(str(random.randint(0,3)))
        f.write(str(random.randint(0,3)))
        index -= 1
        f.write('\n')

main()
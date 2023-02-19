


def main():
    lego_height = 0
    lego_length = 0
    shape = 0

    welcome()

    lego_height = lego_piece_height()
    lego_length = lego_piece_length()
    lego_width =  lego_piece_width()
    shape = pick_a_shape()
    if shape == 1:
        find_wall(lego_height, lego_length)
    elif shape == 2:
        find_floor(lego_length, lego_width)


# welcome message
def welcome():
    print ("Hey there! Welcome to CalcuBrick!")
    print ("************************************************************")
    print ("Demystifying how many legos you need for your build!")
    print ("************************************************************")
    print()


def lego_piece_height():
    # find lego brick height
    lego_brick_height = 1
    lego_plate_height = (1*3)
    while True:
        try:
            lego_height = int(input("Are you using:\nBricks (1)\nor\nPlates (2)?\n"))
            if lego_height == 1:
                lego_height = lego_brick_height
                return lego_height
            elif lego_height == 2:
                lego_height = lego_plate_height
                return lego_height
            else:
                print("Select either bricks or plates.")
        except:
            print ("Remember to use numbers (1 or 2) \nLet's try that again.")

def lego_piece_length():
    # Find lego brick length
    while True:
        try:
            lego_length = int(input("What is the unit length of the lego are you building with?\n"))
            if lego_length <= 22 and lego_length > 0:
                return lego_length
            elif lego_length >22:
                print("Those are pretty big bricks. Let's try something smaller.")
            else:
                print ("We are building with legos in a 3-dimensional world. Try a number between 1 and 22.")
        except:
            print ("Remember we are trying to find the dimensions of the lego and we are using numbers. Put in how many units long it is:")

def lego_piece_width():
    # Find lego brick length
    while True:
        try:
            lego_width = int(input("What is the unit width of the lego are you building with?\n"))
            if lego_width<= 22 and lego_width > 0:
                return lego_width
            elif lego_width > 22:
                print("Those are pretty big bricks. Let's try something smaller.")
            else:
                print("We are building with legos in a 3-dimensional world. Try a number between 1 and 22.")
        except:
            print(
                "Remember we are trying to find the dimensions of the lego and we are using numbers. Put in how many units wide it is:")

def pick_a_shape():
    # which shape to build
    while True:
        try:
            which_struct = int(input("What kind of structure are you looking to build? \nType the corresponding number below: \nwall (1)\nor\nfloor (2)\n\n"))
            if which_struct == 1:
                return which_struct
            if which_struct == 2:
                return which_struct
            else:
                options = input("You need to choose 1 or 2 to choose a structure. Would you like to try a different structure instead? (yes or no)\n")
                if options == ("yes" or "Yes" or "y" or "Y"):
                    main()
                if options == "1":
                    which_struct = 1
                    return which_struct
                if options == "2":
                    which_struct = 2
                    return which_struct
                else:
                    print ("Hope to see you again. Goodbye!")
                    return False
        except:
            print("We are trying to determine the structure you want to build. Use the numbers that correspond to the shape.")

def find_wall(lego_height, lego_length):
    some_num = True
    while some_num == True:
        try:
            print ("\nLets find a wall!\n")
            wall_length = int(input("How many units long do you want your wall to be?\n"))
            if wall_length > 0:
                wall_height = int(input("How many units tall do you want your wall to be?\n"))
                if wall_height > 0:
                    needed_for_height = lego_height * wall_height
                    needed_for_length = float(wall_length/lego_length)
                    print ("Your wall will be ", needed_for_height, "legos tall.")
                    print ("Your wall will be ", needed_for_length, "legos long.")
                    some_num = False
                else:
                    print("Type a number bigger than zero for wall height:")
            else:
                print("Type a number bigger than zero for wall length:")
        except:
            print ("whole numbers please!")
    total_legos_needed = needed_for_length * needed_for_height

    print("You might still need to cut your legos into tiny pieces, but theoretically you would need",
          total_legos_needed, "legos to complete your", wall_length, "by",
          wall_height, " wall.")

# *************************** need to fix calculation
def find_floor(lego_length):
    some_num = True
    lego_width = 0
    while some_num  == True:
        try:
            print("Awesome, let's find a floor!")
            dimensions_wide = int(input("How wide do you want your floor?"))
            dimensions_length = int(input ("How long do you want your floor?"))
            some_num = False
        except:
            print ("your responses should be be whole numbers. Try it again:")
    print ("ok, so you want a", dimensions_wide, "by", dimensions_length, "floor.")
    print ("for a floor you also need to know how wide your legos are.")
    lego_width = int(input("how wide are each of your legos?"))
    build_dimension = dimensions_length * dimensions_wide
    print ("That means that you will need ", ((dimensions_wide * dimensions_length)/(lego_piece_length * lego_piece_width)), "legos ")



# CELLS = 20
#
#
# def inventory():
#     brick_height = [0] * CELLS
#     brick_length = [0] * CELLS
#     brick_width = [0] * CELLS
#     brick_num = [0] * CELLS  # individual bricks of the one type
#     shape_height = 0
#     shape_length = 0
#     shape_width = 0
#
#     cell_count = 0  # how many cells total
#     brick_total = 0  # how many bricks total
#
#     welcome()
#     more = 'y'
#
#     while more == 'y':
#         brick_num[cell_count] = get_brick_count()
#         brick_total = brick_total + brick_num[cell_count]
#         brick_height[cell_count] = get_brick_height()
#         brick_length[cell_count] = get_brick_length()
#         brick_width[cell_count] = get_brick_width()
#         more = more_bricks()
#         cell_count = cell_count + 1
#
#     print("Ok, let's build something cool. Today, it's a cube.\n")
#     shape_height = get_shape_height()
#     shape_length = get_shape_length()
#     shape_width = get_shape_width()
#     print_summary(cell_count, brick_num, brick_total, brick_height,
#                   brick_length, brick_width, shape_height, shape_length,
#                   shape_width)

# ************************************************ need to make into another method
# def welcome():
#     print("Hey there lego builders!")
#     print("It’s time to see what you have in stock to build something cool.")


def get_brick_count():
    while True:
        try:
            bc = int(input("How many bricks do you have?\n"))
            return bc
        except:
            print("Whoops, try a whole number:")


def get_brick_height():
    while True:
        try:
            bh = int(input("How tall are your bricks?\n"))
            return bh
        except:
            print("Whoops, try a whole number:")


def get_brick_length():
    while True:
        try:
            bl = int(input("How long are your bricks?\n"))
            return bl
        except:
            print("Whoops, try a whole number:")


def get_brick_width():
    while True:
        try:
            bw = int(input("How wide are your bricks?\n"))
            return bw
        except:
            print("Whoops, try a whole number:")


def get_shape_height():
    while True:
        try:
            sh = int(input("How tall do you want your cube to be?\n"))
            return sh
        except:
            print("Whoops, try a whole number:")


def get_shape_length():
    while True:
        try:
            sl = int(input("How long do you want your cube to be?\n"))
            return sl
        except:
            print("Whoops, try a whole number:")


def get_shape_width():
    while True:
        try:
            sw = int(input("How wide do you want your cube to be?\n"))
            return sw
        except:
            print("Whoops, try a whole number:")


def more_bricks():
    while True:
        try:
            more_bricks = str(input("Do you have more bricks? (y or n)\n"))
            if more_bricks == "y":
                return str(more_bricks)
            if more_bricks == 'n':
                return str(more_bricks)
            else:
                print("'y' for yes or 'n' for no")
        except:
            print("letters 'y' or 'n' only please")


def print_summary(cell_count, brick_num, brick_total, brick_height,
                  brick_length, brick_width, shape_height, shape_length,
                  shape_width):
    count = 0
    print("You have a total of", brick_total, "bricks for your", shape_height,
          "x", shape_width, "x", shape_length, "cube.")
    print("Here is your inventory:\n")
    print("Qty       height       length       width ")
    print("-----------------------------------------")
    while count < cell_count:
        print(brick_num[count], "        ", brick_height[count], "         ",
              brick_length[count], "          ", brick_width[count])
        count = count + 1

main()


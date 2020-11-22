# ascii-art.py

def draw_box(boxSize=10):
    for i in range(0, boxSize):
        if i == 0 or i == (boxSize - 1):
            print("*" * boxSize)
        else:
            print("*" + " " * (boxSize - 2) + "*")

def draw_box_diagonal(boxSize=10):
    middle_row = ['' for i in range(boxSize)]
    for i in range(0, boxSize):
        if i == 0 or i == (boxSize - 1):
            print("*" * boxSize)
        else:
            for pos in middle_row_position:
                if pos == 0 or pos ==  boxSize - 1 or pos == i:
                    print("*", end = "")
                else:
                    print(" ", end = "")

# Not really ascii art but still loop practice

def words_on_seperate_lines(sent):
    for character in sent:
        if character == " ":
            print("\n")
        else:
            print(character, end="")

def words_on_seperate_lines_2(sent):
    for each in sent.split():
        print(each)

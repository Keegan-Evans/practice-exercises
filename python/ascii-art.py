# ascii-art.py

def draw_box(boxSize=10):
    for i in range(0, boxSize):
        if i == 0 or i == (boxSize - 1):
            print("*" * boxSize)
        else:
            print("*" + " " * (boxSize - 2) + "*")

def draw_box_diagnol(boxSize=10):
    for i in range(0, boxSize):
        if i == 0 or i == (boxSize - 1):
            print("*" * boxSize)
        else:
            print("*" + " " * (boxSize - 2) + "*")

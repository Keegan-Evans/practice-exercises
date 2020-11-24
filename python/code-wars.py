# Tower Builder Kata
def tower_builder(n_floors):
    building_half = (n_floors - 1) 
    floor_blank = lambda flr: " " * (building_half - flr)
    floor_build = lambda flr: "*" * flr 

    floors = []
    for i in range(n_floors):
        floors.append(floor_blank(i) + floor_build(i) + "*" + floor_build(i) + floor_blank(i))
        
    return floors

# best evaluated for kata

def tower_builder_best(n):
    return[("*" * (i*2-1)).center(2*n-1) for i in range(1, n+1)]

# Binary array to number
def binary_array_to_number(arr):
    arr.reverse()
    num = 0
    for pos in range(len(arr)):
       num += arr[pos] * 2**pos 
    return(num)

# Binary Array to Number -more compact

def bin2num_comp(arr):
    from functools import reduce
    arr.reverse()
    return(reduce(lambda a, x : a + x, [arr[i] * 2**i for i in range(len(arr))], 0))
    
# Binary Array to Number Top Solution

def binary_array_to_number_best(arr):
  return int("".join(map(str, arr)), 2)

# https://www.codewars.com/kata/53af2b8861023f1d88000832/train/python
# Are you playing banjo?

def areYouPlayingBanjo(name):
    return "{} {}".format(
        name,
        "plays banjo" if name.lower().startswith("r") else "does not play banjo"
    )
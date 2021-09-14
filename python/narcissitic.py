class show_digits:
    def __init__(self, func):
        self.func = func
    def __call__(self, arg):
        print(arg)
        print(self.func(arg))

@show_digits
def narcissistic(value):
    digits = [int(dig) for dig in str(value)]
    cnt = len(digits)
    total = 0

    while digits:
        total += digits.pop() ** cnt
    
    narc = value == total

    return narc, total


if __name__ == '__main__':

    narcissistic(153)

    narcissistic(23)

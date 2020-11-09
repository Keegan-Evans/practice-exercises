msg = "hello world"
print(msg)

def cap_each(sent):
    new = []
    for word in list(sent):
        new.append(word.capitalize)
    return new

capMsg = cap_each(msg)
print(capMsg)

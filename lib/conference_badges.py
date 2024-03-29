def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]

def assign_rooms(names):
    return [f"Hello, {name}! You'll be assigned to room {index +1}!" for index,name in enumerate(names) if index < 8]

def printer(names):
    [print(x) for x in batch_badge_creator(names)]
    [print(x) for x in assign_rooms(names)]

if __name__ == "__main__":
    printer(["simon", "simon"])
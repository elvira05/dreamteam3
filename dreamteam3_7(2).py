#wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]

def wave(string):
    arr = []
    a = 0
    while a < len(string):
        arr.append(string[:a] + string[a::].title())
        a += 1
    print(arr)

wave('hello')
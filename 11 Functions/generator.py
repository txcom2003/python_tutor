def generator(max):
    i = 0
    while i < max :
        yield i
        i += 1

for i in generator(25):
    print(i)
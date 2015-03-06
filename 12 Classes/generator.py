class inclusive_range:
    def __init__(self, *args):
        arg_cnt = len(args)
        if arg_cnt == 0:
            raise TypeError('No arguments')
        elif arg_cnt == 1:
            self.stop = args[0]
            self.start = 0
            self.step = 1
        elif arg_cnt == 2:
            (self.start, self.stop) = args
            self.step = 1
        elif arg_cnt == 3 :
            (self.start, self.stop, self.step) = args
        else:
            raise TypeError('Too much arguments')

    def __iter__(self):
        i = self.start
        while(i<=self.stop):
            yield i
            i += self.step

for n in inclusive_range(1,25,3) :
    print n,
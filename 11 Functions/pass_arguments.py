
def pass_arguments(this, that, *args, **kwargs):
    print(this,that, args)
    print(kwargs)

pass_arguments(1,2,3,4, one = 1, two = 2, three = 3)

# Function arguments basics:

# Keyword arguments : kwargs is keyword arguments for variable number of arguments

def print_key_value(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


def print_values(**kwargs):
    for key, val in kwargs.items():
        print(val)


def var_num_arguments(*args):
    for arg in args:
        print(arg)


if __name__ == '__main__':
    print_key_value(first='Hello, ', mid='Good ', last='Morning')
    print_values(first="Hello", second="Good", third="Evening")
    # Variable number of arguments
    var_num_arguments("Have a", " Good ", "Day")

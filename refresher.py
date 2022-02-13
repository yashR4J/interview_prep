def exceptionCheck(num):
    try:
        num = int(num) 
        if num < 0 or num > 1:
            print("what's going on")
    except TypeError:
        raise TypeError("Don't act smart with me!")
    except:
        pass
    finally:
        pass

if __name__ == '__main__':
    print("Hi, this document is a python refresher doc", end="!\n")
    name = input("Give me your name: ")
    print(f"It's nice to meet you {name}!")

    while True:
        num = input("Pick a number between 0 and 1: ")
        exceptionCheck(num)
        num = int(num)
        break

    # Ternary operators
    res = "yay!" if num == 1 else "nay!"  
    print(f"{res}")
    
    list_one = [] # lists store sequences
    list_two = [1, 2, 3]

    list_one.append(1)
    list_one.append(2)
    list_one.append(3)

    list_two.pop()
    list_two.append(3)

    assert(list_one[0] == 1)
    assert(list_two[0:2] == list_one[0:2])

    # Tuples

    # You can unpack tuples (or lists) into variables
    a, b, c = (1, 2, 3)  # a is now 1, b is now 2 and c is now 3
    # You can also do extended unpacking
    a, *b, c = (1, 2, 3, 4)  # a is now 1, b is now [2, 3] and c is now 4
    # Tuples are created by default if you leave out the parentheses
    d, e, f = 4, 5, 6  # tuple 4, 5, 6 is unpacked into variables d, e and f

    # Dictionaries

    # Dictionaries store mappings from keys to values
    empty_dict = {}
    # Here is a prefilled dictionary
    filled_dict = {"one": 1, "two": 2, "three": 3}

    # Keys in dictionaries must be immutable -- so ints, floats, strings and tuples
    # Look up values with []
    filled_dict["one"]  # => 1

    list(filled_dict.keys())
    list(filled_dict.values())

    # Check for existence of keys in a dictionary with "in"
    "one" in filled_dict  # => True
    1 in filled_dict      # => False

    # "setdefault()" inserts into a dictionary only if the given key isn't present
    filled_dict.setdefault("five", 5)  # filled_dict["five"] is set to 5
    filled_dict.setdefault("five", 6)  # filled_dict["five"] is still 5

    # Adding to a dictionary
    filled_dict.update({"four":4})  # => {"one": 1, "two": 2, "three": 3, "four": 4}
    filled_dict["four"] = 4         # another way to add to dict

    # Remove keys from a dictionary with del
    del filled_dict["one"]  # Removes the key "one" from filled dict

    for animal in ["dog", "cat", "mouse"]:
        # You can use format() to interpolate formatted strings
        print("{} is a mammal".format(animal))

    for i in range(4): # 1, 2, 3, 4
        print(i, end=" ")
    print()
    for i in range(4, 8): # 4, 5, 6, 7
        print(i, end=" ")
    print()
    for i in range(4, 8, 2): # 4, 6
        print(i, end=" ")
    print()

    # # Writing to a file
    # contents = {"aa": 12, "bb": 21}
    # with open("myfile1.txt", "w+") as file:
    #     file.write(str(contents))        # writes a string to a file

    # with open("myfile2.txt", "w+") as file:
    #     file.write(json.dumps(contents)) # writes an object to a file

    # # Reading from a file
    # with open('myfile1.txt', "r+") as file:
    #     contents = file.read()           # reads a string from a file
    # print(contents)
    # # print: {"aa": 12, "bb": 21}

    # with open('myfile2.txt', "r+") as file:
    #     contents = json.load(file)       # reads a json object from a file
    # print(contents)
    # # print: {"aa": 12, "bb": 21}

    # You can define functions that take a variable number of
    # positional arguments
    def varargs(*args):
        return args

    varargs(1, 2, 3)  # => (1, 2, 3)

    # You can define functions that take a variable number of
    # keyword arguments, as well
    def keyword_args(**kwargs):
        return kwargs

    # Let's call it to see what happens
    keyword_args(big="foot", loch="ness")  # => {"big": "foot", "loch": "ness"}

    # Function Scope
    x = 5

    def set_x(num):
        # Local var x not the same as global variable x
        x = num    # => 43
        print(x)   # => 43

    def set_global_x(num):
        global x
        print(x)   # => 5
        x = num    # global var x is now set to 6
        print(x)   # => 6

    set_x(43)
    set_global_x(6)

    # Python has first class functions
    def create_adder(x):
        def adder(y):
            return x + y
        return adder

    add_10 = create_adder(10)
    add_10(3)   # => 13

    # There are also anonymous functions
    (lambda x: x > 2)(3)                  # => True
    (lambda x, y: x ** 2 + y ** 2)(2, 1)  # => 5

    # There are built-in higher order functions
    list(map(add_10, [1, 2, 3]))          # => [11, 12, 13]
    list(map(max, [1, 2, 3], [4, 2, 1]))  # => [4, 2, 3]

    list(filter(lambda x: x > 5, [3, 4, 5, 6, 7]))  # => [6, 7]

    # We can use list comprehensions for nice maps and filters
    # List comprehension stores the output as a list which can itself be a nested list
    [add_10(i) for i in [1, 2, 3]]         # => [11, 12, 13]
    [x for x in [3, 4, 5, 6, 7] if x > 5]  # => [6, 7]

    # You can construct set and dict comprehensions as well.
    {x for x in 'abcddeef' if x not in 'abc'}  # => {'d', 'e', 'f'}
    {x: x**2 for x in range(5)}  # => {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

    # You can import modules
    from math import sqrt as root
    print(root(16))  # => 4.0

    # Decorators
    # In this example `beg` wraps `say`. If say_please is True then it
    # will change the returned message.
    from functools import wraps


    def beg(target_function):
        @wraps(target_function)
        def wrapper(*args, **kwargs):
            msg, say_please = target_function(*args, **kwargs)
            if say_please:
                return "{} {}".format(msg, "Please! I am poor :(")
            return msg

        return wrapper


    @beg
    def say(say_please=False):
        msg = "Can you buy me a beer?"
        return msg, say_please


    print(say())                 # Can you buy me a beer?
    print(say(say_please=True))  # Can you buy me a beer? Please! I am poor :(
        
    from collections import deque # FIFO

    queue = deque(["Eric", "John", "Michael"])
    queue.append("Terry")
    queue.popleft() # 'Eric'
    
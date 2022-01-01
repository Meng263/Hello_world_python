def function_1(x): return x ** 2


def function_2(x): return x ** 3


def function_3(x): return x ** 4


def function_4(x): return x ** 5


def runCallbacks():
    callbacks = [function_1, function_2, function_3]
    print('nNamed Functions: ')
    for function in callbacks: print('Result:', function(3))
    callbacks = [lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** 4]
    dict = {"key1": "value"}
    for functions in callbacks: print('Result:', function(3))
    for key in dict.values(): print(key)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    runCallbacks()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

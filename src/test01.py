# To exit Python, you can enter exit(), quit(), or select Ctrl-Z
# cd source
# \automatizing\src> python test01.py > food_directory.txt
# \automatizing\src> python test01.py >> food_directory.txt     appends
# clear; python test01.py :-) clears the console

import os
import sys

sys.path.append("/foo_load_path") # This will add the foo directory to the list of paths to look for modules in as well.

print("start **********************************************")

def do_string():
    print("- Hello World")

    name = "World"
    print("- Hello, %s!" % name)
    age = 23
    print("- Hello %s is %d years old." % (name, age))

    # https://www.learnpython.org/en/Basic_String_Operations

    # %s - String (or any object with a string representation, like numbers)
    # %d - Integers
    # %f - Floating point numbers
    # %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
    # %x/%X - Integers in hex representation (lowercase/uppercase)
    # This prints out: A list: [1, 2, 3]
    mylist = [1,2,3]
    lengthOfList = len(mylist)
    print("- A list: %s is %d long" % (mylist, lengthOfList )) # from the "repr" method of object array


    astring = "Hello world!"
    print("in",astring,'- o in', astring.index("o"))
    print("3 to 7 is: '"+astring[3:7]+"'")
    print(astring[::-1]) # reverse :-)
    print(astring.upper())
    print(astring.lower())
    print("startswith Hello?", astring.startswith("Hello"))
    print("endswith x?", astring.endswith("asdfasdfasdf"))

    afewwords = astring.split(" ")
    print("split", afewwords)


# https://www.learnpython.org/en/Conditions
def do_conditions():
    name = "John"
    age = 23
    if name == "John" and age == 23:
        print("Your name is John, and you are also 23 years old.")

    if name == "John" or name == "Rick":
        print("Your name is either John or Rick.")

    if name in ["John", "Rick"]:
        print("Your name is either John or Rick.")


    statement = False
    another_statement = True
    if statement is True:
        # do something
        pass
    elif another_statement is True: # else if
        # do something else
        pass
    else:
        # do another thing
        pass

    x = 2
    if x == 2:
        print("x equals two!")
    else:
        print("x does not equal to two.")


    x = [1,2,3]
    y = [1,2,3]
    print(x == y) # Prints out True,   same value ?
    print(x is y) # Prints out False,  same instance?

    print((not False) == (False)) # Prints out False


def do_loops():
    primes = [2, 3, 5, 7]
    for prime in primes:
        print('for in obj:',primes,':', prime)

    # Prints out the numbers 0,1,2,3,4
    for x in range(5):
        print('for in range5', x)

    # Prints out 3,4,5
    for x in range(3, 6):
        print('for in range(3,6)',x)

    # Prints out 3,5,7
    for x in range(3, 8, 2):
        print('for x in range(3, 8, 2)',x)

    # Prints out 0,1,2,3,4

    count = 0
    while count < 5:
        print('while count < 5',count)
        count += 1  # This is the same as count = count + 1

    count = 0
    while True:
        print('break',count)
        count += 1
        if count >= 5:
            break

    # Prints out only odd numbers - 1,3,5,7,9
    for x in range(10):
        # Check if x is even
        if x % 2 == 0:
            continue
        print('continue',x)


    # Prints out 0,1,2,3,4 and then it prints "count value reached 5"

    count=0
    while(count<5):
        print(count)
        count +=1
    else:
        print("count value reached %d" %(count))

    # Prints out 1,2,3,4
    for i in range(1, 10):
        if(i%5==0):
            break
        print(i)
    else:
        print("this is not printed because for loop")
        print("is terminated because of break but")
        print("not due to fail in condition")


def do_classes():
    class MyClass:
        variable = "blah"

        def function(self):
            print("This is a message inside the class.")

    myobjectx = MyClass()
    myobjecty = MyClass()

    myobjecty.variable = "yackity"

    # Then print out both values
    print(myobjectx.variable)
    print(myobjecty.variable)
    myobjectx.function()


def do_dictionaries():
    phonebook = {
        "John" : 938477566,
        "Jack" : 938377264,
        "Jill" : 947662781
    }
    phonebook["Jillo"] = 947662782
    phonebook["Jack"] = 888888888

    del phonebook["John"] # removes
    phonebook.pop("Jill") # removes

    print(phonebook)

    for name, number in phonebook.items():
        print("Phone number of %s is %d" % (name, number))

def do_module():
    visual_mode = True
    if visual_mode:
        # in visual mode, we draw using graphics
        import module01 as helper
    else:
        # in textual mode, we print out text
        import module02 as helper

    result = helper.calculate_result()

    from module02 import draw_game
    draw_game(result)


    # import mi_package_01.module01 as xxx
    from mi_package_01 import p01module01
    p01module01.do_x()

def do_module2():

    import re

    # Your code goes here
    find_members = []
    for member in dir(re):
        if "find" in member:
            find_members.append(member)

    print(sorted(find_members))

def do_regexp():
    import re
    pattern = re.compile(r"\[(on|off)\]") # Slight optimization
    print(re.search(pattern, "Mono: Playback 65 [75%] [-16.50dB] [on]"))
    # Returns a Match object!
    print(re.search(pattern, "Nada...:-("))
    # Doesn't return anything.
    # End Example

def do_file_manipulation_copy():
    import shutil
    source = '../test_cases/karma.conf.test_subject_01.js'
    # destination = '../dev_folder'
    destination = '../dev_folder/karma.conf.test_subject_01.backup.js'
    # shutil.move('../test_cases/test_subject_01.json', '../dev_folder')
    new_path = shutil.copy(source, destination )
    print('copied: %s to --> %s' %(source, new_path))

def do_file_manipulation_lineReplace():
    import fileinput
    import re

    pattern = re.compile(r"^(.*)ChromeHeadless(.*)$")
    filename = '../test_cases/karma.conf.test_subject_01.js'

    for line in fileinput.input([filename], inplace=True):
        # if line.strip().startswith('initial_mass = '):
        match = re.match(pattern, line)
        if match:
            line = match.group(1) + 'Chrome' + match.group(2) + '\n'
        sys.stdout.write(line)




def main():
    # do_string()
    # do_conditions()
    # do_loops()
    # do_classes()
    # do_dictionaries()
    # do_module()
    # do_module2()
    # do_regexp()
    # do_file_manipulation_copy()
    do_file_manipulation_lineReplace()





print("end ************************************************")

# this means that if this script is executed, then
# main() will be executed
if __name__ == '__main__':
    main()

# module02.py
# import the draw module



numberOfTimesRun = 0

def draw_game(result):
    print("moduleo2.draw_game called! wit result: %s, times: %d" %(result, numberOfTimesRun))


class Screen():
  className = 'Screen'
  numberOfTimesRun = numberOfTimesRun + 1
  print('I %s class have been initialized %d times' % (className, numberOfTimesRun))

# The first time a module is loaded into a running Python script, it is
# initialized by executing the code in the module once. If another module in
# your code imports the same module again, it will not be loaded twice but
# once only - so local variables inside the module act as a "singleton" -
# they are initialized only once.

# This is useful to know, because this means that you can rely on this
# behavior for initializing objects.

# initialize main_screen as a singleton
main_screen = Screen()

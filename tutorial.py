import curses
# note that the wrapper initializes various stdout settings to 
# use the terminal  see this section in module tuorial: 
# https://docs.python.org/3/howto/curses.html#starting-and-ending-a-curses-application
from curses import wrapper

def main(stdscr):
    #stdscr is an object representing the full terminal screen
    stdscr.clear()
    #write to the screen, placing the first char at row, column
    row = 10
    column = 10
    stdscr.addstr(row, column, "Hello World 1")
    row = 15
    column = 15
    stdscr.addstr(row, column, "Hello World 2")
    #now overwrite some of the chars.  note that the letters
    #not written over will remain
    row = 15
    column = 11
    stdscr.addstr(row, column, "OVERWRITE")
    stdscr.refresh()
    #end program when any key is pushed
    stdscr.getch()

# wrapper will initialize within a try/except block
# making debugging easier.
wrapper(main)
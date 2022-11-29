import curses
# note that the wrapper initializes various stdout settings to 
# use the terminal  see this section in module tuorial: 
# https://docs.python.org/3/howto/curses.html#starting-and-ending-a-curses-application
from curses import wrapper

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_RED)
    red_text = curses.color_pair(1)
    #stdscr is an object representing the full terminal screen
    stdscr.clear()

    test_str = "The quick brown fox jumped over the lazy dog."
    
    user_str = ""
    while True:
        #write to the screen, placing the first char at row, column
        stdscr.addstr(0,0, test_str)
        stdscr.refresh()
        key = stdscr.getkey()
        user_str += key
        for i, c in enumerate(user_str):
            if c != test_str[i]:
                stdscr.attron(red_text)
                stdscr.addstr(2,i, c)
                stdscr.attroff(red_text)
            else:
                stdscr.addstr(2,i, c)
        stdscr.refresh()


# wrapper will initialize within a try/except block
# making debugging easier.
wrapper(main)
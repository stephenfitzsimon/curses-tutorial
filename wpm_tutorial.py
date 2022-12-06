import curses
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("This is a wpm test program.")
    stdscr.addstr("\nPress any key to begin...")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target_text, current_text, wpm = 0):
    stdscr.addstr(target_text)
    for i, char in enumerate(current_text):
        stdscr.addstr(0, i, char, curses.color_pair(1))
    

def wpm_test(stdscr):
    target_text = "Hello World! This is example text"
    current_text = []
    while True:
        stdscr.clear()
        display_text(stdscr, target_text, current_text)
        # stdscr.addstr(target_text)
        # for char in current_text:
        #     stdscr.addstr(char, curses.color_pair(1))
        stdscr.refresh()

        key = stdscr.getkey()

        if ord(key) == 27:
            break
        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        else:
            current_text.append(key)     

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    wpm_test(stdscr)

wrapper(main)
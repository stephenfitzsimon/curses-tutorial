import curses
from curses import KEY_ENTER, wrapper

MENU_OPTS = ['Choose Text', 'Practice a Text', 'Exit']
LINES_TO_DISPLAY = 5

def main(stdscr):

    #default to start at the first menu option
    current_row_i = 0
    current_text = None
    #print the menu
    print_menu(stdscr, current_row_i)
    while True:
        curses.curs_set(0) #remove the cursor
        #key listens for the user to press a key
        key = stdscr.getch()
        #clear the screen
        stdscr.clear()

        #determine the currently selected menu item or if the user 
        #has pressed enter
        if key == curses.KEY_UP and current_row_i > 0:
            current_row_i -= 1
        elif key == curses.KEY_DOWN and current_row_i < len(MENU_OPTS) - 1:
            current_row_i += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if MENU_OPTS[current_row_i] == 'Exit':
                #user selected exit, end the program at key press
                break
            elif MENU_OPTS[current_row_i] == 'Choose a Text':
                pass
                #current_text = choose_text(stdscr)
            elif MENU_OPTS[current_row_i] == 'Practice a Text':
                practice_text(stdscr)
        
        #print the menu with the currently selected item
        print_menu(stdscr, current_row_i)
        #refresh the screen
        stdscr.refresh()

def print_menu(stdscr, selected_row_i):
    '''
    Prints a menu to the screen
    Args:
        stdscr : curses screen object produced by curses.wrapper()
        selected_row_i : the user's currently selected row
    '''
    #clear the screen
    stdscr.clear()
    #get the size of the screen
    h, w = stdscr.getmaxyx()
    #set up the highlight color for the currently selected option
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    select_color = curses.color_pair(1)

    # center the menu vertically.  this represents the row in the terminal
    # where the first menu option should be
    start_row = h//2 - len(MENU_OPTS)//2
    for i, option in enumerate(MENU_OPTS):
        #center the current option horizontally
        x = w//2 - len(option)//2
        # place the string vertically
        y = start_row + i
        if i == selected_row_i:
            # the current row is selected by the user, 
            # highlight it.
            stdscr.attron(select_color)
        # print the string to the screen
        stdscr.addstr(y, x, option)
        stdscr.attroff(select_color)
    #refresh the screen
    stdscr.refresh()

def practice_text(stdscr):
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_GREEN)
    wrong_color = curses.color_pair(2)
    right_color = curses.color_pair(3)
    txt = get_text('example_text.txt')
    current_line_idx = 0
    user_text = []
    while True and current_line_idx < len(txt):
        curses.curs_set(1)
        # display the lines up to the testing line
        if current_line_idx < LINES_TO_DISPLAY:
            start = 0
        else:
            start = current_line_idx - LINES_TO_DISPLAY
        prev_lines = txt[start:current_line_idx]
        current_line = txt[current_line_idx]
        
        
        while True:
            stdscr.clear()
            for i, text_line in enumerate(prev_lines):
                stdscr.addstr(i+1, 0, text_line)

            key = stdscr.getkey()
            user_text.append(key)

            for c in user_text:
                user_str = ''.join(user_text)

            stdscr.addstr(7, 0, user_str)
            stdscr.refresh()
            if key == KEY_ENTER or key in [10, 13]:
                break
            
        current_line_idx += 1

def get_text(filename):
    txt = ['Beginning']
    with open(filename) as f:
        txt += [l for l in f]
    return txt

if __name__=='__main__':
    wrapper(main)
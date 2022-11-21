import curses
from curses import wrapper

MENU_OPTS = ['Choose Text', 'About', 'Exit']

def main(stdscr):
    curses.curs_set(0) #remove the cursor

    #default to start at the first menu option
    current_row_i = 0
    #print the menu
    print_menu(stdscr, current_row_i)
    while True:
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
            #user pressed enter, show what item was selected
            #clear the screen
            stdscr.clear()
            #display a string with the menu item
            stdscr.addstr(0, 0, f"You choose {MENU_OPTS[current_row_i]}")
            #refresh to display current string
            stdscr.refresh()
            #listen for a key press
            stdscr.getch()
            if MENU_OPTS[current_row_i] == 'Exit':
                #user selected exit, end the program at key press
                break
        
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

if __name__=='__main__':
    wrapper(main)
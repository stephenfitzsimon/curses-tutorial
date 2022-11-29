from scripture_memory import LINES_TO_DISPLAY


LINES_TO_DISPLAY = 5

def main():
    txt = get_text('example_text.txt')
    current_line_idx = 1
    while current_line_idx < len(txt):
        if current_line_idx < LINES_TO_DISPLAY:
            start = 0
        else:
            start = current_line_idx - LINES_TO_DISPLAY
        prev_lines = txt[start:current_line_idx]
        current_line = txt[current_line_idx]

        print(''.join(prev_lines))
        while True:
            print(f"\nCurrent line: {current_line}")
            user_text = input("Enter the next line:")
            if user_text == current_line:
                print("That's the correct line!")
                break

        current_line_idx += 1

def get_text(filename):
    txt = ['Beginning\n']
    with open(filename) as f:
        txt += [l for l in f]
    return txt

if __name__=='__main__':
    main()
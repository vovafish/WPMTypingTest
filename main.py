import curses
from curses import wrapper


def start_screen(stdsrc):
    stdsrc.clear()
    stdsrc.addstr("Welcome to the Speed Typing Test!")
    stdsrc.addstr("\nPress any key to begin!")
    stdsrc.refresh()
    stdsrc.getkey()


def main(stdsrc):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_WHITE)

    start_screen(stdsrc)


wrapper(main)

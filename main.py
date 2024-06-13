import curses
from curses import wrapper


def main(stdsrc):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_WHITE)

    stdsrc.clear()
    stdsrc.addstr(0, 0, "Hi World!")
    stdsrc.refresh()
    key = stdsrc.getkey()
    print(key)


wrapper(main)

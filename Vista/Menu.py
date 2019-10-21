import curses
import os
import sys

from Controlador import Bulk
from Controlador.client import Client

jsonTxt = ""
menu = ['Send', 'Received', 'Reports', 'Exit']


def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(menu):
        x = w // 2 - len(row) // 2
        y = h // 2 - len(menu) // 2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()


def print_center(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w // 2 - len(text) // 2
    y = h // 2
    stdscr.addstr(y, x, text)
    stdscr.refresh()


def main(stdscr):
    # turn off cursor blinking

    global jsonTxt
    curses.curs_set(0)

    # color scheme for selected row
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # specify the current selected row
    current_row = 0

    # print the menu
    print_menu(stdscr, current_row)

    while 1:
        try:
            key = stdscr.getch()

            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
                current_row += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                print_center(stdscr, "You selected '{}'".format(menu[current_row]))
                stdscr.getch()
                # Bulk
                if current_row == 0:
                    clear = lambda: os.system('cls')
                    clear()
                    sys.stdout.flush()
                    g = input()
                    Bulk.readCSV(g)
                # Players
                if current_row == 1:
                    n = Bulk.dll.start_node

                    print_center(stdscr, "<<" + n.hash + ">>")
                    while 1:
                        key = stdscr.getch()
                        if key == curses.KEY_RIGHT:
                            n = n.prev
                            if n is not None:
                                print_center(stdscr, "<<    " + n.hash + "   >>")
                            else:
                                n = n.pref
                        elif key == curses.KEY_LEFT:
                            n = n.pref
                            if n is not None:
                                print_center(stdscr, "<<    " + n.hash + "   >>")
                            else:
                                n = n.prev
                        elif key == curses.KEY_ENTER or key in [10, 13]:
                            jsonTxt = n.item
                            break
                if current_row == 2:
                    try:
                        while 1:
                            print_center(stdscr, "F2: Tree, F3: Pre-Order,  F4: In-Order, F5: Post-Order ")
                            key = stdscr.getch()
                            if key == curses.KEY_F2:
                                Bulk.ReadBlockJson(jsonTxt)
                                break
                            elif key == curses.KEY_F3:
                                Bulk.Orders(jsonTxt, 1)
                                break
                            elif key == curses.KEY_F4:
                                Bulk.Orders(jsonTxt, 2)
                                break
                            elif key == curses.KEY_F5:
                                Bulk.Orders(jsonTxt, 3)
                                break
                    except:
                        print_center(stdscr, 'Error whit this selection')
                        key = stdscr.getch()
                # if user selected last row, exit the program
                if current_row == len(menu) - 1:
                    break
            print_menu(stdscr, current_row)

        except:
            print_center(stdscr, 'Error')
            continue


curses.wrapper(main)

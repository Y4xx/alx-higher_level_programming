#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    while i < x:
        try:
            print(f"{my_list[i]}", end="")
        except IndexError:
            break
        else:
            i += 1
    print()
    return (i)

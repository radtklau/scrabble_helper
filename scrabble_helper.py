import regex as re
from tkinter import *
from ui import *

if __name__ == "__main__":
    root = Tk()
    user_interface = Ui(root)

    l = input("please enter max length of the word: ")
    r = input("please enter restrictions (e.g. 2a4v): ")
    r_nums = [e for e in re.split("[^0-9]", r) if e != '']

    r_max_num = max(map(int, r_nums))

    with open('wordlist-german.txt') as wl:
        lines = [line.rstrip() for line in wl]

    candidates = []
    f = 0
    for word in lines:
        if len(word) > int(l) or len(word) < r_max_num:
            continue
        for i,ch in enumerate(r):
            if i % 2 != 0:
                continue     
            if word[int(ch) - 1] != r[i + 1]:
                f = 1
                break
        if f == 1:
            f = 0 
            continue
        candidates.append(word)

    print(candidates)

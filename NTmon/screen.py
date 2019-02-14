screen_data = {"title":"NTmon"}

def printscrn(screen):
    print("\033[1;2f", end="")
    for i,line in enumerate(screen):
        print(f"\033[{i + 2};2f{screen[line]}                                    ", end="")
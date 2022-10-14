import sys , os
def clear():
    if sys.platform == "win32":
        os.system("cls")
    if sys.platform == "linux":
        os.system("clear")
    elif sys.platform != "linux" and sys.platform   != "win32":
        sys.exit()
        print("[ ! ] Platform Not Supported")
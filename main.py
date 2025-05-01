from tkinter import Tk
from gui.login_window import Login_window


def main():
    root = Tk()
    app = Login_window(root)
    root.mainloop()


if __name__ == "__main__":
    main()
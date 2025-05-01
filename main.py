from gui import login_dialog
import tkinter as tk

def main():
    root = tk.Tk()
    app = login_dialog.LoginWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()

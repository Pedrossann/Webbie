import tkinter as tk
import App_classes as cls
import os


"""
Runs the program

"""
def main():
    files_list = os.listdir(os.getcwd()+"\Saves")

    root = tk.Tk()
    root.geometry("1200x600")
    root.title("my App")
    root.configure(bg="#484848")

    main_frame = cls.Main_Frame(root)
    main_frame.pack()

    main_grid(main_frame, files_list)

    root.mainloop()


"""
main_grid sorts and then creates frames and grids of the separate files in the folder Saves

input: window = frames will be created in this variable
input: files_list = list of names of csv files in the folder Saves
"""
def main_grid(window, files_list):

    for list in sorted(files_list):
        file_name, dead_end = list.split(".")

        file_name = cls.File_Frame(window, file_name)
        file_name.pack(anchor="w")


if __name__ == "__main__":
    main()

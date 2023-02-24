import tkinter as tk
import os
import csv
import webbrowser as wb


"""
Main frame holds all widgets and frames in the program

input: the_window = where frame is created
"""
class Main_Frame(tk.Frame):
    def __init__(self, the_window):
        tk.Frame.__init__(self, the_window)
        self["bg"]="#BA6000"


"""
Creates frames with names of the files in Saves folder. Then starts and ends Buttons grid

input: the_window = where are frames created
input: file_name = inputs already sorted separated names of the csv files
"""
class File_Frame(tk.Frame):
    def __init__(self, the_window, file_name):
        tk.Frame.__init__(self, the_window)
        self["bg"]="#BA6000"
        self["padx"]=20
        self["pady"]=20

        self.b_open = False
        self.name_button = tk.Button(self,
                                    text=file_name,
                                    font= "10",
                                    width= 90,
                                    height=2,
                                    command= lambda file_name=file_name: self.button_open(self.b_open, the_window, file_name))
        self.name_button.pack()


#open or closes grid of buttons by clicking on the name of the file button
    def button_open(self, b_open, window, file_name):
        self.button = b_open
        if self.b_open == True:
            self.b_open = False
            self.my_grid.grid_destroy(file_name)

        else:
            self.b_open = True
            self.my_grid = Buttons(self, file_name)


"""
Creates grid of buttons, that after clicking open saved web

input: the_window = where are buttons created
input: file_name = name of the file
"""
class Buttons(tk.Button):
    def __init__(self, the_window, file_name):
        tk.Button.__init__(self, the_window)

        _row, _column = 1, -1
        self.button_frame = tk.Frame(the_window, bg="#BA6000")
        self.button_frame.pack(anchor="w")

        self.buttons = []

        with open(f"Saves/{file_name}.csv") as file:

            lines = csv.DictReader(file)

            for line in sorted(lines, key=lambda sor:sor["name"]):

                _row, _column = self.counter(_row, _column)

                self.buttons.append(My_Button(self.button_frame, line, _row, _column, file_name))

            Add_Button(self.button_frame, _row, _column +1, file_name)


    def grid_destroy(self, file_name):
        self.button_frame.destroy()



#counts rows and columns of the separate grids
    def counter(self, _row, _column):
        if _column < 5:
            _column+=1
            return _row, _column
        else:
            _column = 0
            _row +=1
            return _row, _column


"""
Creates separate image buttons that open web after pressing

:input: line = sorted line from csv file
:input: _row, _column = on what row and column in grid should button be added
"""
class My_Button(tk.Button):
    def __init__(self, master, line, _row, _column, file_name):
        tk.Button.__init__(self, master)

        self.image =  tk.PhotoImage(file = os.getcwd() + f"\Images\{line['image']}")

        self["height"] = 250
        self["width"] = 160
        self["anchor"] = "s"
        self["bg"] = "#484848"
        self["pady"] = 10
        self["image"] = self.image
        self["command"] = lambda line=line: wb.open(line["web"])

        self.grid(row=_row, column=_column, sticky="w")

        self.label = tk.Label(master, text=f"{line['name']}", anchor= "s", font= "20", bg="#484848", foreground="#BA6000")
        self.label.grid(row=_row, column=_column, sticky= "s", pady= 20)




"""
Button for adding another information to csv file

input: the_window = where is button created
input: _row = row in the grid where button is created
input: _column = column of the grid where button is created
input: file_name = leads the save in which csv file it should save information
"""
class Add_Button(tk.Button):
    def __init__(self, the_window, _row, _column, file_name):
        tk.Button.__init__(self, the_window)
        self["text"] = "Add"
        self["command"] = lambda self=self: Add_Grid(file_name)
        self["width"] = 5
        self["height"] = 5

        self.grid(row=_row, column=_column, padx= 50, pady= 50)


"""
creates new window in which we can add another buttons to grid

input: file_name = passes the program in which csv file it should save the data
"""
class Add_Grid:
    def __init__(self, file_name):
        self.add_window = tk.Tk()
        self.add_window.eval('tk::PlaceWindow . center') #learn


        name_l = My_Label(self.add_window, "Name: ", 0, 0)
        web_l = My_Label(self.add_window, "Web link: ", 1, 0)
        image_l = My_Label(self.add_window, "Image name:", 2, 0)

        self.name_e = My_Entry(self.add_window, 0, 1)
        self.web_e = My_Entry(self.add_window, 1, 1)
        self.image_e = My_Entry(self.add_window, 2, 1)

        add_button = tk.Button(self.add_window, text="add", command= lambda name_l=name_l: self.close_save(file_name))
        add_button.grid(row= 3, column= 1)

        self.add_window.mainloop()

    def close_save(self, file_name):
        self.name_e = self.name_e.get()
        self.web_e = self.web_e.get()
        self.image_e = self.image_e.get()

        with open(f"Saves\{file_name}.csv", "a") as file:
            file.write(f"{self.name_e},{self.web_e},{self.image_e}.png\n")

        self.add_window.destroy()


"""
Universal label creator

input: the_window = where it should create
input: text = text of the label
input: _row, _column = row and column where it should create the label in the grid
"""
class My_Label(tk.Label):
    def __init__(self, the_window, text, _row, _column):
        tk.Label.__init__(self, the_window)
        self["text"] = text
        self["anchor"] = "e"

        self.grid(row=_row, column=_column, sticky="nsew")


"""
Universal Entry creator

input: the_window = where it should create
input: _row, _column = row and column where it should create the Entry in the grid
"""
class My_Entry(tk.Entry):
    def __init__(self, the_window, _row, _column):
        tk.Entry.__init__(self, the_window)

        self.grid(row=_row, column=_column)

    def __str__(self):
        return self.get

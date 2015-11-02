#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

This program shows a simple
menu. It has one command, which
will terminate the program, when
selected.

author: Jan Bodnar
last modified: December 2010
website: www.zetcode.com
"""

from Tkinter import Tk, Frame, Menu, BOTH, Text, Menu, END
from Tkinter import *
from tkFileDialog import askopenfilename
from multilistbox import  MultiListbox



class Program(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):

        self.parent.title("Typesetting")

        self.min_margin = 10
        self.max_margin = 100
        self.margin_value = self.min_margin

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.openfile)
        fileMenu.add_command(label="Clear", command=self.clear_text)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", menu=fileMenu)

        grid = Frame(self.parent)
        left_grid = Frame(grid)
        w_list_label = Label(left_grid,text="Lista de palabras")
        w_list_label.pack(side=TOP)
        self.w_list = MultiListbox(left_grid,(("Palabra",20),("Longitud",10)))
        self.w_list.insert(1,("bocachancla",len("bocachancla")))
        self.w_list.pack(side=BOTTOM,fill=BOTH,expand=TRUE)
        left_grid.pack(side=LEFT,fill=BOTH,expand=TRUE)


        right_grid = Frame(grid)
        up_grid = Frame(right_grid)
        margin_label = Label(up_grid,text="Margen")
        margin_label.pack(side=LEFT,expand=TRUE)
        self.margin_scale = Scale(up_grid,orient=HORIZONTAL,showvalue=0,\
            variable=self.margin_value,from_=self.min_margin,to=self.max_margin)
        self.margin_scale.pack(side=LEFT)
        self.margin_spinbox = Spinbox(up_grid,\
            textvariable=self.margin_value,from_=self.min_margin,to=self.max_margin)
        self.margin_spinbox.pack(side=RIGHT)
        up_grid.pack(side=TOP)

        self.text = Text(right_grid)
        self.text.pack(side=BOTTOM,fill=BOTH,expand=TRUE)
        right_grid.pack(side=RIGHT,fill=BOTH)
        grid.pack(fill=BOTH, expand=YES)


    def onExit(self):
        self.quit()

    def openfile(self):
        filename = askopenfilename(parent=self.parent)
        lines = [line.rstrip('\n') for line in open(filename,'r')]
        words = []
        for line in lines:
           words.extend(line.split(' '))

        for word in words:
            self.insert_list(word)

        print words

    def clear_text(self):
        self.text.delete("%d.%d"%(0,0),END)
        self.clear_list()

    def insert_text(self,texto):
        self.text.insert(INSERT,texto)

    def clear_list(self):
        self.w_list.delete(0)
        pass

    def insert_list(self,word):
        self.w_list.insert(END,(word,len(word)))
        pass

def main():

    master = Tk()
    master.geometry("500x500+300+300")
    app = Program(master)
    master.mainloop()


if __name__ == '__main__':
    main()                  # Invoke the main event handling loop

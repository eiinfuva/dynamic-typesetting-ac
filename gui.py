#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Python implementation of Typesetting, Dynamic Programming

This program test the implementation software of Text justification at \'typesetting.py\'.
"""
__author__ =  'Ismael Taboada'
__version__=  '1.0'

from Tkinter import Tk, Frame, Menu, BOTH, Text, Menu, END
from Tkinter import *
from tkFileDialog import askopenfilename
from multilistbox import  MultiListbox
import tkMessageBox
from typesetting import typeset



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
        self.words = []

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.openfile)
        fileMenu.add_command(label="Clear", command=self.clear)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", menu=fileMenu)

        grid = Frame(self.parent)
        left_grid = Frame(grid)
        w_list_label = Label(left_grid,text="Lista de palabras")
        w_list_label.pack(side=TOP)
        self.w_list = MultiListbox(left_grid,(("Palabra",20),("Longitud",10)))
        self.w_list.pack(side=BOTTOM,fill=BOTH,expand=TRUE)
        left_grid.pack(side=LEFT,fill=BOTH,expand=TRUE)


        right_grid = Frame(grid)
        up_grid = Frame(right_grid)
        margin_label = Label(up_grid,text="Margen")
        margin_label.pack(side=LEFT,expand=TRUE)
        self.margin_scale = Scale(up_grid,orient=HORIZONTAL,showvalue=0,\
            variable=self.margin_value,from_=self.min_margin,to=self.max_margin,
            command=self.refresh_margin)
        self.margin_scale.pack(side=LEFT)
        self.margin_spinbox = Spinbox(up_grid,\
            textvariable=self.margin_value,from_=self.min_margin,to=self.max_margin)
        self.margin_spinbox.pack(side=LEFT)
        typeset_btn = Button(up_grid, text ="Typeset", command =self.typeset)
        typeset_btn.pack(side=RIGHT)
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
        self.words = []
        for line in lines:
           self.words.extend(line.split(' '))

        for word in self.words:
            self.insert_list(word)

    def refresh_margin(self,value):
        self.margin_value=value

    def get_margin(self):
        return int(self.margin_value)

    def typeset(self):
        try:
            self.clear_text()
            text = typeset(self.words,self.get_margin())
            self.insert_text(text)
        except IOError as e:
            tkMessageBox.showwarning(
            "Exception",
            e )

    def clear_text(self):
        self.text.delete("%d.%d"%(0,0),END)

    def insert_text(self,texto):
        self.text.insert(INSERT,texto)

    def clear_list(self):
        self.w_list.delete(0,END)
        pass

    def insert_list(self,word):
        self.w_list.insert(END,(word,len(word)))
        pass

    def clear(self):
        self.clear_list()
        self.clear_text()

def main():

    master = Tk()
    master.geometry("500x500+300+300")
    app = Program(master)
    master.mainloop()


if __name__ == '__main__':
    main()                  # Invoke the main event handling loop

import Functii as funct
import PySimpleGUI as sg


sg.theme("Reds")
layout=[sg.Text(funct.cpu),sg.Text(size=(15,1))]
window=sg.Window(layout)
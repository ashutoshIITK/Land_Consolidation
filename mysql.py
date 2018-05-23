import MySQLdb
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk, Entry
import re


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
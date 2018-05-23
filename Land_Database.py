import tkinter as tk
import tkinter.messagebox
import pymysql as psql
import MySQLdb as msql
import tkinter.messagebox as tm
from PIL import Image, ImageTk
from tkinter import ttk, Entry, messagebox, Label, Button, FALSE, Tk, Entry

from dateutil.tz import win, sys, time, datetime, os
from datetime import datetime

from autocomplete import Combobox_Autocomplete
from sqlquerry import query
from printform import *

# ----------------------For Login verification-----------------------------------#
# import pyrebase
# from requests import RequestException
# ------------------------------------End----------------------------------------#

import smtplib

# -------------------------Imports for plotting Shapefile------------------------#
import shapefile as shp
import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
# ------------------------------------End-----------------------------------------#

# ------------------------Import of things from other forms (Create)----------------#
from khatauni import khatauni_create
from form2A import form2a_create
from khasra import khasra_create
from ch_form_4a import ch_form_4a_create
from ch_form_4b import ch_form_4b_create
from ch_form_5_extract import chform_5_print
from form5_extract import form5_extract_create
from ch_form_11 import ch_form_11_create
from ch_form_23 import ch_form_23_create
from ch_form_41 import ch_form_41_create
from ch_form_45 import ch_form_45_create

#----------------Printing Forms------------------------------------#

from ch_2a_print import ch_2a_print




FMT = '%H:%M:%S'  # For finding the total time used in the application
entries = []
variables = []
array = []
label_in_forms = []
numcol = 0


def send_email(user, pwd, recipient, subject, body):
    import smtplib

    mail_user = 'askumar'
    mail_pwd = ''
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:

        server = smtplib.SMTP("smtp.cc.iitk.ac.in", 25)
        server.ehlo()
        server.starttls()
        server.login(mail_user, mail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')
    except smtplib.SMTPException as err:
        print(err)
        print("failed to send mail")


def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


class LandDatabase(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Land Consolidation")


        container = tk.Frame(self)


        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.shared_data = {
            "db_name": tk.StringVar(),
            "updatebox_value": tk.StringVar(),
            "insertbox_value": tk.StringVar()}

        self.frames = {}

        for F in (StartPage, PageTwo, PageThree, InputWindow):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, page_name):
        for frame in self.frames.values():
            frame.grid_remove()
        frame = self.frames[page_name]
        frame.grid()
        frame.winfo_toplevel().geometry("")

        menubar = frame.menubar(self)
        self.configure(menu=menubar)


        # ------------------- Login Screen Page ------------------------ #





"""class loginpage(tk.Frame):
    def __init__(self, master=None, width=0.8, height=0.6, useFactor=True):
        tk.Frame.__init__(self, master)
        self.pack()


# ---------------------Firebase Login Details----------------------#
def try_login():
    flag = 0
    config = {
        "apiKey": "AIzaSyDaXOxijAv9wTrbK-5ha68RmyTodKKSNi0",
        "authDomain": "landdatabase-1f5e8.firebaseapp.com",
        "databaseURL": "https://landdatabase-1f5e8.firebaseio.com",
        "storageBucket": "landdatabase-1f5e8.appspot.com"
    }
    global email
    email = username_guess.get()
    password = password_guess.get()
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        if ((user['idToken'] != None)):
            flag = 12

    except RequestException as err:

        print("Trying to login...")
    if (flag == 12):
        # if username_guess.get() == username and password_guess.get()== password :
        messagebox.showinfo("-- COMPLETE --", "You have now logged in.", icon="info")
        login.destroy()
    else:
        messagebox.showinfo("-- ERROR --", "Wrong credentials..Terminating!", icon="warning")
        login.destroy()
        sys.exit()


if __name__ == '__main__':

    login = tk.Tk()
    login.wm_title("Login Page")
    sp = loginpage(login)
    sp.grid()

    img = tk.PhotoImage(file="login.png")
    panel = tk.Label(sp, image=img)
    panel.grid(row=1, column=2, sticky='NE')
    username_text = Label(sp, text="Username:")
    username_guess = Entry(sp)
    password_text = Label(sp, text="Password:")
    password_guess = Entry(sp, show="*")
    attempt_login = Button(text="Login", command=try_login)

    # username_text.pack()     ------------ To speed up first page opening
    username_text.grid(row=0, column=0, sticky='n')
    username_guess.grid(row=0, column=1, sticky='n')
    password_text.grid(row=1, column=0, sticky='n')
    password_guess.grid(row=1, column=1, sticky='n')
    attempt_login.grid(row=2, column=0, sticky='w')


    # If the user tries to kill the window,we must stop our program
    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            login.destroy()
            sys.exit()


    login.protocol("WM_DELETE_WINDOW", on_closing)
    login.mainloop()
"""

# ------------------------End of Login Page-------------------#

# ------------------- Start Page ------------------------ #


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        gui_style = ttk.Style()
        gui_style.configure('My.TButton', foreground='#334353')
        gui_style.configure('My.TFrame', background='#334353')

        self.rowconfigure(0, weight=0)
        self.columnconfigure(0, weight=1)
        self.top = ttk.Frame(self, width=450, height=200, style='My.TFrame', padding=(5, 5, 5, 5))
        self.top.grid(row=0, column=0, sticky=(tk.N, tk.E, tk.S, tk.W))

        self.district = ttk.Label(self.top, text="जिला/District", width=15)
        self.district.grid(row=0, column=0, pady=15, padx=15)

        # -------------------- Combobox for districts in UP ------------------------#

        districts_values = ["Agra", "Firozabad", "Mainpuri", "Mathura", "Aligarh", "Etah", "Hathras", "Kasganj",
                            "Allahabaad", "Fatehpur", "Kaushambi", "Pratapgarh", "Azamgarh", "Ballia",
                            "Mau", "Budaun", "Bareilly", "Pilibhit", "Shahjahanpur", "Basti", "Sant Kabir Nagar",
                            "Siddharthnagar", "Banda", "Chitrakoot", "Hamirpur", "Mahoba", "Bahraich",
                            "Balarampur", "Gonda", "Shravasti", "Ambedkar Nagar", "Amethi", "Barabanki", "Faizabad",
                            "Sultanpur", "Deoria", "Gorakhpur", "Kushinagar", "Maharajganj", "Jalaun", "Jaunpur",
                            "Jhansi", "Lalitpur", "Auraiya", "Etawah", "Farrukhabad", "Kannauj", "Kanpur Dehat",
                            "Kanpur Nagar", "Hardoi", "Lakhimpur Kheri", "Lucknow", "Raebareli", "Sitapur",
                            "Unnao", "Bagpat", "Bulandshahr", "Gautam Buddha Nagar", "Ghaziabad", "Hapur", "Meerut",
                            "Mirzapur", "Sant Ravidas Nagar", "Sonbhadra", "Amroha", "Bijnor", "Moradabad", "Varanasi"
                                                                                                            "Rampur",
                            "Sambhal", "Muzaffarnagar", "Saharanpur", "Shamli", "Chandauli", "Ghazipur"]

        self.district_name = tk.StringVar()
        self.entry_district = ttk.Entry(self.top,textvariable=self.district_name)
        self.entry_district = Combobox_Autocomplete(self.top, districts_values, highlightthickness=0,
                                                    textvariable=self.district_name)
        self.entry_district.grid(row=0, column=1, pady=15, padx=15)

        self.paragana = ttk.Label(self.top, text="परगना/Paragana", width=15)
        self.paragana.grid(row=0, column=2, pady=15, padx=15)

        self.paragana_name = tk.StringVar()
        self.entry_paragana = ttk.Entry(self.top, textvariable=self.paragana_name)
        self.entry_paragana.grid(row=0, column=3, pady=15, padx=15)

        self.tehsil = ttk.Label(self.top, text="तहसील/Tehsil", width=15)
        self.tehsil.grid(row=1, column=0, pady=15, padx=15)

        self.tehsil_name = tk.StringVar()
        self.entry_tehsil = ttk.Entry(self.top, textvariable=self.tehsil_name)
        self.entry_tehsil.grid(row=1, column=1, pady=15, padx=15)

        self.village = ttk.Label(self.top, text="गांव/Village", anchor=tk.W, width=15)
        self.village.grid(row=1, column=2, pady=15, padx=15)

        self.village_name = tk.StringVar()
        self.entry_village = ttk.Entry(self.top, textvariable=self.village_name)
        self.entry_village.grid(row=1, column=3, pady=15, padx=15)

        new_order = (self.entry_district, self.entry_paragana, self.entry_tehsil,self.entry_village)
        for widget in new_order:
            widget.lift()


        self.connect = ttk.Button(self.top, text="संपर्क/Connect", command=self.message)
        self.connect.grid(row=0, column=4, pady=15, padx=15)

        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.original = Image.open('include\images\photo.jpg')
        self.image = ImageTk.PhotoImage(self.original)
        self.display = tk.Canvas(self, bd=0, highlightthickness=0)
        self.display.create_image(0, 0, image=self.image, anchor=tk.NW, tags="IMG")
        self.display.grid(row=1, sticky=tk.W + tk.E + tk.N + tk.S)
        self.bind("<Configure>", self.resize)

    time1 = time.strftime('%H:%M:%S')
    print(time1)

    # ---------------- resize for background image ------------------------#

    def resize(self, event):
        size = (event.width, event.height)
        resized = self.original.resize(size, Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized)
        self.display.delete("IMG")
        self.display.create_image(0, 0, image=self.image, anchor=tk.NW, tags="IMG")

    # ------------------ Menubar------------------------------------------ #

    def menubar(self, root):
        menubar = tk.Menu(root)

        filemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='File', menu=filemenu)
        filemenu.add_command(label='New', command='add function here')

        editmenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Edit', menu=editmenu)
        editmenu.add_command(label='Undo', command='add function here')
        return menubar

    # ------------------ Creating Database in MySql ---------------------- #

    def message(self):
        if (self.district_name.get() == "") | (self.tehsil_name.get() == "") | (
                    self.village_name.get() == "") | (self.paragana_name.get() == ""):
            tkinter.messagebox.showerror('', "Enter a valid entry")
            return
        self.controller.shared_data["db_name"].set(
            "land_records_" + self.district_name.get() + "_" + self.paragana_name.get() + "_" + self.tehsil_name.get() + "_" + self.village_name.get())
        db_name = self.controller.shared_data["db_name"].get()

        try:
            print(db_name)
            connection = msql.connect(host='localhost',user= 'root', db=db_name, charset='utf8')
            print("Databse already exists and connected")
        except:
            connection = msql.connect(host='localhost', user= 'root', charset='utf8')
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE `%s`" % db_name)
            print("New database created")

            connection = msql.connect(host='localhost',user= 'root', db=db_name, charset='utf8')
            cursor = connection.cursor()
            cursor.execute(query)

        self.controller.dbname = db_name
        self.controller.frames[PageTwo].passdbname()
        self.controller.show_frame(PageTwo)  # Page two is called using import function


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.rowconfigure(0, weight=0)
        self.columnconfigure(0, weight=1)

        style = ttk.Style()
        style.configure("TNotebook.Tab", padding=(10, 10), tabmargins=[2, 5, 2, 0])

        # --------------------------For viewing shapefile---------------------------#

        self.button = tk.Button(self, text="Click here to view map", bg='white',
                                command=lambda: self.controller.show_frame(PageThree))
        self.button.grid(row=3, column=0, sticky='W')

        # --------------------------For viewing Report---------------------------#

        # self.button1 = tk.Button(self, text="Progress Report", bg='white',
        #                         command=lambda: self.controller.show_frame(PageFour))
        # self.button1.grid(row=3, column=1, sticky='W')

        # ------------------------- Tab For Filling Form ---------------------- #

        self.notebook = ttk.Notebook(self, height=17)
        self.notebook.grid(row=0, column=0, sticky='NWES')

        self.fill_form = tk.Frame(self.notebook)
        self.notebook.add(self.fill_form, text='Fill Forms/ फॉर्म भरें')

        self.print_form = tk.Frame(self.notebook)
        self.notebook.add(self.print_form, text='Print Forms/ प्रिंट फॉर्म')

        self.print_receipts = tk.Frame(self.notebook)
        self.notebook.add(self.print_receipts, text='Print Receipts/ प्रिंट परची')

        self.insertbox_list = (
             'Khasra', 'Khatauni','C.H. Form 2-A', 'C.H. Form 4-A', 'C.H. Form 4-B', 'C.H. Form 5(Extract)',
             'C.H. Form 11', 'C.H. Form 23', 'C.H. Form 41', 'C.H. Form 45')

        self.fill_form.rowconfigure(0, weight=1)
        self.fill_form.columnconfigure(0, weight=1)

        self.print_form.rowconfigure(0, weight=1)
        self.print_form.columnconfigure(0, weight=1)

        self.print_receipts.rowconfigure(0, weight=1)
        self.print_receipts.columnconfigure(0, weight=1)

        self.listbox1 = tk.Listbox(self.fill_form, background='#99ccff')
        self.listbox1.grid(row=0, column=0, sticky=tk.NSEW, padx=5)

        self.listbox2 = tk.Listbox(self.print_form, background='#99ccff')
        self.listbox2.grid(row=0, column=0, sticky=tk.NSEW, padx=5)

        for i in range(0, 10):
            self.listbox1.insert(tk.END, self.insertbox_list[i])
            self.listbox2.insert(tk.END, self.insertbox_list[i])

        self.listbox1.bind("<Double-1>", lambda x: self.go_to_inputwindow_page())
        self.listbox1.bind('<Enter>', self.snapHighlightToMouse)
        self.listbox1.bind('<Motion>', self.snapHighlightToMouse)
        self.listbox1.bind('<Leave>', self.unhighlight)

        self.listbox2.bind("<Double-1>", lambda x: self.go_to_printform_page())
        self.listbox2.bind('<Enter>', self.snapHighlightToMouse)
        self.listbox2.bind('<Motion>', self.snapHighlightToMouse)
        self.listbox2.bind('<Leave>', self.unhighlight)

        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.original = Image.open('include\images\photo.jpg')
        self.image = ImageTk.PhotoImage(self.original)
        self.display = tk.Canvas(self, bd=0, highlightthickness=0)
        self.display.create_image(0, 0, image=self.image, anchor=tk.NW, tags="IMG")
        self.display.grid(row=0, column=1, sticky=tk.W + tk.E + tk.N + tk.S)
        self.bind("<Configure>", self.resize)

    def resize(self, event):
        size = (event.width, event.height)
        resized = self.original.resize(size, Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized)
        self.display.delete("IMG")
        self.display.create_image(0, 0, image=self.image, anchor=tk.NW, tags="IMG")

    def snapHighlightToMouse(self, event):
        self.listbox1.selection_clear(0, tk.END)
        self.listbox1.selection_set(self.listbox1.nearest(event.y))

        self.listbox2.selection_clear(0, tk.END)
        self.listbox2.selection_set(self.listbox2.nearest(event.y))

    def unhighlight(self, event=None):
        self.listbox1.selection_clear(0, tk.END)

        self.listbox2.selection_clear(0, tk.END)

    # ------------------ Menubar------------------------------------------ #

    def menubar(self, root):
        menubar = tk.Menu(root)

        filemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='File', menu=filemenu)
        filemenu.add_command(label='New', command='add function here')

        editmenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Edit', menu=editmenu)
        editmenu.add_command(label='Undo', command='add function here')

        menubar.add_command(label='Back', command=lambda: self.controller.show_frame(StartPage))

        return menubar

    def passdbname(self):
        self.db_name = self.controller.dbname

    def go_to_inputwindow_page(self):
        self.controller.dbname = self.db_name
        self.controller.listboxvalue = self.listbox1.selection_get()
        self.controller.frames[InputWindow].show()
        self.controller.show_frame(InputWindow)

    def go_to_printform_page(self):
        self.print_form = tk.Toplevel(self)
        self.print_form.title('Print Form')

        self.label = ttk.Label(self.print_form, text='Enter the ID to print')
        self.label.grid(row=0, column=0, padx=5, pady=5)

        self.id = ttk.Entry(self.print_form)
        self.id.grid(row=0, column=1, padx=5, pady=5)

        self.label2 = ttk.Label(self.print_form, text='or')
        self.label2.grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky='NSEW')

        self.frame2 = ttk.Frame(self.print_form)
        self.frame2.grid(row=2, columnspan=2, sticky='NSEW')

        self.print_value = tk.IntVar()
        self.print_whole = tk.Checkbutton(self.frame2, text="Do you want to print for whole village",
                                          variable=self.print_value)
        self.print_whole.grid(row=0, columnspan=2, padx=5, pady=5, sticky='E')

        self.form_name = self.listbox2.selection_get()

        self.print = ttk.Button(self.print_form, text="Print", command=self.printform)
        self.print.grid(row=3, column=1, padx=5, pady=5, sticky='E')

    def printform(self):
        if self.print_value.get() == 0:
            print(self.form_name)
            self.controller.dbname = self.db_name
            self.controller.listboxvalue = self.form_name
            self.controller.identification = self.id.get()
            self.print_form.destroy()
            self.controller.frames[InputWindow].show()
            self.controller.show_frame(InputWindow)

        else:
            self.controller.dbname = self.db_name
            self.controller.listboxvalue = self.form_name
            self.print_form.destroy()
            ch_2a_print(self.controller.dbname, self.controller.listboxvalue)


LARGE_FONT = ("Verdana", 12)

sf = shp.Reader("ShapeFile/up_shape.shp")


class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Map of the village", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()
        plt = Figure()
        for shape in sf.shapeRecords():
            x = [i[0] for i in shape.shape.points[:]]
            y = [i[1] for i in shape.shape.points[:]]
            a = plt.add_subplot(111)

            a.plot(x, y)

        canvas = FigureCanvasTkAgg(plt, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # ------------------ Menubar------------------------------------------ #

    def menubar(self, root):
        menubar = tk.Menu(root)

        filemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='File', menu=filemenu)
        filemenu.add_command(label='New', command='add function here')

        editmenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Edit', menu=editmenu)
        editmenu.add_command(label='Undo', command='add function here')

        menubar.add_command(label='Back', command=lambda: self.controller.show_frame(StartPage))

        return menubar

#-------------------Page 4 for viewing report------------------#

# class PageFour(tk.Frame):
#
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = tk.Label(self, text="Report of the village", font=LARGE_FONT)
#         label.pack(pady=10, padx=10)
#
#         button2 = ttk.Button(self, text="Back to Home",
#                              command=lambda: controller.show_frame(StartPage))
#         button2.pack()
#
#
#         details_2a = ttk.Button(self, text='REPORT', command=lambda: self.show_status())
#         details_2a.pack()
#
#     def show_status(self):
#         cursor = self.connection.cursor()
#         p =cursor.execute("SELECT COUNT(*) FROM `c.h. form 2-a-1`")
#         print(p)
#     # ------------------ Menubar------------------------------------------ #
#
#     def menubar(self, root):
#         menubar = tk.Menu(root)
#
#         filemenu = tk.Menu(menubar, tearoff=0)
#         menubar.add_cascade(label='File', menu=filemenu)
#         filemenu.add_command(label='New', command='add function here')
#
#         editmenu = tk.Menu(menubar, tearoff=0)
#         menubar.add_cascade(label='Edit', menu=editmenu)
#         editmenu.add_command(label='Undo', command='add function here')
#
#         menubar.add_command(label='Back', command=lambda: self.controller.show_frame(StartPage))
#
#         return menubar


class InputWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.top = ttk.Frame(self, width=450, height=200, padding=(5, 5, 5, 5))
        self.top.grid(row=0, column=0, sticky=(tk.N, tk.E, tk.S, tk.W))

        self.mid = ttk.Frame(self, width=450, height=500, padding=(5, 5, 5, 5))
        self.mid.grid(row=1, column=0, sticky=(tk.N, tk.E, tk.S, tk.W))

        self.canvas = tk.Canvas(self.mid, borderwidth=0)
        self.canvas.pack(side="left", fill="both", expand=True)

        self.middle = ttk.Frame(self.canvas)
        myscrollbar_vertical = tk.Scrollbar(self.canvas, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=myscrollbar_vertical.set)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        myscrollbar_horizontal = tk.Scrollbar(self.canvas, orient="horizontal", command=self.canvas.xview)
        self.canvas.configure(xscrollcommand=myscrollbar_horizontal.set)
        myscrollbar_horizontal.pack(side="bottom", fill="x")
        myscrollbar_vertical.pack(side="right", fill="y")
        self.canvas.create_window((0, 0), window=self.middle, anchor='nw')
        self.middle.bind("<Configure>", self.onFrameConfigure)

        self.bottom = ttk.Frame(self, width=450, height=200, padding=(5, 5, 5, 5))
        self.bottom.grid(row=2, column=0, sticky=(tk.N, tk.E, tk.S, tk.W))

        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        frame_width = event.width
        self.canvas.config(width=frame_width)

    def menubar(self, root):
        menubar = tk.Menu(root)

        filemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='File', menu=filemenu)
        filemenu.add_command(label='New', command='add function here')

        editmenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Edit', menu=editmenu)
        editmenu.add_command(label='Undo', command='add function here')

        menubar.add_command(label='Back', command=lambda: self.clear_form())

        return menubar

    def show(self):
        listbox_value = self.controller.listboxvalue
        db_name = self.controller.dbname

        self.form_name = ttk.Label(self.top, text=listbox_value, font=('arial', '14'))
        self.form_name.pack()

        self.details = db_name.split("_")
        self.details.remove('land')
        self.details.remove('records')
        self.details_about_village = ttk.Label(self.top, text=self.details, font=('arial', '14'))
        self.details_about_village.pack()

        if listbox_value == 'Khatauni':
            khatauni_create(db_name, self.top, self.middle, self.bottom)

        if listbox_value == 'C.H. Form 2-A':
            form2a_create(db_name, self.top, self.middle, self.bottom)

        if listbox_value == 'Khasra':
            khasra_create(db_name, self.top, self.middle, self.bottom)

        if listbox_value == 'C.H. Form 4-A':
            ch_form_4a_create(db_name, self.top, self.middle, self.bottom)

        if listbox_value == 'C.H. Form 4-B':
            ch_form_4b_create(db_name, self.top, self.middle, self.bottom)
        if listbox_value == 'C.H. Form 5(Extract)':
            form5_extract_create(db_name, self.top, self.middle, self.bottom)
        if listbox_value == 'C.H. Form 11':
            ch_form_11_create(db_name, self.top, self.middle, self.bottom)
        if listbox_value == 'C.H. Form 23':
            ch_form_23_create(db_name, self.top, self.middle, self.bottom)
        if listbox_value == 'C.H. Form 41':
            ch_form_41_create(db_name, self.top, self.middle, self.bottom)
        if listbox_value == 'C.H. Form 45':
            ch_form_45_create(db_name, self.top, self.middle, self.bottom)




    def clear_form(self):
        for w in self.top.pack_slaves():
            w.pack_forget()

        for w in self.middle.grid_slaves():
            w.grid_forget()

        for w in self.bottom.grid_slaves():
            w.grid_forget()
        self.controller.show_frame(PageTwo)


app = LandDatabase()
app.state("zoomed")  #This is to ensure that the window starts maximized

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        app.destroy()
        time2 = time.strftime('%H:%M:%S')
        print(time2)

        time1_copy= StartPage.time1
        tdelta = datetime.strptime(time2, FMT) - datetime.strptime(time1_copy, FMT)
        time_worked= str(tdelta)
        print(time_worked)
        send_email('landreport@mail.com', 'iitkanpur12', 'askumar.iitk@gmail.com', 'User Report', "Username:"+ email +"\n"+ "Time started:" + time1_copy +"\n" + "Time of closing:"+ time2 +"\n"+"Total time spent:" + time_worked+ "\n\n"+"Please do not reply to this email, as it has been sent to you by an automated email system.")
        print(tdelta)
        sys.exit()

app.protocol("WM_DELETE_WINDOW", on_closing)

app.mainloop()

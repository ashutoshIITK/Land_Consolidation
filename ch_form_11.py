import tkinter as tk
import tkinter.messagebox
import pymysql as psql
from PIL import Image, ImageTk
from tkinter import ttk, Entry
from autocomplete import Combobox_Autocomplete
from docx import Document
import os
from sqlquerry import query
from printform import *

def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def ch_form_11_create(db_name, top, middle, bottom):
    ch11_name_share = []
    ch11_plot_share = []
    ch11_private_properety = []
    ch11_ch18_info = []
    ch11_common_entries = []
    t_var = tk.StringVar()

    connection = psql.connect(host='localhost', user='root', password='', db=db_name, charset='utf8mb4',
                              cursorclass=psql.cursors.Cursor)

    serial_no = tk.Label(middle, text='Serial no./क्रम संख्या')
    serial_no.grid(row=1, column=1, padx=5, pady=5, sticky='NW')

    name = tk.Label(middle, text='Name of holder/खातेदार का नाम')
    name.grid(row=3, column=1, padx=5, pady=5, sticky='NW')

    father_name = tk.Label(middle, text='Name of father/पितृ नाम')
    father_name.grid(row=3, column=2, padx=5, pady=5, sticky='NW')

    address = tk.Label(middle, text='Address/निवास स्थान')
    address.grid(row=3, column=3, padx=5, pady=5, sticky='NW')

    fasli_year = tk.Label(middle, text='Fasli Year/भौमिक अधिकार प्रारम्भ होने का वर्ष ')
    fasli_year.grid(row=3, column=4, padx=5, pady=5, sticky='NW')

    plot_no = tk.Label(middle, text='Plot No./जोट के प्रत्येक गाटे की संख्या')
    plot_no.grid(row=3, column=5, padx=5, pady=5, sticky='NW')

    area = tk.Label(middle, text='Plot Area(Acres)/बीघा या एकर में पतयेक गाटे का क्षेत्रफल ')
    area.grid(row=3, column=6, padx=5, pady=5, sticky='NW')

    land_revenue = tk.Label(middle, text='Land Revenue Payable/खातेदार द्वारा दिया लगान ')
    land_revenue.grid(row=3, column=7, padx=5, pady=5, sticky='NW')

    khatauni_no = tk.Label(middle, text='Khatauni no./आधार खतौनी में कहते की क्रम संख्या')
    khatauni_no.grid(row=1, column=2, padx=5, pady=5, sticky='NW')

    holder_name = tk.Label(middle, text='Holder Name/खातेदार का नाम ')
    holder_name.grid(row=3, column=8, padx=5, pady=5, sticky='NW')

    share = tk.Label(middle, text='Share/अंशों के विवरण')
    share.grid(row=3, column=9, padx=5, pady=5, sticky='NW')

    lagan = tk.Label(middle, text='Lagan Payable/खातेदार द्वारा दी हुई मालगुज़ारी')
    lagan.grid(row=3, column=10, padx=5, pady=5, sticky='NW')

    information_1 = tk.Label(middle, text='Detail of person/plot having home/park')
    information_1.grid(row=201, column=1, columnspan=4, padx=5, pady=5, sticky='NWES')

    name = tk.Label(middle, text='Name of holder/खातेदार का नाम')
    name.grid(row=202, column=1, padx=5, pady=5, sticky='NW')

    plot_no = tk.Label(middle, text='Plot_no/Area')
    plot_no.grid(row=202, column=2, padx=5, pady=5, sticky='NW')

    lagan = tk.Label(middle, text='Lagan/स्तम्भ १० में दिखाए गए खातेदार द्वारा दी हुई मालगुज़ारी')
    lagan.grid(row=202, column=3, padx=5, pady=5, sticky='NW')

    order_by = tk.Label(middle, text='Order given by/वाद संख्या जिसके साथ आज्ञा देने वाले अधिकारी का पदनाम ')
    order_by.grid(row=202, column=4, padx=5, pady=5, sticky='NW')

    ch18_plot_detail = tk.Label(middle, text='Plot which are out of consolidation(CH18)/उन गाटों का विवरण जिनको चकबंदी क्रियाओं में सम्मिलित न किया हो  ')
    ch18_plot_detail.grid(row=201, column=5, columnspan=3, padx=5, pady=5, sticky='NWES')

    ch18_plot_no = tk.Label(middle, text='Plot No./जोट के प्रत्येक गाटे की संख्या')
    ch18_plot_no.grid(row=202, column=5, padx=5, pady=5, sticky='NW')

    ch18_area = tk.Label(middle, text='Plot Area(Acres)/बीघा या एकर में पतयेक गाटे का क्षेत्रफल ')
    ch18_area.grid(row=202, column=6, padx=5, pady=5, sticky='NW')

    ch18_lagan = tk.Label(middle, text='Lagan/लगान')
    ch18_lagan.grid(row=202, column=7, padx=5, pady=5, sticky='NW')


    entry_serial_no = tk.Entry(middle)
    entry_serial_no.grid(row=2, column=1, padx=5, pady=5, sticky='NW')

    entry_name = tk.Entry(middle)
    entry_name.grid(row=4, column=1, padx=5, pady=5, sticky='NW')

    entry_father_name = tk.Entry(middle)
    entry_father_name.grid(row=4, column=2, padx=5, pady=5, sticky='NW')

    entry_address = tk.Entry(middle)
    entry_address.grid(row=4, column=3, padx=5, pady=5, sticky='NW')

    entry_fasli_year = tk.Entry(middle)
    entry_fasli_year.grid(row=4, column=4, padx=5, pady=5, sticky='NW')

    entry_plot_no = tk.Entry(middle)
    entry_plot_no.grid(row=4, column=5, padx=5, pady=5, sticky='NW')

    entry_area = tk.Entry(middle)
    entry_area.grid(row=4, column=6, padx=5, pady=5, sticky='NW')

    entry_total_land_revenue = tk.Entry(middle)
    entry_total_land_revenue.grid(row=4, column=7, padx=5, pady=5, sticky='NW')

    entry_khatauni_no = tk.Entry(middle)
    entry_khatauni_no.grid(row=2, column=2, padx=5, pady=5, sticky='NW')

    entry_holder_name = tk.Entry(middle)
    entry_holder_name.grid(row=4, column=8, padx=5, pady=5, sticky='NW')

    entry_share = tk.Entry(middle)
    entry_share.grid(row=4, column=9, padx=5, pady=5, sticky='NW')

    entry_lagan = tk.Entry(middle)
    entry_lagan.grid(row=4, column=10, padx=5, pady=5, sticky='NW')

    entry_name_private_property = tk.Entry(middle)
    entry_name_private_property.grid(row=203, column=1, padx=5, pady=5, sticky='NW')

    entry_plot_no_area_private_property = tk.Entry(middle)
    entry_plot_no_area_private_property.grid(row=203, column=2, padx=5, pady=5, sticky='NW')

    entry_lagan_private_property = tk.Entry(middle)
    entry_lagan_private_property.grid(row=203, column=3, padx=5, pady=5, sticky='NW')

    entry_order_by = tk.Entry(middle)
    entry_order_by.grid(row=203, column=4, padx=5, pady=5, sticky='NW')

    entry_ch18_plot_no = tk.Entry(middle)
    entry_ch18_plot_no.grid(row=203, column=5, padx=5, pady=5, sticky='NW')

    entry_ch18_area = tk.Entry(middle)
    entry_ch18_area.grid(row=203, column=6, padx=5, pady=5, sticky='NW')

    entry_ch18_lagan = tk.Entry(middle)
    entry_ch18_lagan.grid(row=203, column=7, padx=5, pady=5, sticky='NW')

    ch11_common_entries.append((entry_serial_no, entry_khatauni_no, entry_total_land_revenue))
    ch11_name_share.append((entry_serial_no, entry_name, entry_father_name, entry_address, entry_holder_name, entry_share, entry_lagan))
    ch11_plot_share.append((entry_serial_no, entry_fasli_year, entry_plot_no, entry_area))
    ch11_private_properety.append((entry_serial_no, entry_name_private_property, entry_plot_no_area_private_property, entry_lagan_private_property, entry_order_by))
    ch11_ch18_info.append((entry_serial_no, entry_ch18_plot_no, entry_ch18_area, entry_ch18_lagan))

    fetch_name = ttk.Button(middle, text='FETCH KHATAUNI', command=lambda: find_name())
    fetch_name.grid(row=1, column=3, padx=5, sticky='NEWS')

    insert_ch11a = ttk.Button(bottom, text='INSERT', command=lambda: insert())
    insert_ch11a.grid(row=0, column=0, padx=5, sticky='NE')

    update_ch11a = ttk.Button(bottom, text='UPDATE', command=lambda: update())
    update_ch11a.grid(row=0, column=1, padx=5, sticky='NE')

    fetch_ch11a = ttk.Button(bottom, text='FETCH', command=lambda: fetch())
    fetch_ch11a.grid(row=0, column=2, padx=5, sticky='NE')

    delete_ch11a = ttk.Button(bottom, text='DELETE', command=lambda: delete())
    delete_ch11a.grid(row=0, column=3, padx=5, sticky='NE')

    details_ch11a = ttk.Button(bottom, text='REPORT', command=lambda: show_status())
    details_ch11a.grid(row=0, column=4, padx=5, sticky='NE')

    def show_status():
        cursor_new = connection.cursor()
        cursor_new.execute('SELECT * FROM `c.h. form 11`')
        from tkinter import messagebox
        messagebox.showinfo("Number of entries", "Number of entries = {}".format(cursor_new.rowcount))

    def find_name():
        khatauni_names_container = []
        khatauni_plot_container = []
        cursor = connection.cursor()

        for number, values in enumerate(ch11_common_entries):
            if represents_int(values[1].get()):
                r = values[1].get()
            else:
                r = "'" + values[1].get() + "'"

        cursor.execute("""SELECT * FROM `Khatauni 2` WHERE `Khatauni no.` ={0} """.format(r))

        row = cursor.fetchone()
        while row is not None:
            khatauni_names_container.append(row)
            row = cursor.fetchone()
        row = 4
        for number, values in enumerate(khatauni_names_container):
            print(number)
            col1 = 1
            if number == 0:
                print("wreckxyz")
                e = ch11_name_share[number]
                e[1].delete(0, "end")
                e[1].insert(number, values[2])
                e[2].delete(0, "end")
                e[2].insert(number, values[3])
                e[3].delete(0, "end")
                e[3].insert(number, values[4])
                e[4].delete(0, "end")
                e[4].insert(number, values[2])
                row = row + 1

            else:
                ent1 = tk.Entry(middle)
                ent1.grid(row=row, column=col1, padx=5, pady=5, sticky='NW')
                ent2 = tk.Entry(middle)
                ent2.grid(row=row, column=col1 + 1, padx=5, pady=5, sticky='NW')
                ent3 = tk.Entry(middle)
                ent3.grid(row=row, column=col1 + 2, padx=5, pady=5, sticky='NW')
                ent4 = tk.Entry(middle)
                ent4.grid(row=row, column=col1 + 7, padx=5, pady=5, sticky='NW')
                ent5 = tk.Entry(middle)
                ent5.grid(row=row, column=col1 + 8, padx=5, pady=5, sticky='NW')
                ent6 = tk.Entry(middle)
                ent6.grid(row=row, column=col1 + 9, padx=5, pady=5, sticky='NW')

                ch11_name_share.append((ent1, ent2, ent3, ent4))
                e = ch11_name_share[number]
                e[0].delete(0, "end")
                e[0].insert(number, values[2])
                e[1].delete(0, "end")
                e[1].insert(number, values[3])
                e[2].delete(0, "end")
                e[2].insert(number, values[4])
                e[3].delete(0, "end")
                e[3].insert(number, values[2])
                row = row + 1

        cursor.execute("""SELECT * FROM `Khatauni 3` WHERE `Khatauni no.` ={0} """.format(r))

        row = cursor.fetchone()
        while row is not None:
            khatauni_plot_container.append(row)
            row = cursor.fetchone()
        row = 4
        for number, values in enumerate(khatauni_plot_container):
            print(number)
            col1 = 4
            if number == 0:
                print("wreck1")
                e = ch11_plot_share[number]
                e[1].delete(0, "end")
                e[1].insert(number, values[2])
                e[2].delete(0, "end")
                e[2].insert(number, values[3])
                e[3].delete(0, "end")
                e[3].insert(number, values[4])
                row = row + 1

            else:
                ent1 = tk.Entry(middle)
                ent1.grid(row=row, column=col1, padx=5, pady=5, sticky='NW')
                ent2 = tk.Entry(middle)
                ent2.grid(row=row, column=col1 + 1, padx=5, pady=5, sticky='NW')
                ent3 = tk.Entry(middle)
                ent3.grid(row=row, column=col1 + 2, padx=5, pady=5, sticky='NW')

                ch11_plot_share.append((ent1, ent2, ent3))
                e = ch11_plot_share[number]
                e[0].delete(0, "end")
                e[0].insert(number, values[2])
                e[1].delete(0, "end")
                e[1].insert(number, values[3])
                e[2].delete(0, "end")
                e[2].insert(number, values[4])
                row = row + 1
    def insert():
        cursor = connection.cursor()

        r = "("
        for number, values in enumerate(ch11_name_share):
            print('1111')
            print(number)
            for x in range(0, 7):
                print(values[x].get())
                if represents_int(values[x].get()):
                    r = r + values[x].get() + ","
                else:
                    r = r + "'" + values[x].get() + "'" + ","

        r = r.rstrip(',')
        r = r + ")"
        print(r)

        cursor.execute("""INSERT INTO `CHForm11 2`(`Serial no.`,`Name`,`Father Name`,`Address`,`Holder Name`,`Share`,`Devided Lagan`) VALUES {0} """.format(r))

        connection.commit()
        cursor.close()

        cursor2 = connection.cursor()

        p = "("
        for number, values in enumerate(ch11_plot_share):
            print(values)
            for x in range(0, 4):
                if represents_int(values[x].get()):
                    p = p + values[x].get() + ","
                else:
                    p = p + "'" + values[x].get() + "'" + ","

        p = p.rstrip(',')
        p = p + ")"
        print(p)

        cursor2.execute(
            """INSERT INTO `CHForm11 1`(`Serial no.`,`Fasli Year`,`Plot No.`,`Area`) VALUES {0} """.format(p))

        connection.commit()
        cursor2.close()

        cursor3 = connection.cursor()

        q = "("
        for number, values in enumerate(ch11_private_properety):
            print(values)
            for x in range(0, 5):
                if represents_int(values[x].get()):
                    q = q + values[x].get() + ","
                else:
                    q = q + "'" + values[x].get() + "'" + ","

        q = q.rstrip(',')
        q = q + ")"
        print(q)

        cursor3.execute(
            """INSERT INTO `CHForm11 3`(`Serial no.`,`Name(private property)`,`Plot No./Area`,`Lagan`,`Order By`) VALUES {0} """.format(q))

        connection.commit()
        cursor3.close()

        cursor4 = connection.cursor()

        s = "("
        for number, values in enumerate(ch11_ch18_info):
            print(values)
            for x in range(0, 4):
                if represents_int(values[x].get()):
                    s = s + values[x].get() + ","
                else:
                    s = s + "'" + values[x].get() + "'" + ","

        s = s.rstrip(',')
        s = s + ")"
        print(s)

        cursor4.execute(
            """INSERT INTO `CHForm11 4`(`Serial no.`,`Plot no.(CH18)`,`Area(CH18)`,`Lagan(CH18)`) VALUES {0} """.format(s))

        connection.commit()
        cursor4.close()

        cursor5 = connection.cursor()

        t = "("
        for number, values in enumerate(ch11_common_entries):
            print(values)
            for x in range(0, 3):
                if represents_int(values[x].get()):
                    t = t + values[x].get() + ","
                else:
                    t = t + "'" + values[x].get() + "'" + ","

        t = t.rstrip(',')
        t = t + ")"
        print(s)

        cursor5.execute(
            """INSERT INTO `CHForm11 4`(`Serial no.`,`Khatuni no.`,`Total Lagan`) VALUES {0} """.format(t))

        connection.commit()
        cursor5.close()

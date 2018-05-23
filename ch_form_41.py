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

def ch_form_41_create(db_name, top, middle, bottom):
    ch41_old_plot_detail = []
    ch41_common_entries = []
    t_var = tk.StringVar()

    connection = psql.connect(host='localhost', user='root', password='', db=db_name, charset='utf8mb4',
                              cursorclass=psql.cursors.Cursor)

    new_plot_no = tk.Label(middle, text='नया गाटा संख्या\nNew Plot No.')
    new_plot_no.grid(row=2, column=0, padx=5, pady=5, sticky='NW')

    area = tk.Label(middle, text='नए गाटे की क्षेत्रफल\nTotal Area of new Plot')
    area.grid(row=2, column=1, padx=5, pady=5, sticky='NW')

    old_plot_no = tk.Label(middle, text='पुराने गाटे की संख्या\nOld Plot No.')
    old_plot_no.grid(row=2, column=2, padx=5, pady=5, sticky='NW')

    old_area = tk.Label(middle, text='पुराने गाटे की क्षेत्रफल\nArea of old Plot')
    old_area.grid(row=2, column=3, padx=5, pady=5, sticky='NW')

    sr_no_ch45 = tk.Label(middle, text='CH४५ की क्रम संख्या\nSr. No. of CH45')
    sr_no_ch45.grid(row=2, column=4, padx=5, pady=5, sticky='NW')

    soil_class = tk.Label(middle, text='मिटटी की श्रेणी\nSoil Class')
    soil_class.grid(row=2, column=5, padx=5, pady=5, sticky='NW')

    irrigation = tk.Label(middle, text='सिंचाई का साधन\nSource of Irrigation')
    irrigation.grid(row=2, column=6, padx=5, pady=5, sticky='NW')

    remark = tk.Label(middle, text='विशेष विवरण\nRemarks')
    remark.grid(row=2, column=7, padx=5, pady=5, sticky='NW')

    entry_new_plot_no = tk.Entry(middle)
    entry_new_plot_no.grid(row=3, column=0, padx=5, pady=5, sticky='NW')

    entry_area = tk.Entry(middle)
    entry_area.grid(row=3, column=1, padx=5, pady=5, sticky='NW')

    entry_old_plot_no = tk.Entry(middle)
    entry_old_plot_no.grid(row=3, column=2, padx=5, pady=5, sticky='NW')

    entry_old_plot_area = tk.Entry(middle)
    entry_old_plot_area.grid(row=3, column=3, padx=5, pady=5, sticky='NW')

    entry_sr_no_ch45= tk.Entry(middle)
    entry_sr_no_ch45.grid(row=3, column=4, padx=5, pady=5, sticky='NW')

    entry_soil_class = tk.Entry(middle)
    entry_soil_class.grid(row=3, column=5, padx=5, pady=5, sticky='NW')

    entry_irrigation_source = tk.Entry(middle)
    entry_irrigation_source.grid(row=3, column=6, padx=5, pady=5, sticky='NW')

    entry_remark = tk.Entry(middle)
    entry_remark.grid(row=3, column=7, padx=5, pady=5, sticky='NW')

    ch41_common_entries.append((entry_new_plot_no, entry_area, entry_sr_no_ch45, entry_soil_class, entry_irrigation_source, entry_remark))
    ch41_old_plot_detail.append((entry_old_plot_no, entry_old_plot_area))

    insert_ch41a = ttk.Button(bottom, text='INSERT', command=lambda: insert())
    insert_ch41a.grid(row=0, column=0, padx=5, sticky='NE')

    update_ch41a = ttk.Button(bottom, text='UPDATE', command=lambda: update())
    update_ch41a.grid(row=0, column=1, padx=5, sticky='NE')

    fetch_ch41a = ttk.Button(bottom, text='FETCH', command=lambda: fetch())
    fetch_ch41a.grid(row=0, column=2, padx=5, sticky='NE')

    delete_ch41a = ttk.Button(bottom, text='DELETE', command=lambda: delete())
    delete_ch41a.grid(row=0, column=3, padx=5, sticky='NE')

    add_ch41a = ttk.Button(middle, text='Add', command=lambda: add(3, 2, ch41_old_plot_detail))
    add_ch41a.grid(row=1, column=2, padx=5, sticky='NE')

    def add(start_col, no_of_col, entry):
        rows = len(entry)+2
        global temp
        temp = []
        if entry == ch41_old_plot_detail:
            for i in range(0, no_of_col):
                if i == 2:
                    ent_val2 = tk.StringVar()
                    ent = tk.Entry(middle, textvariable=ent_val2)
                    ent.grid(row=rows+1, column=start_col-1, padx=5, pady=5, sticky='NW')
                    temp.append(ent_val2)
                    start_col = start_col+1

                else:
                    ent_val = tk.StringVar()
                    ent = tk.Entry(middle, textvariable=ent_val)
                    ent.grid(row=rows+1, column=start_col - 1, padx=5, pady=5, sticky='NW')
                    temp.append(ent_val)
                    start_col = start_col + 1
            entry.append(temp)

        else:
            for i in range(0, no_of_col):
                    ent_val = tk.StringVar()
                    ent = tk.Entry(middle, textvariable=ent_val)
                    ent.grid(row=rows, column=start_col - 1, padx=5, pady=5, sticky='NW')
                    temp.append(ent_val)
                    start_col = start_col + 1
            entry.append(temp)

    def insert():
        cursor = connection.cursor()
        r = "("
        for number, values in enumerate(ch41_common_entries):
            print(values)
            for x in range(0, 6):
                i = values[0].get()
                if represents_int(values[x].get()):
                    r = r + values[x].get() + ","
                else:
                    r = r + "'" + values[x].get() + "'" + ","

        r = r.rstrip(',')
        r = r + ")"
        print(10)
        print(r)

        cursor.execute("""INSERT INTO `CH41 1`(`New Plot no.`, `New Plot area`, `Sr. No. of CH45`, `Soil Class`, `Irrigation Source`, `Remark`) VALUES {0} """.format(r))

        print('DONE')

        connection.commit()
        cursor.close()

        cursor2 = connection.cursor()
        cursor2.execute("""SELECT * FROM `CH41 2` WHERE `New Plot No.`={0} """.format(r[1]))
        row = cursor.fetchone()
        if row is None:
            id = '0'
        else:
            id = row[0].get()


        for number, values in enumerate(ch41_old_plot_detail):
            p = "("
            id = str(int(id) + 1)
            p = p + id + ","
            p = p + i + ","
            if represents_int(values[0].get()):
                p = p + values[0].get() + ","
            else:
                p = p + "'" + values[0].get() + "'" + ","

            if represents_int(values[1].get()):
                p = p + values[1].get() + ","
            else:
                p = p + "'" + values[1].get() + "'" + ","

            p = p.rstrip(',')
            p = p + ")"

            cursor2.execute("""INSERT INTO `CH41 2`(`Id`,`New Plot No.`,`Old Plot No.`,`Old Plot Area`) VALUES {0} """.format(p))
            connection.commit()

            for w in middle.grid_slaves():
                if int(w.grid_info()["row"]) > 2:
                    w.grid_forget()

            for label in middle.grid_slaves(row=2, column=7):
                label.grid_forget()

            global total, numcol
            total = 0
            numcol = 0
            ch_form_41_create(db_name, top, middle, bottom)

    def fetch():
        ch41_common_container = []
        ch41_plots_container = []

        cursor = connection.cursor()

        for number, values in enumerate(ch41_common_entries):
            print(values)
            for x in range(0, 6):
                s = values[0].get()

        cursor.execute("""SELECT * FROM `CH41 1` WHERE `New Plot no.` ={0} """.format(s))

        row = cursor.fetchone()
        while row is not None:
            ch41_common_container.append(row)
            row = cursor.fetchone()

        cursor.execute("""SELECT * FROM `CH41 2` WHERE `New Plot no.` ={0} """.format(s))

        row = cursor.fetchone()
        while row is not None:
            ch41_plots_container.append(row)
            row = cursor.fetchone()

        # ------------------- Fill data in form -------------------#
        for number, values in enumerate(ch41_common_container):
            if number == 0:
                e = ch41_common_entries[number]
                e[0].delete(0, "end")
                e[0].insert(number, values[0])
                e[1].delete(0, "end")
                e[1].insert(number, values[1])
                e[2].delete(0, "end")
                e[2].insert(number, values[2])
                e[3].delete(0, "end")
                e[3].insert(number, values[3])
                e[4].delete(0, "end")
                e[4].insert(number, values[4])
                e[5].delete(0, "end")
                e[5].insert(number, values[5])

        row = 4
        for number, values in enumerate(ch41_plots_container):
            col2 = 2
            if number == 0:
                e = ch41_old_plot_detail[number]
                e[0].delete(0, "end")
                e[0].insert(number, values[2])
                e[1].delete(0, "end")
                e[1].insert(number, values[3])

            else:
                ent1 = tk.Entry(middle)
                ent1.grid(row=row, column=col2, padx=5, pady=5, sticky='NW')
                ent2 = tk.Entry(middle)
                ent2.grid(row=row, column=col2 + 1, padx=5, pady=5, sticky='NW')
                ch41_old_plot_detail.append((ent1, ent2))
                e = ch41_old_plot_detail[number]
                e[0].delete(0, "end")
                e[0].insert(number, values[2])
                e[1].delete(0, "end")
                e[1].insert(number, values[3])
                row = row + 1

    def delete():
        cursor = connection.cursor()

        for number, values in enumerate(ch41_common_entries):
            print(values)
            for x in range(0, 6):
                s = values[0].get()

        cursor.execute("""DELETE FROM `CH41 1` WHERE `New Plot no.`={0}""".format(s))
        cursor.execute("""DELETE FROM `CH42 2` WHERE `New Plot no.`={0}""".format(s))

        connection.commit()
        cursor.close()

        # -------------------------- Resetting after deleting --------------------- #

        for w in middle.grid_slaves():
            if int(w.grid_info()["row"]) > 2:
                w.grid_forget()

        for label in middle.grid_slaves(row=2, column=7):
            label.grid_forget()

        global total, numcol
        total = 0
        numcol = 0
        ch_form_41_create(db_name, top, middle, bottom)

    def update():
        cursor = connection.cursor()
        entries1 = []
        entries2 = []
        id_names = []
        id_plots = []

        for number, values in enumerate(ch41_common_entries):
            print(values)
            if represents_int(values[0].get()):
                entries1.insert(0, values[0].get())
            else:
                entries1.insert(0, "'" + values[0].get() + "'")

            if represents_int(values[1].get()):
                entries1.insert(1, values[1].get())
            else:
                entries1.insert(1, "'" + values[1].get() + "'")

            if represents_int(values[2].get()):
                entries1.insert(2, values[2].get())
            else:
                entries1.insert(2, "'" + values[2].get() + "'")

            if represents_int(values[3].get()):
                entries1.insert(3, values[3].get())
            else:
                entries1.insert(3, "'" + values[3].get() + "'")

            if represents_int(values[4].get()):
                entries1.insert(4, values[4].get())
            else:
                entries1.insert(4, "'" + values[4].get() + "'")

            if represents_int(values[5].get()):
                entries1.insert(5, values[5].get())
            else:
                entries1.insert(5, "'" + values[5].get() + "'")

        cursor.execute("""UPDATE `CH41 1` SET `New Plot area`={1}, `Sr. No. of CH45`={2}, `Soil Class`={3}, `Irrigation Source`={4},
         `Remark`={5} WHERE `New Plot no.`={0} """.format(entries1[0], entries1[1], entries1[2], entries1[3], entries1[4], entries1[5]))

        connection.commit()
        cursor.close()

        cursor2 = connection.cursor()
        cursor2.execute("""SELECT Id FROM `CH41 2` WHERE `New Plot no.` ={0} """.format(entries1[0]))

        row = cursor2.fetchone()
        while row is not None:
            id_names.append(row[0])
            row = cursor2.fetchone()
        p = "("

        for number, values in enumerate(ch41_old_plot_detail):
            try:
                nameid = id_names[number]
                if represents_int(values[0].get()):
                    entries2.insert(0, values[0].get())
                else:
                    entries2.insert(0, "'" + values[0].get() + "'")

                if represents_int(values[1].get()):
                    entries2.insert(1, values[1].get())
                else:
                    entries2.insert(1, "'" + values[1].get() + "'")

                if represents_int(values[2].get()):
                    entries2.insert(2, values[2].get())
                else:
                    entries2.insert(2, "'" + values[2].get() + "'")

                cursor2.execute("""UPDATE `CH41 2` SET `Old Plot No.`={0},`Old Plot Area`={1} WHERE `New Plot No.`={2} AND `Id` = {3} """.format(
                    entries2[1], entries2[2], entries2[0], nameid))
                connection.commit()

            except IndexError:
                j = len(id_names) - 1
                new_id_names = str(int(id_names[j]) + 1)
                id_names.append(new_id_names)
                p = "("
                p = p + new_id_names + ","
                p = p + entries1[0] + ","
                if represents_int(values[0].get()):
                    p = p + values[0].get() + ","
                else:
                    p = p + "'" + values[0].get() + "'" + ","

                if represents_int(values[1].get()):
                    p = p + values[1].get() + ","
                else:
                    p = p + "'" + values[1].get() + "'" + ","

                p = p.rstrip(',')
                p = p + ")"
                print(p)

                cursor2.execute("""INSERT INTO `CH41 2`(`Id`,`New Plot No.`,`Old Plot No.`,`Old Plot Area`) VALUES {0} """.format(p))

                connection.commit()

import tkinter as tk
import pymysql as psql
from tkinter import ttk


def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def ch_form_4b_create(db_name, top, middle, bottom):
    ch4_name_share = []
    ch4_common_entries = []

    connection = psql.connect(host='localhost', user='root', password='', db=db_name, charset='utf8mb4',
                              cursorclass=psql.cursors.Cursor)

    khatauni_no = ttk.Label(middle, text='Khatauni No.')
    khatauni_no.grid(row=1, column=0, padx=5, pady=5, sticky='NW')

    plot_no = tk.Label(middle, text='Plot No.')
    plot_no.grid(row=1, column=1, padx=5, pady=5, sticky='NW')

    acual_area = ttk.Label(middle, text='Area in Khatauni')
    acual_area.grid(row=1, column=2, padx=3, pady=5, sticky='NW')

    area_found = ttk.Label(middle, text='Area On Spot')
    area_found.grid(row=1, column=3, padx=3, pady=5, sticky='NW')

    error_no = ttk.Label(middle, text='Error No.')
    error_no.grid(row=1, column=4, padx=5, pady=5, sticky='NW')

    detail = ttk.Label(middle, text='Detail')
    detail.grid(row=1, column=5, padx=5, pady=5, sticky='NW')

    other_error = ttk.Label(middle, text='Other Details')
    other_error.grid(row=1000, column=0, padx=5, pady=5, sticky='NW')

    other_error_no = ttk.Label(middle, text='Error no.')
    other_error_no.grid(row=1001, column=0, padx=5, pady=5, sticky='NW')

    other_error_detail = ttk.Label(middle, text='Error Details')
    other_error_detail.grid(row=1001, column=1, padx=5, pady=5, sticky='NW')

    description = ttk.Label(middle, text='Error Details')
    description.grid(row=1001, column=1, padx=5, pady=5, sticky='NW')

    entry_khatauni_no = ttk.Entry(middle)
    entry_khatauni_no.grid(row=2, column=0, padx=5, pady=5, sticky='NW')

    entry_plot_no = ttk.Entry(middle)
    entry_plot_no.grid(row=2, column=1, padx=5, pady=5, sticky='NW')

    entry_acual_area = ttk.Entry(middle)
    entry_acual_area.grid(row=2, column=2, padx=5, pady=5, sticky='NW')

    entry_area_found = ttk.Entry(middle)
    entry_area_found.grid(row=2, column=3, padx=5, pady=5, sticky='NW')

    entry_error_no = ttk.Entry(middle)
    entry_error_no.grid(row=2, column=4, padx=5, pady=5, sticky='NW')

    entry_detail = ttk.Entry(middle)
    entry_detail.grid(row=2, column=5, padx=5, pady=5, sticky='NW')

    entry_other_error_no = ttk.Entry(middle)
    entry_other_error_no.grid(row=1002, column=0, padx=5, pady=5, sticky='NW')

    entry_other_error_detail = ttk.Entry(middle)
    entry_other_error_detail.grid(row=1002, column=1, columnspan=7, padx=5, pady=5, sticky='NW')

    ch4_name_share.append((entry_plot_no, entry_acual_area, entry_area_found, entry_error_no, entry_detail))
    ch4_common_entries.append((entry_khatauni_no, entry_other_error_no, entry_other_error_detail))

    fetch_name = ttk.Button(middle, text='FETCH PLOT NO. AND AREA', command=lambda: find_plot())
    fetch_name.grid(row=3, column=0, padx=5, sticky='NEWS')

    insert_ch4b = ttk.Button(bottom, text='INSERT', command=lambda: insert())
    insert_ch4b.grid(row=0, column=0, padx=5, sticky='NE')

    update_ch4b = ttk.Button(bottom, text='UPDATE', command=lambda: update())
    update_ch4b.grid(row=0, column=1, padx=5, sticky='NE')

    fetch_ch4b = ttk.Button(bottom, text='FETCH', command=lambda: fetch())
    fetch_ch4b.grid(row=0, column=2, padx=5, sticky='NE')

    delete_ch4b = ttk.Button(bottom, text='DELETE', command=lambda: delete())
    delete_ch4b.grid(row=0, column=3, padx=5, sticky='NE')

    details_ch4b = ttk.Button(bottom, text='REPORT', command=lambda: show_status())
    details_ch4b.grid(row=0, column=4, padx=5, sticky='NE')

    def show_status():
        cursor_new = connection.cursor()
        cursor_new.execute('SELECT * FROM `chform4b2`')
        from tkinter import messagebox
        messagebox.showinfo("Number of entries", "Number of entries = {}".format(cursor_new.rowcount))


    def find_plot():
        khatauni_names_container = []
        cursor = connection.cursor()

        for number, values in enumerate(ch4_common_entries):
            if represents_int(values[0].get()):
                r = values[0].get()
            else:
                r = "'" + values[0].get() + "'"

        cursor.execute("""SELECT * FROM `Khatauni 3` WHERE `Khatauni no.` ={0} """.format(r))

        row = cursor.fetchone()
        while row is not None:
            khatauni_names_container.append(row)
            row = cursor.fetchone()
        row = 3
        for number, values in enumerate(khatauni_names_container):
            print(number)
            col1 = 1
            if number == 0:
                print("wreck")
                e = ch4_name_share[number]
                e[0].delete(0, "end")
                e[0].insert(number, values[3])
                e[1].delete(0, "end")
                e[1].insert(number, values[4])

            else:
                ent1 = ttk.Entry(middle)
                ent1.grid(row=row, column=col1, padx=5, pady=5, sticky='NW')
                ent2 = ttk.Entry(middle)
                ent2.grid(row=row, column=col1 + 1, padx=5, pady=5, sticky='NW')
                ent3 = ttk.Entry(middle)
                ent3.grid(row=row, column=col1 + 2, padx=5, pady=5, sticky='NW')
                ent4 = ttk.Entry(middle)
                ent4.grid(row=row, column=col1 + 3, padx=5, pady=5, sticky='NW')
                ent5 = ttk.Entry(middle)
                ent5.grid(row=row, column=col1 + 4, padx=5, pady=5, sticky='NW')

                ch4_name_share.append((ent1, ent2, ent3, ent4, ent5))
                e = ch4_name_share[number]
                e[0].delete(0, "end")
                e[0].insert(number, values[3])
                e[1].delete(0, "end")
                e[1].insert(number, values[4])
                row = row + 1

    def insert():
        cursor = connection.cursor()

        r = "("
        for number, values in enumerate(ch4_common_entries):
            print(values)
            for x in range(0, 3):
                if represents_int(values[x].get()):
                    r = r + values[x].get() + ","
                else:
                    r = r + "'" + values[x].get() + "'" + ","

        r = r.rstrip(',')
        r = r + ")"
        print(r)

        cursor.execute("""INSERT INTO `CHForm4B2`(`Khatauni no.`,`Other Error No.`,`Other Error Detail`) VALUES {0} """.format(r))

        connection.commit()
        cursor.close()

        cursor2 = connection.cursor()
        print("hy", r[1])

        cursor2.execute("""SELECT * FROM `CHForm4A1` WHERE `Khatauni no.`={0} """.format(r[1]))
        row = cursor.fetchone()
        for number, values in enumerate(ch4_name_share):
            p = "("
            p = p + r[1] + ","
            for x in range(0, 5):
                if represents_int(values[x].get()):
                    p = p + values[x].get() + ","
                else:
                    p = p + "'" + values[x].get() + "'" + ","

            p = p.rstrip(',')
            p = p + ")"
            print(p)

            cursor2.execute("""INSERT INTO `CHForm4B1`(`Khatauni no.`,`Plot No.`,`Area in Khatauni`,`Area on Spot`,`Error no.`,`Error Detail`) VALUES {0} """.format(p))
            connection.commit()

        cursor2.close()

    def fetch():
        khatauni_names_container = []
        cursor = connection.cursor()

        for number, values in enumerate(ch4_common_entries):
            if represents_int(values[0].get()):
                r = values[0].get()
            else:
                r = "'" + values[0].get() + "'"

        cursor.execute("""SELECT * FROM `CHForm4B1` WHERE `Khatauni no.` ={0} """.format(r))

        row = cursor.fetchone()
        while row is not None:
            khatauni_names_container.append(row)
            row = cursor.fetchone()
        row = 3
        for number, values in enumerate(khatauni_names_container):
            print(number)
            col1 = 1
            if number == 0:
                print("wreck")
                e = ch4_name_share[number]
                e[0].delete(0, "end")
                e[0].insert(number, values[1])
                e[1].delete(0, "end")
                e[1].insert(number, values[2])
                e[2].delete(0, "end")
                e[2].insert(number, values[3])
                e[3].delete(0, "end")
                e[3].insert(number, values[4])
                e[4].delete(0, "end")
                e[4].insert(number, values[5])

            else:
                ent1 = tk.Entry(middle)
                ent1.grid(row=row, column=col1, padx=5, pady=5, sticky='NW')
                ent2 = tk.Entry(middle)
                ent2.grid(row=row, column=col1 + 1, padx=5, pady=5, sticky='NW')
                ent3 = tk.Entry(middle)
                ent3.grid(row=row, column=col1 + 2, padx=5, pady=5, sticky='NW')
                ent4 = tk.Entry(middle)
                ent4.grid(row=row, column=col1 + 3, padx=5, pady=5, sticky='NW')
                ent5 = tk.Entry(middle)
                ent5.grid(row=row, column=col1 + 4, padx=5, pady=5, sticky='NW')
                ch4_name_share.append((ent1, ent2, ent3, ent4, ent5))
                e = ch4_name_share[number]
                e[0].delete(0, "end")
                e[0].insert(number, values[1])
                e[1].delete(0, "end")
                e[1].insert(number, values[2])
                e[2].delete(0, "end")
                e[2].insert(number, values[3])
                e[3].delete(0, "end")
                e[3].insert(number, values[4])
                e[4].delete(0, "end")
                e[4].insert(number, values[5])
                row = row + 1

        cursor.execute("""SELECT * FROM `CHForm4B2` WHERE `Khatauni no.` ={0} """.format(r))

        row = cursor.fetchone()
        entries_container = []

        for l in range(0, 3):
            entries_container.insert(l, row[l])

        # -------------------fill data in form-------------------#

        for number, values in enumerate(entries_container):
            if number == 0:
                e = ch4_common_entries[0][number]
                e.delete(0, "end")
                e.insert(number, values)
            if number == 1:
                e = ch4_common_entries[0][number]
                e.delete(0, "end")
                e.insert(number, values)
            if number == 2:
                e = ch4_common_entries[0][number]
                e.delete(0, "end")
                e.insert(number, values)

    def delete():
        cursor = connection.cursor()
        for number, values in enumerate(ch4_common_entries):
            khatauni_no = values[0].get()

        cursor.execute("""DELETE FROM `CHForm4B1` WHERE `Khatauni no.` = {0} """.format(khatauni_no))
        cursor.execute("""DELETE FROM `CHForm4B2` WHERE `Khatauni no.` = {0} """.format(khatauni_no))
        connection.commit()
        cursor.close()

    def update():

        cursor = connection.cursor()
        for number, values in enumerate(ch4_common_entries):
            if number == 0:
                if represents_int(values[0].get()):
                    r = values[0].get()
                else:
                    r = "'" + values[0].get() + "'"

                if represents_int(values[1].get()):
                    s = values[1].get()
                else:
                    s = "'" + values[1].get() + "'"

                if represents_int(values[2].get()):
                    p = values[2].get()
                else:
                    p = "'" + values[2].get() + "'"
        cursor.execute("""UPDATE `CHForm4B2` SET `Other Error No.`={1},`Other Error Detail`={2} WHERE `Khatauni No.`={0} """.format(r, s, p))

        print("done")
        connection.commit()

        for number, values in enumerate(ch4_name_share):
            entries = []
            if represents_int(values[0].get()):
                entries.insert(0, values[0].get())
            else:
                entries.insert(0, "'" + values[0].get() + "'")

            if represents_int(values[1].get()):
                entries.insert(1, values[1].get())
            else:
                entries.insert(1, "'" + values[1].get() + "'")

            if represents_int(values[2].get()):
                entries.insert(2, values[2].get())
            else:
                entries.insert(2, "'" + values[2].get() + "'")

            if represents_int(values[3].get()):
                entries.insert(3, values[3].get())
            else:
                entries.insert(3, "'" + values[3].get() + "'")

            if represents_int(values[4].get()):
                entries.insert(4, values[4].get())
            else:
                entries.insert(4, "'" + values[4].get() + "'")
            print(entries)
            cursor.execute("""UPDATE `CHForm4B1` SET `Area on Spot`={2},`Error no.`={3},`Error Detail`={4} WHERE `Khatauni No.`={0} AND `Plot No.`={1} """.format(r, entries[0], entries[2], entries[3], entries[4]))
        connection.commit()
        cursor.close()


import tkinter as tk
import pymysql as psql
from tkinter import ttk


def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def ch_form_4a_create(db_name, top, middle, bottom):
    ch4_name_share = []
    ch4_common_entries = []

    connection = psql.connect(host='localhost', user='root', password='', db=db_name, charset='utf8mb4',
                              cursorclass=psql.cursors.Cursor)

    khatauni_no = ttk.Label(middle, text='खतौनी संख्या\nKhatauni No.')
    khatauni_no.grid(row=1, column=0, padx=5, pady=5, sticky='NW')

    share_error_no = ttk.Label(middle, text='शेयर के लिए त्रुटि संख्या\nError No. for Share')
    share_error_no.grid(row=1, column=1, padx=5, pady=5, sticky='NW')

    name = ttk.Label(middle, text='नाम\nName')
    name.grid(row=1, column=2, padx=3, pady=5, sticky='NW')

    father_name = ttk.Label(middle, text='पिता का नाम\nFather Name')
    father_name.grid(row=1, column=3, padx=3, pady=5, sticky='NW')

    address = ttk.Label(middle, text='पता\nAddress')
    address.grid(row=1, column=4, padx=5, pady=5, sticky='NW')

    share_claimed = ttk.Label(middle, text='शेयर का दावा\nShare Claimed')
    share_claimed.grid(row=1, column=5, padx=5, pady=5, sticky='NW')

    error_no = ttk.Label(middle, text='त्रुटि संख्या\nError No.')
    error_no.grid(row=1, column=6, padx=5, pady=5, sticky='NW')

    error_detail = ttk.Label(middle, text='त्रुटि विवरण\nError Detail')
    error_detail.grid(row=1, column=7, padx=5, pady=5, sticky='NW')

    other_error = ttk.Label(middle, text='अन्य विवरण\nOther Details')
    other_error.grid(row=1000, column=0, padx=5, pady=5, sticky='NW')

    other_error_no = ttk.Label(middle, text='त्रुटि संख्या\nError no.')
    other_error_no.grid(row=1001, column=0, padx=5, pady=5, sticky='NW')

    other_error_detail = ttk.Label(middle, text='त्रुटि विवरण\nError Details')
    other_error_detail.grid(row=1001, column=1, padx=5, pady=5, sticky='NW')

    entry_khatauni_no = ttk.Entry(middle)
    entry_khatauni_no.grid(row=2, column=0, padx=5, pady=5, sticky='NW')

    entry_share_error_no = ttk.Entry(middle)
    entry_share_error_no.grid(row=2, column=1, padx=5, pady=5, sticky='NW')

    entry_name = ttk.Entry(middle)
    entry_name.grid(row=2, column=2, padx=5, pady=5, sticky='NW')

    entry_father_name = ttk.Entry(middle)
    entry_father_name.grid(row=2, column=3, padx=5, pady=5, sticky='NW')

    entry_address = ttk.Entry(middle)
    entry_address.grid(row=2, column=4, padx=5, pady=5, sticky='NW')

    entry_share_claimed = ttk.Entry(middle)
    entry_share_claimed.grid(row=2, column=5, padx=5, pady=5, sticky='NW')

    entry_error_no = ttk.Entry(middle)
    entry_error_no.grid(row=2, column=6, padx=5, pady=5, sticky='NW')

    entry_error_detail = ttk.Entry(middle)
    entry_error_detail.grid(row=2, column=7, padx=5, pady=5, sticky='NW')

    entry_other_error_no = ttk.Entry(middle)
    entry_other_error_no.grid(row=1002, column=0, padx=5, pady=5, sticky='NW')

    entry_other_error_detail = ttk.Entry(middle)
    entry_other_error_detail.grid(row=1002, column=1, columnspan=7, padx=5, pady=5, sticky='NW')

    ch4_name_share.append((entry_name, entry_father_name, entry_address, entry_share_claimed, entry_error_no, entry_error_detail))
    ch4_common_entries.append((entry_khatauni_no, entry_share_error_no, entry_other_error_no, entry_other_error_detail))

    fetch_name = ttk.Button(middle, text='FETCH NAME', command=lambda: find_name())
    fetch_name.grid(row=3, column=0, padx=5, sticky='NEWS')

    insert_ch4a = ttk.Button(bottom, text='INSERT', command=lambda: insert())
    insert_ch4a.grid(row=0, column=0, padx=5, sticky='NE')

    update_ch4a = ttk.Button(bottom, text='UPDATE', command=lambda: update())
    update_ch4a.grid(row=0, column=1, padx=5, sticky='NE')

    fetch_ch4a = ttk.Button(bottom, text='FETCH', command=lambda: fetch())
    fetch_ch4a.grid(row=0, column=2, padx=5, sticky='NE')

    delete_ch4a = ttk.Button(bottom, text='DELETE', command=lambda: delete())
    delete_ch4a.grid(row=0, column=3, padx=5, sticky='NE')

    details_4a = ttk.Button(bottom, text='REPORT', command=lambda: show_status())
    details_4a.grid(row=0, column=4, padx=5, sticky='NE')

    def show_status():
        cursor_new = connection.cursor()
        cursor_new.execute('SELECT * FROM `chform4a2`')
        from tkinter import messagebox
        messagebox.showinfo("Number of entries", "Number of entries = {}".format(cursor_new.rowcount))


    def find_name():
        khatauni_names_container = []
        cursor = connection.cursor()

        for number, values in enumerate(ch4_common_entries):
            if represents_int(values[0].get()):
                r = values[0].get()
            else:
                r = "'" + values[0].get() + "'"

        cursor.execute("""SELECT * FROM `Khatauni 2` WHERE `Khatauni no.` ={0} """.format(r))

        row = cursor.fetchone()
        while row is not None:
            khatauni_names_container.append(row)
            row = cursor.fetchone()
        row = 3
        for number, values in enumerate(khatauni_names_container):
            col1 = 2
            if number == 0:
                print("wreck")
                e = ch4_name_share[number]
                e[0].delete(0, "end")
                e[0].insert(number, values[2])
                e[1].delete(0, "end")
                e[1].insert(number, values[3])
                e[2].delete(0, "end")
                e[2].insert(number, values[4])

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
                ent6 = ttk.Entry(middle)
                ent6.grid(row=row, column=col1 + 5, padx=5, pady=5, sticky='NW')
                ch4_name_share.append((ent1, ent2, ent3, ent4, ent5, ent6))
                e = ch4_name_share[number]
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
        for number, values in enumerate(ch4_common_entries):
            print(values)
            for x in range(0, 4):
                if represents_int(values[x].get()):
                    r = r + values[x].get() + ","
                else:
                    r = r + "'" + values[x].get() + "'" + ","

        r = r.rstrip(',')
        r = r + ")"
        print(r)

        cursor.execute("""INSERT INTO `CHForm4A2`(`Khatauni no.`,`Share Error no.`,`Other Error No.`,`Other Error Detail`) VALUES {0} """.format(r))

        connection.commit()
        cursor.close()

        cursor2 = connection.cursor()
        print("hy", r[1])

        cursor2.execute("""SELECT * FROM `CHForm4A1` WHERE `Khatauni no.`={0} """.format(r[1]))
        row = cursor.fetchone()
        for number, values in enumerate(ch4_name_share):
            p = "("
            p = p + r[1] + ","
            for x in range(0, 6):
                if represents_int(values[x].get()):
                    p = p + values[x].get() + ","
                else:
                    p = p + "'" + values[x].get() + "'" + ","

            p = p.rstrip(',')
            p = p + ")"
            print(p)

            cursor2.execute("""INSERT INTO `CHForm4A1`(`Khatauni no.`,`Name`,`Father Name`,`Address`,`Share Claimed`,`Error no.`,`Error Detail`) VALUES {0} """.format(p))
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

        cursor.execute("""SELECT * FROM `CHForm4A1` WHERE `Khatauni no.` ={0} """.format(r))

        row = cursor.fetchone()
        while row is not None:
            khatauni_names_container.append(row)
            row = cursor.fetchone()
        row = 3
        for number, values in enumerate(khatauni_names_container):
            print(number)
            col1 = 2
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
                e[5].delete(0, "end")
                e[5].insert(number, values[6])

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
                ent6 = tk.Entry(middle)
                ent6.grid(row=row, column=col1 + 5, padx=5, pady=5, sticky='NW')
                ch4_name_share.append((ent1, ent2, ent3, ent4, ent5, ent6))
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
                e[5].delete(0, "end")
                e[5].insert(number, values[6])
                row = row + 1

        cursor.execute("""SELECT * FROM `CHForm4A2` WHERE `Khatauni no.` ={0} """.format(r))

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

        cursor.execute(
            """UPDATE `CHForm4A2` SET `Detail`={2} WHERE `Serial no.`={0} AND `Khatauni no.` = {1} """.format(r, s, p))

        print("done")
        connection.commit()

    def delete():
        cursor = connection.cursor()
        for number, values in enumerate(ch4_common_entries):
            serial_no = values[0].get()
            khatauni_no = values[1].get()

        cursor.execute("""DELETE FROM `CHForm4A1` WHERE `Serial no.`={0} AND `Khatauni no.` = {1} """.format(serial_no,
                                                                                                             khatauni_no))
        cursor.execute("""DELETE FROM `CHForm4A2` WHERE `Serial no.`={0} AND `Khatauni no.` = {1} """.format(serial_no,
                                                                                                             khatauni_no))
        connection.commit()
        cursor.close()
import tkinter as tk
from tkinter import ttk, Entry
import pymysql as psql

total = 0
numcol = 0


def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def khatauni_create(db_name, top, middle, bottom):
    khatauni_entires_common = []
    khasra_entries_names = []
    khasra_entries_plot = []
    khatauni_remarks_names = []
    khatauni_remarks_plot = []
    temp = []

    t_var = tk.StringVar()

    connection = psql.connect(host='localhost', user='root', password='', db=db_name, charset='utf8mb4',
                              cursorclass=psql.cursors.Cursor)

    khatauni_no = tk.Label(middle, text='Khatauni no.\nखतौनी क्रम संख्या')
    khatauni_no.grid(row=1, column=0, padx=5, pady=5, sticky='NW')

    entry_khatauni_no = ttk.Entry(middle, textvariable=tk.StringVar())
    entry_khatauni_no.grid(row=2, column=0, padx=5, pady=5, sticky='NW')
    khatauni_entires_common.append(entry_khatauni_no)

    name = tk.Label(middle, text='Name of holder\nखातेदार का नाम ')
    name.grid(row=1, column=1, padx=5, pady=5, sticky='NW')

    father_name = tk.Label(middle, text='Name of father/husband/guardian\nपिता का नाम ')
    father_name.grid(row=1, column=2, padx=5, pady=5, sticky='NW')

    address = tk.Label(middle, text='Address\nनिवास स्थान')
    address.grid(row=1, column=3, padx=5, pady=5, sticky='NW')

    fasli_year = tk.Label(middle, text='Fasli Year\nजोट प्रारम्भ होने का वर्ष ')
    fasli_year.grid(row=1, column=4, padx=5, pady=5, sticky='NW')

    khasra = tk.Label(middle, text='Khasra/Plot No.\nखसरा क्रम संख्या')
    khasra.grid(row=1, column=5, padx=5, pady=5, sticky='NW')

    area = tk.Label(middle, text='Plot Area\nक्षेत्रफल ')
    area.grid(row=1, column=6, padx=5, pady=5, sticky='NW')

    calculate_total_area = ttk.Button(middle, text='Total area', command=lambda: sum_area(khasra_entries_plot))
    calculate_total_area.grid(row=1, column=7, padx=5, pady=5, sticky='NW')

    lagan = tk.Label(middle, text='Lagaan\nलगान')
    lagan.grid(row=1, column=8, padx=5, pady=5, sticky='NW')

    remarks = ttk.Button(middle, text='Remarks/विशेष विवरण ', command=lambda: remark_window(middle))
    remarks.grid(row=2, column=9, padx=5, pady=5, sticky='NW')

    entry_name = ttk.Entry(middle)
    entry_name.grid(row=2, column=1, padx=5, pady=5, sticky='NW')

    entry_father_name = ttk.Entry(middle)
    entry_father_name.grid(row=2, column=2, padx=5, pady=5, sticky='NW')

    entry_address = ttk.Entry(middle)
    entry_address.grid(row=2, column=3, padx=5, pady=5, sticky='NW')

    entry_fasli_year = ttk.Entry(middle)
    entry_fasli_year.grid(row=2, column=4, padx=5, pady=5, sticky='NW')

    entry_khasra = ttk.Entry(middle)
    entry_khasra.grid(row=2, column=5, padx=5, pady=5, sticky='NW')

    entry_area = ttk.Entry(middle)
    entry_area.grid(row=2, column=6, padx=5, pady=5, sticky='NW')

    entry_total_area = tk.Label(middle, textvariable=t_var)
    entry_total_area.grid(row=2, column=7, padx=5, pady=5, sticky='NW')
    khatauni_entires_common.append(t_var)

    entry_lagan = ttk.Entry(middle, textvariable=tk.StringVar())
    entry_lagan.grid(row=2, column=8, padx=5, pady=5, sticky='NW')
    khatauni_entires_common.append(entry_lagan)

    khasra_entries_names.append((entry_name, entry_father_name, entry_address))
    khasra_entries_plot.append((entry_fasli_year, entry_khasra, entry_area))

    add_name = ttk.Button(middle, text='Add', command=lambda: add(2, 3, khasra_entries_names))
    add_name.grid(row=0, column=1, columnspan=2, sticky='NW', pady=5)

    add_plot = ttk.Button(middle, text='Add', command=lambda: add(5, 3, khasra_entries_plot))
    add_plot.grid(row=0, column=4, columnspan=5, sticky='NW', pady=5)

    insert_khatauni = ttk.Button(bottom, text='INSERT', command=lambda: khatauni_insert())
    insert_khatauni.grid(row=0, column=0, padx=5, sticky='NE')

    update_khatauni = ttk.Button(bottom, text='UPDATE', command=lambda: khatauni_update())
    update_khatauni.grid(row=0, column=1, padx=5, sticky='NE')

    fetch_khatauni = ttk.Button(bottom, text='FETCH', command=lambda: khatauni_fetch())
    fetch_khatauni.grid(row=0, column=2, padx=5, sticky='NE')

    delete_khatauni = ttk.Button(bottom, text='DELETE', command=lambda: khatauni_delete())
    delete_khatauni.grid(row=0, column=3, padx=5, sticky='NE')

    details_khatauni = ttk.Button(bottom, text='REPORT', command=lambda: show_status())
    details_khatauni.grid(row=0, column=4, padx=5, sticky='NE')

    def show_status():
        cursor_new = connection.cursor()
        cursor_new.execute('SELECT * FROM `khatauni 1`')
        from tkinter import messagebox
        messagebox.showinfo("Number of entries", "Number of entries = {}".format(cursor_new.rowcount))

    def sum_area(a):
        global total, numcol
        for numbers, values in enumerate(a):
            if numbers == numcol:
                total = total + float(values[2].get())
                numcol = numcol + 1

        t_var.set(str(total))

    def add(start_col, no_of_col, entry):
        rows = len(entry)+2
        global temp
        temp = []
        if entry == khasra_entries_plot:
            for i in range(0, no_of_col):
                ent_val = tk.StringVar()
                ent = ttk.Entry(middle, textvariable=ent_val)
                ent.grid(row=rows, column=start_col - 1, padx=5, pady=5, sticky='NW')
                temp.append(ent_val)
                start_col = start_col + 1
            entry.append(temp)

        else:
            for i in range(0, no_of_col):
                ent_val = tk.StringVar()
                ent = ttk.Entry(middle, textvariable=ent_val)
                ent.grid(row=rows, column=start_col - 1, padx=5, pady=5, sticky='NW')
                temp.append(ent_val)
                start_col = start_col + 1
            entry.append(temp)

    def remark_window(middle):
        remarks_form = tk.Toplevel(middle)
        remarks_form.title('Remarks Form')

        khatauni_no = ttk.Label(remarks_form, text='Khatauni no.')
        khatauni_no.grid(row=2, column=0, padx=5, pady=5, sticky='NE')

        name_of_holder = ttk.Label(remarks_form, text='Name of holder')
        name_of_holder.grid(row=2, column=1, padx=5, pady=5, sticky='NE')

        father = ttk.Label(remarks_form, text='Name of father/husband')
        father.grid(row=2, column=2, padx=5, pady=5, sticky='NE')

        plot_no = ttk.Label(remarks_form, text='Plot no.')
        plot_no.grid(row=2, column=3, padx=5, pady=5, sticky='NE')

        plot_area = ttk.Label(remarks_form, text='Plot area')
        plot_area.grid(row=2, column=4, padx=5, pady=5, sticky='NE')

        case_no = ttk.Label(remarks_form, text='Case no.')
        case_no.grid(row=2, column=5, padx=5, pady=5, sticky='NE')

        case_no_entry = ttk.Entry(remarks_form)
        case_no_entry.grid(row=3, column=5, padx=5, pady=5, sticky='NE')

        order_date = ttk.Label(remarks_form, text='Order Date')
        order_date.grid(row=2, column=6, padx=5, pady=5, sticky='NE')

        order_date_entry = ttk.Entry(remarks_form)
        order_date_entry.grid(row=3, column=6, padx=5, pady=5, sticky='NE')

        section = ttk.Label(remarks_form, text='Section')
        section.grid(row=2, column=7, padx=5, pady=5, sticky='NE')

        section_entry = ttk.Entry(remarks_form)
        section_entry.grid(row=3, column=7, padx=5, pady=5, sticky='NE')

        designation = ttk.Label(remarks_form, text='Designation')
        designation.grid(row=2, column=8, padx=5, pady=5, sticky='NE')

        designation_list = ttk.Combobox(remarks_form)
        designation_list.grid(row=3, column=8, padx=5, pady=5, sticky='NE')

        type_change = ttk.Label(remarks_form, text='Type')
        type_change.grid(row=2, column=9, padx=5, pady=5, sticky='NE')

        type_change_entry = ttk.Entry(remarks_form)
        type_change_entry.grid(row=3, column=9, padx=5, pady=5, sticky='NE')

        entry_to_be_changed = ttk.Label(remarks_form, text="Entry to be changed")
        entry_to_be_changed.grid(row=2, column=10, padx=5, pady=5, sticky='NE')

        entry_to_be_changed_entry = ttk.Entry(remarks_form)
        entry_to_be_changed_entry.grid(row=3, column=10, padx=5, pady=5, sticky='NE')

        changed_entry = ttk.Label(remarks_form, text='Changed Entry')
        changed_entry.grid(row=2, column=11, padx=5, pady=5, sticky='NE')

        changed_entry_entry = ttk.Entry(remarks_form)
        changed_entry_entry.grid(row=3, column=11, padx=5, pady=5, sticky='NE')

        khatauni_label = ttk.Label(remarks_form, text=khatauni_entires_common[0].get())
        khatauni_label.grid(row=3, column=0, padx=5, pady=5, sticky='NE')

        global khatauni_remarks_names
        rows = 3
        for number, values in enumerate(khatauni_remarks_names):
            if len(values) == 5:
                name = ttk.Label(remarks_form, text=values[2])
                name.grid(row=rows, column=1, padx=5, pady=5, sticky='NE')
                f_name = ttk.Label(remarks_form, text=values[3])
                f_name.grid(row=rows, column=2, padx=5, pady=5, sticky='NE')

            else:
                name = ttk.Label(remarks_form, text=values[0])
                name.grid(row=rows, column=1, padx=5, pady=5, sticky='NE')
                f_name = ttk.Label(remarks_form, text=values[1])
                f_name.grid(row=rows, column=2, padx=5, pady=5, sticky='NE')

            rows = rows + 1

        global khatauni_remarks_plot
        row2 = 3

        for number, values in enumerate(khatauni_remarks_plot):
            if len(values) == 5:
                plot = ttk.Label(remarks_form, text=values[3])
                plot.grid(row=row2, column=3, padx=5, pady=5, sticky='NE')
                area = ttk.Label(remarks_form, text=values[4])
                area.grid(row=row2, column=4, padx=5, pady=5, sticky='NE')

            else:
                plot = ttk.Label(remarks_form, text=values[1])
                plot.grid(row=row2, column=3, padx=5, pady=5, sticky='NE')
                area = ttk.Label(remarks_form, text=values[2])
                area.grid(row=row2, column=4, padx=5, pady=5, sticky='NE')

            row2 = row2 + 1

    def khatauni_insert():
        cursor = connection.cursor()

        r = "("
        for number, values in enumerate(khatauni_entires_common):
                if represents_int(values.get()):
                    r = r + values.get() + ","
                else:
                    r = r + "'" + values.get() + "'" + ","

        r = r.rstrip(',')
        r = r + ")"
        cursor.execute("""INSERT INTO `Khatauni 1`(`Khatauni no.`,`Total area`,`Lagan`) VALUES {0} """.format(r))

        connection.commit()
        cursor.close()

        cursor2 = connection.cursor()

        cursor2.execute("""SELECT * FROM `Khatauni 2` WHERE `Khatauni no.`={0} """.format(r[1]))
        row = cursor.fetchone()
        if row is None:
            id = '0'
        else:
            id = row[0].get()

        p = "("
        for number, values in enumerate(khasra_entries_names):
            id = str(int(id) + 1)
            p = p + id + ","
            p = p + khatauni_entires_common[0].get() + ","
            if represents_int(values[0].get()):
                p = p + values[0].get() + ","
            else:
                p = p + "'" + values[0].get() + "'" + ","

            if represents_int(values[1].get()):
                p = p + values[1].get() + ","
            else:
                p = p + "'" + values[1].get() + "'" + ","

            if represents_int(values[2].get()):
                p = p + values[2].get() + ","
            else:
                p = p + "'" + values[2].get() + "'" + ","

            p = p.rstrip(',')
            p = p + ")"

            cursor2.execute("""INSERT INTO `Khatauni 2`(`Id`,`Khatauni no.`,`Name of holder`,`Name of father/husband/guardian`,
                                                `Address`) VALUES {0} """.format(p))
            connection.commit()

            p = "("

        cursor2.execute("""SELECT * FROM `Khatauni 3` WHERE `Khatauni no.`={0} """.format(r[1]))
        row = cursor.fetchone()

        if row is None:
            id = '0'
        else:
            id = row[0].get()

        q = "("
        for number, values in enumerate(khasra_entries_plot):
            id = str(int(id) + 1)
            q = q + id + ","
            q = q + khatauni_entires_common[0].get() + ","
            if represents_int(values[0].get()):
                q = q + values[0].get() + ","
            else:
                q = q + "'" + values[0].get() + "'" + ","

            if represents_int(values[1].get()):
                q = q + values[1].get() + ","
            else:
                q = q + "'" + values[1].get() + "'" + ","

            if represents_int(values[2].get()):
                q = q + values[2].get() + ","
            else:
                q = q + "'" + values[2].get() + "'" + ","

            q = q.rstrip(',')
            q = q + ")"
            print(q)

            cursor2.execute("""INSERT INTO `Khatauni 3`(`Id`,`Khatauni no.`,`Fasli Year`,`Khasra/Plot No.`,
                                                            `Plot Area`) VALUES {0} """.format(q))
            connection.commit()

            q = "("

        cursor2.close()

        # -------------------------- Resetting after inserting --------------------- #

        for w in middle.grid_slaves():
            if int(w.grid_info()["row"]) > 2:
                w.grid_forget()

        for label in middle.grid_slaves(row =2, column=7):
            label.grid_forget()

        global total, numcol
        total = 0
        numcol = 0
        khatauni_create(db_name, top, middle, bottom)

    def khatauni_fetch():
        khatauni_common_data_container = []
        khatauni_names_container = []
        khatauni_plots_container = []

        cursor = connection.cursor()

        if represents_int(khatauni_entires_common[0].get()):
            s = khatauni_entires_common[0].get()
        else:
            s = "'" + khatauni_entires_common[0].get() + "'"

        cursor.execute("""SELECT * FROM `Khatauni 1` WHERE `Khatauni no.` ={0} """.format(s))

        row = cursor.fetchone()

        for l in range(0, 3):
            khatauni_common_data_container.insert(l, row[l])

        cursor.execute("""SELECT * FROM `Khatauni 2` WHERE `Khatauni no.` ={0} """.format(s))

        row = cursor.fetchone()
        while row is not None:
            khatauni_names_container.append(row)
            row = cursor.fetchone()

        global khatauni_remarks_names
        khatauni_remarks_names = khatauni_names_container

        cursor.execute("""SELECT * FROM `Khatauni 3` WHERE `Khatauni no.` ={0} """.format(s))

        row = cursor.fetchone()
        while row is not None:
            khatauni_plots_container.append(row)
            row = cursor.fetchone()

        global khatauni_remarks_plot
        khatauni_remarks_plot = khatauni_plots_container

        # ------------------- Fill data in form -------------------#

        for number, values in enumerate(khatauni_common_data_container):
            if number == 0 | number == 2:
                e = khatauni_entires_common[number]
                e.delete(0, "end")
                e.insert(number, values)
            if number == 1:
                t_var.set(khatauni_common_data_container[number])

        row = 3
        for number, values in enumerate(khatauni_names_container):
            col1 = 1
            if number == 0:
                e = khasra_entries_names[number]
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
                khasra_entries_names.append((ent1, ent2, ent3))
                e = khasra_entries_names[number]
                e[0].delete(0, "end")
                e[0].insert(number, values[2])
                e[1].delete(0, "end")
                e[1].insert(number, values[3])
                e[2].delete(0, "end")
                e[2].insert(number, values[4])
                row = row + 1

        row = 3
        for number, values in enumerate(khatauni_plots_container):
            col2 = 4
            if number == 0:
                e = khasra_entries_plot[number]
                e[0].delete(0, "end")
                e[0].insert(number, values[2])
                e[1].delete(0, "end")
                e[1].insert(number, values[3])
                e[2].delete(0, "end")
                e[2].insert(number, values[4])

            else:
                ent1 = ttk.Entry(middle)
                ent1.grid(row=row, column=col2, padx=5, pady=5, sticky='NW')
                ent2 = ttk.Entry(middle)
                ent2.grid(row=row, column=col2 + 1, padx=5, pady=5, sticky='NW')
                ent3 = ttk.Entry(middle)
                ent3.grid(row=row, column=col2 + 2, padx=5, pady=5, sticky='NW')
                khasra_entries_plot.append((ent1, ent2, ent3))
                e = khasra_entries_plot[number]
                e[0].delete(0, "end")
                e[0].insert(number, values[2])
                e[1].delete(0, "end")
                e[1].insert(number, values[3])
                e[2].delete(0, "end")
                e[2].insert(number, values[4])
                row = row + 1

        for number, values in enumerate(khatauni_remarks_names):
            print("llll", values)

    def khatauni_update():
        cursor = connection.cursor()
        entries1 = []
        entries2 = []
        entries3 = []
        id_names = []
        id_plots = []

        for number, values in enumerate(khatauni_entires_common):
            if represents_int(values.get()):
                entries1.insert(number, values.get())
            else:
                entries1.insert(number, "'" + values.get() + "'")
            if number == 1:
                t_var.set(values.get())
        r = entries1[0]

        cursor.execute("""UPDATE `Khatauni 1` SET `Total area`={0},`Lagan`={1} WHERE `Khatauni no.`={2} """.format(entries1[1], entries1[2], entries1[0]))

        connection.commit()
        cursor.close()

        cursor2 = connection.cursor()

        # ---------------------- Updating and inserting in Khatauni 2 ------------------------- #

        cursor2.execute("""SELECT Id FROM `Khatauni 2` WHERE `Khatauni no.` ={0} """.format(r))

        row = cursor2.fetchone()
        while row is not None:
            id_names.append(row[0])
            row = cursor2.fetchone()
        p = "("

        for number, values in enumerate(khasra_entries_names):
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

                cursor2.execute("""UPDATE `Khatauni 2` SET `Name of holder`={0},`Name of father/husband/guardian`={1},`Address`={2} 
                                                            WHERE `Khatauni no.`={3} AND `Id` = {4} """.format(entries2[0], entries2[1], entries2[2], r, nameid))
                connection.commit()

            except IndexError:
                if len(id_names) == 0:
                    new_id_names = str(1)
                else:
                    j = len(id_names) - 1
                    new_id_names = str(int(id_names[j]) + 1)
                p = p + new_id_names + ","
                p = p + khatauni_entires_common[0].get() + ","
                if represents_int(values[0].get()):
                    p = p + values[0].get() + ","
                else:
                    p = p + "'" + values[0].get() + "'" + ","

                if represents_int(values[1].get()):
                    p = p + values[1].get() + ","
                else:
                    p = p + "'" + values[1].get() + "'" + ","

                if represents_int(values[2].get()):
                    p = p + values[2].get() + ","
                else:
                    p = p + "'" + values[2].get() + "'" + ","

                p = p.rstrip(',')
                p = p + ")"

                cursor2.execute("""INSERT INTO `Khatauni 2`(`Id`,`Khatauni no.`,`Name of holder`,`Name of father/husband/guardian`,
                                                                `Address`) VALUES {0} """.format(p))
                connection.commit()

                p = "("

        # ---------------------- Updating and inserting in Khatauni 3 ------------------------- #

        cursor2.execute("""SELECT `Id` FROM `Khatauni 3` WHERE `Khatauni no.` ={0} """.format(r))

        row = cursor2.fetchone()
        while row is not None:
            id_plots.append(row[0])
            row = cursor2.fetchone()

        q = "("

        for number, values in enumerate(khasra_entries_plot):
            try:
                plotid = id_plots[number]
                if represents_int(values[0].get()):
                    entries3.insert(0, values[0].get())
                else:
                    entries3.insert(0, "'" + values[0].get() + "'")

                if represents_int(values[1].get()):
                    entries3.insert(1, values[1].get())
                else:
                    entries3.insert(1, "'" + values[1].get() + "'")

                if represents_int(values[2].get()):
                    entries3.insert(2, values[2].get())
                else:
                    entries3.insert(2, "'" + values[2].get() + "'")

                cursor2.execute("""UPDATE `Khatauni 3` SET `Fasli Year`={0},`Khasra/Plot No.`={1},`Plot Area`={2} 
                                                    WHERE `Khatauni no.`={3} AND `Id`={4} """.format(entries3[0], entries3[1], entries3[2], r, plotid))

                connection.commit()

            except IndexError:
                if len(id_plots) == 0:
                    new_id_plots = str(1)
                else:
                    i = len(id_plots) - 1
                    new_id_plots = str(int(id_plots[i]) + 1)
                id_plots.append(new_id_plots)
                q = q + new_id_plots + ","
                q = q + khatauni_entires_common[0].get() + ","
                if represents_int(values[0].get()):
                    q = q + values[0].get() + ","
                else:
                    q = q + "'" + values[0].get() + "'" + ","

                if represents_int(values[1].get()):
                    q = q + values[1].get() + ","
                else:
                    q = q + "'" + values[1].get() + "'" + ","

                if represents_int(values[2].get()):
                    q = q + values[2].get() + ","
                else:
                    q = q + "'" + values[2].get() + "'" + ","

                q = q.rstrip(',')
                q = q + ")"
                print(q)
                cursor2.execute("""INSERT INTO `Khatauni 3`(`Id`,`Khatauni no.`,`Fasli Year`,`Khasra/Plot No.`,
                                                            `Plot Area`) VALUES {0} """.format(q))
                connection.commit()

                q = "("

        cursor2.close()

        # -------------------------- Resetting after updating --------------------- #

        for w in middle.grid_slaves():
            if int(w.grid_info()["row"]) > 2:
                w.grid_forget()

        for label in middle.grid_slaves(row=2, column=7):
            label.grid_forget()

        global total, numcol
        total = 0
        numcol = 0
        khatauni_create(db_name, top, middle, bottom)

    def khatauni_delete():
        cursor = connection.cursor()

        if represents_int(khatauni_entires_common[0].get()):
            khataunino = khatauni_entires_common[0].get()
        else:
            khataunino = "'" + khatauni_entires_common[0].get() + "'"

        cursor.execute("""DELETE FROM `Khatauni 1` WHERE `Khatauni no.`={0}""".format(khataunino))
        cursor.execute("""DELETE FROM `Khatauni 2` WHERE `Khatauni no.`={0}""".format(khataunino))
        cursor.execute("""DELETE FROM `Khatauni 3` WHERE `Khatauni no.`={0}""".format(khataunino))

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
        khatauni_create(db_name, top, middle, bottom)








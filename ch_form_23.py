import tkinter as tk
import pymysql as psql
from tkinter import ttk, Entry


def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def ch_form_23_create(db_name, top, middle, bottom):
    ch23_table2 = []
    ch23_table1 = []
    ch23_new_plot_detail = []
    ch23_table3 = []
    ch23_table4 = []
    t_var = tk.StringVar()

    connection = psql.connect(host='localhost', user='root', password='', db=db_name, charset='utf8mb4',
                              cursorclass=psql.cursors.Cursor)

    serial_no = tk.Label(middle, text='Serial no.')
    serial_no.grid(row=2, column=1, padx=5, pady=5, sticky='NW')

    name = tk.Label(middle, text='Name of holder')
    name.grid(row=2, column=2, padx=5, pady=5, sticky='NW')

    father_name = tk.Label(middle, text='Name of father')
    father_name.grid(row=2, column=3, padx=5, pady=5, sticky='NW')

    address = tk.Label(middle, text='Address')
    address.grid(row=2, column=4, padx=5, pady=5, sticky='NW')

    land_category = tk.Label(middle, text='Land Category')
    land_category.grid(row=2, column=5, padx=5, pady=5, sticky='NW')

    fetch_info = ttk.Button(middle, text='FETCH CH-11', command=lambda: find_name())
    fetch_info.grid(row=2, column=7, padx=5, sticky='NEWS')

    serial_no_ch11 = tk.Label(middle, text='Sr.No. of CH11')
    serial_no_ch11.grid(row=2, column=6, padx=5, pady=5, sticky='NW')

    plot_no = tk.Label(middle, text='Plot No.')
    plot_no.grid(row=101, column=1, padx=5, pady=5, sticky='NW')

    total_area = tk.Label(middle, text='Total Plot Area(Acres)')
    total_area.grid(row=101, column=2, padx=5, pady=5, sticky='NW')

    non_consolidated_area = tk.Label(middle, text='Plot Area(Acres)\n out of consolidation')
    non_consolidated_area.grid(row=101, column=3, padx=5, pady=5, sticky='NW')

    consolidated_area = tk.Label(middle, text='Plot Area(Acres)\n in consolidation')
    consolidated_area.grid(row=101, column=4, padx=4, pady=5, sticky='NW')

    exchange_rate = tk.Label(middle, text='Exchange Rate for\n consolidated area')
    exchange_rate.grid(row=101, column=5, padx=5, pady=5, sticky='NW')

    land_value = tk.Label(middle, text='Anna Value of land\nin consolidation')
    land_value.grid(row=101, column=6, padx=5, pady=5, sticky='NW')

    lagan_plots = tk.Label(middle, text='Lagan of\nindividual plots')
    lagan_plots.grid(row=101, column=7, padx=5, pady=5, sticky='NW')

    reservation_anna_value = tk.Label(middle, text='Land contributed for\n public(anna value of land)')
    reservation_anna_value.grid(row=201, column=1, padx=5, pady=5, sticky='NW')

    reservation_area = tk.Label(middle, text='Land contributed for\n public(area of land)')
    reservation_area.grid(row=201, column=2, padx=5, pady=5, sticky='NW')

    reservation_lagan = tk.Label(middle, text='Lagaan of Land\ncontributed for public\nto be reduced')
    reservation_lagan.grid(row=201, column=3, padx=5, pady=5, sticky='NW')

    amount_of_compensation = tk.Label(middle, text='Amount of compensation\nfor contribution for\n public purpose')
    amount_of_compensation.grid(row=201, column=4, padx=5, pady=5, sticky='NW')

    net_evaluation = tk.Label(middle, text='Net evaluation to be alloted')
    net_evaluation.grid(row=201, column=5, padx=5, pady=5, sticky='NW')

    info = ttk.Label(middle, text='Proposed Holding')
    info.grid(row=300, column=1, columnspan=6, padx=5, pady=5, sticky='NW')

    land_category = ttk.Label(middle, text='Land Category')
    land_category.grid(row=301, column=1, padx=5, pady=5, sticky='NW')

    new_plot_no = ttk.Label(middle, text='New Plot No.')
    new_plot_no.grid(row=301, column=2, padx=5, pady=5, sticky='NW')

    new_total_area = ttk.Label(middle, text='Plot Area(Acres)')
    new_total_area.grid(row=301, column=3, padx=5, pady=5, sticky='NW')

    exchange_ratio = ttk.Label(middle, text='Exchange Ratio')
    exchange_ratio.grid(row=301, column=4, padx=5, pady=5, sticky='NW')

    valuation = ttk.Label(middle, text='Valuation(Plot area*exchange ratio)')
    valuation.grid(row=301, column=5, padx=5, pady=5, sticky='NW')

    new_land_revenue = ttk.Label(middle, text='Land Revenue payable \n(Total lagan-lagan of \ncontributed land)')
    new_land_revenue.grid(row=301, column=6, padx=5, pady=5, sticky='NW')

    add_proposed_holding = ttk.Button(middle, text='Add', command=lambda: add(1, 6, ch23_new_plot_detail))
    add_proposed_holding.grid(row=301, column=7, columnspan=2, sticky='NW', pady=5)

    entry_serial_no = ttk.Entry(middle)
    entry_serial_no.grid(row=3, column=1, padx=5, pady=5, sticky='NW')
    ch23_table2.append(entry_serial_no)

    entry_name = ttk.Entry(middle)
    entry_name.grid(row=3, column=2, padx=5, pady=5, sticky='NW')

    entry_father_name = ttk.Entry(middle)
    entry_father_name.grid(row=3, column=3, padx=5, pady=5, sticky='NW')

    entry_address = ttk.Entry(middle)
    entry_address.grid(row=3, column=4, padx=5, pady=5, sticky='NW')

    entry_land_category = ttk.Entry(middle)
    entry_land_category.grid(row=3, column=5, padx=5, pady=5, sticky='NW')

    entry_sr_no_ch11 = ttk.Entry(middle)
    entry_sr_no_ch11.grid(row=3, column=6, padx=5, pady=5, sticky='NW')
    ch23_table2.append(entry_sr_no_ch11)

    entry_plot_no = ttk.Entry(middle)
    entry_plot_no.grid(row=102, column=1, padx=5, pady=5, sticky='NW')

    entry_total_area = ttk.Entry(middle)
    entry_total_area.grid(row=102, column=2, padx=5, pady=5, sticky='NW')

    entry_consolidated_area = ttk.Entry(middle)
    entry_consolidated_area.grid(row=102, column=3, padx=5, pady=5, sticky='NW')

    entry_non_consolidated_area = ttk.Entry(middle)
    entry_non_consolidated_area.grid(row=102, column=4, padx=5, pady=5, sticky='NW')

    entry_exchange_entry = ttk.Entry(middle)
    entry_exchange_entry.grid(row=102, column=5, padx=5, pady=5, sticky='NW')

    entry_land_valuation = ttk.Entry(middle)
    entry_land_valuation.grid(row=102, column=6, padx=5, pady=5, sticky='NW')

    entry_individual_lagan = ttk.Entry(middle)
    entry_individual_lagan.grid(row=102, column=7, padx=5, pady=5, sticky='NW')

    entry_reservation_anna_value = ttk.Entry(middle)
    entry_reservation_anna_value.grid(row=202, column=1, padx=5, pady=5, sticky='NW')

    entry_reservation_area = ttk.Entry(middle)
    entry_reservation_area.grid(row=202, column=2, padx=5, pady=5, sticky='NW')

    entry_reservation_lagan = ttk.Entry(middle)
    entry_reservation_lagan.grid(row=202, column=3, padx=5, pady=5, sticky='NW')

    entry_amount_of_compensation = ttk.Entry(middle)
    entry_amount_of_compensation.grid(row=202, column=4, padx=5, pady=5, sticky='NW')

    entry_net_evaluation = ttk.Entry(middle)
    entry_net_evaluation.grid(row=202, column=5, padx=5, pady=5, sticky='NW')

    entry_new_land_category = ttk.Entry(middle)
    entry_new_land_category.grid(row=302, column=1, padx=5, pady=5, sticky='NW')

    entry_new_plot_no = ttk.Entry(middle)
    entry_new_plot_no.grid(row=302, column=2, padx=5, pady=5, sticky='NW')

    entry_new_total_area = ttk.Entry(middle)
    entry_new_total_area.grid(row=302, column=3, padx=5, pady=5, sticky='NW')

    entry_new_exchange_ratio = ttk.Entry(middle)
    entry_new_exchange_ratio.grid(row=302, column=4, padx=5, pady=5, sticky='NW')

    entry_new_valuation = ttk.Entry(middle)
    entry_new_valuation.grid(row=302, column=5, padx=5, pady=5, sticky='NW')

    entry_new_land_revenue = ttk.Entry(middle)
    entry_new_land_revenue.grid(row=302, column=6, padx=5, pady=5, sticky='NW')

    ch23_new_plot_detail.append((entry_serial_no, entry_new_land_category, entry_new_plot_no, entry_new_total_area,
                                 entry_new_exchange_ratio, entry_new_valuation, entry_new_land_revenue))
    ch23_table1.append((entry_serial_no, entry_name, entry_father_name, entry_address))
    ch23_table3.append((entry_serial_no, entry_plot_no, entry_total_area, entry_non_consolidated_area, entry_consolidated_area,
                        entry_exchange_entry, entry_land_valuation, entry_individual_lagan))
    ch23_table4.append((entry_serial_no, entry_reservation_anna_value, entry_reservation_area, entry_reservation_lagan,
                        entry_amount_of_compensation, entry_net_evaluation))

    insert_ch23a = ttk.Button(bottom, text='INSERT', command=lambda: insert())
    insert_ch23a.grid(row=0, column=0, padx=5, sticky='NE')

    update_ch23a = ttk.Button(bottom, text='UPDATE', command=lambda: update())
    update_ch23a.grid(row=0, column=1, padx=5, sticky='NE')

    fetch_ch23a = ttk.Button(bottom, text='FETCH', command=lambda: fetch())
    fetch_ch23a.grid(row=0, column=2, padx=5, sticky='NE')

    delete_ch23a = ttk.Button(bottom, text='DELETE', command=lambda: delete())
    delete_ch23a.grid(row=0, column=3, padx=5, sticky='NE')

    def add(start_col, no_of_col, entry):
        global temp
        temp = []
        rows = 303 + len(entry)
        for i in range(0, no_of_col):
            ent_val2 = tk.StringVar()
            ent = ttk.Entry(middle, textvariable=ent_val2)
            ent.grid(row=rows, column=start_col, padx=5, pady=5, sticky='NW')
            temp.append(ent_val2)
            start_col = start_col+1
        entry.append(temp)

    def find_name():
        ch11_names_container = []
        ch11_plot_container = []
        ch2_plot_info = []
        cursor = connection.cursor()

        s = "'" + ch23_table2[1].get() + "'"

        cursor.execute("""SELECT `Name`,`Father Name`,`Address` FROM `CHForm11 2` WHERE `Serial no.` ={0} """.format(s))

        row = cursor.fetchone()
        while row is not None:
            ch11_names_container.append(row)
            row = cursor.fetchone()

        row = 3
        for number, values in enumerate(ch11_names_container):
            col1 = 2
            if number == 0:
                e = ch23_table1[number]
                e[1].delete(0, "end")
                e[1].insert(number, values[0])
                e[2].delete(0, "end")
                e[2].insert(number, values[1])
                e[3].delete(0, "end")
                e[3].insert(number, values[2])

                row = row + 1

            else:
                ent1 = ttk.Entry(middle)
                ent1.grid(row=row, column=col1, padx=5, pady=5, sticky='NW')
                ent2 = ttk.Entry(middle)
                ent2.grid(row=row, column=col1 + 1, padx=5, pady=5, sticky='NW')
                ent3 = ttk.Entry(middle)
                ent3.grid(row=row, column=col1 + 2, padx=5, pady=5, sticky='NW')

                ch23_table1.append((entry_serial_no, ent1, ent2, ent3))
                e = ch23_table1[number]
                e[1].delete(0, "end")
                e[1].insert(number, values[0])
                e[2].delete(0, "end")
                e[2].insert(number, values[1])
                e[3].delete(0, "end")
                e[3].insert(number, values[2])

                row = row + 1

        cursor.execute("""SELECT `Plot No.`,`Area` FROM `CHForm11 1` WHERE `Serial no.` ={0} """.format(s))

        row = cursor.fetchone()

        cursor2 = connection.cursor()

        while row is not None:
            ch11_plot_container.append(row)
            row = cursor.fetchone()
        row = 102
        for number, values in enumerate(ch11_plot_container):
            col1 = 1
            plot2A = "'" + values[0] + "'"
            cursor2.execute("""SELECT `Area (Non consolidable)`,`Area (Consolidable)`,`Modified exchange ratio`,`Valuation as modified by superior authorities (col27 X col30)`
                               FROM `C.H. Form 2-A-1` WHERE `Plot No` ={0} """.format(plot2A))
            row2 = cursor2.fetchone()

            if number == 0:
                e = ch23_table3[number]
                e[1].delete(0, "end")
                e[1].insert(number, values[0])
                e[2].delete(0, "end")
                e[2].insert(number, values[1])
                if row2 is not None:
                    ch2_plot_info.append(row2)
                    row2 = cursor2.fetchone()
                    values2 = ch2_plot_info[number]
                    print("aaaaa")
                    print(values2)
                    e[4].delete(0, "end")
                    e[4].insert(number, values2[0])
                    e[3].delete(0, "end")
                    e[3].insert(number, values2[1])
                    e[5].delete(0, "end")
                    e[5].insert(number, values2[2])
                    e[6].delete(0, "end")
                    e[6].insert(number, values2[3])
                row = row + 1

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
                ent7 = ttk.Entry(middle)
                ent7.grid(row=row, column=col1 + 6, padx=5, pady=5, sticky='NW')

                ch23_table3.append((entry_serial_no, ent1, ent2, ent3, ent4, ent5, ent6, ent7))
                e = ch23_table3[number]
                e[1].delete(0, "end")
                e[1].insert(number, values[0])
                e[2].delete(0, "end")
                e[2].insert(number, values[1])

                if row2 is not None:
                    ch2_plot_info.append(row2)
                    row2 = cursor2.fetchone()
                    values2 = ch2_plot_info[number]
                    print("ddddd")
                    print(values2)
                    e[3].delete(0, "end")
                    e[3].insert(number, values2[0])
                    e[4].delete(0, "end")
                    e[4].insert(number, values2[1])
                    e[5].delete(0, "end")
                    e[5].insert(number, values2[2])
                    e[6].delete(0, "end")
                    e[6].insert(number, values2[3])

                row = row + 1

    def insert():
        serial_no = []
        cursor = connection.cursor()

        r = "("
        for number, values in enumerate(ch23_table2):
            if number == 0:
                serial_no = "'" + values.get() + "'"

            if represents_int(values.get()):
                r = r + values.get() + ","
            else:
                r = r + "'" + values.get() + "'" + ","

        r = r.rstrip(',')
        r = r + ")"
        print("y")

        cursor.execute("""INSERT INTO `CH23 2`(`Serial no.`,`Sr. no. of CH11`) VALUES {0} """.format(r))

        connection.commit()

        cursor.close()

        cursor2 = connection.cursor()

        cursor2.execute("""SELECT * FROM `CH23 1` WHERE `Serial no.`={0} """.format(serial_no))
        row = cursor2.fetchone()
        if row is None:
            id = '0'
        else:
            id = row[0]

        p = "("
        for number, values in enumerate(ch23_table1):
            id = str(int(id) + 1)
            p = p + id + ","
            print(values)
            for x in range(0, 4):
                print(values[x].get())
                if represents_int(values[x].get()):
                    p = p + values[x].get() + ","
                else:
                    p = p + "'" + values[x].get() + "'" + ","

            p = p.rstrip(',')
            p = p + ")"
            print(p)

            cursor2.execute(
                    """INSERT INTO `CH23 1`(`Id`,`Serial no.`,`Name of holder`,`Name of father/husband/guardian`,`Address`) 
                      VALUES {0} """.format(p))

            connection.commit()
            p = "("

        cursor2.close()

        cursor3 = connection.cursor()

        cursor3.execute("""SELECT * FROM `CH23 3` WHERE `Serial no.`={0} """.format(serial_no))
        row = cursor3.fetchone()
        if row is None:
            id = '0'
        else:
            id = row[0]

        q = "("
        for number, values in enumerate(ch23_table3):
            id = str(int(id) + 1)
            q = q + id + ","
            print(values)
            for x in range(0, 8):
                if represents_int(values[x].get()):
                    q = q + values[x].get() + ","
                else:
                    q = q + "'" + values[x].get() + "'" + ","

            q = q.rstrip(',')
            q = q + ")"
            print(q)

            cursor3.execute(
                """INSERT INTO `CH23 3`(`Id`,`Serial no.`,`Plot no.`,`Area of plot`,`Area of plot for CH18`,
                `Area of plot in consolidation`,`Exchange rate of consolidated area`,`Value of consolidated area`,
                `Lagan of inividual plot`) VALUES {0} """.format(q))

            connection.commit()
            q = "("

        cursor3.close()

        cursor4 = connection.cursor()
        s = "("
        for number, values in enumerate(ch23_table4):
            print(values)
            for x in range(0, 6):
                if represents_int(values[x].get()):
                    s = s + values[x].get() + ","
                else:
                    s = s + "'" + values[x].get() + "'" + ","

            s = s.rstrip(',')
            s = s + ")"
            print(s)

            cursor4.execute(
                """INSERT INTO `CH23 4`(`Serial no.`,`Contribution for public purpose in terms of anna value`,
                `Contribution for public purpose in terms of area`,`Reservation lagan`,
                `Amount of compensation`,`Net evaluation`) VALUES {0} """.format(s))

            connection.commit()
            s = "("

        cursor4.close()

        cursor5 = connection.cursor()
        cursor5.execute("""SELECT * FROM `CH23 5` WHERE `Serial no.`={0} """.format(serial_no))
        row = cursor5.fetchone()
        if row is None:
            id = '0'
        else:
            id = row[0]

        t = "("
        for number, values in enumerate(ch23_new_plot_detail):
            id = str(int(id) + 1)
            t = t + id + ","
            print(values)
            for x in range(0, 7):
                if represents_int(values[x].get()):
                    t = t + values[x].get() + ","
                else:
                    t = t + "'" + values[x].get() + "'" + ","

        t = t.rstrip(',')
        t = t + ")"
        print(s)

        cursor5.execute(
            """INSERT INTO `CH23 5`(`Id`,`Serial no.`,`Land category`,`New plot no.`,`Area`,`Exchange rate`,
            `Net Evaluation of new plot`,`New land revenue`) VALUES {0} """.format(t))

        connection.commit()
        cursor5.close()
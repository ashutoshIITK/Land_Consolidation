import tkinter as tk
import pymysql as psql
from tkinter import ttk


def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def khasra_create(db_name, top, middle, bottom):
    khasra_entries_crop = []
    khatauni_value = []

    connection = psql.connect(host='localhost', user='root', password='', db=db_name, charset='utf8mb4',
                              cursorclass=psql.cursors.Cursor)

    plot_no = tk.Label(middle, text='गाटे की क्रम संख्या\nPlot No.')
    plot_no.grid(row=1, column=0, padx=5, pady=5, sticky='NW')

    khatauni_no = ttk.Label(middle, text='खतौनी क्रम संख्या\nKhatauni no.')
    khatauni_no.grid(row=1, column=1, padx=5, pady=5, sticky='NW')

    area = tk.Label(middle, text='क्षेत्रफल\nTotal Area')
    area.grid(row=1, column=3, padx=5, pady=5, sticky='NW')

    name = tk.Label(middle, text='नाम\nName')
    name.grid(row=1, column=2, padx=5, pady=5, sticky='NW')

    source_of_irrigation = tk.Label(middle, text='सिंचाई का साधन\nSource of Irrigation')
    source_of_irrigation.grid(row=1, column=4, padx=5, pady=5, sticky='NW')

    kharif_crop = tk.Label(middle, text='खरीफ फसल\nKharif Crop')
    kharif_crop.grid(row=0, column=5, columnspan=3, padx=5, pady=5, sticky='NWES')

    kharif_crop_name = tk.Label(middle, text='Crop Name')
    kharif_crop_name.grid(row=1, column=5, padx=5, pady=5, sticky='NW')

    kharif_crop_irrigated = tk.Label(middle, text='सिंचित क्षेत्रफल\nIrrigated Area')
    kharif_crop_irrigated.grid(row=1, column=6, padx=5, pady=5, sticky='NW')

    kharif_crop_non_irrigated = tk.Label(middle, text='असिंचित क्षेत्रफल\nNon-Irrigated Area')
    kharif_crop_non_irrigated.grid(row=1, column=7, padx=5, pady=5, sticky='NW')

    rabi_crop = tk.Label(middle, text='रबी फसल\nRabi Crop')
    rabi_crop.grid(row=3, column=5, columnspan=3, padx=5, pady=5, sticky='NWES')

    rabi_crop_name = tk.Label(middle, text='फसल का नाम\nCrop Name')
    rabi_crop_name.grid(row=4, column=5, padx=5, pady=5, sticky='NW')

    rabi_crop_irrigated = tk.Label(middle, text='सिंचित क्षेत्रफल\nIrrigated Area')
    rabi_crop_irrigated.grid(row=4, column=6, padx=5, pady=5, sticky='NW')

    rabi_crop_non_irrigated = tk.Label(middle, text='असिंचित क्षेत्रफल\nNon-Irrigated Area')
    rabi_crop_non_irrigated.grid(row=4, column=7, padx=5, pady=5, sticky='NW')

    zaid_crop = tk.Label(middle, text='ज़ैद फसल\nZaid Crop')
    zaid_crop.grid(row=6, column=5, columnspan=3, padx=5, pady=5, sticky='NWES')

    zaid_crop_name = tk.Label(middle, text='फसल का नाम\nCrop Name')
    zaid_crop_name.grid(row=7, column=5, padx=5, pady=5, sticky='NW')

    zaid_crop_irrigated = tk.Label(middle, text='सिंचित क्षेत्रफल\nIrrigated Area')
    zaid_crop_irrigated.grid(row=7, column=6, padx=5, pady=5, sticky='NW')

    zaid_crop_non_irrigated = tk.Label(middle, text='असिंचित क्षेत्रफल\n\nNon-Irrigated Area')
    zaid_crop_non_irrigated.grid(row=7, column=7, padx=5, pady=5, sticky='NW')

    two_crop = tk.Label(middle, text='Two Crop area')
    two_crop.grid(row=9, column=5, columnspan=3, padx=5, pady=5, sticky='NWSE')

    two_crop_irrigated_area = tk.Label(middle, text='सिंचाई योग्य क्षेत्रफल\nIrrigatable Area')
    two_crop_irrigated_area.grid(row=10, column=5, padx=5, pady=5, sticky='NW')

    two_crop_non_irrigated_area = ttk.Label(middle, text='सिंचाई अयोग्य क्षेत्रफल\nNon-Irrigatable Area')
    two_crop_non_irrigated_area.grid(row=10, column=7, padx=5, pady=5, sticky='NW')

    description_of_trees = ttk.Label(middle, text='वृक्षों का विवरण\nDescripton Of Trees')
    description_of_trees.grid(row=1, column=8, padx=5, pady=5, sticky='NW')

    remarks = ttk.Label(middle, text='विशेष विवरण\nRemarks')
    remarks.grid(row=1, column=9, padx=5, pady=5, sticky='NW')

    entry_plot_no = ttk.Entry(middle)
    entry_plot_no.grid(row=2, column=0, padx=5, pady=5, sticky='NW')

    entry_khatauni_no = ttk.Entry(middle)
    entry_khatauni_no.grid(row=2, column=1, padx=5, pady=5, sticky='NW')

    entry_source_of_irrigation = ttk.Entry(middle)
    entry_source_of_irrigation.grid(row=2, column=4, padx=5, pady=5, sticky='NW')

    entry_kharif_crop_name = ttk.Entry(middle)
    entry_kharif_crop_name.grid(row=2, column=5, padx=5, pady=5, sticky='NW')

    entry_kharif_crop_irrigated = ttk.Entry(middle)
    entry_kharif_crop_irrigated.grid(row=2, column=6, padx=5, pady=5, sticky='NW')

    entry_kharif_crop_non_irrigated = ttk.Entry(middle)
    entry_kharif_crop_non_irrigated.grid(row=2, column=7, padx=5, pady=5, sticky='NW')

    entry_rabi_crop_name = ttk.Entry(middle)
    entry_rabi_crop_name.grid(row=5, column=5, padx=5, pady=5, sticky='NW')

    entry_rabi_crop_irrigated = ttk.Entry(middle)
    entry_rabi_crop_irrigated.grid(row=5, column=6, padx=5, pady=5, sticky='NW')

    entry_rabi_crop_non_irrigated = ttk.Entry(middle)
    entry_rabi_crop_non_irrigated.grid(row=5, column=7, padx=5, pady=5, sticky='NW')

    entry_zaid_crop_name = ttk.Entry(middle)
    entry_zaid_crop_name.grid(row=8, column=5, padx=5, pady=5, sticky='NW')

    entry_zaid_crop_irrigated = ttk.Entry(middle)
    entry_zaid_crop_irrigated.grid(row=8, column=6, padx=5, pady=5, sticky='NW')

    entry_zaid_crop_non_irrigated = ttk.Entry(middle)
    entry_zaid_crop_non_irrigated.grid(row=8, column=7, padx=5, pady=5, sticky='NW')

    entry_two_crop_irrigated_area = ttk.Entry(middle)
    entry_two_crop_irrigated_area.grid(row=11, column=5, padx=5, pady=5, sticky='NW')

    entry_two_crop_non_irrigated_area = ttk.Entry(middle)
    entry_two_crop_non_irrigated_area.grid(row=11, column=7, padx=9, pady=5, sticky='NW')

    entry_description_of_trees = ttk.Entry(middle)
    entry_description_of_trees.grid(row=2, column=8, padx=5, pady=5, sticky='NW')

    entry_remarks = ttk.Entry(middle)
    entry_remarks.grid(row=2, column=9, padx=5, pady=5, sticky='NW')

    khasra_entries_crop.append((entry_plot_no, entry_khatauni_no, entry_source_of_irrigation, entry_kharif_crop_name, entry_kharif_crop_irrigated, entry_kharif_crop_non_irrigated,
                                entry_rabi_crop_name, entry_rabi_crop_irrigated, entry_rabi_crop_non_irrigated, entry_zaid_crop_name, entry_zaid_crop_irrigated,
                                entry_zaid_crop_non_irrigated, entry_two_crop_irrigated_area, entry_two_crop_non_irrigated_area, entry_description_of_trees, entry_remarks))

    fetch_from_khatauni = ttk.Button(middle, text='FIND KHATAUNI', command=lambda: find_khatauni_no())
    fetch_from_khatauni.grid(row=0, column=0, padx=5, sticky='NEWS')

    fetch_name = ttk.Button(middle, text='FIND NAME & AREA', command=lambda: find_name_from_khatauni())
    fetch_name.grid(row=0, column=1, padx=5, sticky='NEWS')

    insert_khasra = ttk.Button(bottom, text='INSERT', command=lambda: khasra_insert())
    insert_khasra.grid(row=0, column=0, padx=5, sticky='NE')

    update_khasra = ttk.Button(bottom, text='UPDATE', command=lambda: khasra_update())
    update_khasra.grid(row=0, column=1, padx=5, sticky='NE')

    fetch_khasra = ttk.Button(bottom, text='FETCH', command=lambda: khasra_fetch())
    fetch_khasra.grid(row=0, column=2, padx=5, sticky='NE')

    delete_khasra = ttk.Button(bottom, text='DELETE', command=lambda: khasra_delete())
    delete_khasra.grid(row=0, column=3, padx=5, sticky='NE')

    details_khasra = ttk.Button(bottom, text='REPORT', command=lambda: show_status())
    details_khasra.grid(row=0, column=4, padx=5, sticky='NE')

    def show_status():
        cursor_new = connection.cursor()
        cursor_new.execute('SELECT * FROM `khasra`')
        from tkinter import messagebox
        messagebox.showinfo("Number of entries", "Number of entries = {}".format(cursor_new.rowcount))

    def find_khatauni_no():
        khatauni_plots_container = []

        cursor = connection.cursor()
        for number, values in enumerate(khasra_entries_crop):
            for x in range(0, 1):
                r = "'" + values[0].get() + "'"

        cursor.execute("""SELECT * FROM `Khatauni 3` WHERE `Khasra/Plot No.` ={0} """.format(r))

        row = cursor.fetchone()
        while row is not None:
            khatauni_plots_container.append(row)
            row = cursor.fetchone()

        header = tk.Label(middle, text="List Of Khatauni No.")
        header.grid(row=4, column=0, padx=5, pady=5, sticky='NW')

        for number, values in enumerate(khatauni_plots_container):
            khatauni_value.insert(number, values[1])
            name = tk.Label(middle, text=values[1])
            name.grid(row=number + 5, column=0, padx=5, pady=5, sticky='NWES')

    def find_name_from_khatauni():
        khatauni_names_container = []
        cursor = connection.cursor()

        for number, values in enumerate(khasra_entries_crop):
                if represents_int(values[1].get()):
                    r = values[1].get()
                else:
                    r = "'" + values[1].get() + "'"

        cursor.execute("""SELECT * FROM `Khatauni 2` WHERE `Khatauni no.` ={0} """.format(r))

        row = cursor.fetchone()
        while row is not None:
            khatauni_names_container.append(row)
            row = cursor.fetchone()

        for number, values in enumerate(khatauni_names_container):
            name = tk.Label(middle, text=values[2])
            name.grid(row=number+2, column=2, padx=5, pady=5, sticky='NW')

        khatauni_plots_container = []
        cursor = connection.cursor()
        for number, values in enumerate(khasra_entries_crop):
            for x in range(0, 1):
                r = "'" + values[0].get() + "'"

        cursor.execute("""SELECT * FROM `Khatauni 3` WHERE `Khasra/Plot No.` ={0} """.format(r))

        row = cursor.fetchone()
        while row is not None:
            khatauni_plots_container.append(row)
            row = cursor.fetchone()

        for number, values in enumerate(khatauni_plots_container):
            print(number)
            print(values[2])
            name = tk.Label(middle, text=values[4])
            name.grid(row=2, column=3, padx=5, pady=5, sticky='NW')

    def khasra_insert():
        cursor = connection.cursor()

        r = "("
        for number, values in enumerate(khasra_entries_crop):
            for x in range(0, 16):
                if represents_int(values[x].get()):
                    r = r + values[x].get() + ","
                else:
                    r = r + "'" + values[x].get() + "'" + ","

        r = r.rstrip(',')
        r = r + ")"
        print("hy", r)

        cursor.execute("""INSERT INTO `Khasra`(`Plot no.`,`Khatauni no.`,`Source of Irrigation`,`Kharif crop Name`,`Kharif crop irrigated area`,`Kharif crop non-irrigated ares`,
        `Rabi crop Name`,`Rabi crop irrigated area`,`Rabi crop non-irrigated ares`,`Zaid crop Name`,`Zaid crop irrigated area`,`Zaid crop non-irrigated ares`,
        `Two crop irrigated area`,`Two crop non-irrigated area`,`Description of trees`,`Remark`) VALUES {0} """.format(r))

        connection.commit()
        cursor.close()

        # -------------------------- Resetting after deleting --------------------- #

        for w in middle.grid_slaves():
            if int(w.grid_info()['row']) > 1:
                w.grid_forget()

        khasra_create(db_name, top, middle, bottom)

    def khasra_fetch():
        khasra_entries_container = []

        cursor = connection.cursor()

        for number, values in enumerate(khasra_entries_crop):
                if represents_int(values[0].get()):
                    s = values[0].get()
                else:
                    s = "'" + values[0].get() + "'"

                if represents_int(values[1].get()):
                    r = values[1].get()
                else:
                    r = "'" + values[1].get() + "'"

        cursor.execute("""SELECT * FROM `Khasra` WHERE `Plot no.` ={0} AND `Khatauni no.` = {1} """.format(s, r))

        row = cursor.fetchone()

        for l in range(0, 16):
            khasra_entries_container.insert(l, row[l])

        #-------------------fill data in form-------------------#

        for number, values in enumerate(khasra_entries_container):
            if number == 0:
                e = khasra_entries_crop[0][number]
                e.delete(0, "end")
                e.insert(number, values)
            if number == 1:
                e = khasra_entries_crop[0][number]
                e.delete(0, "end")
                e.insert(number, values)
            if number == 2:
                e = khasra_entries_crop[0][number]
                e.delete(0, "end")
                e.insert(number, values)
            if number == 3:
                e = khasra_entries_crop[0][number]
                e.delete(0, "end")
                e.insert(number, values)
            if number == 4:
                e = khasra_entries_crop[0][number]
                e.delete(0, "end")
                e.insert(number, values)
            if number == 5:
                e = khasra_entries_crop[0][number]
                e.delete(0, "end")
                e.insert(number, values)
            if number == 6:
                e = khasra_entries_crop[0][number]
                e.delete(0, "end")
                e.insert(number, values)
            if number == 7:
                e = khasra_entries_crop[0][number]
                e.delete(0, "end")
                e.insert(number, values)
            if number == 8:
                e = khasra_entries_crop[0][number]
                e.delete(0, "end")
                e.insert(number, values)
            if number == 9:
                e = khasra_entries_crop[0][number]
                e.delete(0, "end")
                e.insert(number, values)
            if number == 10:
                e = khasra_entries_crop[0][number]
                e.delete(0, "end")
                e.insert(number, values)
            if number == 11:
                e = khasra_entries_crop[0][number]
                e.delete(0, "end")
                e.insert(number, values)
            if number == 12:
                e = khasra_entries_crop[0][number]
                e.delete(0, "end")
                e.insert(number, values)
            if number == 13:
                e = khasra_entries_crop[0][number]
                e.delete(0, "end")
                e.insert(number, values)
            if number == 14:
                e = khasra_entries_crop[0][number]
                e.delete(0, "end")
                e.insert(number, values)
            if number == 15:
                e = khasra_entries_crop[0][number]
                e.delete(0, "end")
                e.insert(number, values)

    def khasra_update():
        cursor = connection.cursor()
        entries = []

        for number, values in enumerate(khasra_entries_crop):
            if number == 0:
                if represents_int(values[0].get()):
                    r = values[0].get()
                else:
                    r = "'" + values[0].get() + "'"

                if represents_int(values[1].get()):
                    s = values[1].get()
                else:
                    s = "'" + values[1].get() + "'"
        for number, values in enumerate(khasra_entries_crop):
            for x in range(0, 16):
                if represents_int(values[x].get()):
                    entries.insert(x, values)
                else:
                    entries.insert(x, "'" + values[x].get() + "'")

        cursor.execute("""UPDATE `Khasra` SET `Source of Irrigation`={0},`Kharif crop Name`={2},`Kharif crop irrigated area`={3},`Kharif crop non-irrigated ares`={4},`Rabi crop Name`={5},`Rabi crop irrigated area`={6},`Rabi crop non-irrigated ares`={7},`Zaid crop Name`={8},`Zaid crop irrigated area`={9},`Zaid crop non-irrigated ares`={10},
                `Two crop irrigated area`={11},`Two crop non-irrigated area`={12},`Description of trees`={13},`Remark`={14} WHERE `Plot no.`={1} AND `Khatauni no.` = {15} """.format(entries[1], r,entries[2], entries[3], entries[4], entries[5], entries[6], entries[7], entries[8], entries[9], entries[10], entries[11], entries[12], entries[13], entries[14], s))

        connection.commit()

    def khasra_delete():
        cursor = connection.cursor()

        for number, values in enumerate(khasra_entries_crop):
            for x in range(0,1):
                if represents_int(values[x].get()):
                    khasra_no = values[x].get()
                else:
                    khasra_no = "'" + values[x].get() + "'"

        cursor.execute("""DELETE FROM `Khasra` WHERE `Plot no.`={0} AND `Khatauni no.` = {1} """.format(khasra_no))

        connection.commit()
        cursor.close()

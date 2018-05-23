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

def form5_extract_create(db_name, top, middle, bottom):
    khasra_entries_crop = []
    temp = []
    t_var = tk.StringVar()

    connection = psql.connect(host='localhost', user='root', password='', db=db_name, charset='utf8mb4',
                              cursorclass=psql.cursors.Cursor)


    khatauni_no = tk.Label(middle, text='Khatauni No.')
    khatauni_no.grid(row=1, column=0, padx=5, pady=5, sticky='NW')

    name = tk.Label(middle, text='Name')
    name.grid(row=1, column=1, padx=5, pady=5, sticky='NW')

    father_name = tk.Label(middle, text='Father Name')
    father_name.grid(row=1, column=2, padx=5, pady=5, sticky='NW')

    address = tk.Label(middle, text='Address')
    address.grid(row=1, column=3, padx=5, pady=5, sticky='NW')

    class_of_tenure = tk.Label(middle, text='Class of Tenure')
    class_of_tenure.grid(row=1, column=4, padx=5, pady=5, sticky='NW')

    kharif_crop = tk.Label(middle, text='Fasli Year')
    kharif_crop.grid(row=1, column=5, columnspan=3, padx=5, pady=5, sticky='NWES')

    plot_no = tk.Label(middle, text='Plot No.')
    plot_no.grid(row=1, column=6, padx=5, pady=5, sticky='NW')

    total_area = tk.Label(middle, text='Area')
    total_area.grid(row=1, column=7, padx=5, pady=5, sticky='NW')

    consolidable_area = tk.Label(middle, text='Consolidable Area')
    consolidable_area.grid(row=1, column=8, padx=5, pady=5, sticky='NW')

    non_consolidable_area = tk.Label(middle, text='Non-Consolidable Area')
    non_consolidable_area.grid(row=1, column=9, padx=5, pady=5, sticky='NW')

    exchange_ratio = tk.Label(middle, text='Exchange Ratio in Anna')
    exchange_ratio.grid(row=5, column=5, columnspan=3, padx=5, pady=5, sticky='NWES')

    total_value = tk.Label(middle, text='Total Value of Consolidable Area')
    total_value.grid(row=6, column=5, padx=5, pady=5, sticky='NW')

    description = tk.Label(middle, text='Description of Trees, Wells, Tube-Wells')
    description.grid(row=6, column=6, padx=5, pady=5, sticky='NW')

    measurement_and_age = tk.Label(middle, text='Measurement and Age')
    measurement_and_age.grid(row=6, column=7, padx=5, pady=5, sticky='NW')

    estimated_value = tk.Label(middle, text='Estimated value')
    estimated_value.grid(row=9, column=5, columnspan=3, padx=5, pady=5, sticky='NWES')

    name_of_owner = tk.Label(middle, text='Name of owner')
    name_of_owner.grid(row=10, column=5, padx=5, pady=5, sticky='NW')

    land_revenue= tk.Label(middle, text='land Revenue Payable')
    land_revenue.grid(row=10, column=6, padx=5, pady=5, sticky='NW')

    remarks = tk.Label(middle, text='Remarks')
    remarks.grid(row=1, column=9, padx=5, pady=5, sticky='NW')


    entry_khatauni_no = tk.Entry(middle)
    entry_khatauni_no.grid(row=2, column=0, padx=5, pady=5, sticky='NW')

    entry_name = tk.Entry(middle)
    entry_name.grid(row=2, column=1, padx=5, pady=5, sticky='NW')

    entry_father_name = tk.Entry(middle)
    entry_father_name.grid(row=2, column=1, padx=5, pady=5, sticky='NW')

    entry_address = tk.Entry(middle)
    entry_address.grid(row=2, column=3, padx=5, pady=5, sticky='NW')

    entry_class_of_tenure = tk.Entry(middle)
    entry_class_of_tenure.grid(row=2, column=4, padx=5, pady=5, sticky='NW')

    entry_fasli_year = tk.Entry(middle)
    entry_fasli_year.grid(row=3, column=5, padx=5, pady=5, sticky='NW')

    entry_plot_no = tk.Entry(middle)
    entry_plot_no.grid(row=3, column=6, padx=5, pady=5, sticky='NW')

    entry_total_area = tk.Entry(middle)
    entry_total_area.grid(row=3, column=7, padx=5, pady=5, sticky='NW')

    entry_consolidable_area = tk.Entry(middle)
    entry_consolidable_area.grid(row=7, column=5, padx=5, pady=5, sticky='NW')

    entry_non_consolidable_area = tk.Entry(middle)
    entry_non_consolidable_area.grid(row=7, column=6, padx=5, pady=5, sticky='NW')

    entry_exachange_ratio = tk.Entry(middle)
    entry_exachange_ratio.grid(row=7, column=7, padx=5, pady=5, sticky='NW')

    entry_total_value = tk.Entry(middle)
    entry_total_value.grid(row=11, column=5, padx=5, pady=5, sticky='NW')

    entry_description = tk.Entry(middle)
    entry_description.grid(row=11, column=6, padx=5, pady=5, sticky='NW')

    entry_measurement_and_age = tk.Entry(middle)
    entry_measurement_and_age.grid(row=11, column=7, padx=5, pady=5, sticky='NW')

    entry_estimated_value = tk.Entry(middle)
    entry_estimated_value.grid(row=14, column=5, padx=5, pady=5, sticky='NW')

    entry_name_of_owner = tk.Entry(middle)
    entry_name_of_owner.grid(row=14, column=7, padx=9, pady=5, sticky='NW')

    entry_land_revenue = tk.Entry(middle)
    entry_land_revenue.grid(row=2, column=8, padx=5, pady=5, sticky='NW')

    entry_remarks = tk.Entry(middle)
    entry_remarks.grid(row=2, column=9, padx=5, pady=5, sticky='NW')
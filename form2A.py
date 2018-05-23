import tkinter as tk
from tkinter import ttk, Entry
import pymysql as psql


def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def form2a_create(db_name, top, middle, bottom):
    table1_2a = []
    table2_2a = []
    table3_2a = []
    temp = []

    connection = psql.connect(host='localhost', user='root', password='', db=db_name, charset='utf8',
                              cursorclass=psql.cursors.Cursor)

    plot_no = ttk.Label(middle, text='गाटा संख्या\nPlot no.')
    plot_no.grid(row=1, column=0, padx=5, pady=5, sticky='NW')

    area = ttk.Label(middle, text='क्षेत्रफल\nArea')
    area.grid(row=0, column=2, columnspan=3, padx=5, pady=5, sticky='NW')

    area_khasra = ttk.Label(middle, text='जैसा की आधार खसरा के स्तम्भ २ में अभिलिखित है\nAs recorded in Khasra')
    area_khasra.grid(row=1, column=1, padx=5, pady=5, sticky='NW')

    area_bandobast = ttk.Label(middle, text='जैसा की चालू बंदोबस्त में अभिलिखित है\nAs recorded in settlement')
    area_bandobast.grid(row=1, column=2, padx=5, pady=5, sticky='NW')

    area_onspot = ttk.Label(middle, text='जैसा स्थल पर पाया जाये\nAs found on spot')
    area_onspot.grid(row=1, column=3, padx=5, pady=5, sticky='NW')

    khatauni_info = ttk.Label(middle, text='खतौनी नंबर\nKhatauni no.')
    khatauni_info.grid(row=1, column=4, padx=5, pady=5, sticky='NW')

    khatauni_area = ttk.Label(middle, text='खतौनी में क्षेत्रफल\nArea in Khatauni')
    khatauni_area.grid(row=1, column=5, padx=5, pady=5, sticky='NW')

    khatauni_name = ttk.Label(middle, text='खातेदार का नाम\nName of Tenure holder')
    khatauni_name.grid(row=1, column=6, padx=5, pady=5, sticky='NW')

    khatauni_father_name = ttk.Label(middle, text='पिता का नाम\nName of Father')
    khatauni_father_name.grid(row=1, column=7, padx=5, pady=5, sticky='NW')

    khatauni_address = ttk.Label(middle, text='पता\nAddress')
    khatauni_address.grid(row=1, column=8, padx=5, pady=5, sticky='NW')

    plot_no_entry = ttk.Entry(middle)
    plot_no_entry.grid(row=2, column=0, padx=5, pady=5, sticky='NW')
    table1_2a.append(plot_no_entry)

    area_onspot_entry = ttk.Entry(middle)
    area_onspot_entry.grid(row=2, column=3, padx=5, pady=5, sticky='NW')
    table1_2a.append(area_onspot_entry)

    add_items = ttk.Button(middle, text='Add', command=lambda: add(0, 7, table2_2a))
    add_items.grid(row=150, column=0, columnspan=2, sticky='NW', pady=5)

    label1 = ttk.Label(middle, text="""समुतरितृओं के विवरण, यदिकोई हो, जैसे कुआँ, नलकूप आदि, जो गाते में स्तिथ हो या बाग़ से भिन्न पेड़, जो गाटा या उसक सीमाओं में स्तिथ हो \nDetails of improvements, if any, like a well,tube-well etc.,existing in the
plot or trees other than those constituting a groove standing in the plot """)
    label1.grid(row=150, column=1, columnspan=7, padx=5, pady=5, sticky='NW')

    description = ttk.Label(middle, text="Description")
    description.grid(row=151, column=0, padx=5, pady=5, sticky='NW')

    description_entry = ttk.Entry(middle)
    description_entry.grid(row=152, column=0, padx=5, pady=5, sticky='NW')

    measurement = ttk.Label(middle, text="माप\nMeasurement")
    measurement.grid(row=151, column=1, padx=5, pady=5, sticky='NW')

    measurement_entry = ttk.Entry(middle)
    measurement_entry.grid(row=152, column=1, padx=5, pady=5, sticky='NW')

    age = ttk.Label(middle, text="उम्र\nAge")
    age.grid(row=151, column=2, padx=5, pady=5, sticky='NW')

    age_entry = ttk.Entry(middle)
    age_entry.grid(row=152, column=2, padx=5, pady=5, sticky='NW')

    value = ttk.Label(middle, text="अनुमानित मूल्य\nEstimated Value")
    value.grid(row=151, column=3, padx=5, pady=5, sticky='NW')

    value_entry = ttk.Entry(middle)
    value_entry.grid(row=152, column=3, padx=5, pady=5, sticky='NW')

    name = ttk.Label(middle, text="मालिक का नाम\nName of owner")
    name.grid(row=151, column=4, padx=5, pady=5, sticky='NW')

    name_entry = ttk.Entry(middle)
    name_entry.grid(row=152, column=4, padx=5, pady=5, sticky='NW')

    address = ttk.Label(middle, text="पता\nAddress")
    address.grid(row=151, column=5, padx=5, pady=5, sticky='NW')

    address_entry = ttk.Entry(middle)
    address_entry.grid(row=152, column=5, padx=5, pady=5, sticky='NW')

    share = ttk.Label(middle, text="Share")
    share.grid(row=151, column=6, padx=5, pady=5, sticky='NW')

    share_entry = ttk.Entry(middle)
    share_entry.grid(row=152, column=6, padx=5, pady=5, sticky='NW')

    table2_2a.append((description_entry, measurement_entry, age_entry, value_entry, name_entry, address_entry, share_entry))

    add_groves = ttk.Button(middle, text='Add', command=lambda: add(7, 2, table3_2a))
    add_groves.grid(row=150, column=7, columnspan=2, sticky='NW', pady=5)

    label2 = ttk.Label(middle, text="""उस वर्ष के, जिसमे धरा ४ के अधीन विज्ञाति जारी की गयी थी, ठीक पूर्व के कृषि वर्ष में विद्यमान बागुन का विवरण\nDetails of the groves existing
in the agricultural year""")
    label2.grid(row=150, column=8,  padx=5, pady=5, sticky='NW')

    nature = ttk.Label(middle, text="प्रकृति\nNature")
    nature.grid(row=151, column=7, padx=5, pady=5, sticky='NW')

    nature_entry = ttk.Entry(middle)
    nature_entry.grid(row=152, column=7, padx=5, pady=5, sticky='NW')

    area_groove = ttk.Label(middle, text="क्षेत्रफल\nArea")
    area_groove.grid(row=151, column=8, padx=5, pady=5, sticky='NW')

    area_groove_entry = ttk.Entry(middle)
    area_groove_entry.grid(row=152, column=8, padx=5, pady=5, sticky='NW')
    table3_2a.append((nature_entry, area_groove_entry))

    label3 = ttk.Label(middle, text="आकृष्ट क्षेत्रफल का विवरण\nDetails of uncultivated area")
    label3.grid(row=200, column=1, columnspan=2, padx=5, pady=5, sticky='NW')

    nature_uncultivated = ttk.Label(middle, text="प्रकृति\nNature")
    nature_uncultivated.grid(row=201, column=0, padx=5, pady=5, sticky='NW')

    nature_uncultivated_entry = ttk.Entry(middle)
    nature_uncultivated_entry.grid(row=202, column=0, padx=5, pady=5, sticky='NW')
    table1_2a.append(nature_uncultivated_entry)

    included = ttk.Label(middle, text="जोट में सम्मेलिट्\nIncluded in holdings")
    included.grid(row=201, column=1, padx=5, pady=5, sticky='NW')

    included_entry = ttk.Entry(middle)
    included_entry.grid(row=202, column=1, padx=5, pady=5, sticky='NW')
    table1_2a.append(included_entry)

    not_included = ttk.Label(middle, text="जोट में असम्मिलित\nNot included in holdings")
    not_included.grid(row=201, column=2, padx=5, pady=5, sticky='NW')

    not_included_entry = ttk.Entry(middle)
    not_included_entry.grid(row=202, column=2, padx=5, pady=5, sticky='NW')
    table1_2a.append(not_included_entry)

    label4 = ttk.Label(middle, text="सिंचाई का विवरण\nDetails of irrigation")
    label4.grid(row=200, column=4, columnspan=2, padx=5, pady=5, sticky='NW')

    source = ttk.Label(middle, text="सिंचाई का साधन\nSource")
    source.grid(row=201, column=3, padx=5, pady=5, sticky='NW')

    source_entry = ttk.Entry(middle)
    source_entry.grid(row=202, column=3, padx=5, pady=5, sticky='NW')
    table1_2a.append(source_entry)

    method = ttk.Label(middle, text="तरीका\nMethod")
    method.grid(row=201, column=4, padx=5, pady=5, sticky='NW')

    method_entry = ttk.Entry(middle)
    method_entry.grid(row=202, column=4, padx=5, pady=5, sticky='NW')
    table1_2a.append(method_entry)

    area_irrigable = ttk.Label(middle, text="सिंचाई योग्य क्षेत्रफल\nIrrigable Area")
    area_irrigable.grid(row=201, column=5, padx=5, pady=5, sticky='NW')

    area_irrigable_entry = ttk.Entry(middle)
    area_irrigable_entry.grid(row=202, column=5, padx=5, pady=5, sticky='NW')
    table1_2a.append(area_irrigable_entry)

    label5 = ttk.Label(middle, text="सामान्यता बोई जाने वाली फैसले\nCrops generally grown during")
    label5.grid(row=200, column=7, columnspan=2, padx=5, pady=5, sticky='NW')

    kharif = ttk.Label(middle, text="खरीफ\nKharif")
    kharif.grid(row=201, column=6, padx=5, pady=5, sticky='NW')

    kharif_entry = ttk.Entry(middle)
    kharif_entry.grid(row=202, column=6, padx=5, pady=5, sticky='NW')
    table1_2a.append(kharif_entry)

    rabi = ttk.Label(middle, text="रबी\nRabi")
    rabi.grid(row=201, column=7, padx=5, pady=5, sticky='NW')

    rabi_entry = ttk.Entry(middle)
    rabi_entry.grid(row=202, column=7, padx=5, pady=5, sticky='NW')
    table1_2a.append(rabi_entry)

    zaid = ttk.Label(middle, text="ज़ैद\nZaid")
    zaid.grid(row=201, column=8, padx=5, pady=5, sticky='NW')

    zaid_entry = ttk.Entry(middle)
    zaid_entry.grid(row=202, column=8, padx=5, pady=5, sticky='NW')
    table1_2a.append(zaid_entry)

    physical_features = ttk.Label(middle, text="गाते की प्राकृतिक रूप रेखा\nPhysical features of the plot")
    physical_features.grid(row=300, column=0, padx=5, pady=5, sticky='NW')

    physical_features_entry = ttk.Entry(middle)
    physical_features_entry.grid(row=301, column=0, padx=5, pady=5, sticky='NW')
    table1_2a.append(physical_features_entry)

    soil_class = ttk.Label(middle, text="भूमि का वर्ग जैसा की चालू बंदोबस्त में अभिलिखित है\nSoil class in current settlement")
    soil_class.grid(row=300, column=1, padx=5, pady=5, sticky='NW')

    soil_class_entry = ttk.Entry(middle)
    soil_class_entry.grid(row=301, column=1, padx=5, pady=5, sticky='NW')
    table1_2a.append(soil_class_entry)

    label6 = ttk.Label(middle, text="क्षेत्रफल\nArea")
    label6.grid(row=299, column=3, padx=5, pady=5, sticky='NW')

    non_consolidable = ttk.Label(middle, text="जोट चकबंदी योग्य न हो\nNon-consolidable")
    non_consolidable.grid(row=300, column=2, padx=5, pady=5, sticky='NW')

    non_consolidable_entry = ttk.Entry(middle)
    non_consolidable_entry.grid(row=301, column=2, padx=5, pady=5, sticky='NW')
    table1_2a.append(non_consolidable_entry)

    consolidable = ttk.Label(middle, text="चकबंदी योग्य\nConsolidable")
    consolidable.grid(row=300, column=3, padx=5, pady=5, sticky='NW')

    consolidable_entry = ttk.Entry(middle)
    consolidable_entry.grid(row=301, column=3, padx=5, pady=5, sticky='NW')
    table1_2a.append(consolidable_entry)

    label7 = ttk.Label(middle, text="संचालक चकबंदी अधिकारी द्वारा यथा अवधारित गाते के चकबंदी योग्य क्षेत्र का आने में विनिमय अनुपात\nExchange ratio(in annas) and valuation of consolidable area")
    label7.grid(row=299, column=4, columnspan=4, padx=5, pady=5, sticky='NW')

    byaco = ttk.Label(middle, text="गाटे के चकबंदी योग्य क्षेत्र का मूल्याङ्कन\nExchange ratio by A.C.O")
    byaco.grid(row=300, column=4, padx=5, pady=5, sticky='NW')

    byaco_entry = ttk.Entry(middle)
    byaco_entry.grid(row=301, column=4, padx=5, pady=5, sticky='NW')
    table1_2a.append(byaco_entry)

    valuation1 = ttk.Label(middle, text="जमीन का मूल्यांकन\nValuation of plot")
    valuation1.grid(row=300, column=5, padx=5, pady=5, sticky='NW')

    valuation1_entry = ttk.Entry(middle)
    valuation1_entry.grid(row=301, column=5, padx=5, pady=5, sticky='NW')
    table1_2a.append(valuation1_entry)

    modified_exchange = ttk.Label(middle, text="संशोधित विनिमय अनुपात\nModified exchange ratio")
    modified_exchange.grid(row=300, column=6, padx=5, pady=5, sticky='NW')

    modified_exchange_entry = ttk.Entry(middle)
    modified_exchange_entry.grid(row=301, column=6, padx=5, pady=5, sticky='NW')
    table1_2a.append(modified_exchange_entry)

    valuation2 = ttk.Label(middle, text="वरिष्ठ पदाधिकारिओं द्वारा यथा परिष्कृत\nModified valuation")
    valuation2.grid(row=300, column=7, padx=5, pady=5, sticky='NW')

    valuation2_entry = ttk.Entry(middle)
    valuation2_entry.grid(row=301, column=7, padx=5, pady=5, sticky='NW')
    table1_2a.append(valuation2_entry)

    label8 = ttk.Label(middle, text="जोत चकबंदी आकर-पत्र २३ का खता संख्या, जिसमे प्रादिस्ट हो और क्षेत्रफल /मूल्याङ्कन यदि आंशिक रूप से प्रादिस्ट हो\nKhata no. of C.H. form 23 to which alloted with area/valuation if partly alloted")
    label8.grid(row=310, columnspan=4, padx=5, pady=5, sticky='NW')

    by_aco = ttk.Label(middle, text="संचालक चकबंदी अधिकारी द्वारा यथाप्रस्तावित\nAs proposed by A.C.O")
    by_aco.grid(row=311, column=0, padx=5, pady=5, sticky='NW')

    by_aco_entry = ttk.Entry(middle)
    by_aco_entry.grid(row=312, column=0, padx=5, pady=5, sticky='NW')
    table1_2a.append(by_aco_entry)

    by_co = ttk.Label(middle, text="चकबंदी अधिकारी द्वारा यथाप्रस्तावित\nAs modifies by C.O.")
    by_co.grid(row=311, column=1, padx=5, pady=5, sticky='NW')

    by_co_entry = ttk.Entry(middle)
    by_co_entry.grid(row=312, column=1, padx=5, pady=5, sticky='NW')
    table1_2a.append(by_co_entry)

    by_others = ttk.Label(middle, text="""अपील और पुनरीक्षण में यथाप्रस्तावित\nAs modifies in appeals and revison""")
    by_others.grid(row=311, column=2, padx=5, pady=5, sticky='NW')

    remarks = ttk.Button(middle, text="विशेष विवरण\nRemarks", command=lambda: remark_window(middle))
    remarks.grid(row=311, column=3, padx=5, pady=5, sticky='NW')

    insert_2a = ttk.Button(bottom, text='INSERT', command=lambda: form_insert())
    insert_2a.grid(row=0, column=0, padx=5, sticky='NE')

    update_2a = ttk.Button(bottom, text='UPDATE', command=lambda: form_update())
    update_2a.grid(row=0, column=1, padx=5, sticky='NE')

    fetch_2a = ttk.Button(bottom, text='FETCH', command=lambda: form_fetch())
    fetch_2a.grid(row=0, column=2, padx=5, sticky='NE')

    delete_2a = ttk.Button(bottom, text='DELETE', command=lambda: form_delete())
    delete_2a.grid(row=0, column=3, padx=5, sticky='NE')

    details_2a = ttk.Button(bottom, text='REPORT', command=lambda: show_status())
    details_2a.grid(row=0, column=4, padx=5, sticky='NE')

    def add(start_col, no_of_col, entry):
        global temp
        temp = []
        rows = 152 + len(entry)
        for i in range(0, no_of_col):
            ent_val2 = tk.StringVar()
            ent = ttk.Entry(middle, textvariable=ent_val2)
            ent.grid(row=rows, column=start_col, padx=5, pady=5, sticky='NW')
            temp.append(ent_val2)
            start_col = start_col+1
        entry.append(temp)

    def remark_window(middle):
        remarks_form = tk.Toplevel(middle)
        remarks_form.title('Remarks Form')

        case_no = ttk.Label(remarks_form, text='Case no.')
        case_no.grid(row=2, column=0, padx=5, pady=5, sticky='NE')

        case_no_entry = ttk.Entry(remarks_form)
        case_no_entry.grid(row=3, column=0, padx=5, pady=5, sticky='NE')

        order_date = ttk.Label(remarks_form, text='Order Date')
        order_date.grid(row=2, column=1, padx=5, pady=5, sticky='NE')

        order_date_entry = ttk.Entry(remarks_form)
        order_date_entry.grid(row=3, column=1, padx=5, pady=5, sticky='NE')

        section = ttk.Label(remarks_form, text='Section')
        section.grid(row=2, column=2, padx=5, pady=5, sticky='NE')

        section_entry = ttk.Entry(remarks_form)
        section_entry.grid(row=3, column=2, padx=5, pady=5, sticky='NE')

        designation = ttk.Label(remarks_form, text='Designation')
        designation.grid(row=2, column=3, padx=5, pady=5, sticky='NE')

        designation_list = ttk.Combobox(remarks_form)
        designation_list.grid(row=3, column=3, padx=5, pady=5, sticky='NE')

        type_change = ttk.Label(remarks_form, text='Type')
        type_change.grid(row=2, column=4, padx=5, pady=5, sticky='NE')

        type_change_entry = ttk.Entry(remarks_form)
        type_change_entry.grid(row=3, column=4, padx=5, pady=5, sticky='NE')

        entry_to_be_changed = ttk.Label(remarks_form, text="Entry to be changed")
        entry_to_be_changed.grid(row=2, column=5, padx=5, pady=5, sticky='NE')

        entry_to_be_changed_entry = ttk.Entry(remarks_form)
        entry_to_be_changed_entry.grid(row=3, column=5, padx=5, pady=5, sticky='NE')

        changed_entry = ttk.Label(remarks_form, text='Changed Entry')
        changed_entry.grid(row=2, column=6, padx=5, pady=5, sticky='NE')

        changed_entry_entry = ttk.Entry(remarks_form)
        changed_entry_entry.grid(row=3, column=6, padx=5, pady=5, sticky='NE')

    def form_insert():
        plot_number = []
        cursor = connection.cursor()

        p = "("
        for number, values in enumerate(table1_2a):
            if number == 0:
                plot_number = "'" + values.get() + "'"
            if represents_int(values.get()):
                p = p + values.get() + ","
            else:
                p = p + "'" + values.get() + "'" + ","

        p = p.rstrip(',')
        p = p + ")"
        print(plot_number)
        print(p)

        cursor.execute("""INSERT INTO `C.H. Form 2-A-1`(`Plot No`,`As found on spot`,`Details of uncultivated area (Nature)`,
                          `Details of uncultivated area (Included in holding)`,`Details of uncultivated area (not included in holding)`,`Source`,
                          `Method`,`Irrigable area`,`Kharif`,`Rabi`,`Zaid`,`Physical features of the plot`,`Solid class in current settlement`,`Area (Non consolidable)`,
                          `Area (Consolidable)`,`Exchange ratio in annas (in words)`,`Valutaion of the consolidable area of the plot (col27 x col28)`,
                          `Modified exchange ratio`,`Valuation as modified by superior authorities (col27 X col30)`,`Khata no (As proposed by ACO )`,
                          `Khata no (As modified by CO)`) VALUES {0}""".format(p))

        connection.commit()
        cursor.close()

        cursor2 = connection.cursor()

        cursor2.execute("""SELECT * FROM `C.H. Form 2-A-2` WHERE `Plot No`={0} """.format(plot_number))
        row = cursor.fetchone()
        if row is None:
            id = '0'
        else:
            id = row[0].get()

        q = "("
        for number, values in enumerate(table2_2a):
            id = str(int(id) + 1)
            q = q + id + ","
            if represents_int(table1_2a[0].get()):
                q = q + table1_2a[0].get() + ","
            else:
                q = q + "'" + table1_2a[0].get() + "'" + ","

            q = q + "'" + values[0].get() + "'" + ","
            q = q + "'" + values[1].get() + "'" + ","
            q = q + "'" + values[2].get() + "'" + ","
            q = q + "'" + values[3].get() + "'" + ","
            q = q + "'" + values[4].get() + "'" + ","
            q = q + "'" + values[5].get() + "'" + ","

            if represents_int(values[6].get()):
                q = q + values[6].get() + ","
            else:
                q = q + "'" + values[6].get() + "'" + ","

            q = q.rstrip(',')
            q = q + ")"
            print(q)

            cursor2.execute("""INSERT INTO `C.H. Form 2-A-2`(`Id`,`Plot No`,`Description`,`Measurement`,`Age`,`Estimated Value`,
                              `Name of owner`,`Address`,`Share`) VALUES {0} """.format(q))
            connection.commit()

            q = "("

        cursor2.close()

        cursor3 = connection.cursor()

        cursor3.execute("""SELECT * FROM `C.H. Form 2-A-3` WHERE `Plot No`={0} """.format(plot_number))
        row = cursor.fetchone()
        if row is None:
            id = '0'
        else:
            id = row[0].get()

        r = "("
        for number, values in enumerate(table2_2a):
            id = str(int(id) + 1)
            r = r + id + ","
            if represents_int(table1_2a[0].get()):
                r = r + table1_2a[0].get() + ","
            else:
                r = r + "'" + table1_2a[0].get() + "'" + ","

            r = r + "'" + values[0].get() + "'" + ","
            r = r + "'" + values[1].get() + "'" + ","

            r = r.rstrip(',')
            r = r + ")"
            print(r)

            cursor3.execute("""INSERT INTO `C.H. Form 2-A-3`(`Id`,`Plot No`,`Nature`,`Area`) VALUES {0} """.format(r))
            connection.commit()

            r = "("

        cursor3.close()

        # -------------------------- Resetting after deleting --------------------- #

        for w in middle.grid_slaves():
            if int(w.grid_info()['row']) > 1:
                w.grid_forget()

        form2a_create(db_name, top, middle, bottom)

    def show_status():
        cursor_new = connection.cursor()
        cursor_new.execute('SELECT * FROM `c.h. form 2-a-1`')
        from tkinter import messagebox
        messagebox.showinfo("Number of entries", "Number of entries = {}".format(cursor_new.rowcount))


    def form_fetch():
        khatauni_no_container = []
        khatauni_names_container = []
        total_plot_area = 0
        table1_2a_container = []
        table2_2a_container = []
        table3_2a_container = []

        cursor = connection.cursor()

        s = "'" + table1_2a[0].get() + "'"

        cursor.execute('SELECT `Khatauni no.`, `Plot Area` FROM `khatauni 3` WHERE `Khasra/Plot No.` ={0} '.format(s))

        row = cursor.fetchone()
        while row is not None:
            total_plot_area = round((total_plot_area + float(row[1])), 4)
            khatauni_no_container.append(row)
            row = cursor.fetchone()

        for number, values in enumerate(khatauni_no_container):
            r = "'" + values[0] + "'"    # storing the khatauni no in r

            cursor.execute("""SELECT `Name of holder`, `Name of father/husband/guardian`,`Address` 
                            FROM `khatauni 2` WHERE `Khatauni no.` ={0} """.format(r))
            row = cursor.fetchone()
            while row is not None:
                khatauni_names_container.append(row)
                row = cursor.fetchone()

            cursor = connection.cursor()

            cursor.execute("""SELECT * FROM `C.H. Form 2-A-1` WHERE `Plot No` ={0} """.format(s))

            row = cursor.fetchone()
            table1_2a_container.append(row)

            cursor.execute("""SELECT * FROM `C.H. Form 2-A-2` WHERE `Plot No` ={0} """.format(s))

            row = cursor.fetchone()
            while row is not None:
                table2_2a_container.append(row)
                row = cursor.fetchone()

            cursor.execute("""SELECT * FROM `C.H. Form 2-A-3` WHERE `Plot No` ={0} """.format(s))

            row = cursor.fetchone()
            while row is not None:
                table3_2a_container.append(row)
                row = cursor.fetchone()

        cursor = connection.cursor()

        cursor.execute("""SELECT * FROM `C.H. Form 2-A-1` WHERE `Plot No` ={0} """.format(s))

        row = cursor.fetchone()
        table1_2a_container.append(row)

        cursor.execute("""SELECT * FROM `C.H. Form 2-A-2` WHERE `Plot No` ={0} """.format(s))

        row = cursor.fetchone()
        while row is not None:
            table2_2a_container.append(row)
            row = cursor.fetchone()

        cursor.execute("""SELECT * FROM `C.H. Form 2-A-3` WHERE `Plot No` ={0} """.format(s))

        row = cursor.fetchone()
        while row is not None:
            table3_2a_container.append(row)
            row = cursor.fetchone()

        # ---------------------- Print in C.H form 2A --------------------------- #

        row_to_print = 2

        total_plot_area_label = ttk.Label(middle, text=str(total_plot_area))
        total_plot_area_label.grid(row=row_to_print, column=1, padx=5, pady=5, sticky='NW')

        for number, values in enumerate(khatauni_no_container):

            khatauni_no_label = ttk.Label(middle, text=values[1])
            khatauni_no_label.grid(row=row_to_print, column=4, padx=5, pady=5, sticky='NW')

            khatauni_area_label = ttk.Label(middle, text=values[1])
            khatauni_area_label.grid(row=row_to_print, column=5, padx=5, pady=5, sticky='NW')

            for index, entries in enumerate(khatauni_names_container):

                name_label = ttk.Label(middle, text=entries[0])
                name_label.grid(row=row_to_print, column=6, padx=5, pady=5, sticky='NW')

                guardian_label = ttk.Label(middle, text=entries[1])
                guardian_label.grid(row=row_to_print, column=7, padx=5, pady=5, sticky='NW')

                address_label = ttk.Label(middle, text=entries[2])
                address_label.grid(row=row_to_print, column=8, padx=5, pady=5, sticky='NW')

                row_to_print = row_to_print + 1

        for number, values in enumerate(table1_2a_container):
            e = table1_2a
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
            e[6].delete(0, "end")
            e[6].insert(number, values[6])
            e[7].delete(0, "end")
            e[7].insert(number, values[7])
            e[8].delete(0, "end")
            e[8].insert(number, values[8])
            e[9].delete(0, "end")
            e[9].insert(number, values[9])
            e[10].delete(0, "end")
            e[10].insert(number, values[10])
            e[11].delete(0, "end")
            e[11].insert(number, values[11])
            e[12].delete(0, "end")
            e[12].insert(number, values[12])
            e[13].delete(0, "end")
            e[13].insert(number, values[13])
            e[14].delete(0, "end")
            e[14].insert(number, values[14])
            e[15].delete(0, "end")
            e[15].insert(number, values[15])
            e[16].delete(0, "end")
            e[16].insert(number, values[16])
            e[17].delete(0, "end")
            e[17].insert(number, values[17])
            e[18].delete(0, "end")
            e[18].insert(number, values[18])
            e[19].delete(0, "end")
            e[19].insert(number, values[19])
            e[20].delete(0, "end")
            e[20].insert(number, values[20])

        row = 153
        for number, values in enumerate(table2_2a_container):
            col1 = 0
            if number == 0:
                e = table2_2a[number]
                e[0].delete(0, "end")
                e[0].insert(number, values[2])
                e[1].delete(0, "end")
                e[1].insert(number, values[3])
                e[2].delete(0, "end")
                e[2].insert(number, values[4])
                e[3].delete(0, "end")
                e[3].insert(number, values[5])
                e[4].delete(0, "end")
                e[4].insert(number, values[6])
                e[5].delete(0, "end")
                e[5].insert(number, values[7])
                e[6].delete(0, "end")
                e[6].insert(number, values[8])


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
                table2_2a.append((ent1, ent2, ent3, ent4, ent5, ent6, ent7))
                e = table2_2a[number]
                e[0].delete(0, "end")
                e[0].insert(number, values[2])
                e[1].delete(0, "end")
                e[1].insert(number, values[3])
                e[2].delete(0, "end")
                e[2].insert(number, values[4])
                e[3].delete(0, "end")
                e[3].insert(number, values[5])
                e[4].delete(0, "end")
                e[4].insert(number, values[6])
                e[5].delete(0, "end")
                e[5].insert(number, values[7])
                e[6].delete(0, "end")
                e[6].insert(number, values[8])
                row = row + 1

        row = 153
        for number, values in enumerate(table3_2a_container):
            col2 = 7
            if number == 0:
                e = table3_2a[number]
                e[0].delete(0, "end")
                e[0].insert(number, values[2])
                e[1].delete(0, "end")
                e[1].insert(number, values[3])

            else:
                ent1 = ttk.Entry(middle)
                ent1.grid(row=row, column=col2, padx=5, pady=5, sticky='NW')
                ent2 = ttk.Entry(middle)
                ent2.grid(row=row, column=col2 + 1, padx=5, pady=5, sticky='NW')
                table3_2a.append((ent1, ent2))
                e = table3_2a[number]
                e[0].delete(0, "end")
                e[0].insert(number, values[2])
                e[1].delete(0, "end")
                e[1].insert(number, values[3])
                row = row + 1

    def form_update():
        cursor = connection.cursor()
        entries1 = []
        entries2 = []
        entries3 = []
        id_names = []
        id_plots = []
        plot_number = []

        for number, values in enumerate(table1_2a):
            if number == 0:
                plot_number = "'" + values.get() + "'"
            if represents_int(values.get()):
                entries1.insert(number, values.get())
            else:
                entries1.insert(number, "'" + values.get() + "'")

        cursor.execute("""UPDATE `C.H. Form 2-A-1` SET `As found on spot`={0},`Details of uncultivated area (Nature)`={1},
                        `Details of uncultivated area (Included in holding)`={2},`Details of uncultivated area (not included in holding)`={3},
                        `Source`={4},`Method`={5},`Irrigable area`={6},`Kharif`={7},`Rabi`={8},`Zaid`={9},`Physical features of the plot`={10},
                        `Solid class in current settlement`={11},`Area (Non consolidable)`={12},`Area (Consolidable)`={13},`Exchange ratio in annas (in words)`={14},
                        `Valutaion of the consolidable area of the plot (col27 x col28)`={15},`Modified exchange ratio`={16},
                        `Valuation as modified by superior authorities (col27 X col30)`={17},`Khata no (As proposed by ACO )`={18},
                        `Khata no (As modified by CO)`={19} WHERE `Plot No`={20} """.format(entries1[1], entries1[2], entries1[3], entries1[4],
                                                                                           entries1[5], entries1[6], entries1[7], entries1[8],
                                                                                           entries1[9], entries1[10], entries1[11], entries1[12],
                                                                                           entries1[13], entries1[14], entries1[15], entries1[16],
                                                                                           entries1[17], entries1[18], entries1[19], entries1[20], entries1[0]))

        connection.commit()
        cursor.close()

        cursor2 = connection.cursor()

        # ---------------------- Updating and inserting in C.H. Form 2-A-2 ------------------------- #

        cursor2.execute("""SELECT Id FROM `C.H. Form 2-A-2` WHERE `Plot No` ={0} """.format(plot_number))

        row = cursor2.fetchone()
        while row is not None:
            id_names.append(row[0])
            row = cursor2.fetchone()
        p = "("

        for number, values in enumerate(table2_2a):
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

                if represents_int(values[3].get()):
                    entries2.insert(3, values[3].get())
                else:
                    entries2.insert(3, "'" + values[3].get() + "'")

                entries2.insert(4, "'" + values[4].get() + "'")

                entries2.insert(5, "'" + values[5].get() + "'")

                if represents_int(values[6].get()):
                    entries2.insert(6, values[6].get())
                else:
                    entries2.insert(6, "'" + values[6].get() + "'")

                print("r is ", plot_number)
                print("name id ", nameid)
                print(entries2)

                cursor2.execute("""UPDATE `C.H. Form 2-A-2` SET `Description`={0},`Measurement`={1},`Age`={2},`Estimated Value`={3},`Name of owner`={4},
                                  `Address`={5},`Share`={6} WHERE `Plot No`={7} AND `Id`={8} """.format(entries2[0], entries2[1], entries2[2], entries2[3], entries2[4],
                                                                                                          entries2[5], entries2[6], plot_number, nameid))
                connection.commit()

            except IndexError:
                if len(id_names) == 0:
                    new_id_names = str(1)
                else:
                    j = len(id_names) - 1
                    new_id_names = str(int(id_names[j]) + 1)
                id_names.append(new_id_names)
                p = p + new_id_names + ","
                p = p + table1_2a[0].get() + ","
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

                if represents_int(values[3].get()):
                    p = p + values[3].get() + ","
                else:
                    p = p + "'" + values[3].get() + "'" + ","

                p = p + "'" + values[4].get() + "'" + ","

                p = p + "'" + values[5].get() + "'" + ","

                if represents_int(values[6].get()):
                    p = p + values[6].get() + ","
                else:
                    p = p + "'" + values[6].get() + "'" + ","

                p = p.rstrip(',')
                p = p + ")"

                cursor2.execute("""INSERT INTO `C.H. Form 2-A-2`(`Id`,`Plot No`,`Description`,`Measurement`,`Age`,`Estimated Value`,
                                  `Name of owner`,`Address`,`Share`) VALUES {0} """.format(p))
                connection.commit()

                p = "("

        # ---------------------- Updating and inserting in C.H. Form 2-A-3 ------------------------- #

        cursor2.execute("""SELECT `Id` FROM `C.H. Form 2-A-3` WHERE `Plot No` ={0} """.format(plot_number))

        row = cursor2.fetchone()
        while row is not None:
            id_plots.append(row[0])
            row = cursor2.fetchone()

        q = "("

        for number, values in enumerate(table3_2a):
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

                cursor2.execute("""UPDATE `C.H. Form 2-A-3` SET `Nature`={0},`Area`={1}
                                                            WHERE `Plot No`={2} AND `Id`={3} """.format(entries3[0], entries3[1], plot_number, plotid))

                connection.commit()

            except IndexError:
                if len(id_plots) == 0:
                    new_id_plots = str(1)
                else:
                    i = len(id_plots) - 1
                    new_id_plots = str(int(id_plots[i]) + 1)
                id_plots.append(new_id_plots)
                q = q + new_id_plots + ","
                q = q + table1_2a[0].get() + ","
                if represents_int(values[0].get()):
                    q = q + values[0].get() + ","
                else:
                    q = q + "'" + values[0].get() + "'" + ","

                if represents_int(values[1].get()):
                    q = q + values[1].get() + ","
                else:
                    q = q + "'" + values[1].get() + "'" + ","

                q = q.rstrip(',')
                q = q + ")"
                cursor2.execute("""INSERT INTO `C.H. Form 2-A-3`(`Id`,`Plot No`,`Nature`,`Area`) VALUES {0} """.format(q))
                connection.commit()

                q = "("

        cursor2.close()

        # -------------------------- Resetting after deleting --------------------- #

        for w in middle.grid_slaves():
            if int(w.grid_info()['row']) > 1:
                w.grid_forget()

        form2a_create(db_name, top, middle, bottom)

    def form_delete():
        cursor = connection.cursor()

        if represents_int(table1_2a[0].get()):
            plotno = table1_2a[0].get()
        else:
            plotno = "'" + table1_2a[0].get() + "'"

        cursor.execute("""DELETE FROM `C.H. Form 2-A-1` WHERE `Plot No`={0}""".format(plotno))
        cursor.execute("""DELETE FROM `C.H. Form 2-A-2` WHERE `Plot No`={0}""".format(plotno))
        cursor.execute("""DELETE FROM `C.H. Form 2-A-3` WHERE `Plot No`={0}""".format(plotno))

        connection.commit()
        cursor.close()

        # -------------------------- Resetting after deleting --------------------- #

        for w in middle.grid_slaves():
            if int(w.grid_info()['row']) > 1:
                w.grid_forget()

        form2a_create(db_name, top, middle, bottom)

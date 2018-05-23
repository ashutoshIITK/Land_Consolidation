import pymysql as psql
import xlsxwriter


def chform_5_print(db_name, top, middle, bottom):
    khatauni_1_entries = []
    khatauni_2_entries = []
    khatauni_3_entries = []
    total_plot_area = 0
    ch_form_2a_1_entries = []
    ch_form_2a_2_entries = []
    ch_form_4b_1_entries = []
    ch_form_4b_2_entries = []

    connection = psql.connect(host='localhost', user='root', password='', db=db_name, charset='utf8mb4',
                                  cursorclass=psql.cursors.Cursor)

    #creates the workbook
    workbook = xlsxwriter.Workbook('ch_form_5(extract).xlsx')
    worksheet = workbook.add_worksheet("My sheet")

    #formatting definitions
    bold = workbook.add_format({'bold': True})


    #sets up the header row
    worksheet.write('A1', 'no. of Khata of the current Annual register',bold)
    worksheet.write('B1', 'name of tenure-holder', bold)
    worksheet.write('C1', 'Percentage Share', bold)
    worksheet.write('D1', 'Residence', bold)
    worksheet.write('E1', 'class of tenure', bold)
    worksheet.write('F1', 'Year of commencement', bold)
    worksheet.write('G1', 'Plot no.', bold)
    worksheet.write('H1', 'Total area', bold)
    worksheet.write('I1', 'Area non consolidable', bold)
    worksheet.write('J1', 'area consolidable', bold)
    worksheet.write('K1', 'exchange ratio', bold)
    worksheet.write('L1', 'valuation of annas', bold)
    worksheet.write('M1', 'exchange ratio', bold)
    worksheet.autofilter('A1:K1')


    cursor = connection.cursor()

    cursor.execute("""SELECT * FROM `khatauni 1`""")

    row = cursor.fetchone()

    while row is not None:
        khatauni_1_entries.append(row)
        row = cursor.fetchone()

    row_to_write1 = 2
    row_to_write2 = 2
    row_to_write3 = 2

    for number, values in enumerate(khatauni_1_entries):
        r = "'" + values[0] + "'"  # storing the khatauni no in r

        worksheet.write(row_to_write1, 0, values[0])

        cursor.execute("""SELECT `Name of holder`,`Address` FROM `khatauni 2` WHERE `Khatauni no.` ={0} """.format(r))
        row = cursor.fetchone()
        while row is not None:
            worksheet.write(row_to_write1, 1, row[0])
            worksheet.write(row_to_write1, 3, row[1])
            row_to_write1 = row_to_write1 + 1
            row = cursor.fetchone()

        cursor.execute("""SELECT `Khasra/Plot No.`, `Plot Area` FROM `khatauni 3` WHERE `Khatauni no.` ={0} """.format(r))
        row = cursor.fetchone()
        while row is not None:
            worksheet.write(row_to_write2, 6, row[0])
            worksheet.write(row_to_write2, 7, row[1])
            plot_no = "'" + row[0] + "'"
            cursor2 = connection.cursor()
            cursor2.execute("""SELECT `Area (Non consolidable)`, `Area (Consolidable)` FROM `C.H. Form 2-A-1` 
                              WHERE `Plot No` ={0} """.format(plot_no))
            row2 = cursor2.fetchone()
            if row2 is not None:
                worksheet.write(row_to_write2, 8, row2[0])
                worksheet.write(row_to_write2, 9, row2[1])

            cursor2.execute("""SELECT `Description`, `Measurement`,`Age` FROM `C.H. Form 2-A-2` 
                                          WHERE `Plot No` ={0} """.format(plot_no))
            row2 = cursor2.fetchone()
            while row2 is not None:
                worksheet.write(row_to_write3, 10, row2[0])
                worksheet.write(row_to_write3, 11, row2[1])
                worksheet.write(row_to_write3, 12, row2[0])
                row_to_write3 = row_to_write3 + 1
                row2 = cursor2.fetchone()

            row_to_write2 = row_to_write2 + 1
            row = cursor.fetchone()

        Max = row_to_write1
        if row_to_write2 > Max :
            Max = row_to_write2

        if row_to_write3 > Max:
            Max = row_to_write3

        row_to_write1 = Max
        row_to_write2 = Max
        row_to_write3 = Max

    #close out everything and save
    print("Printed!")
    cursor.close()
    workbook.close()
    connection.close()
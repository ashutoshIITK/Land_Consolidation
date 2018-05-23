
import xlsxwriter
import pymysql as psql


def ch_2a_print(db_name,form_name):
    # Placeholders


    connection = psql.connect(host='localhost', user='root', password='', db=db_name, charset='utf8mb4',
                              cursorclass=psql.cursors.Cursor)
    workbook = xlsxwriter.Workbook('CH_Form_2A.xlsx')
    worksheet = workbook.add_worksheet("CH_Form_2A")
    bold = workbook.add_format({'bold': True})
    worksheet.write('A1', 'Plot No.', bold)
    worksheet.write('B1', 'As found on spot', bold)
    worksheet.write('C1', 'Details of uncultivated area (Nature)', bold)
    worksheet.write('D1', 'Details of uncultivated area (Included in holding)', bold)
    worksheet.write('E1','Details of uncultivated area (not included in holding)',bold)
    worksheet.write('F1', 'Source', bold)
    worksheet.write('G1', 'Method', bold)
    worksheet.write('H1', 'Irrigable area', bold)
    worksheet.write('I1', 'Kharif', bold)
    worksheet.write('J1', 'Rabi', bold)
    worksheet.write('K1', 'Zaid', bold)
    worksheet.write('L1', 'Physical features of the plot', bold)
    worksheet.write('M1', 'Solid class in current settlement', bold)
    worksheet.write('N1', 'Area (Non consolidable)', bold)
    worksheet.write('O1', 'Area (Consolidable)', bold)
    worksheet.write('P1', 'Exchange ratio in annas (in words)', bold)
    worksheet.write('Q1', 'Valutaion of the consolidable area of the plot (col27 x col28)', bold)
    worksheet.write('R1', 'Modified exchange ratio', bold)
    worksheet.write('S1', 'Valuation as modified by superior authorities (col27 X col30)', bold)
    worksheet.write('T1', 'Khata no (As proposed by ACO )', bold)
    worksheet.write('U1', 'Khata no (As modified by CO)', bold)
    worksheet.write('V1', 'Id', bold)
    worksheet.write('W1', 'Plot No', bold)
    worksheet.write('X1', 'Description', bold)
    worksheet.write('Y1', 'Measurement', bold)
    worksheet.write('Z1', 'Age', bold)
    worksheet.write('AA1', 'Estimated Value', bold)
    worksheet.write('AB1', 'Name of owner', bold)
    worksheet.write('AC1', 'Address', bold)
    worksheet.write('AD1', 'Share', bold)
    worksheet.write('AE1', 'Nature', bold)
    worksheet.write('AF1', 'Area', bold)

    cursor1 = connection.cursor()
    cursor2 = connection.cursor()
    cursor3 = connection.cursor()
    cursor1.execute("""SELECT * FROM `c.h. form 2-a-1`""")
    cursor2.execute("""SELECT * FROM `c.h. form 2-a-2`""")
    cursor3.execute("""SELECT `Nature`, `Area` FROM `c.h. form 2-a-3`""")

    print(form_name)
    row_no= 1
    col_no =0

    for row in cursor1.fetchall():
        for i in range(0,21):
            worksheet.write(row_no,col_no,row[i])
            col_no = col_no + 1


        row_no = row_no + 1
        col_no_previous= col_no
        col_back = col_no
        col_no = 0

    row_no =1
    for row1 in cursor2.fetchall():
        for i in range(0, 9):
           worksheet.write(row_no, col_no_previous, row1[i])
           col_no_previous= col_no_previous + 1

        row_no = row_no + 1
        col = col_no_previous
        col_no_previous= col_back

    col_no_previous1 = col
    col_back1 = col

    row_no = 1
    for row2 in cursor3.fetchall():
        for i in range(0, 2):
            print(row2[i])
            print(col_no_previous1)
            print(row_no)
            print('\n')
            worksheet.write(row_no, col_no_previous1, row2[i])
            col_no_previous1 = col_no_previous1 + 1

        row_no = row_no + 1
        col_no_previous1 = col_back1



    print("Printed!")
    cursor1.close()
    cursor2.close()
    cursor3.close()



    workbook.close()

    connection.close()
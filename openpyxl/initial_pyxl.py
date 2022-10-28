from openpyxl import load_workbook, workbook

wb = load_workbook('./exel_file/demo_1.xlsx')

ws = wb.active
#print(ws["A2"].value)

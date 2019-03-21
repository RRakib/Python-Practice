#### Importing OpenpyXL as XL
# import openpyxl as xl
# -----------------------------------------------------------
# # Creating workbook
# wb = xl.load_workbook("transactions.xlsx")
# -----------------------------------------------------------
# # Defining Sheet
# sheet = wb["Sheet1"]
# -----------------------------------------------------------
# # Looping through rows and calculating 90% discount and creating new cell with correct value
# for row in range(2 , sheet.max_row + 1):
#     cell_value = sheet.cell(row , 3)
#     cell_value_new = sheet.cell(row, 4)
#     cell_correct_value = cell_value.value * 0.9
#     cell_value_new.value = cell_correct_value
# -----------------------------------------------------------
# # Creating New File and Saving
# wb.save("transactions2.xlsx")
# -----------------------------------------------------------
import xlrd
file_loc="C:/Users/ruhi.shrivastava/Desktop/read.xlsx"
wb=xlrd.open_workbook(file_loc)
ws=wb.sheet_by_index(0)
val=ws.cell_value(0,0)
print(val)
print("total rows",ws.nrows)
print("total cols",ws.ncols)

import xlwt
import xlrd
import docx

Train_Calc_Book=xlwt.Workbook(encoding='utf-8', style_compression=0)

sheet1=Train_Calc_Book.add_sheet('sheet1',cell_overwrite_ok=True)
sheet2=Train_Calc_Book.add_sheet('sheet2',cell_overwrite_ok=True)


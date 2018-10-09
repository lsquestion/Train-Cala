#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import xlwt
import xlrd
from main import *


Train_Calc_Book=xlwt.Workbook(encoding='utf-8', style_compression=0)

sheet1=Train_Calc_Book.add_sheet('综合特性',cell_overwrite_ok=True)
sheet2=Train_Calc_Book.add_sheet('对速度特性',cell_overwrite_ok=True)
sheet3=Train_Calc_Book.add_sheet('对时间特性',cell_overwrite_ok=True)



for i in range(len(Trac_Chara_speed_List)):
	for j in range(len(Trac_Chara_speed_List[0])):
		sheet2.write(i,j,label=Trac_Chara_speed_List[i][j])

for i in range(len(Trac_Chara_time_list)):
	for j in range(len(Trac_Chara_time_list[0])):
		sheet3.write(i,j,label=Trac_Chara_time_list[i][j])
	
Train_Calc_Book.save('牵引特性.xls')
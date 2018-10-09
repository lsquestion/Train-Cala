#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from parameter import *
from calc_func import *
import numpy as np
import matplotlib.pyplot as plt	
#import xlwt
#import xlrd



Mass_T_Weight=T_Car_Weight*T_Car_Num #拖车车重
Mass_M_Weight=M_Car_Weight*M_Car_Num #动车车重

Mass_Rota=round(Mass_T_Weight*0.05+Mass_M_Weight*0.1,2)

Mass_Weight_AW0=Mass_T_Weight+Mass_M_Weight #列车AW0质量

Mass_Weight_AW1=Mass_Weight_AW0+(T_Car_Pa_AW1*T_Car_Num+M_Car_Pa_AW1*M_Car_Num)*Pa_Weight #列车AW1质量
Mass_Weight_AW2=Mass_Weight_AW0+(T_Car_Pa_AW2*T_Car_Num+M_Car_Pa_AW2*M_Car_Num)*Pa_Weight #列车AW2质量
Mass_Weight_AW3=Mass_Weight_AW0+(T_Car_Pa_AW3*T_Car_Num+M_Car_Pa_AW3*M_Car_Num)*Pa_Weight #列车AW3质量


Trac_Chara_point=Trac_Point_voltage([Cons_Power_Point,Nature_Point,Trac_Voltage])#计算特性点

Speed_list=List_comb(list(np.arange(0,Speed_Max+Speed_Step,Speed_Step)),Trac_Chara_point)

Trac_Chara_speed_List=Trac_Chara_speed(Speed_list,Mass_Weight_AW2,Mass_Rota,T_Car_Num,T_Car_Axle_num,M_Car_Num,M_Car_Axle_num)


Trac_Chara_time_list=Trac_Chara_time(Time_Step,80,Mass_Weight_AW2,Mass_Rota,T_Car_Num,T_Car_Axle_num,M_Car_Num,M_Car_Axle_num)



#Time_list=list(np.arange(0,50+Time_step,Time_step))



'''
speed=0
a=0
Time=0
while speed<=(40/3.6):
	speed+=a*Time_Step
	Time+=Time_Step
	Trac_Force=Trac_Chara(370,speed*3.6,36,60)
	Res_Force=Resistance_Calc(speed*3.6,Mass_Weight_AW2,T_Car_Num,T_Car_Axle_num,M_Car_Num,M_Car_Axle_num)
	a=Acce_Calc(Trac_Force,Res_Force,Mass_Weight_AW2,Mass_Rota)

Ave_acc=speed/(Time+0.2)
#
(speed*3.6,Time,Ave_acc)	
'''
'''
Trac_Chara_speed_List=[]

for i in Speed_list:#需要一个统一的函数，以速度为统一标准进行计算，统一到一个维度里
	Trac_Force=Trac_Chara(370,i,36,60)
	Res_Force=Resistance_Calc(i,Mass_Weight_AW2,T_Car_Num,T_Car_Axle_num,M_Car_Num,M_Car_Axle_num)
	acc=Acce_Calc(Trac_Force,Res_Force,Mass_Weight_AW2,Mass_Rota)


	Trac_Chara_speed_List.append([i,Trac_Force,Res_Force,acc])
	

#print(Trac_Chara_List)

'''


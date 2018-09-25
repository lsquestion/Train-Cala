#!/usr/bin/env python3

from parameter import *
from calc_func import *
import numpy as np

Mass_T_Weight=T_Car_Weight*T_Car_Num #拖车车重
Mass_M_Weight=M_Car_Weight*M_Car_Num #动车车重

Mass_Rota=round(Mass_T_Weight*0.05+Mass_M_Weight*0.1,2)

Mass_Weight_AW0=Mass_T_Weight+Mass_M_Weight #列车AW0质量

Mass_Weight_AW1=Mass_Weight_AW0+(T_Car_Pa_AW1*T_Car_Num+M_Car_Pa_AW1*M_Car_Num)*Pa_Weight #列车AW1质量
Mass_Weight_AW2=Mass_Weight_AW0+(T_Car_Pa_AW2*T_Car_Num+M_Car_Pa_AW2*M_Car_Num)*Pa_Weight #列车AW2质量
Mass_Weight_AW3=Mass_Weight_AW0+(T_Car_Pa_AW3*T_Car_Num+M_Car_Pa_AW3*M_Car_Num)*Pa_Weight #列车AW3质量

Speed_list=list(np.arange(0,Speed_Max+Speed_Step,Speed_Step))

Trac_chara_list=[]

for i in Speed_list:
	Trac_chara_list.append(Trac_Chara(350,i,36,60))



print(Trac_chara_list)




from parameter import *

Mass_T_Weight=T_Car_Weight*T_Car_Num #拖车车重
Mass_M_Weight=M_Car_Weight*M_Car_Num #动车车重

Mass_Rota=round(Mass_T_Weight*0.05+Mass_M_Weight*0.1,2)

Mass_Weight_AW0=Mass_T_Weight+Mass_M_Weight #列车AW0质量

Mass_Weight_AW1=Mass_Weight_AW0+(T_Car_Pa_AW1*T_Car_Num+M_Car_Pa_AW1*M_Car_Num)*Pa_Weight #列车AW1质量
Mass_Weight_AW2=Mass_Weight_AW0+(T_Car_Pa_AW2*T_Car_Num+M_Car_Pa_AW2*M_Car_Num)*Pa_Weight #列车AW2质量
Mass_Weight_AW3=Mass_Weight_AW0+(T_Car_Pa_AW3*T_Car_Num+M_Car_Pa_AW3*M_Car_Num)*Pa_Weight #列车AW3质量



def Trac_Cha(Trac_kN,speed,Cons_Power_Point,Nature_Point):
	Trac_Cons_power=
	if speed<=Cons_Power_Point:
		Trc_kN=Trc_kN
	elif speed>Cons_Power_Point and speed<Nature_Point:
		Trc_kN=Trc_kN*Cons_Power_Point/speed
	else:
		Trc_kN=Trc_kN*Nature_Point*Nature_Point/speed/speed
		
		




print(Mass_Weight_AW0,Mass_Weight_AW1,Mass_Weight_AW2,Mass_Weight_AW3,Mass_Rota)




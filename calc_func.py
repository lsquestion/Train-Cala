#!/usr/bin/env python3


def Trac_Chara(Trac_kN,speed,Cons_Power_Point,Nature_Point):#牵引特性曲线函数
	Trac_Cons_power=Trac_kN*Cons_Power_Point
	Trac_Nature_power=Trac_Cons_power*Nature_Point
	if speed<=Cons_Power_Point:
		Trac_kN=Trac_kN
	elif speed>Cons_Power_Point and speed<Nature_Point:
		Trac_kN=Trac_kN*Cons_Power_Point/speed
	else:
		Trac_kN=Trac_Cons_power*Nature_Point/speed/speed
	Trac_kN=round(Trac_kN,2)
	return [speed,Trac_kN]
		
def Trac_Point_voltage(Cons_Power_Point,Nature_Point,Trac_Voltage=1500,voltage=1000):
	Cons_Power_Point=voltage/Trac_Voltage*Cons_Power_Point
	Nature_Point=voltage/Trac_Voltage*Nature_Point

	return Cons_Power_Point,Nature_Point




		
trac=Trac_Chara(350,51,36,60)

point1,point2=Trac_Point_voltage(30,60)

print(point1,point2)
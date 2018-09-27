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
	return Trac_kN
		
def Resistance_Calc(speed,Train_Weight,T_car_num,T_car_Axle,M_car_num,M_car_Axle,Slope=0):#计算阻力
	C=0.129*(T_car_num*T_car_Axle+M_car_num*M_car_Axle)
	C0=0.6378*0.1/9.81
	C1=0.0091*0.1/9.81
	C2=(38.083+6.285*(T_car_num+M_car_num))*0.000001*11.2
	Res_Force=Train_Weight*(C0+C1*speed)+(C2*speed*speed)+(9.81*Slope*Train_Weight)/1000+C

	return Res_Force


def Slope_Res():#计算坡道阻力
	pass

def Acce_Calc(Trac_Force,Res_Force,Train_Weight,Mass_Rota):#计算加速度
	a=(Trac_Force-Res_Force)/(Train_Weight+Mass_Rota)
	return a

def Ave_Acce():#计算平均加速度
	pass

def Adhesion_Calc():#计算黏着力
	pass

def Rescue_mode():
	pass


def Trac_Point_voltage(L=[],Trac_Voltage=1500,voltage=1000):#根据电压计算牵引特性点
	Cons_Power_Point=voltage/Trac_Voltage*L[0]
	Nature_Point=voltage/Trac_Voltage*L[1]
	Trac_Chara_point=[Cons_Power_Point,Nature_Point]
	return Trac_Chara_point


def List_comb(L1=None,L2=None):#把特性点组合速度列表中
	L_comb=L1+L2
	L_comb.sort()
	return L_comb


		
trac=Trac_Chara(350,51,36,60)

point1,point2=Trac_Point_voltage([30,60])

#print(point1,point2)
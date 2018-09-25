def Trac_Chara(Trac_kN,speed,Cons_Power_Point,Nature_Point):#牵引特性曲线函数
	Trac_Cons_power=Trac_kN*Cons_Power_Point
	Trac_Nature_power=Trac_Cons_power*Nature_Point
	if speed<=Cons_Power_Point:
		Trac_kN=Trac_kN
	elif speed>Cons_Power_Point and speed<Nature_Point:
		Trac_kN=Trac_kN*Cons_Power_Point/speed
	else:
		Trac_kN=Trac_Cons_power*Nature_Point/speed/speed
	return Trac_kN
		
		
		
		
trac=Trac_Chara(350,50,36,60)

print(trac)
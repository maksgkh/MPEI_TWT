import numpy as np
import matplotlib.pyplot as plt
import CoolProp.CoolProp as ct
q=700 #Расход Тонн/ч
d=300 #Диаметр турбопровода мм
L=500 #Метров
Delta=2 #Шероховатость мм/м
p_in=3*101325 #Давление АТМ
T=80+273.15 #Температура в К
D=ct.PropsSI("D","T",T,"P",p_in,"water") #Плотность
Q=q/D #
F=np.pi*(d/2)**2
V=Q/F
M=ct.PropsSI("Viscosity","P",p_in,"T",T,'Water')
Re=(d*V)/(M/D)
if Re<2300:
    l=64/Re
elif Re<4000:
    l=0
elif Re<10/Delta and Re==10/Delta:
    l=0.3164/Re**0.25
elif Re<560/Delta and Re==560/Delta:
    l=0.11*(Delta+(68/Re))
else:
    l=0.11*Delta**0.25

# Какую массу имеет метан при обьеме 64 м3 при атмосферном давлении и T = 0°C
import numpy as np
import CoolProp.CoolProp as ct
import matplotlib.pyplot as plt

#Дано
t=273.15 #температура в К
p=101325 #давление
v=64     #объём
R=8.3145 #универсальная газовая постоянная
M=0.016  #молярная масса CH4

#Решение 1
m1=(p*v*M)/(R*t)
print(f'{m1}кг')

#Решение 2
d1=ct.PropsSI("D","T",t,"P",p,"CH4")
m2=v*d1

#График
tt=np.linspace(117.15, 107.15,1000)
m_1=(p*v*M)/(R*tt)
d2=ct.PropsSI("D","T",tt,"P",p,"CH4")
m_2=v*d2
plt.plot(tt,m_1,'r')
plt.plot(tt,m_2,'b')
plt.xlabel('T')
plt.ylabel('m')
plt.title('Зависимость m от T')
plt.scatter(111.65,ct.PropsSI("D","T",111.65,"P",p,"CH4"),color="blue")
plt.grid()
plt.show()

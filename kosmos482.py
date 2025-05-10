import math 

rho_base = 1.225 #6.81 * 10**-8
h = 25 #height in km
H = 8.5 #scale height

rho = rho_base * math.exp(-h / H)

v = 7800
CD= 2.2
A = 1.5
kg = 495
#e = math.exp(- 80 / 8.5)



Fdrag = 0.5 * rho * v**2 * CD * A

a = Fdrag / kg

print(round(a, 8))  # rounds to 8 decimal places

#!/usr/bin/env python
# coding: utf-8

# In[6]:


name=input("Escriba su nombre : ")
salBrut= float(input("Salario Bruto: "))
comisiones=float(input("Comisiones: "))
otros=float(input("Otros ingresos ocasionales: "))
noGrav= float(input("Reembolso de gastos no salariales ni gravables: "))
porc_asocSol=float(input("Porcentaje Asociación solidarista: "))
planComp=float(input("Plan de Pensiones Complementarias: "))
print("Usuario: ", name)
ingresos=salBrut+comisiones+otros
print("Total Ingresos Laborales: ", ingresos+noGrav)
enf_mat=ingresos*0.055
print("Enfermedad y Maternidad 5.5%: ", enf_mat)
ivm=ingresos*0.0384
print("Invalidez y Muerte 3.84%: ", ivm)
bPop=ingresos*0.01
print("Aporte Trabajador Banco Popular 1%: ", bPop)
asocSol=ingresos*(porc_asocSol/100) 
print("Asociación Solidarista: ", asocSol)
salGrav=ingresos-planComp

#Renta
if(salGrav<=863000):
    renta=0
elif(salGrav<=1267000):
    renta=(salGrav-863001)*0.10
elif(salGrav<=2223000):
    renta=(1267000-863001)*0.10+(salGrav-1267001)*0.15 
elif(salGrav<=4445000):
    renta=(1267000-863001)*0.10+(2223000-1267001)*0.15+(salGrav-2223001)*0.20
elif(salGrav>=4445001):
    renta=(1267000-863001)*0.10+(2223000-1267001)*0.15+(4445001-2223001)*0.20+(salGrav-4445001)*0.25
    
print("Salario Gravable", salGrav)
print("Impuesto sobre la Renta empleados: ", renta)
totDed=enf_mat+ivm+bPop+asocSol+renta
print("Total deducciones: ", totDed)
neto=ingresos+noGrav-totDed
print("Ingresos netos: ", neto)


# In[ ]:





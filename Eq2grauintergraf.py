# Sophia Pinto
# Aprimoramento de código: Interfaces gráficas

# Importações de bibliotecas

import numpy as np
import tkinter as tk 
from tkinter import *
import matplotlib
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

matplotlib.use('TkAgg')


# Definição de função
def calcular():
  a= int (textbox1.get())
  b= int (textbox2.get())
  c= int (textbox3.get())
  delta = (b**2 - 4*a*c)
  
  if a==0:
    labelfinal ["text"] = "Se a=0, não é equação do segundo grau."

  if delta < 0:
    labelfinal ["text"] = "Delta é menor que 0, não possui nenhuma raiz real."
            
  elif  delta==0:
    x1 = (-b + delta**(1/2)) / (2*a)
    labelfinal ["text"] = "Delta é igual a 0 , raíz 1 = ", x1
            
  else:
    x1 = (-b + delta**(1/2)) / (2*a)
    x2 = (-b - delta**(1/2)) / (2*a)
    labelfinal ["text"] = "As raízes da equação são:  ", x1 , "e" , x2


def grafico (): 
    
    a= int (textbox1.get())
    b= int (textbox2.get())
    c= int (textbox3.get())
    delta = (b**2 - 4*a*c)
    x1 = (-b + delta**(1/2)) / (2*a)
    x2 = (-b - delta**(1/2)) / (2*a)
    
    eixox = []
    eixoy = []
    zero = []

    variacao = abs(x1 - x2)
    
    if variacao < 3:
        variacao = 3
    print(variacao)

    for x in np.arange(x1 - variacao, x2 + variacao, variacao / 100):
        y= a*(x**2) + b*x + c
        eixox.append(x)
        eixoy.append(y)
        zero.append(0.0)
        
    plt.plot(eixox,eixoy,color="blue")
    plt.plot(eixox,zero,color="black")
    plt.show()
    
    
    
    
# GUI
root = tk.Tk() 


# Widgets
label1 = Label (root, text = "Escreva o coeficiente a:  ")
label2 = Label (root, text = "Escreva o coeficiente b:  ")
label3 = Label (root, text = "Escreva o coeficiente c:  ")
labelfinal = Label (root, text= "Resultado:" )

textbox1 = Entry (root)  
textbox2 = Entry (root)
textbox3 = Entry (root)

button1= Button (root, text= "Calcular", command= calcular)
button2= Button (root, text= "Ver gráfico", command= grafico)


#Layout
label1.grid (row=0,column=0)
label2.grid (row=1,column=0)
label3.grid (row=2,column=0)
labelfinal.grid (row=3,column=0)
  
textbox1.grid (row=0,column=1)
textbox2.grid (row=1,column=1)
textbox3.grid (row=2,column=1)

button1.grid (row=5,column=1)
button2.grid (row=6,column=1)

root.mainloop() # Usado para a exibição da tela.

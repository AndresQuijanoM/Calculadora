import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import messagebox

def init_window():
    Lista_de_op=[]
    window=tk.Tk()
    window.title('Mi aplicacion')
    window.geometry('400x250')
    window.config(bg='SteelBlue1')

    label=tk.Label(window,text='Calculadora',font=('Arial bold',18),bg='SteelBlue1',fg='white')
    label.grid(column=0,row=0)

    entrada1=tk.Entry(window,width=10)
    entrada2=tk.Entry(window,width=10)

    entrada1.grid(column=1,row=1)
    entrada2.grid(column=1,row=2)

    label_entrada1=tk.Label(window,text='Ingrese primer numero',font=('Arial bold',12),bg='SteelBlue1',fg='white')
    label_entrada1.grid(column=0,row=1)

    label_entrada2=tk.Label(window,text='Ingrese el segundo numero',font=('Arial bold',12),bg='SteelBlue1',fg='white')
    label_entrada2.grid(column=0,row=2)

    label_operador=tk.Label(window,text='Escoja un operador',font=('Arial bold',12),bg='SteelBlue1',fg='white')
    label_operador.grid(column=0,row=3)

    combo_operadores=ttk.Combobox(window)
    #valores del seleccionador
    combo_operadores['values']=['+','-','x','/','pow']
    #opcion por defecto
    combo_operadores.current(0)
    combo_operadores.grid(column=1,row=3)

    label_resultado=tk.Label(window,text='Resultado:',font=('Arial bold',15),bg='SteelBlue1',fg='white')
    label_resultado.grid(column=0,row=5)
    
    #witget barra progresiva
    style=ttk.Style()
    style.theme_use('default')
    style.configure('steelBlue2.Horizontal.TProgressbar',background='steelBlue2')
    bar=Progressbar(window,length=200,style='steelBlue2.Horizontal.TProgressbar')
    bar['value']=0
    bar.grid(column=1,row=6)

    #witget checkbutton
    chk_state= tk.BooleanVar()
    chk_state.set(False)
    boton_c= tk.Checkbutton(window, text='Guardar operación', var=chk_state,bg='SteelBlue1')
    boton_c.grid(column=0,row=4)
    
    def calculadora(num1,num2,operador):
        if operador=='+':
             resultado=num1+num2
        elif operador=='-':
            resultado=num1-num2
        elif operador=='x':
            resultado=num1*num2
        elif operador=='/':
            resultado=round(num1/num2,2)
        else:
            resultado=num1**num2
        return resultado
    def click_calcular(label,num1,num2,operador,state,Lista_de_op):
        if num1=='' and num2=='':
            messagebox.showerror('ERROR','Faltan los datos para hacer la operación')  #widget mensaje de error
        elif num1=='' or num2=='':
            messagebox.showerror('ERROR','Falta un dato para hacer la operación')  #widget mensaje de error
        elif operador=='/' and num2=='0':
            messagebox.showerror('ERROR','No puedes dividir por 0')  #widget mensaje de error
        else:
            valor1=float(num1)
            valor2=float(num2)
            res=calculadora(valor1,valor2,operador)
            bar['value']=200
            label.configure(text='Resultado: '+str(res))
            if state==True:
                if operador=='pow':
                    operador='^'
                cadena=str(num1)+(operador)+str(num2)+'='+str(res)
                Lista_de_op.append(cadena)

    def historial(lista_de_op):
        window_2=tk.Tk()
        window_2.title('Historial')
        window_2.geometry('400x250')
        window_2.config(bg='lightgreen')
        for i in range(len(lista_de_op)):
            label=tk.Label(window_2,text=lista_de_op[i],font=('Arial bold',14),bg='lightgreen',fg='black')
            label.grid(column=0,row=i)

    #boton calcular
    boton=tk.Button(window,
                    command=lambda: click_calcular(
                        label_resultado,
                        entrada1.get(),
                        entrada2.get(),
                        combo_operadores.get(),
                        chk_state.get(),Lista_de_op),
                    text='Calcular',
                    bg="steelBlue2",
                    fg="white")
    boton.grid(column=1,row=4)

    #boton Mostrar historial
    boton_2=tk.Button(window,text='Mostrar historial',bg='steelBlue2',fg='white',command=lambda: historial(Lista_de_op))
    boton_2.grid(column=0,row=6)


    window.mainloop()
def main():
    init_window()
    
    
main()

import tkinter as tk

ventana = tk.Tk()
ventana.title('mi prueba')
ventana.geometry('300x200')  # Define tamaño de la ventana

tk.Label(ventana, text='hola mundo', font=('Arial', 16)).pack(pady=20)
tk.Button(ventana, text='Cerrar', command=ventana.destroy).pack()

ventana.mainloop()



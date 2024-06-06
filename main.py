import math
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
# Definindo a função polinomial de grau 5
def polynomial(x, a1, a2, a3, a4, a5, a6):
    return a1 * x**5 + a2 * x**4 + a3 * x**3 + a4 * x**2 + a5 * x + a6

# Implementando o algoritmo da seção áurea
def golden_section_search(f, a, b, tol, a1, a2, a3, a4, a5, a6):
    gr = (math.sqrt(5) + 1) / 2  # Razão áurea
    c = b - (b - a) / gr
    d = a + (b - a) / gr

    while abs(b - a) > tol:
        if f(c, a1, a2, a3, a4, a5, a6) < f(d, a1, a2, a3, a4, a5, a6):
            b = d
        else:
            a = c
        
        c = b - (b - a) / gr
        d = a + (b - a) / gr
    
    return (b + a) / 2

# Função para obter os valores da interface gráfica e executar o algoritmo
def find_minimum():
    a1 = float(entry_a1.get())
    a2 = float(entry_a2.get())
    a3 = float(entry_a3.get())
    a4 = float(entry_a4.get())
    a5 = float(entry_a5.get())
    a6 = float(entry_a6.get())
    a = float(entry_a.get())
    b = float(entry_b.get())
    tol = float(entry_tol.get())
    
    min_x = golden_section_search(polynomial, a, b, tol, a1, a2, a3, a4, a5, a6)
    min_f = polynomial(min_x, a1, a2, a3, a4, a5, a6)
    
    result_label.config(text=f"O mínimo da função ocorre em x = {min_x:.4f} com valor f(x) = {min_f:.4f}")

# Criando a interface gráfica com Tkinter
root = tk.Tk()
root.title("Minimização com Seção Áurea")

# Adicionando campos para entrada dos coeficientes do polinômio
tk.Label(root, text="Coeficientes do polinômio").grid(row=0, columnspan=2)
tk.Label(root, text="a1:").grid(row=1, column=0)
entry_a1 = tk.Entry(root)
entry_a1.grid(row=1, column=1)

tk.Label(root, text="a2:").grid(row=2, column=0)
entry_a2 = tk.Entry(root)
entry_a2.grid(row=2, column=1)

tk.Label(root, text="a3:").grid(row=3, column=0)
entry_a3 = tk.Entry(root)
entry_a3.grid(row=3, column=1)

tk.Label(root, text="a4:").grid(row=4, column=0)
entry_a4 = tk.Entry(root)
entry_a4.grid(row=4, column=1)

tk.Label(root, text="a5:").grid(row=5, column=0)
entry_a5 = tk.Entry(root)
entry_a5.grid(row=5, column=1)

tk.Label(root, text="a6:").grid(row=6, column=0)
entry_a6 = tk.Entry(root)
entry_a6.grid(row=6, column=1)

# Adicionando campos para entrada dos extremos do intervalo e a tolerância
tk.Label(root, text="Extremos do intervalo e tolerância").grid(row=7, columnspan=2)
tk.Label(root, text="a:").grid(row=8, column=0)
entry_a = tk.Entry(root)
entry_a.grid(row=8, column=1)

tk.Label(root, text="b:").grid(row=9, column=0)
entry_b = tk.Entry(root)
entry_b.grid(row=9, column=1)

tk.Label(root, text="Tolerância (EPSILON):").grid(row=10, column=0)
entry_tol = tk.Entry(root)
entry_tol.grid(row=10, column=1)

# Botão para executar o algoritmo e mostrar o resultado
tk.Button(root, text="Encontrar Mínimo", command=find_minimum).grid(row=11, columnspan=2)

# Label para mostrar o resultado
result_label = tk.Label(root, text="")
result_label.grid(row=12, columnspan=2)



root.mainloop()
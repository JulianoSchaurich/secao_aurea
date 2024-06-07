import math
import tkinter as tk

# Valores para teste
a1 = 1
a2 = -3
a3 = 2
a4 = -1
a5 = 4
a6 = -2

# Extremos do intervalo e a tolerância
a = -2
b = 2
tol = 0.0001

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
def find_minimum(entry_a1, entry_a2, entry_a3, entry_a4, entry_a5, entry_a6, entry_a, entry_b, entry_tol, result_label):
    result_label.config(text="Calculando o mínimo...")

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

# Função para criar a interface gráfica com Tkinter
def create_gui():
    root = tk.Tk()
    root.title("Minimização com Seção Áurea")

    # Adicionando campos para entrada dos coeficientes do polinômio
    tk.Label(root, text="Coeficientes do polinômio").grid(row=0, columnspan=2, sticky=tk.W)
    entries = {}
    for i in range(1, 7):
        tk.Label(root, text=f"a{i}:").grid(row=i, column=0, sticky=tk.W)
        entries[f'entry_a{i}'] = tk.Entry(root)
        entries[f'entry_a{i}'].grid(row=i, column=1, sticky=tk.W)
        # Definindo os valores de teste como placeholders
        entries[f'entry_a{i}'].insert(0, f"{eval('a' + str(i))}")

    # Adicionando campos para entrada dos extremos do intervalo e a tolerância
    tk.Label(root, text="Extremos do intervalo e tolerância").grid(row=7, columnspan=2, sticky=tk.W)
    tk.Label(root, text="a:").grid(row=8, column=0, sticky=tk.W)
    entries['entry_a'] = tk.Entry(root)
    entries['entry_a'].grid(row=8, column=1, sticky=tk.W)
    entries['entry_a'].insert(0, a)

    tk.Label(root, text="b:").grid(row=9, column=0, sticky=tk.W)
    entries['entry_b'] = tk.Entry(root)
    entries['entry_b'].grid(row=9, column=1, sticky=tk.W)
    entries['entry_b'].insert(0, b)

    tk.Label(root, text="Tolerância (EPSILON):").grid(row=10, column=0, sticky=tk.W)
    entries['entry_tol'] = tk.Entry(root)
    entries['entry_tol'].grid(row=10, column=1, sticky=tk.W)
    entries['entry_tol'].insert(0, tol)

    # Botão para executar o algoritmo e mostrar o resultado
    tk.Button(root, text="Encontrar Mínimo", command=lambda: find_minimum(**entries, result_label=result_label)).grid(row=11, columnspan=2, sticky=tk.W)

    # Label para mostrar o resultado
    result_label = tk.Label(root, text="")
    result_label.grid(row=12, columnspan=2, sticky=tk.W)

    root.mainloop()

# Função principal para execução da interface gráfica
def main():
    create_gui()

if __name__ == "__main__":
    main()

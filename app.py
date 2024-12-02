import tkinter as tk
from calculos import calculo_valor_arroba  # Importa a função de cálculo

# Função chamada ao clicar no botão "Calcular"
def calcular():
    try:
        # Pega os valores digitados pelo usuário
        peso_bovino = float(entry_peso.get())
        preco_arroba = float(entry_preco.get())

        # Realiza o cálculo usando a função importada
        peso_arroba, valor_calc = calculo_valor_arroba(peso_bovino, preco_arroba)

        # Formata o resultado
        valor_final = "{:.2f}".format(valor_calc)
        peso_arroba_format = "{:.2f}".format(peso_arroba)

        # Exibe o resultado no rótulo
        label_resultado.config(
            text=f"Peso em arrobas: {peso_arroba_format} arrobas\nValor total: R$ {valor_final}"
        )
    except ValueError:
        # Exibe mensagem de erro caso os valores não sejam válidos
        label_resultado.config(text="Erro: Por favor, insira valores válidos.")

# Função para limpar os campos de entrada e o resultado
def limpar():
    entry_peso.delete(0, tk.END)  # Limpa o campo do peso
    entry_preco.delete(0, tk.END)  # Limpa o campo do preço
    label_resultado.config(text="")  # Limpa o rótulo do resultado

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora de Arroba")

# Tamanho fixo para a janela
root.geometry("600x350")

# Define cor de fundo
root.configure(bg="#e1f5fe")

# Estilo básico
font_label = ("Arial", 16)
font_button = ("Arial", 16, "bold")
widget_width = 25

# Criação do frame central
frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor="center")  # Centraliza o frame

# Título do programa
tk.Label(frame, text="Calculadora de Valor da Arroba", font=("Arial", 20, "bold"), bg="#ffffff", fg="#007acc").grid(
    row=0, columnspan=2, pady=(0, 20))

# Campo para entrada do peso
tk.Label(frame, text="Peso do bovino (kg):", bg="#ffffff", font=font_label).grid(row=1, column=0, padx=10, pady=5,
                                                                                 sticky='e')
entry_peso = tk.Entry(frame, font=font_label, width=widget_width, relief="solid", bd=1)
entry_peso.grid(row=1, column=1, padx=10, pady=5)

# Campo para entrada do preço
tk.Label(frame, text="Preço da arroba (R$):", bg="#ffffff", font=font_label).grid(row=2, column=0, padx=10, pady=5,
                                                                                  sticky='e')
entry_preco = tk.Entry(frame, font=font_label, width=widget_width, relief="solid", bd=1)
entry_preco.grid(row=2, column=1, padx=10, pady=5)

# Botão para calcular
btn_calcular = tk.Button(frame, text="Calcular", command=calcular, font=font_button, bg="#4caf50", fg="white",
                         relief="raised", bd=2, width=widget_width)
btn_calcular.grid(row=3, columnspan=2, pady=20)

# Botão para limpar os campos
btn_limpar = tk.Button(frame, text="Limpar", command=limpar, font=font_button, bg="#f44336", fg="white",
                       relief="raised", bd=2, width=widget_width)
btn_limpar.grid(row=4, columnspan=2, pady=10)

# Rótulo para exibir o resultado
label_resultado = tk.Label(frame, text="", bg="#ffffff", font=("Arial", 16, "italic"), fg="#333333")
label_resultado.grid(row=5, columnspan=2, pady=10)

# Atalhos de teclado
root.bind('<Return>', lambda event: calcular())  # Tecla Enter para calcular
root.bind('<Control-q>', lambda event: root.quit())  # Ctrl+Q para sair

# Loop da interface
root.mainloop()

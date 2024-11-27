import tkinter as tk

# função para calcular o valor total da arroba
def calculo_valor_arroba(peso_vivo, preco_arroba):
    peso_vivo_half = peso_vivo / 2  # metade do peso vivo
    peso_arroba = (peso_vivo_half / 15) - 1  # peso em arrobas
    valor_total = peso_arroba * preco_arroba  # calcula o valor total
    return peso_arroba, valor_total  # retorna peso em arrobas e valor total

# função chamada ao clicar no botão "calcular"
def calcular():
    try:
        # pega os valores digitados pelo usuário
        peso_bovino = float(entry_peso.get())
        preco_arroba = float(entry_preco.get())

        # realiza o cálculo
        peso_arroba, valor_calc = calculo_valor_arroba(peso_bovino, preco_arroba)

        # formata o resultado
        valor_final = "{:.2f}".format(valor_calc)
        peso_arroba_format = "{:.2f}".format(peso_arroba)

        # exibe o resultado no rótulo
        label_resultado.config(
            text=f"peso em arrobas: {peso_arroba_format} arrobas\nvalor total: R$ {valor_final}"
        )
    except ValueError:
        # exibe mensagem de erro caso os valores não sejam válidos
        label_resultado.config(text="erro: por favor, insira valores válidos.")

# função para limpar os campos de entrada e o resultado
def limpar():
    entry_peso.delete(0, tk.END)  # limpa o campo do peso
    entry_preco.delete(0, tk.END)  # limpa o campo do preço
    label_resultado.config(text="")  # limpa o rótulo do resultado

# configuração da janela principal
root = tk.Tk()
root.title("cálculo de valor da arroba")

# tamanho fixo para a janela
root.geometry("800x600")

# define cor de fundo
root.configure(bg="#e1f5fe")

# estilo básico
font_label = ("arial", 16)
font_button = ("arial", 16, "bold")
widget_width = 25

# criação do frame central
frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor="center")  # centraliza o frame

# título do programa
tk.Label(frame, text="calculadora de valor da arroba", font=("arial", 20, "bold"), bg="#ffffff", fg="#007acc").grid(
    row=0, columnspan=2, pady=(0, 20))

# campo para entrada do peso
tk.Label(frame, text="peso do bovino (kg):", bg="#ffffff", font=font_label).grid(row=1, column=0, padx=10, pady=5,
                                                                                 sticky='e')
entry_peso = tk.Entry(frame, font=font_label, width=widget_width, relief="solid", bd=1)
entry_peso.grid(row=1, column=1, padx=10, pady=5)

# campo para entrada do preço
tk.Label(frame, text="preço da arroba (R$):", bg="#ffffff", font=font_label).grid(row=2, column=0, padx=10, pady=5,
                                                                                  sticky='e')
entry_preco = tk.Entry(frame, font=font_label, width=widget_width, relief="solid", bd=1)
entry_preco.grid(row=2, column=1, padx=10, pady=5)

# botão para calcular
btn_calcular = tk.Button(frame, text="calcular", command=calcular, font=font_button, bg="#4caf50", fg="white",
                         relief="raised", bd=2, width=widget_width)
btn_calcular.grid(row=3, columnspan=2, pady=20)

# botão para limpar os campos
btn_limpar = tk.Button(frame, text="limpar", command=limpar, font=font_button, bg="#f44336", fg="white",
                       relief="raised", bd=2, width=widget_width)
btn_limpar.grid(row=4, columnspan=2, pady=10)

# rótulo para exibir o resultado
label_resultado = tk.Label(frame, text="", bg="#ffffff", font=("arial", 16, "italic"), fg="#333333")
label_resultado.grid(row=5, columnspan=2, pady=10)

# atalhos de teclado
root.bind('<Return>', lambda event: calcular())  # tecla enter para calcular
root.bind('<Control-q>', lambda event: root.quit())  # ctrl+q para sair

# loop da interface
root.mainloop()

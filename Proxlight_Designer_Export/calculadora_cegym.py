from tkinter import *


"""
entry0 = faturamento total
entry1 = escola percentual
entry2 = prof passagem mensal
entry3 = professor percentual
entry4 = imposto
entry5 = faturamento liquido
entry6 = escola total
entry7 = professor participacao
entry8 = prof. participação + passagem
entry9 = Lucro CEGYM
"""

def btn_clicked():
    # global faturamento_total
    faturamento_total = entry0.get()
    # global escola_percentual
    escola_percentual = entry1.get()
    # global prof_passagem_mensal
    prof_passagem_mensal = entry2.get()
    # global professor_percentual
    professor_percentual = entry3.get()
    # global imposto
    imposto = entry4.get()
    # global faturamento_liquido
    faturamento_liquido = float(faturamento_total) - (float(faturamento_total) * (float(imposto) / 100))
    # global escola_total
    escola_total = float(faturamento_liquido) * (float(escola_percentual) / 100)
    # global professor_participacao
    professor_participacao = (float(faturamento_liquido) - escola_total) * (float(professor_percentual) / 100)
    # global prof_participacao_passagem
    prof_participacao_passagem = float(professor_participacao) + float(prof_passagem_mensal)
    # global lucro_cegym
    lucro_cegym = float(faturamento_liquido) - float(escola_total) - float(prof_participacao_passagem)
    
    entry5.config(text=f'R$ {faturamento_liquido:,.2f}', fg="#ffffff", bg="#DAF9CC")
    entry6.config(text=f'R$ {escola_total:,.2f}', fg="#ffffff", bg="#DAF9CC")
    entry7.config(text=f'R$ {professor_participacao:,.2f}', fg="#ffffff", bg="#DAF9CC")
    entry8.config(text=f'R$ {prof_participacao_passagem:,.2f}', fg="#ffffff", bg="#DAF9CC")
    entry9.config(text=f'R$ {lucro_cegym:,.2f}', fg="#ffffff", bg="#DAF9CC")
    
        
    print("Button Clicked")


window = Tk()

window.geometry("650x500")
window.configure(bg = "#f4f4f4")
canvas = Canvas(
    window,
    bg = "#f4f4f4",
    height = 500,
    width = 650,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = r"C:\Users\belig\OneDrive\Python\MeuProjeto\Projetos\Calculadora_CEGYM\Proxlight_Designer_Export\Background.png")
background = canvas.create_image(
    325.0, 250.0,
    image=background_img)

entry0_img = PhotoImage(file = r"C:\Users\belig\OneDrive\Python\MeuProjeto\Projetos\Calculadora_CEGYM\Proxlight_Designer_Export\img_textBox0.png")
entry0_bg = canvas.create_image(
    220.0, 123.5,
    image = entry0_img,)

entry0 = Entry(
    bd = 0,
    bg = "#003caa",
    fg = '#ffffff',
    highlightthickness = 0)

entry0.place(
    x = 164.0, y = 110,
    width = 112.0,
    height = 25)


entry1_img = PhotoImage(file = r"C:\Users\belig\OneDrive\Python\MeuProjeto\Projetos\Calculadora_CEGYM\Proxlight_Designer_Export\img_textBox1.png")
entry1_bg = canvas.create_image(
    220.0, 176.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#003caa",
    fg = '#ffffff',
    highlightthickness = 0)
entry1.pack()

entry1.place(
    x = 164.0, y = 163,
    width = 112.0,
    height = 25)


entry2_img = PhotoImage(file = r"C:\Users\belig\OneDrive\Python\MeuProjeto\Projetos\Calculadora_CEGYM\Proxlight_Designer_Export\img_textBox2.png")
entry2_bg = canvas.create_image(
    220.0, 230.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#003caa",
    fg = '#ffffff',
    highlightthickness = 0)

entry2.place(
    x = 164.0, y = 217,
    width = 112.0,
    height = 25)

entry3_img = PhotoImage(file = r"C:\Users\belig\OneDrive\Python\MeuProjeto\Projetos\Calculadora_CEGYM\Proxlight_Designer_Export\img_textBox3.png")
entry3_bg = canvas.create_image(
    220.0, 282.5,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#003caa",
    fg = '#ffffff',
    highlightthickness = 0)

entry3.place(
    x = 164.0, y = 269,
    width = 112.0,
    height = 25)

entry4_img = PhotoImage(file = r"C:\Users\belig\OneDrive\Python\MeuProjeto\Projetos\Calculadora_CEGYM\Proxlight_Designer_Export\img_textBox4.png")
entry4_bg = canvas.create_image(
    220.0, 335.5,
    image = entry4_img)

entry4 = Entry(
    bd = 0,
    bg = "#3c3c3c",
    fg = '#ffffff',
    highlightthickness = 0)

entry4.place(
    x = 164.0, y = 322,
    width = 112.0,
    height = 25)
entry4.insert(0, 15)


entry5_img = PhotoImage(file = r"C:\Users\belig\OneDrive\Python\MeuProjeto\Projetos\Calculadora_CEGYM\Proxlight_Designer_Export\img_textBox5.png")
entry5_bg = canvas.create_image(
    512.0, 123.5,
    image = entry5_img)

entry5 = Label(
    bd = 0,
    bg = "#3c3c3c",
    highlightthickness = 0)

entry5.place(
    x = 456.0, y = 110,
    width = 112.0,
    height = 25)
entry5.config(state=DISABLED)


entry6_img = PhotoImage(file = r"C:\Users\belig\OneDrive\Python\MeuProjeto\Projetos\Calculadora_CEGYM\Proxlight_Designer_Export\img_textBox6.png")
entry6_bg = canvas.create_image(
    512.0, 176.5,
    image = entry6_img)

entry6 = Label(
    bd = 0,
    bg = "#3c3c3c",
    highlightthickness = 0)

entry6.place(
    x = 456.0, y = 163,
    width = 112.0,
    height = 25)
entry6.config(state=DISABLED)

entry7_img = PhotoImage(file = r"C:\Users\belig\OneDrive\Python\MeuProjeto\Projetos\Calculadora_CEGYM\Proxlight_Designer_Export\img_textBox7.png")
entry7_bg = canvas.create_image(
    512.0, 229.5,
    image = entry7_img)

entry7 = Label(
    bd = 0,
    bg = "#3c3c3c",
    highlightthickness = 0)

entry7.place(
    x = 456.0, y = 216,
    width = 112.0,
    height = 25)
entry7.config(state=DISABLED)

entry8_img = PhotoImage(file = r"C:\Users\belig\OneDrive\Python\MeuProjeto\Projetos\Calculadora_CEGYM\Proxlight_Designer_Export\img_textBox8.png")
entry8_bg = canvas.create_image(
    512.0, 282.5,
    image = entry8_img)

entry8 = Label(
    bd = 0,
    bg = "#3c3c3c",
    highlightthickness = 0)

entry8.place(
    x = 456.0, y = 269,
    width = 112.0,
    height = 25)
entry8.config(state=DISABLED)

entry9_img = PhotoImage(file = r"C:\Users\belig\OneDrive\Python\MeuProjeto\Projetos\Calculadora_CEGYM\Proxlight_Designer_Export\img_textBox9.png")
entry9_bg = canvas.create_image(
    512.0, 334.5,
    image = entry9_img)

entry9 = Label(
    bd = 0,
    bg = "#3c3c3c",
    highlightthickness = 0)

entry9.place(
    x = 456.0, y = 321,
    width = 112.0,
    height = 25)
entry9.config(state=DISABLED)

img0 = PhotoImage(file = r"C:\Users\belig\OneDrive\Python\MeuProjeto\Projetos\Calculadora_CEGYM\Proxlight_Designer_Export\img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 265, y = 396,
    width = 104,
    height = 45)


entry0.insert(0, 0)
entry1.insert(0, 0)
entry2.insert(0, 0)
entry3.insert(0, 0)

# logo do tkinter
window.iconbitmap(r"C:\Users\belig\OneDrive\Python\MeuProjeto\Projetos\Calculadora_CEGYM\Proxlight_Designer_Export\Logo-Cegym.ico")
window.title("Calculadora CEGYM")


window.resizable(False, False)
window.mainloop()

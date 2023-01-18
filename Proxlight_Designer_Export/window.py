from tkinter import *


def btn_LTC():
    print("Button LTC Clicked")
    

def btn_esaude():
    print("Button ESTUDIO SAUDE Clicked")
    

def btn_concept():
    print("Button CONCEPT Clicked")
    

def btn_atmos():
    print("Button ATMOS Clicked")
    

def btn_sula():
    print("Button SULAMERICANA Clicked")
    

def btn_ebateca():
    print("Button EBATECA Clicked")
    

def btn_malta():
    print("Button MALTA Clicked6")
    

def btn_aldeia():
    print("Button ALDEIA Clicked")
    

def btn_cepe():
    faturamento_total = float(entry0.get())
    escola_percentual = float(entry1.get())
    prof_passagem_mensal = float(entry2.get())
    professor_percentual = float(entry3.get())
    alunos = float(entry4.get())
    hora_aula = float(entry11.get())
    imposto = float(entry5.get())
    #horas_trabalhadas_mensais = float(entry12.get())
    
    faturamento_liquido = '-'
    escola_total = faturamento_liquido * (escola_percentual / 100)
    #professor_participacao = hora_aula * horas_trabalhadas
    # prof_participacao_passagem = professor_participacao + prof_passagem_mensal
    lucro_cegym = faturamento_total - escola_total - prof_participacao_passagem
    
    entry6.config(text=f'R$ {faturamento_liquido:,.2f}', fg="#ffffff", bg="#DAF9CC")
    entry7.config(text=f'R$ {escola_total:,.2f}', fg="#ffffff", bg="#DAF9CC")
    #entry8.config(text=f'R$ {professor_participacao:,.2f}', fg="#ffffff", bg="#DAF9CC")
    entry9.config(text=f'R$ {prof_participacao_passagem:,.2f}', fg="#ffffff", bg="#DAF9CC")
    entry10.config(text=f'R$ {lucro_cegym:,.2f}', fg="#ffffff", bg="#DAF9CC")
    print("Button CEPE Clicked")
    

def btn_reset():
    entry0.delete(0, END)
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.config(text=0)
    entry7.config(text=0)
    entry8.config(text=0)
    entry9.config(text=0)
    entry10.config(text=0)
    print("Button RESET Clicked")
    


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

background_img = PhotoImage(file = r"calculadora_CEGYM\Proxlight_Designer_Export\background.png")
background = canvas.create_image(
    324.5, 251.0,
    image=background_img)


# FATURAMENTO TOTAL---------------------------------------------------
entry0_img = PhotoImage(file = r"calculadora_CEGYM\Proxlight_Designer_Export\img_textBox0.png")
entry0_bg = canvas.create_image(
    220.0, 113.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#003caa",
    fg = '#ffffff',
    highlightthickness = 0)

entry0.place(
    x = 164.0, y = 100,
    width = 112.0,
    height = 25)


# ESCOLA PERCENTUAL-------------------------------------------
entry1_img = PhotoImage(file = r"calculadora_CEGYM\Proxlight_Designer_Export\img_textBox1.png")
entry1_bg = canvas.create_image(
    220.0, 166.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#003caa",
    fg = '#ffffff',
    highlightthickness = 0)

entry1.place(
    x = 164.0, y = 153,
    width = 112.0,
    height = 25)


# PROF PASSAGEM MENSAL-------------------------------------------
entry2_img = PhotoImage(file = r"calculadora_CEGYM\Proxlight_Designer_Export\img_textBox2.png")
entry2_bg = canvas.create_image(
    220.0, 220.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#003caa",
    fg = '#ffffff',
    highlightthickness = 0)

entry2.place(
    x = 164.0, y = 207,
    width = 112.0,
    height = 25)


# PROFESSOR PERCENTUAL-------------------------------------------
entry3_img = PhotoImage(file = r"calculadora_CEGYM\Proxlight_Designer_Export\img_textBox3.png")
entry3_bg = canvas.create_image(
    220.0, 272.5,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#003caa",
    fg = '#ffffff',
    highlightthickness = 0)

entry3.place(
    x = 164.0, y = 259,
    width = 112.0,
    height = 25)


# ALUNOS-------------------------------------------
entry4_img = PhotoImage(file = r"calculadora_CEGYM\Proxlight_Designer_Export\img_textBox4.png")
entry4_bg = canvas.create_image(
    220.0, 325.5,
    image = entry4_img)

entry4 = Entry(
    bd = 0,
    bg = "#003caa",
    fg = '#ffffff',
    highlightthickness = 0)

entry4.place(
    x = 164.0, y = 312,
    width = 112.0,
    height = 25)


# IMPOSTOS-------------------------------------------
entry5_img = PhotoImage(file = r"calculadora_CEGYM\Proxlight_Designer_Export\img_textBox5.png")
entry5_bg = canvas.create_image(
    220.0, 378.5,
    image = entry5_img)

entry5 = Entry(
    bd = 0,
    bg = "#3c3c3c",
    fg = '#ffffff',
    highlightthickness = 0)

entry5.place(
    x = 456.0, y = 100,
    width = 112.0,
    height = 25)
entry5.insert(0, 15)



# FATURAMENTO LIQUIDO-------------------------------------------
entry6_img = PhotoImage(file = r"calculadora_CEGYM\Proxlight_Designer_Export\img_textBox6.png")
entry6_bg = canvas.create_image(
    512.0, 113.5,
    image = entry6_img)

entry6 = Label(
    bd = 0,
    bg = "#3c3c3c",
    highlightthickness = 0)

entry6.place(
    x = 456.0, y = 153,
    width = 112.0,
    height = 25)
entry6.config(state=DISABLED)



# ESCOLA TOTAL-------------------------------------------
entry7_img = PhotoImage(file = r"calculadora_CEGYM\Proxlight_Designer_Export\img_textBox7.png")
entry7_bg = canvas.create_image(
    512.0, 166.5,
    image = entry7_img)

entry7 = Label(
    bd = 0,
    bg = "#3c3c3c",
    highlightthickness = 0)

entry7.place(
    x = 456.0, y = 206,
    width = 112.0,
    height = 25)
entry7.config(state=DISABLED)



# PROFESSOR PARTICIPACAO-------------------------------------------
entry8_img = PhotoImage(file = r"calculadora_CEGYM\Proxlight_Designer_Export\img_textBox8.png")
entry8_bg = canvas.create_image(
    512.0, 219.5,
    image = entry8_img)

entry8 = Label(
    bd = 0,
    bg = "#3c3c3c",
    highlightthickness = 0)

entry8.place(
    x = 456.0, y = 259,
    width = 112.0,
    height = 25)
entry8.config(state=DISABLED)



# PROFESSOR PARTICIPACAO + PASSAGEM-------------------------------------------
entry9_img = PhotoImage(file = r"calculadora_CEGYM\Proxlight_Designer_Export\img_textBox9.png")
entry9_bg = canvas.create_image(
    512.0, 272.5,
    image = entry9_img)

entry9 = Label(
    bd = 0,
    bg = "#3c3c3c",
    highlightthickness = 0)

entry9.place(
    x = 456.0, y = 311,
    width = 112.0,
    height = 25)
entry9.config(state=DISABLED)


# LUCRO CEGYM -------------------------------------------
entry10_img = PhotoImage(file = r"calculadora_CEGYM\Proxlight_Designer_Export\img_textBox10.png")
entry10_bg = canvas.create_image(
    512.0, 324.5,
    image = entry10_img)

entry10 = Label(
    bd = 0,
    bg = "#3c3c3c",
    highlightthickness = 0)

entry10.place(
    x = 456.0, y = 364,
    width = 112.0,
    height = 25)
entry10.config(state=DISABLED)


# Hora Aula -------------------------------------------
entry11_img = PhotoImage(file = r"calculadora_CEGYM\Proxlight_Designer_Export\img_textBox11.png")
entry11_bg = canvas.create_image(
    512.0, 377.5,
    image = entry11_img)

entry11 = Entry(
    bd = 0,
    bg = "#3c3c3c",
    fg = '#ffffff',
    highlightthickness = 0)

entry11.place(
    x = 164.0, y = 364,
    width = 112.0,
    height = 25)
entry11.insert(0, 'hora aula')

#-------------------------------------------------------------------------------------
img0 = PhotoImage(file = r"calculadora_CEGYM\Proxlight_Designer_Export\img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_LTC,
    relief = "flat")

b0.place(
    x = 490, y = 445,
    width = 55,
    height = 30)

img1 = PhotoImage(file = r"calculadora_CEGYM\Proxlight_Designer_Export\img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_esaude,
    relief = "flat")

b1.place(
    x = 432, y = 445,
    width = 55,
    height = 30)

img2 = PhotoImage(file = r"calculadora_CEGYM\Proxlight_Designer_Export\img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_concept,
    relief = "flat")

b2.place(
    x = 372, y = 445,
    width = 55,
    height = 30)

img3 = PhotoImage(file = r"calculadora_CEGYM\Proxlight_Designer_Export\img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_atmos,
    relief = "flat")

b3.place(
    x = 311, y = 445,
    width = 55,
    height = 30)

img4 = PhotoImage(file = r"calculadora_CEGYM\Proxlight_Designer_Export\img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_sula,
    relief = "flat")

b4.place(
    x = 254, y = 445,
    width = 54,
    height = 30)

img5 = PhotoImage(file = r"calculadora_CEGYM\Proxlight_Designer_Export\img5.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_ebateca,
    relief = "flat")

b5.place(
    x = 195, y = 445,
    width = 54,
    height = 30)

img6 = PhotoImage(file = r"calculadora_CEGYM\Proxlight_Designer_Export\img6.png")
b6 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_malta,
    relief = "flat")

b6.place(
    x = 133, y = 445,
    width = 56,
    height = 30)

img7 = PhotoImage(file = r"calculadora_CEGYM\Proxlight_Designer_Export\img7.png")
b7 = Button(
    image = img7,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_aldeia,
    relief = "flat")

b7.place(
    x = 75, y = 445,
    width = 55,
    height = 30)

img8 = PhotoImage(file = r"calculadora_CEGYM\Proxlight_Designer_Export\img8.png")
b8 = Button(
    image = img8,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_cepe,
    relief = "flat")

b8.place(
    x = 16, y = 445,
    width = 55,
    height = 30)

img9 = PhotoImage(file = r"calculadora_CEGYM\Proxlight_Designer_Export\img9.png")
b9 = Button(
    image = img9,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_reset,
    relief = "flat")

b9.place(
    x = 578, y = 12,
    width = 55,
    height = 30)

#config teste
entry0.insert(0, 2000)
entry1.insert(0, 30)
entry2.insert(0, 90)
entry3.insert(0, 40)
entry4.insert(0, 5)





window.resizable(False, False)
window.mainloop()

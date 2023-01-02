from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("630x481")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 481,
    width = 630,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = r"C:\Users\belig\OneDrive\Python\MeuProjeto\Projetos\Calculador CEGYM\Proxlight_Designer_Export\background.png")
background = canvas.create_image(
    315.0, 240.5,
    image=background_img)

img0 = PhotoImage(file = r"C:\Users\belig\OneDrive\Python\MeuProjeto\Projetos\Calculador CEGYM\Proxlight_Designer_Export\img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 490, y = 436,
    width = 87,
    height = 27)

entry0_img = PhotoImage(file = r"C:\Users\belig\OneDrive\Python\MeuProjeto\Projetos\Calculador CEGYM\Proxlight_Designer_Export\img_textBox0.png")
entry0_bg = canvas.create_image(
    359.0, 454.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#ffde9d",
    highlightthickness = 0)

entry0.place(
    x = 313, y = 446,
    width = 92,
    height = 14)

entry1_img = PhotoImage(file = r"C:\Users\belig\OneDrive\Python\MeuProjeto\Projetos\Calculador CEGYM\Proxlight_Designer_Export\img_textBox1.png")
entry1_bg = canvas.create_image(
    340.0, 426.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry1.place(
    x = 329, y = 419,
    width = 22,
    height = 13)

entry2_img = PhotoImage(file = r"C:\Users\belig\OneDrive\Python\MeuProjeto\Projetos\Calculador CEGYM\Proxlight_Designer_Export\img_textBox2.png")
entry2_bg = canvas.create_image(
    380.0, 369.0,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#ffde9d",
    highlightthickness = 0)

entry2.place(
    x = 334, y = 361,
    width = 92,
    height = 14)

entry3_img = PhotoImage(file = r"C:\Users\belig\OneDrive\Python\MeuProjeto\Projetos\Calculador CEGYM\Proxlight_Designer_Export\img_textBox3.png")
entry3_bg = canvas.create_image(
    365.0, 338.5,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry3.place(
    x = 334, y = 331,
    width = 62,
    height = 13)

entry4_img = PhotoImage(file = r"C:\Users\belig\OneDrive\Python\MeuProjeto\Projetos\Calculador CEGYM\Proxlight_Designer_Export\img_textBox4.png")
entry4_bg = canvas.create_image(
    412.0, 310.5,
    image = entry4_img)

entry4 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry4.place(
    x = 381, y = 303,
    width = 62,
    height = 13)

entry5_img = PhotoImage(file = r"C:\Users\belig\OneDrive\Python\MeuProjeto\Projetos\Calculador CEGYM\Proxlight_Designer_Export\img_textBox5.png")
entry5_bg = canvas.create_image(
    331.0, 281.5,
    image = entry5_img)

entry5 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry5.place(
    x = 320, y = 274,
    width = 22,
    height = 13)

entry6_img = PhotoImage(file = r"C:\Users\belig\OneDrive\Python\MeuProjeto\Projetos\Calculador CEGYM\Proxlight_Designer_Export\img_textBox6.png")
entry6_bg = canvas.create_image(
    377.0, 223.0,
    image = entry6_img)

entry6 = Entry(
    bd = 0,
    bg = "#ffde9d",
    highlightthickness = 0)

entry6.place(
    x = 331, y = 215,
    width = 92,
    height = 14)

entry7_img = PhotoImage(file = r"C:\Users\belig\OneDrive\Python\MeuProjeto\Projetos\Calculador CEGYM\Proxlight_Designer_Export\img_textBox7.png")
entry7_bg = canvas.create_image(
    407.0, 195.0,
    image = entry7_img)

entry7 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry7.place(
    x = 361, y = 187,
    width = 92,
    height = 14)

entry8_img = PhotoImage(file = r"C:\Users\belig\OneDrive\Python\MeuProjeto\Projetos\Calculador CEGYM\Proxlight_Designer_Export\img_textBox8.png")
entry8_bg = canvas.create_image(
    298.0, 165.5,
    image = entry8_img)

entry8 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry8.place(
    x = 287, y = 158,
    width = 22,
    height = 13)

entry9_img = PhotoImage(file = r"C:\Users\belig\OneDrive\Python\MeuProjeto\Projetos\Calculador CEGYM\Proxlight_Designer_Export\img_textBox9.png")
entry9_bg = canvas.create_image(
    397.0, 137.0,
    image = entry9_img)

entry9 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry9.place(
    x = 351, y = 129,
    width = 92,
    height = 14)

window.resizable(False, False)
window.mainloop()
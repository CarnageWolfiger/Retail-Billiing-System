import os
import sqlite3
import tempfile
import tkinter as tk
from tkinter import *


conn = sqlite3.connect('billing_database.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS bills (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        bill_number INTEGER,
        customer_name TEXT,
        phone_number TEXT,
        bath_soap REAL,
        face_cream REAL,
        face_wash REAL,
        hair_spray REAL,
        hair_gel REAL,
        body_lotion REAL,
        rice REAL,
        oil REAl,
        daal REAL,
        wheat REAL,
        sugar REAL,
        tea REAl,
        maaza REAL,
        pepsi REAL,
        sprite REAL,
        dew REAL,
        frooti REAL,
        coca_cola REAL,
        cosmetic_price REAL,
        grocery_price REAL,
        colddrink_price REAL,
        cosmetic_tax REAL,
        grocery_tax REAL,
        colddrink_tax REAL,
        total_bill REAL
    )
''')
conn.commit()



def load_last_bill_number():
    try:
        with open("last_bill_number.txt", "r") as file:
            last_bill_number = int(file.read())
    except FileNotFoundError:
        last_bill_number = 1
    return last_bill_number


def save_last_bill_number(billnumber):
    with open("last_bill_number.txt", "w") as file:
        file.write(str(billnumber))


def insert_into_database():
    c.execute('''
        INSERT INTO bills (
            bill_number, customer_name, phone_number,
            bath_soap,face_cream,face_wash,hair_spray,hair_gel,body_lotion,
            rice,oil,daal,wheat,sugar,tea,
            maaza,pepsi,sprite,dew,frooti,coca_cola,
            cosmetic_price, grocery_price, colddrink_price,
            cosmetic_tax, grocery_tax, colddrink_tax, total_bill
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        int(billnumber_entry.get()), name_entry.get(), phone_entry.get(),
        float(bathsoap_entry.get()), float(facecream_entry.get()), float(facewash_entry.get()),
        float(hairspray_entry.get()), float(hairgel_entry.get()), float(bodylotion_entry.get()),
        float(rice_entry.get()), float(oil_entry.get()), float(Daal_entry.get()),
        float(wheat_entry.get()), float(sugar_entry.get()), float(tea_entry.get()),
        float(maaza_entry.get()), float(pepsi_entry.get()), float(sprite_entry.get()),
        float(dew_entry.get()), float(frooti_entry.get()), float(cocacola_entry.get()),
        float(cosmeticprice_entry.get()), float(groceryprice_entry.get()), float(colddrinkprice_entry.get()),
        float(cosmetictax_entry.get()), float(Grocerytax_entry.get()), float(colddrinktax_entry.get()), float(totalbill)
    ))
    conn.commit()


def billbutton_clicked():
    global billnumber
    billnumber += 1
    billnumber_entry.delete(0, tk.END)
    billnumber_entry.insert(0, str(billnumber))
    save_last_bill_number(billnumber)


def clear_and_billnumber():
    clear()
    billbutton_clicked()


def print():
    file = tempfile.mktemp(".txt")
    open(file, "w").write(textarea.get(1.0, END))
    os.startfile(file, "print")


def clear():
    name_entry.delete(0, END)
    phone_entry.delete(0, END)
    billnumber_entry.delete(0, END)
    bathsoap_entry.delete(0, END)
    bathsoap_entry.insert(0,0)
    facecream_entry.delete(0, END)
    facecream_entry.insert(0, 0)
    facewash_entry.delete(0, END)
    facewash_entry.insert(0, 0)
    hairspray_entry.delete(0, END)
    hairspray_entry.insert(0, 0)
    hairgel_entry.delete(0, END)
    hairgel_entry.insert(0, 0)
    bodylotion_entry.delete(0, END)
    bodylotion_entry.insert(0, 0)
    rice_entry.delete(0, END)
    rice_entry.insert(0, 0)
    oil_entry.delete(0, END)
    oil_entry.insert(0, 0)
    Daal_entry.delete(0, END)
    Daal_entry.insert(0, 0)
    wheat_entry.delete(0, END)
    wheat_entry.insert(0, 0)
    sugar_entry.delete(0, END)
    sugar_entry.insert(0, 0)
    tea_entry.delete(0, END)
    tea_entry.insert(0, 0)
    maaza_entry.delete(0, END)
    maaza_entry.insert(0, 0)
    pepsi_entry.delete(0, END)
    pepsi_entry.insert(0, 0)
    sprite_entry.delete(0, END)
    sprite_entry.insert(0, 0)
    dew_entry.delete(0, END)
    dew_entry.insert(0, 0)
    frooti_entry.delete(0, END)
    frooti_entry.insert(0, 0)
    cocacola_entry.delete(0, END)
    cocacola_entry.insert(0, 0)
    cosmeticprice_entry.delete(0, END)
    groceryprice_entry.delete(0, END)
    colddrinkprice_entry.delete(0, END)
    cosmetictax_entry.delete(0, END)
    Grocerytax_entry.delete(0, END)
    colddrinktax_entry.delete(0, END)
    textarea.delete(1.0, END)


def billfunction():
    textarea.insert(END, f"\nBill No :{billnumber_entry.get()}\n")
    textarea.insert(END, f"\nCustomer Name : {name_entry.get()}")
    textarea.insert(END, f"\nPhone No. : {phone_entry.get()}")
    textarea.insert(END, "\n============================================")
    textarea.insert(END, "\nProduct\t\tQuantity\t\tPrice")
    textarea.insert(END, "\n============================================")
    if bathsoap_entry.get() != '0':
        textarea.insert(END, f"\nBath Soap\t\t{bathsoap_entry.get()}\t\t{soapprice}")
    if facecream_entry.get() != '0':
        textarea.insert(END, f"\nFace Cream\t\t{facecream_entry.get()}\t\t{facecreamprice}")
    if facewash_entry.get() != '0':
        textarea.insert(END, f"\nFace Wash\t\t{facewash_entry.get()}\t\t{facewashprice}")
    if hairspray_entry.get() != '0':
        textarea.insert(END, f"\nHair Spray\t\t{hairspray_entry.get()}\t\t{hairsprayprice}")
    if hairgel_entry.get() != '0':
        textarea.insert(END, f"\nHair Gel\t\t{hairgel_entry.get()}\t\t{hairgelprice}")
    if bodylotion_entry.get() != '0':
        textarea.insert(END, f"\nBody Lotion\t\t{bodylotion_entry.get()}\t\t{bodylotionprice}")
    if rice_entry.get() != '0':
        textarea.insert(END, f"\nRice\t\t{rice_entry.get()}Kg\t\t{riceprice}")
    if oil_entry.get() != '0':
        textarea.insert(END, f"\nOil\t\t{oil_entry.get()}Kg\t\t{oilprice}")
    if Daal_entry.get() != '0':
        textarea.insert(END, f"\nDaal\t\t{Daal_entry.get()}Kg\t\t{daalprice}")
    if wheat_entry.get() != '0':
        textarea.insert(END, f"\nWheat\t\t{wheat_entry.get()}Kg\t\t{wheatprice}")
    if sugar_entry.get() != '0':
        textarea.insert(END, f"\nSugar\t\t{sugar_entry.get()}Kg\t\t{sugarprice}")
    if tea_entry.get() != '0':
        textarea.insert(END, f"\nTea\t\t{tea_entry.get()}Kg\t\t{teaprice}")
    if maaza_entry.get() != '0':
        textarea.insert(END, f"\nMaaza\t\t{maaza_entry.get()}Ltr\t\t{maazaprice}")
    if pepsi_entry.get() != '0':
        textarea.insert(END, f"\nPepsi\t\t{pepsi_entry.get()}Ltr\t\t{pepsiprice}")
    if sprite_entry.get() != '0':
        textarea.insert(END, f"\nSprite\t\t{sprite_entry.get()}Ltr\t\t{spriteprice}")
    if dew_entry.get() != '0':
        textarea.insert(END, f"\nDew\t\t{dew_entry.get()}Ltr\t\t{dewprice}")
    if frooti_entry.get() != '0':
        textarea.insert(END, f"\nFrooti\t\t{frooti_entry.get()}Ltr\t\t{frootiprice}")
    if cocacola_entry.get() != '0':
        textarea.insert(END, f"\nCoca Cola\t\t{cocacola_entry.get()}Kg\t\t{cocacolaprice}")
    textarea.insert(END, "\n--------------------------------------------")
    if cosmetictax_entry.get() != '0':
        textarea.insert(END, f"\nCosmetic Tax (GST) :\t\t{cosmetictax_entry.get()}")
    if Grocerytax_entry.get() != '0':
        textarea.insert(END, f"\nGrocery Tax (GST) :\t\t{Grocerytax_entry.get()}")
    if colddrinktax_entry.get() != '0':
        textarea.insert(END, f"\nCold Drink Tax (GST) :\t\t{colddrinktax_entry.get()}")
    textarea.insert(END, "\n============================================")
    textarea.insert(END, f"\nTotal BILL :\t\t{totalbill}")
    insert_into_database()


def total():
    global soapprice, facecreamprice, hairsprayprice, bodylotionprice, hairgelprice, riceprice, oilprice, daalprice, wheatprice, sugarprice, teaprice
    global maazaprice, pepsiprice, spriteprice, dewprice, frootiprice, cocacolaprice, facewashprice, totalbill
    soapprice = int(bathsoap_entry.get()) * 10
    facecreamprice = int(facecream_entry.get()) * 80
    facewashprice = int(facewash_entry.get()) * 130
    hairsprayprice = int(hairspray_entry.get()) * 190
    bodylotionprice = int(bodylotion_entry.get()) * 220
    hairgelprice = int(hairgel_entry.get()) * 120
    totalcosmeticprice = soapprice + facewashprice + hairsprayprice + facecreamprice + bodylotionprice + hairgelprice
    cosmeticprice_entry.delete(0, END)
    cosmeticprice_entry.insert(0, totalcosmeticprice)
    cosmetictax = round(totalcosmeticprice * 0.1, 2)
    cosmetictax_entry.delete(0, END)
    cosmetictax_entry.insert(0, cosmetictax)
    riceprice = int(rice_entry.get()) * 23
    oilprice = int(oil_entry.get()) * 155
    daalprice = int(Daal_entry.get()) * 130
    wheatprice = int(wheat_entry.get()) * 21
    sugarprice = int(sugar_entry.get()) * 48
    teaprice = int(tea_entry.get()) * 30
    totalgroceryprice = riceprice + oilprice + daalprice + wheatprice + sugarprice + teaprice
    groceryprice_entry.delete(0, END)
    groceryprice_entry.insert(0, totalgroceryprice)
    grocerytax = round(totalgroceryprice * 0.05, 2)
    Grocerytax_entry.delete(0, END)
    Grocerytax_entry.insert(0, grocerytax)
    maazaprice = int(maaza_entry.get()) * 40
    pepsiprice = int(pepsi_entry.get()) * 50
    spriteprice = int(sprite_entry.get()) * 40
    dewprice = int(dew_entry.get()) * 40
    frootiprice = int(frooti_entry.get()) * 80
    cocacolaprice = int(cocacola_entry.get()) * 40
    totalcolddrinkprice = maazaprice + pepsiprice + spriteprice + dewprice + frootiprice + cocacolaprice
    colddrinkprice_entry.delete(0, END)
    colddrinkprice_entry.insert(0, totalcolddrinkprice)
    colddrinktax = round(totalcolddrinkprice * 0.12, 2)
    colddrinktax_entry.delete(0, END)
    colddrinktax_entry.insert(0, colddrinktax)
    totalbill = round(
        totalcosmeticprice + cosmetictax + totalgroceryprice + grocerytax + totalcolddrinkprice + colddrinktax, 2)


# GUI
window = Tk()
window.title("Retail Billing System")
window.geometry('1270x685')
window.resizable(False, False)

label_1 = Label(window, text="Retail Billing System", font=('times new roman', 30, 'bold'), bg='grey20', fg='gold',
                bd=12)
label_1.pack(fill='both')

billnumber = load_last_bill_number()

# CUSTOMER DETAILS

cd_frame = LabelFrame(window, text="Customer's Details", font=('times new roman', 15, 'bold'), fg="gold", bd=8,
                      bg="grey20")
cd_frame.pack(fill="both")
name_label = Label(cd_frame, text="Name", font=('times new roman', 15, 'bold'), fg="white", bg="grey20")
name_label.grid(row=0, column=0, padx=20)
name_entry = Entry(cd_frame, font=("arial", 15), bd=7, width=18)
name_entry.grid(row=0, column=1, padx=8)

phone_label = Label(cd_frame, text="Phone No.", font=('times new roman', 15, 'bold'), fg="white", bg="grey20")
phone_label.grid(row=0, column=2, padx=20)
phone_entry = Entry(cd_frame, font=("arial", 15), bd=7, width=18)
phone_entry.grid(row=0, column=3, padx=8)

billnumber_label = Label(cd_frame, text="Bill No.", font=('times new roman', 15, 'bold'), fg="white", bg="grey20")
billnumber_label.grid(row=0, column=4, padx=20)
billnumber_entry = Entry(cd_frame, font=("arial", 15), bd=7, width=18)
billnumber_entry.insert(0, str(billnumber))
billnumber_entry.grid(row=0, column=5, padx=8)

# PRODUCT FRAME

product_frame = LabelFrame(window)
product_frame.pack(pady=10, fill="both")

# Cosmetics frame

cosmetic_frame = LabelFrame(product_frame, text="Cosmetics(in quantity)", font=('times new roman', 15, 'bold'),
                            fg="gold", bd=8, bg="grey20")
cosmetic_frame.grid(row=0, column=0)

bathsoap_label = Label(cosmetic_frame, text="Bath Soap\n(10 Rs.)", font=('times new roman', 13, 'bold'), fg="white",
                       bg="grey20")
bathsoap_label.grid(row=0, column=0, padx=20)
bathsoap_entry = Entry(cosmetic_frame, font=("arial", 15), bd=5, width=10)
bathsoap_entry.grid(row=0, column=1, padx=8, pady=5)
bathsoap_entry.insert(0, 0)

facecream_label = Label(cosmetic_frame, text="Face Cream\n(80 Rs.)", font=('times new roman', 13, 'bold'), fg="white",
                        bg="grey20")
facecream_label.grid(row=1, column=0, padx=20)
facecream_entry = Entry(cosmetic_frame, font=("arial", 15), bd=5, width=10)
facecream_entry.grid(row=1, column=1, padx=8, pady=5)
facecream_entry.insert(0, 0)

facewash_label = Label(cosmetic_frame, text="Face wash\n(130 Rs.)", font=('times new roman', 13, 'bold'), fg="white",
                       bg="grey20")
facewash_label.grid(row=2, column=0, padx=20)
facewash_entry = Entry(cosmetic_frame, font=("arial", 15), bd=5, width=10)
facewash_entry.grid(row=2, column=1, padx=8, pady=5)
facewash_entry.insert(0, 0)

hairspray_label = Label(cosmetic_frame, text="Hair Spray\n(190 Rs.)", font=('times new roman', 13, 'bold'), fg="white",
                        bg="grey20")
hairspray_label.grid(row=3, column=0, padx=20)
hairspray_entry = Entry(cosmetic_frame, font=("arial", 15), bd=5, width=10)
hairspray_entry.grid(row=3, column=1, padx=8, pady=5)
hairspray_entry.insert(0, 0)

hairgel_label = Label(cosmetic_frame, text="Hair Gel\n(120 Rs.)", font=('times new roman', 13, 'bold'), fg="white",
                      bg="grey20")
hairgel_label.grid(row=4, column=0, padx=20)
hairgel_entry = Entry(cosmetic_frame, font=("arial", 15), bd=5, width=10)
hairgel_entry.grid(row=4, column=1, padx=8, pady=5)
hairgel_entry.insert(0, 0)

bodylotion_label = Label(cosmetic_frame, text="Body Lotion\n(220 Rs.)", font=('times new roman', 13, 'bold'),
                         fg="white", bg="grey20")
bodylotion_label.grid(row=5, column=0, padx=20)
bodylotion_entry = Entry(cosmetic_frame, font=("arial", 15), bd=5, width=10)
bodylotion_entry.grid(row=5, column=1, padx=8, pady=5)
bodylotion_entry.insert(0, 0)

# Grocery frame

grocery_frame = LabelFrame(product_frame, text="Groceries(in Kg)", font=('times new roman', 15, 'bold'), fg="gold",
                           bd=8, bg="grey20")
grocery_frame.grid(row=0, column=1, padx=5)

rice_label = Label(grocery_frame, text="Rice\n(23 Rs.)", font=('times new roman', 13, 'bold'), fg="white", bg="grey20")
rice_label.grid(row=0, column=0, padx=20)
rice_entry = Entry(grocery_frame, font=("arial", 15), bd=5, width=10)
rice_entry.grid(row=0, column=1, padx=8, pady=5)
rice_entry.insert(0, 0)

oil_label = Label(grocery_frame, text="Oil\n(155 Rs.)", font=('times new roman', 13, 'bold'), fg="white", bg="grey20")
oil_label.grid(row=1, column=0, padx=20)
oil_entry = Entry(grocery_frame, font=("arial", 15), bd=5, width=10)
oil_entry.grid(row=1, column=1, padx=8, pady=5)
oil_entry.insert(0, 0)

Daal_label = Label(grocery_frame, text="Daal\n(130 Rs.)", font=('times new roman', 13, 'bold'), fg="white", bg="grey20")
Daal_label.grid(row=2, column=0, padx=20)
Daal_entry = Entry(grocery_frame, font=("arial", 15), bd=5, width=10)
Daal_entry.grid(row=2, column=1, padx=8, pady=5)
Daal_entry.insert(0, 0)

wheat_label = Label(grocery_frame, text="Wheat\n(21 Rs.)", font=('times new roman', 13, 'bold'), fg="white",
                    bg="grey20")
wheat_label.grid(row=3, column=0, padx=20)
wheat_entry = Entry(grocery_frame, font=("arial", 15), bd=5, width=10)
wheat_entry.grid(row=3, column=1, padx=8, pady=5)
wheat_entry.insert(0, 0)

sugar_label = Label(grocery_frame, text="Sugar\n(48 Rs.)", font=('times new roman', 13, 'bold'), fg="white",
                    bg="grey20")
sugar_label.grid(row=4, column=0, padx=20)
sugar_entry = Entry(grocery_frame, font=("arial", 15), bd=5, width=10)
sugar_entry.grid(row=4, column=1, padx=8, pady=5)
sugar_entry.insert(0, 0)

tea_label = Label(grocery_frame, text="Tea\n(30 Rs.)", font=('times new roman', 13, 'bold'), fg="white", bg="grey20")
tea_label.grid(row=5, column=0, padx=20)
tea_entry = Entry(grocery_frame, font=("arial", 15), bd=5, width=10)
tea_entry.grid(row=5, column=1, padx=8, pady=5)
tea_entry.insert(0, 0)

# Cold Drink Frame

colddrink_frame = LabelFrame(product_frame, text="Cold Drinks (in quantity)", font=('times new roman', 15, 'bold'),
                             fg="gold", bd=8, bg="grey20")
colddrink_frame.grid(row=0, column=2)

maaza_label = Label(colddrink_frame, text="Maaza\n(40 Rs.)", font=('times new roman', 13, 'bold'), fg="white",
                    bg="grey20")
maaza_label.grid(row=0, column=0, padx=20)
maaza_entry = Entry(colddrink_frame, font=("arial", 15), bd=5, width=10)
maaza_entry.grid(row=0, column=1, padx=8, pady=5)
maaza_entry.insert(0, 0)

pepsi_label = Label(colddrink_frame, text="Pepsi\n(50 Rs.)", font=('times new roman', 13, 'bold'), fg="white",
                    bg="grey20")
pepsi_label.grid(row=1, column=0, padx=20)
pepsi_entry = Entry(colddrink_frame, font=("arial", 15), bd=5, width=10)
pepsi_entry.grid(row=1, column=1, padx=8, pady=5)
pepsi_entry.insert(0, 0)

sprite_label = Label(colddrink_frame, text="Sprite\n(40 Rs.)", font=('times new roman', 13, 'bold'), fg="white",
                     bg="grey20")
sprite_label.grid(row=2, column=0, padx=20)
sprite_entry = Entry(colddrink_frame, font=("arial", 15), bd=5, width=10)
sprite_entry.grid(row=2, column=1, padx=8, pady=5)
sprite_entry.insert(0, 0)

dew_label = Label(colddrink_frame, text="Dew\n(40 Rs.)", font=('times new roman', 13, 'bold'), fg="white", bg="grey20")
dew_label.grid(row=3, column=0, padx=20)
dew_entry = Entry(colddrink_frame, font=("arial", 15), bd=5, width=10)
dew_entry.grid(row=3, column=1, padx=8, pady=5)
dew_entry.insert(0, 0)

frooti_label = Label(colddrink_frame, text="Frooti\n(80 Rs.)", font=('times new roman', 13, 'bold'), fg="white",
                     bg="grey20")
frooti_label.grid(row=4, column=0, padx=20)
frooti_entry = Entry(colddrink_frame, font=("arial", 15), bd=5, width=10)
frooti_entry.grid(row=4, column=1, padx=8, pady=5)
frooti_entry.insert(0, 0)

cocacola_label = Label(colddrink_frame, text="Coca Cola\n(40 Rs.)", font=('times new roman', 13, 'bold'), fg="white",
                       bg="grey20")
cocacola_label.grid(row=5, column=0, padx=20)
cocacola_entry = Entry(colddrink_frame, font=("arial", 15), bd=5, width=10)
cocacola_entry.grid(row=5, column=1, padx=8, pady=5)
cocacola_entry.insert(0, 0)

# BILL AREA FRAME

bill_frame = LabelFrame(product_frame, bd=7)
bill_frame.grid(row=0, column=3, padx=5)

billarea_label = Label(bill_frame, text="Bill Area", font=('times new roman', 15, 'bold'))
billarea_label.pack()

scrollbar = Scrollbar(bill_frame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill='both')

textarea = Text(bill_frame, height=18, width=45, yscrollcommand=scrollbar.set)
textarea.pack()

scrollbar.config(command=textarea.yview)

# BILL MENU FRAME

billmenu_frame = LabelFrame(window, text="Bill Menu", font=('times new roman', 15, 'bold'), fg="gold", bd=8,
                            bg="grey20")
billmenu_frame.pack(fill="both")

cosmeticprice_label = Label(billmenu_frame, text="Cosmetic Price", font=('times new roman', 15, 'bold'), fg="white",
                            bg="grey20")
cosmeticprice_label.grid(row=0, column=0, padx=20)
cosmeticprice_entry = Entry(billmenu_frame, font=("arial", 15), bd=5, width=10)
cosmeticprice_entry.grid(row=0, column=1, padx=8, pady=5)

groceryprice_label = Label(billmenu_frame, text="Grocery Price", font=('times new roman', 15, 'bold'), fg="white",
                           bg="grey20")
groceryprice_label.grid(row=1, column=0, padx=20)
groceryprice_entry = Entry(billmenu_frame, font=("arial", 15), bd=5, width=10)
groceryprice_entry.grid(row=1, column=1, padx=8, pady=5)

colddrinkprice_label = Label(billmenu_frame, text="Cold Drink Price", font=('times new roman', 15, 'bold'), fg="white",
                             bg="grey20")
colddrinkprice_label.grid(row=2, column=0, padx=20)
colddrinkprice_entry = Entry(billmenu_frame, font=("arial", 15), bd=5, width=10)
colddrinkprice_entry.grid(row=2, column=1, padx=8, pady=5)

cosmetictax_label = Label(billmenu_frame, text="Cosmetic Tax (GST)\n(10%)", font=('times new roman', 13, 'bold'),
                          fg="white",
                          bg="grey20")
cosmetictax_label.grid(row=0, column=2, padx=20)
cosmetictax_entry = Entry(billmenu_frame, font=("arial", 15), bd=5, width=10)
cosmetictax_entry.grid(row=0, column=3, padx=8, pady=5)

Grocerytax_label = Label(billmenu_frame, text="Grocery Tax (GST)\n(5%)", font=('times new roman', 13, 'bold'),
                         fg="white", bg="grey20")
Grocerytax_label.grid(row=1, column=2, padx=20)
Grocerytax_entry = Entry(billmenu_frame, font=("arial", 15), bd=5, width=10)
Grocerytax_entry.grid(row=1, column=3, padx=8, pady=5)

colddrinktax_label = Label(billmenu_frame, text="Cold Drink Tax (GST)\n(12%)", font=('times new roman', 13, 'bold'),
                           fg="white", bg="grey20")
colddrinktax_label.grid(row=2, column=2, padx=20)
colddrinktax_entry = Entry(billmenu_frame, font=("arial", 15), bd=5, width=10)
colddrinktax_entry.grid(row=2, column=3, padx=8, pady=5)

# BUTTONS

total_button = Button(billmenu_frame, text="TOTAL", font=('times new roman', 15, 'bold'), bd=8, bg="grey20", fg="white",
                      width=8, command=total)
total_button.grid(row=1, column=4, padx=11, pady=5)
bill_button = Button(billmenu_frame, text="Bill", font=('times new roman', 15, 'bold'), bd=8, bg="grey20", fg="white",
                     width=8, command=billfunction)
bill_button.grid(row=1, column=5, padx=11, pady=5)
print_button = Button(billmenu_frame, text="PRINT", font=('times new roman', 15, 'bold'), bd=8, bg="grey20", fg="white",
                      width=8, command=print)
print_button.grid(row=1, column=6, padx=11, pady=5)
clear_button = Button(billmenu_frame, text="CLEAR", font=('times new roman', 15, 'bold'), bd=8, bg="grey20", fg="white",
                      width=8, command=clear_and_billnumber)
clear_button.grid(row=1, column=7, padx=11, pady=5)

window.protocol("WM_DELETE_WINDOW", lambda: [conn.close(), window.destroy()])

window.mainloop()
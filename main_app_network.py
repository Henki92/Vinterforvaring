# Use Tkinter for python 2, tkinter for python 3

from textwrap import wrap

import os
from reportlab.pdfgen import canvas
from reportlab.platypus import Table
from reportlab.lib.units import cm
import time
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfbase.pdfmetrics import stringWidth
from tkinter import *



def print_function(inputData):
    filepath = '//kontoret/delad_mapp/Automower/'
    os.system("TASKKILL /F /IM AcroRD32.exe")
    number = 1
    for file in os.listdir(filepath):
        if file.endswith('.pdf'):
            number = int(file[0:3]) + 1
    number = str(number).zfill(3)
    try:
        number = number + inputData[3].split()[0]
    except IndexError:
        pass
    update_recipt(number, inputData, filepath)
    time.sleep(1)
    os.listdir(filepath)
    os.startfile(filepath.replace('/', '\\') + number + ".pdf")


def update_recipt(number, inputData, filepath):
    widthA4, heightA4 = A4
    c = canvas.Canvas(filepath + number + ".pdf", pagesize=A4)

    # Rubrik kvitto
    c.setFont('Helvetica', 20)
    c.setLineWidth(.8)
    str1 = 'Mullhyttans Cykel & Såg Service AB'
    str1Len = stringWidth(str1, 'Helvetica', 20)
    c.drawString(widthA4 / 2 - str1Len / 2, heightA4 * 9.2 / 10, str1)

    c.setLineWidth(.3)
    c.setFont('Times-Roman', 18)
    str1 = 'Automower vinterförvaring'
    str1Len = stringWidth(str1, 'Helvetica', 18)
    c.drawString(widthA4 / 2 - str1Len / 2, heightA4 * 8.9 / 10, str1)

    str1 = 'OBS! Detta är en värdehandling!'
    str1Len = stringWidth(str1, 'Helvetica', 18)
    c.drawString(widthA4 / 2 - str1Len / 2, heightA4 * 8.6 / 10, str1)

    str1 = "Löpnummer: " + number[0:3]
    str1Len = stringWidth(str1, 'Helvetica', 18)
    c.drawString(widthA4 / 2 - str1Len / 2, heightA4 * 8.1 / 10, str1)

    #datum
    c.setFont('Times-Roman', 12)
    str1 = "Datum: {}".format(time.strftime("%Y-%m-%d"))
    str1Len = stringWidth(str1, 'Helvetica', 12)
    c.drawString(widthA4 / 2 - str1Len / 2, heightA4 * 8.4 / 10, str1)

    c.setFont('Times-Roman', 15)
    t = c.beginText()
    t.setTextOrigin(2.5 * cm, heightA4 * 7.5 / 10)

    t.textLines('Serienummer: ' + inputData[0])
    t.textLines('Modell: ' + inputData[1])
    t.textLines('Pinkod: ' + inputData[2])
    t.textLines('Namn: ' + inputData[3])
    t.textLines('Adress: ' + inputData[4])
    t.textLines('Telefon: ' + inputData[5])
    t.textLines('E-post: ' + inputData[6])
    text = 'Arbete utöver service: ' + inputData[7]
    wraped_text = "\n".join(wrap(text, 80))
    t.textLines(wraped_text)

    c.drawText(t)

    c.setFont('Helvetica', 15)
    t = c.beginText()
    t.setTextOrigin(2.5 * cm, heightA4 * 4.5 / 10)
    t.textLines( 'Kontakta oss när det närmar sig utlämning: \n E-post: tomasmullhyttan@telia.com \n SMS: 0703 - 53 92 73 \n Telefon: 0585-40338' )
    c.drawText(t)



    # Under text
    data = [['', 'Mullhyttans Cykel & Såg', '', ''],
            ['Org.nr:', '556229-3745', '', ''],
            ['Address:', 'Selhagsvägen 3', '', ''],
            ['', '716 94 Mullhyttan', '', ''],
            ['Telefon:', '0585-40338', '', ''],
            ['Email:', 'mullhyttanscykel@telia.com', '', ''],
            ['Facebook:', 'https://www.facebook.com/mullhyttans123/', '', ''],
            ['Blocket:', 'https://www.blocket.se/mullhyttanscykel-sagservice', '', '']
            ]

    width = 6 * cm
    height = 4 * cm
    d = Table(data, style=[  # ('BOX',(0,0),(-1,-1),0.5,colors.black),
        # ('GRID',(0,0),(-1,-1),0.25,colors.black),
        # Artikelnummer kolumnen
        ('RIGHTPADDING', (0, 0), (0, -1), 15),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        # Beskrivning kolumnen
        ('RIGHTPADDING', (1, 0), (1, -1), 50),
        ('ALIGN', (1, 0), (1, -1), 'LEFT'),
        # Antal kolumnen
        ('ALIGN', (2, 0), (2, -1), 'LEFT'),
        # Pris kolumnen
        ('ALIGN', (3, 0), (3, -1), 'LEFT'),
    ])

    d.wrapOn(c, width, height)
    d.drawOn(c, widthA4 * 1.5 / 10, heightA4 * 1.5 / 10)

    c.save()


# Centers all pop ups to center of screen
def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))


master = Tk()
master.geometry("700x450")
master.title("Vinterförvaring")
center(master)
labelwidth = 25
labelfontsize = 14
entrywidth = 60
Label(master, text="Serienummer: ", width=labelwidth, font=("Courier", labelfontsize)).grid(row=0)
Label(master, text="Modell: ", width=labelwidth, font=("Courier", labelfontsize)).grid(row=1)
Label(master, text="Pinkod: ", width=labelwidth, font=("Courier", labelfontsize)).grid(row=2)
Label(master, text="Namn: ", width=labelwidth, font=("Courier", labelfontsize)).grid(row=3)
Label(master, text="Adress: ", width=labelwidth, font=("Courier", labelfontsize)).grid(row=4)
Label(master, text="Telefon: ", width=labelwidth, font=("Courier", labelfontsize)).grid(row=5)
Label(master, text="E-post: ", width=labelwidth, font=("Courier", labelfontsize)).grid(row=6)
Label(master, text="Arbete utöver service: ", width=labelwidth, font=("Courier", labelfontsize)).grid(row=7)
Label(master, text="      ", width=labelwidth, font=("Courier", labelfontsize)).grid(row=8)

e0 = Entry(master, width=entrywidth)
e1 = Entry(master, width=entrywidth)
e2 = Entry(master, width=entrywidth)
e3 = Entry(master, width=entrywidth)
e4 = Entry(master, width=entrywidth)
e5 = Entry(master, width=entrywidth)
e6 = Entry(master, width=entrywidth)
e7 = Entry(master, width=entrywidth)
b0 = Button(master, width=entrywidth, text="Skriv ut")

e0.grid(row=0, column=1)
e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)
e5.grid(row=5, column=1)
e6.grid(row=6, column=1)
e7.grid(row=7, column=1)
b0.grid(row=8, column=1)


def go_to_next_entry(event, entry_list, this_index):
    if this_index == 8 and event:
        input_data = [""]*8
        for idx1, entry1 in enumerate(entry_list[0:-1]):
            input_data[idx1] = entry1.get()
            entry1.delete(0, 'end')
        print_function(input_data)
        go_to_next_entry(0, entries, 8)
    next_index = (this_index + 1) % len(entry_list)
    entry_list[next_index].focus_set()


entries = [child for child in master.winfo_children() if isinstance(child, Entry) or isinstance(child, Button)]
for idx, entry in enumerate(entries):
    entry.bind('<Return>', lambda e, idx=idx: go_to_next_entry(e, entries, idx))


def button_command():
    go_to_next_entry(1, entries, 8)


b0.configure(command=button_command)
go_to_next_entry(0, entries, 8)
mainloop()



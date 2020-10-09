# Use Tkinter for python 2, tkinter for python 3
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from textwrap import wrap

import os
from reportlab.pdfgen import canvas
from reportlab.platypus import Table
from reportlab.lib.units import cm
import time
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfbase.pdfmetrics import stringWidth


def print_function(inputData):
    os.system("TASKKILL /F /IM AcroRD32.exe")
    number = 1
    for file in os.listdir():
        if file.endswith('.pdf'):
            number = int(file[0:3]) + 1
    number = str(number).zfill(3)
    try:
        number = number + inputData[3].split()[0]
    except IndexError:
        pass
    update_recipt(number, inputData)
    os.startfile(number + ".pdf")


def update_recipt(number, inputData):
    widthA4, heightA4 = A4
    c = canvas.Canvas(number + ".pdf", pagesize=A4)

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

    c.setFont('Times-Roman', 14)
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

    # Artiklar osv
    data = [['Serienummer: ' + inputData[0]],
            ['Modell: ' + inputData[1]],
            ['Pinkod: ' + inputData[2]],
            ['Namn: ' + inputData[3]],
            ['Adress: ' + inputData[4]],
            ['Telefon: ' + inputData[5]],
            ['E-post: ' + inputData[6]],
            ['Arbete utöver service: ' + inputData[7]]
            ]

    f = Table(data, colWidths=(15 * cm),
              style=[('FONTSIZE', (0, 0), (-1, -1), 16),
                     ('LINEBELOW', (0, 0), (-1, -1), 2, colors.black),
                     ('BOTTOMPADDING', (0, 0), (-1, -1), 10)
                     ]
              )
    width = 6 * cm
    height = 4 * cm
    #f.wrapOn(c, width, height)
    #f.drawOn(c, 2.5 * cm, heightA4 * 5.5 / 10)

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

Window.clearcolor = (0.5, 0.5, 0.5, 1)
Window.size = (700, 700)


class User(Screen):
    buttonSkrivut = ObjectProperty()

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        Window.bind(on_key_down=self._on_keyboard_down)

    def _on_keyboard_down(self, instance, keyboard, keycode, text, modifiers):
        if self.buttonSkrivut.focus and keycode == 40:  # 40 - Enter key pressed
            self.abc()

    def abc(self):
        data = ["", "", "", "", "", "", "", ""]
        data[0] = self.textSerienummer.text
        data[1] = self.textModell.text
        data[2] = self.textPinkod.text
        data[3] = self.textNamn.text
        data[4] = self.textAdress.text
        data[5] = self.textTelefon.text
        data[6] = self.textAdress.text
        data[7] = self.textAnnat.text

        print_function(data)
        print('Printing receipt')


class Test(App):

    def build(self):
        return self.root


if __name__ == '__main__':
    Test().run()



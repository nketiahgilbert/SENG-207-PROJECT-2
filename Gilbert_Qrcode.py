#Nketiah Gilbert
#10978665
#BMEN
import PySimpleGUI as sg
import qrcode

sg.theme("One Dark Pro")
font = ('JetBrains Mono',20)

qr_image= [sg.Image('',key ='-QrCode-')]

layout = [
     [sg.Text('Input Your Text To Generate QrCode')],
     [sg.Input('',key='-Text-')],
     [sg.Button('Create', key='-Create-'), sg.Button('Exit')],
     [sg.Column([qr_image], justification='center')]
             
]
 
window = sg.Window(" QR CODE GENERATOR", layout,font=font)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event =='-Create-':
        text = values['-Text-']
        if text:
            img = qrcode.make(text)
            img.save('qr.png')
            window['-QrCode-'].update('qr.png')

window.close()
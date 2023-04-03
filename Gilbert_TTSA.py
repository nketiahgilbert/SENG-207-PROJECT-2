#Nketiah Gilbert
#10978665
#BMEN
import PySimpleGUI as sg
import pyttsx3

engine= pyttsx3.init()
VoiceEngine= engine.getProperty('voices')



layout = [  [sg.Text('Enter text to speak:',text_color='black',background_color='#14445a',)],
    [sg.InputText(key='user input',background_color='#416577'),sg.Button('Speak',button_color='#517381')],  
    [sg.Text('Select the type of voice:',text_color='black',background_color='#14445a'),
    [ sg.Text('Adjust Speed'),sg.Slider(range=(130, 400), 
                orientation='h', size=(50, 10), enable_events=True, key = '-SPEED-',
                 default_value= 130) ],
    sg.Radio('Male', 'RADIO1', default=True, key='male',
background_color='#517381'),sg.Radio('Female', 'RADIO1', key='female',background_color='#517381')],
     
]

window = sg.Window('Text To Speech App', layout,background_color='#14445a')

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Speak':
        tts=pyttsx3.init()
        rate= values['-SPEED-']
        tts.setProperty('rate',rate)
        text = values['user input']
        if values['male']:
            engine.setProperty('voice', VoiceEngine[0].id)
        elif values['female']:
           engine.setProperty('voice', VoiceEngine[1].id) 
    
        engine.say(text)
        engine.runAndWait()

window.close()
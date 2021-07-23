import wikipedia
import PySimpleGUI as sg
import wolframalpha
client = wolframalpha.Client("2X5P5W-5V72QLVEKH")


sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Ask me anything--'), sg.InputText()],
          [sg.Button('Ok'), sg.Button('Cancel')]]

# Create the Window
window = sg.Window('Assistant', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    try:
        wiki_res = wikipedia.summary(values[0], sentences=1)
        wolf_res = next(client.query(values[0]).results).text
        sg.PopupNonBlocking(f"Wikipedia: {wiki_res}\n\nWolfram: {wolf_res}")

    except wikipedia.exceptions.PageError:
        res = client.query(values[0])
        wolf_res = next(client.query(values[0]).results).text
        sg.PopupNonBlocking(f"Wolfram: {wolf_res}")

    except wikipedia.exceptions.DisambiguationError:
        res = client.query(values[0])
        wolf_res = next(client.query(values[0]).results).text
        sg.PopupNonBlocking(f"Wolfram: {wolf_res}")

    except:
        wiki_res = wikipedia.summary(values[0], sentences=1)
        sg.PopupNonBlocking(f"Wikipedia: {wiki_res}")

window.close()

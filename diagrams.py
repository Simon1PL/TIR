import PySimpleGUI as sg
from tinydb import TinyDB, Query
import matplotlib.pyplot as plt

db = TinyDB('solar_database.json')
sg.theme('Dark Red')
layout = [[sg.Text('Date Chooser Test Harness', key='-TXT-')],
          [sg.Button('display diagram'), sg.Exit()]]

window = sg.Window('window', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'display diagram':
        date = sg.popup_get_date()
        if date[0] > 9:
            date_s = date[2].__str__() + '-' + date[0].__str__() + '-' + date[1].__str__()
        else:
            date_s = date[2].__str__() + '-0' + date[0].__str__() + '-' + date[1].__str__()

        print(date_s)
        measurements = Query()
        result = db.search(measurements.date == date_s)
        plot_data = []
        for r in result:
            if float(r["G"]) != 0:
                plot_data.append(float(r['I']) * float(r["V"]) / (float(r["G"]) * float(r['S'])))
        plt.plot(plot_data)
        plt.savefig('diagram.png')
        plt.show()

window.close()

import PySimpleGUI as sg
#from TicTacToe import board 

playerChar = 'X'

sg.theme('Dark Green 5')
layout = [[sg.Button(' ', key='UpperLeft', size=(4,2)), sg.Button(' ', key='UpperMiddle', size=(4,2)), sg.Button(' ', key='UpperRight', size=(4,2))],
            [sg.Button(' ', key='MiddleLeft', size=(4,2)), sg.Button(' ', key='MiddleMiddle', size=(4,2)), sg.Button(' ', key='MiddleRight', size=(4,2))],
            [sg.Button(' ', key='LowerLeft', size=(4,2)), sg.Button(' ', key='LowerMiddle', size=(4,2)), sg.Button(' ', key='LowerRight', size=(4,2))]
                        ]
window = sg.Window('Tic-Tac-Toe', layout, finalize=True)

while True: #event loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Close":
        break
    elif event == 'UpperLeft':
        window['UpperLeft'].update(playerChar)
    elif event == 'UpperMiddle':
        window['UpperMiddle'].update(playerChar)
    elif event == 'UpperRight':
        window['UpperRight'].update(playerChar)
    elif event == 'MiddleLeft':
        window['MiddleLeft'].update(playerChar)
    elif event == 'MiddleMiddle':
        window['MiddleMiddle'].update(playerChar)
    elif event == 'MiddleRight':
        window['MiddleRight'].update(playerChar)
    elif event == 'LowerLeft':
        window['LowerLeft'].update(playerChar)
    elif event == 'LowerMiddle':
        window['LowerMiddle'].update(playerChar)
    elif event == 'LowerRight':
        window['LowerRight'].update(playerChar)
        

import sys,random,time
import os
import PySimpleGUI as sg
import sys
import pyautogui
import pytesseract as tess
from PIL import Image
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#import ventanasSG as vsg
#from apscheduler.schedulers.background import BackgroundScheduler

class Image_to_text:
    def __init__(self):
        pass

    def img_text(self):
        my_img = Image.open('D:\\Usuario\\esc\\ImageToText\\screenshot.png')
        return tess.image_to_string(my_img)

    def capture(self):
        points = {}
        screensize = sg.Window.get_screen_size()
        window = sg.Window('',[[sg.Graph(screensize, (0, screensize[1]), (screensize[0], 0),enable_events=True, key='-G-', background_color='lightblue', k = '-G-')]],
                           location=(0, 0),
                           keep_on_top=True,
                           element_padding=(0, 0),
                           margins=(0, 0),
                           right_click_menu=[[''], ['Controls', 'Exit']],
                           grab_anywhere=False,
                           no_titlebar=True,
                           finalize=True,
                           alpha_channel=0.2)

        for i in ['O', 'W', 'H']:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Exit'):
                break
            if event == '-G-':
                window['-G-'].draw_point((values['-G-']), size=6)
                points[i] = values['-G-']

        window.close()
        return points

    def show(self):
        window = sg.Window('Image To Text',
                           layout = [[sg.Multiline(size=(60, 15), k='-M-')], [sg.Button('CLEAR', k='-CLS-')],[sg.Button('CAPTURE', k='-CP-')]],
                           finalize = True)

        while True:
            event,values = window.read(timeout=1000)

            if event in (sg.WIN_CLOSED, 'Exit'):
                break
            for i in ['-CLS-','-CP-']:
                window[i].expand(expand_x = True ,expand_y = False ,expand_row = True)

            if event == '-CLS-':
                pass
            elif event == '-CP-':
                window.hide()
                points = self.capture()
                pyautogui.screenshot('screenshot.png', region=(points['O'][0], points['O'][1],
                                                               points['W'][0]-points['O'][0],
                                                               points['H'][1]-points['O'][1]))
                window['-M-'].update(self.img_text())
                window.UnHide()

        window.close()


if __name__ == '__main__':
    sg.theme('LightGray2')
    Image_to_text().show()


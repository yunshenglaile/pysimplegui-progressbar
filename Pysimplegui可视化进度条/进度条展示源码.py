# import PySimpleGUI as sg
# import time
# mylist = [1,2,3,4,5,6,7,8]
# for i, item in enumerate(mylist):
#   sg.one_line_progress_meter( 'This is my progress meter!' , i+1, len(mylist),  '-key-' )
#   time.sleep(1)

import PySimpleGUI as sg
import time
mylist = [1,2,3,4,5,6,7,8]
progressbar = [ [sg.ProgressBar(len(mylist), orientation= 'h' , size=(51, 10), key= '-progressbar-' )]]
outputwin = [ [sg.Output(size=(78,20))]]
layout = [ [sg.Frame( 'Progress' ,layout= progressbar)], [sg.Frame('Output' , layout = outputwin)], [sg.Submit( 'Start',key='-start-' ),sg.Cancel('Cancel',key='-cancel-')]]
window = sg.Window( 'Custom Progress Meter' , layout)
progress_bar = window[ '-progressbar-' ]
while True:
  event, values = window.read(timeout=10)
  if event == '-cancel-' or event is None:
    break
  elif event == '-start-':
    for i,item in enumerate(mylist):
      print(item)
      time.sleep(1)
      progress_bar.UpdateBar(i + 1)
window.close()
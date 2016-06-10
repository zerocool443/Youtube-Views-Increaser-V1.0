import webbrowser
import os
import time



url =  input("Enter the video url ")

refreshrate = input("Enter the refresh rate in seconds")

browserr = input("Enter your default browser name")


def letsdoit():
    os.system("TASKKILL /F /IM "+browserr+".exe")
    webbrowser.open(url)
    time.sleep(int(refreshrate))

views = input("How many views you want")
for i in range(int(views)+1):
    letsdoit()

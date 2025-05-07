import pygetwindow as gw

class Utilities:
    def __init__(self):
        pass

    def detectWaframeWindow(self):
        for win in gw.getAllTitles():
            if win == "Warframe":
                print("warframe está aberto")

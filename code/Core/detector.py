import cv2
import mss
import numpy as np
import easyocr
import time
class Detector:

    def __init__(self):
        pass

    def detectRelicScreen(self):
        #Instead of looking the whole screen for "Void Fissure/Relic", I can look the left upper half of the screen for that phrase
            #It goes from 0 to half of the screen horizontaly and vertically and then to the middle
            #And finally take the screenshot, it will shorten the processing time
        #This method will ONLY run when warframe has been detected by the application
        # 1 - Use openCv to find "Void Fissure/Relics" withing a screenshot then,
        # 2 - Use easyOcr to extract the part prime name to search it in warframe market
            #The problem, most of the time easyOcr doesnt extract text properly... some key words are missing, maybe i'll have to use something else
        pass

    def detectPartPrime(self):
        pass

  

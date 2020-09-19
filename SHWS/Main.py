import os
from PIL import Image
import oob as ob
import random

BACKGROUND = Image.open(".\\page.jpg")

minLeft = 160
minTop = 205
maxLeft = 1200

# Think 1: After each WORD we leave some blank space
currentX = minLeft
currentY = minTop
count = 1
currentLinePix = 0
lineNumber = 0

para = input("Holy fuck dude, Cant you just do your homework on your own once? gahh Just write you txt file name you dumb idiotic kid....\n")
txtFile = open(f".\\inputs\\{para}.txt", 'r').read().splitlines()

countPage = 0
l = []
first = BACKGROUND

while True:
    
    currentX = minLeft
    currentY = minTop
    currentLinePix = 0
    lineNumber = 0
    count = 0

    for line in txtFile:
        if not line:
            lineNumber += 1
            currentY = minTop + (65 * lineNumber) + (3 * lineNumber)
            currentLinePix += 65
            currentX = 160
            continue
        if lineNumber == 26:
            if count == 0:
                first = BACKGROUND.convert("RGB")
                count += 1
            else:
                l.append(BACKGROUND.convert("RGB"))
            currentX = minLeft
            currentY = minTop
            currentLinePix = 0
            lineNumber = 0
            BACKGROUND = Image.open(".\\page.jpg")
        for word in line:
            for letter in word:
                if letter == " ":
                    rand = random.randint(28, 34)
                    currentX += rand
                    continue
                TEXT = f".\\texts\\{ob.upLow(letter)}\\{letter}.png" # Gets the desired image
                if letter == "a":
                    currentX += 3
                foreground = Image.open(TEXT).resize((55, 60), Image.ANTIALIAS) # Resizes it to the perfect size and loads it
                BACKGROUND.paste(foreground, (currentX, currentY), foreground) # pastes the image! Work on postion of it
                currentX += 47
                currentY = currentY + 3
                if currentY > (221 + currentLinePix):
                    currentY = currentY - 1
                if currentY > (244 + currentLinePix):
                    currentY = currentY - 7
                if currentX > maxLeft:
                    lineNumber += 1
                    currentY = minTop + (65 * lineNumber) + (3 * lineNumber)
                    currentLinePix += 65
                    currentX = 160
                    if lineNumber == 26:
                        if count == 0:
                            first = BACKGROUND.convert("RGB")
                            count += 1
                        else:
                            l.append(BACKGROUND.convert("RGB"))
                        currentX = minLeft
                        currentY = minTop
                        currentLinePix = 0
                        lineNumber = 0
                        BACKGROUND = Image.open(".\\page.jpg")
        lineNumber += 1
        currentY = minTop + (65 * lineNumber) + (3 * lineNumber)
        currentLinePix += 65
        currentX = 160
        if lineNumber == 26:
            if count == 0:
                first = BACKGROUND.convert("RGB")
                count += 1
            else:
                l.append(BACKGROUND.convert("RGB"))
            currentX = minLeft
            currentY = minTop
            currentLinePix = 0
            lineNumber = 0
            BACKGROUND = Image.open(".\\page.jpg")
    break

first.save(r'myImages.pdf', save_all=True, append_images=l)

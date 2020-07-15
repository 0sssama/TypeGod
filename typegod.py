        #############################################
        #                                           #
        #           TypeGod game, by 0ssama         #
        #       Contact: 0ssama@protonmail.com      #
        #                                           #
        #############################################




import os, time, random, sys
from info import texts
from ColorIt import *
from readchar import readkey, key
import threading

os.system('cls' if os.name == 'nt' else 'clear')
initColorIt()

def run():
    print ( color ( " _____  __   __  ____    _____    ____    ___    ____  " , colors.RED ))
    print ( color ( "|_   _| \ \ / / |  _ \  | ____|  / ___|  / _ \  |  _ \ " , colors.RED ))
    print ( color ( "  | |    \ V /  | |_) | |  _|   | |  _  | | | | | | | |" , colors.RED ))
    print ( color ( "  | |     | |   |  __/  | |___  | |_| | | |_| | | |_| |" , colors.RED ))
    print ( color ( "  |_|     |_|   |_|     |_____|  \____|  \___/  |____/ " , colors.RED ))

def countdown(secs):
    while secs!=0:
        print (' >',secs)
        time.sleep(1)
        secs-=1
        print ("\033[A                             \033[A")

def colorize(letters, index):
    letters[index] = background(color(letters[index], (0,0,0) ), colors.WHITE)
    return letters

finished = False

def timer():
    global s
    global m
    s = 0
    m = 0
    while not finished:
        for i in range(60):
            if finished:
                break
            time.sleep(1)
            s+=1
        if s > 59:
            s = 0
            m += 1

run()
time.sleep(0.5)
print (color("\n      =======>", colors.RED), color("practice typing fast and", colors.GREEN), color("<=======\n", colors.RED))
print (color("      ====>", colors.RED), color("improve your typing speed (WPM)", colors.GREEN), color("<===", colors.RED))
time.sleep(0.7)
print ("\n  Are you ready ? (type 'go' to start)")
start = input('>>>> ')
if start.strip().lower() == 'go':
    asciiLetters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890éçè-()=+'\"&.:,;!?/[]}{#@"
    os.system('cls' if os.name == 'nt' else 'clear')
    paragraphOriginal = texts[random.randint(0,(len(texts)-1))]
    paragraphLetters = list(paragraphOriginal)
    userWord = ''
    paragraphWords = paragraphOriginal.split(' ')
    countdown(3)
    crntLetterIndex = 0
    crntWordIndex = 0
    lastLetterIsWrong = False
    nOfWrongLetters = 0
    lettersTyped = 0
    highestWPM = 0
    timer_thread = threading.Thread(target = timer)
    timer_thread.start()
    score_info = open("SCORE")
    highscore = score_info.read()
    if highscore.strip() == '':
        highscore = '0'
    try:
        highscore = float(highscore)
    except:
        highscore = '0'
    score_info.close()
    while not finished:
        seconds = '0'+str(s) if s<10 else str(s)
        minutes = '0'+str(m) if m<10 else str(m)
        secondsInMins = int(int(s) * (10/6))
        if s == 0:
            if m == 0:
                wordPerMinute = 0
            else:
                timeInMinute = float(m)
                wordPerMinute = lettersTyped / (5*timeInMinute)
        else:
            timeInMinute = float(str(m)+'.'+str(secondsInMins))
            wordPerMinute = lettersTyped / (5*timeInMinute)
        if wordPerMinute > highestWPM:
            highestWPM = wordPerMinute
        print ("WPM: {:.2f};\nHIGHEST WPM SCORE: {};\nTIME: {}:{};\n\n".format(wordPerMinute, str(highscore)+' WPM', minutes, seconds))
        paragraphInterface = ''.join(paragraphLetters)
        print (paragraphInterface + '\n')
        print (' >', userWord+'|')
        print ("\n\n  PRESS 'CTRL+C' TO QUIT")
        if crntLetterIndex == len(paragraphOriginal):
            print ('\n' + color('YOU WON!', colors.GREEN))
            print('\n Time elapsed: {}:{};'.format(minutes, seconds))
            print ('\n Highest WPM this round: {:.2f};\n'.format(highestWPM))
            try:
                highscore = float(highscore)
            except:
                open('SCORE', 'w').close()
                infoedit = open('SCORE', 'w')
                infoedit.write('0')
                infoedit.close()
                finished = True
                exit()
            else:
                if highestWPM > highscore:
                    print ('NEW HIGH SCORE! -- saved.\n ')
                    open('SCORE', 'w').close()
                    infoedit = open('SCORE', 'w')
                    infoedit.write(str("{:.2f}".format(highestWPM)))
                    infoedit.close()
                finished = True
                exit()
        keyPressed = readkey()

        if keyPressed in asciiLetters:
            letterIsRight = keyPressed == paragraphOriginal[crntLetterIndex]
            if letterIsRight:
                if lastLetterIsWrong:
                    userWord = userWord + color(keyPressed, colors.RED)
                    lastLetterIsWrong = True
                    nOfWrongLetters += 1
                else:
                    userWord = userWord + keyPressed
                    paragraphLetters = colorize(paragraphLetters, crntLetterIndex)
                    crntLetterIndex += 1
                    lettersTyped += 1
            else:
                userWord = userWord + color(keyPressed, colors.RED)
                lastLetterIsWrong = True
                nOfWrongLetters += 1


        elif keyPressed == key.SPACE:
            if userWord == paragraphWords[crntWordIndex]:
                paragraphLetters = colorize(paragraphLetters, crntLetterIndex)
                crntWordIndex += 1
                crntLetterIndex += 1
                userWord = ''
            else:
                userWord = userWord + ' '
                lastLetterIsWrong = True
                nOfWrongLetters += 1


        elif keyPressed == key.BACKSPACE:
            if userWord == '':
                lastLetterIsWrong = False
                pass
            else:
                if lastLetterIsWrong:
                    if userWord[-1] == ' ':
                        userWord = userWord[:-1]
                        nOfWrongLetters -= 1
                        if nOfWrongLetters == 0:
                            lastLetterIsWrong = False
                    else:
                        userWord = userWord[:-22]
                        nOfWrongLetters -= 1
                        if nOfWrongLetters == 0:
                            lastLetterIsWrong = False
                else:
                    if userWord[-1] == ' ':
                        userWord = userWord[:-1]
                    else:
                        userWord = userWord[:-1]
                        paragraphLetters = list(paragraphOriginal)
                        for i in range(crntLetterIndex-1):
                            paragraphLetters = colorize(paragraphLetters, i)
                        if crntLetterIndex == 0:
                            pass
                        else:
                            crntLetterIndex -= 1

        elif keyPressed == key.CTRL_C:
            finished  = True
            exit()
        else:
            pass
        os.system('cls' if os.name == 'nt' else 'clear')

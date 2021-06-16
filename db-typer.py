import sqlite3
import keyboard
import time

conn = sqlite3.connect('Memo.db')
cursor = conn.cursor()
cursor = conn.execute('SELECT title FROM comhuaweiproviderNotePadbackupnote_items_tb LIMIT 200 OFFSET 108')



def fixNewLine(str):
    newStr = ''

    for i in range(0, len(str)):

        if(i == 0 or i == 1 or i == len(str) - 1 or i == len(str) - 2 or i == len(str) - 3):
            continue

        if str[i] == 'n' and str[i-1] == '\\':
            newStr += '@'
        else:
            if str[i] != '\\':
               newStr += str[i]


    newStr += '$'

    return newStr

def GetRows():

    count = 108

    for row in cursor:
        rowString = fixNewLine(str(row))

        keyboard.write(str(count))
        keyboard.press_and_release('enter')

        time.sleep(1)

        for i in range(0, len(rowString)):
            if rowString[i] == '@':
                keyboard.press_and_release('shift+enter')
            elif rowString[i] == '$':
                keyboard.press_and_release('enter')
            else:
                keyboard.write(rowString[i])

            time.sleep(0.05)



        time.sleep(1)

        count += 1
        print('Finished ' , (count - 1) , ' / 381')

        if(count % 10 == 0):
            keyboard.write('-------------------------------------------')
            keyboard.press_and_release('enter')
            time.sleep(0.5)
        



print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)
GetRows()

print('----[ FINISHED ]----')


#conn.commit()
conn.close()
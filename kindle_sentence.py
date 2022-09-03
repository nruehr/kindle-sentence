# coding=utf-8
import os
import re
import win_unicode_console
import clipboard

# export the sentences from a kindle my clippings text file
# open the textfile, read it and save it as text 
# might have to adjust the drive letter
with open('H:/documents/My Clippings.txt', encoding='utf-8') as notes:
    text = notes.read()

# rearrange the text
text2 = re.sub("- Your Highlight on page .*\n\n", "", text)
text3 = re.sub("==========", "", text2)
# test
# copy the text to the clipboard
clipboard.copy(text3)
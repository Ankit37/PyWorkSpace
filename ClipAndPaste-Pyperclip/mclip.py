#!python3
#mclip.py- A multi-clipboard program
import sys
import pyperclip

Text= {'agree':"""Yes, I agree, sounds fine to me.""",'busy':"""Sorry, I am bit busy. Can we do this later.""",'upsell': """Would you consider making this a monthly donation?"""}

if len(sys.argv)<2:
    print("Usage is mclip.py [keyPhrase] - copy phrase text")
    sys.exit()

keyPhrase=sys.argv[1] #First command line agrument is keyPhrase
if keyPhrase in Text:
    pyperclip.copy(Text[keyPhrase])
print(pyperclip.paste())
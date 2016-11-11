# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.

import urllib.request 
from bs4 import BeautifulSoup 
import sys
from os.path import basename, splitext

def uprint(*objects, sep=' ', end='\n', file=sys.stdout): #function that will help with encoding/decoding
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)
              

url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html' #hardcode the url we want
html = urllib.request.urlopen(url).read() #uses urllib library to fetch the URL given
soup = BeautifulSoup(html, 'lxml') #recode the HTML with HTML parser

soup_string = str(soup)

string1 = soup_string.replace("students", "AMAZING students")
string2 = string1.replace("https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg", "media/angel.jpg")
string3 = string2.replace("logo2.png","media/logo.png")
#make soup a string. string method replace. create a new file f = open('BSI.html,', 'w') f.write(pass new string) f.close() 

f = open('BSI_Admissions.html', 'w')
f.write(string3)
f.close()
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

def uprint(*objects, sep=' ', end='\n', file=sys.stdout): #function that will help with encoding/decoding
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

print ("BSI Admissions - U of M School of Info")
url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html' #hardcode the url we want
html = urllib.request.urlopen(url).read() #uses urllib library to fetch the URL given
soup = BeautifulSoup(html, 'lxml') #recode the HTML with HTML parser

student = [] #create list to hold all the headlines grabbed from website
for story_heading in soup.find_all(class_="story-heading"): #find tags used to identify headlines >>> need anchor tag
    if story_heading.p: 
        student.append(story_heading.a.text.replace("\n", " ").strip()) #if has anchor tag, add to list 
    else:                                                                       #also strip strings and replace new lines and tabs with regular spaces
        student.append(story_heading.contents[0].strip()) 
        
uprint ("bye")


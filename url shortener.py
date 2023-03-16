# pip install pyshorteners
# pip install pyperclip

import pyshorteners
link = input('Enter the url that you want to shorten: ');

def shortenurl(link):
    q = pyshorteners.Shortener()
    print("\n\nThe shortened url is :" + q.tinyurl.short(link))

shortenurl(link)
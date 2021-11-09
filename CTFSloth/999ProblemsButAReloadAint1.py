import sys
import urllib.request

while True:
    page = urllib.request.urlopen("http://ctf.slothparadise.com/about.php").read().decode('utf-8')
    if 'KEY' in page:
        print(page)
        sys.exit()

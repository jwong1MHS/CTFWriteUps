import urllib.request
import sys

page = urllib.request.urlopen('http://ctf.slothparadise.com/walled_garden.php?name=anon').read().decode('utf-8')

while True:
    split1 = page.split("<pre>")
    split2 = split1[1].split("</pre>")
    page = urllib.request.urlopen('http://ctf.slothparadise.com/walled_garden.php?name=anon&captcha=' + split2[0]).read().decode('utf-8')
    if 'KEY' in page:
        print(page)
        sys.exit
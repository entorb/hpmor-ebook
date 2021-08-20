import os
import re
import glob
import requests

from bs4 import BeautifulSoup  # pip install beautifulsoup4

# TODO: fetch original EN HPMOR as well

languages = ('en', 'de')

for lang in languages:
    for dir in (f'html-1-download/{lang}/', f'html-2-chapters-extracted/{lang}/', f'html-3-cleaned/{lang}/', 'output'):
        os.makedirs(dir, exist_ok=True)


def download_file(url: str, filepath: str):
    """download file from url to filepath"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0 ',
    }
    cont = requests.get(url, headers=headers, verify=True).content
    # verify=False -> skip SSL cert verification: CERTIFICATE_VERIFY_FAILED
    with open(filepath, mode='bw') as fh:
        fh.write(cont)


def download_all_chapters():
    """Downloads into html-1-download/<lang>/ only if fileOut does not exist"""
    chapter_last = 122
    for lang in languages:
        if lang == 'en':
            chapter_last = 122
            urlBase = f"http://www.hpmor.com/chapter/<---chapter--->/"
        elif lang == 'de':
            chapter_last = 121
            urlBase = f"https://www.fanfiktion.de/s/60044849000ccc541aef297e/<---chapter--->/"
        for chapter in range(0+1, chapter_last+1):
            fileOut = f"html-1-download/{lang}/%03d.html" % chapter
            if not os.path.exists(fileOut):
                print(f"downloading chapter %03d" % chapter)
                url = urlBase.replace("<---chapter--->", str(chapter))
                download_file(url=url, filepath=fileOut)


def extract_chapter_text():
    """
    extract chapter text from html and writes result into html-2-chapters-extracted/
    2 modifications are done: removal of comments and removal of javascript
    """
    for lang in languages:
        for fileIn in sorted(glob.glob(f"html-1-download/{lang}/*.html")):
            (filePath, fileName) = os.path.split(fileIn)
            fileOut = f"html-2-chapters-extracted/{lang}/{fileName}"
            with open(fileIn, mode='r', encoding='utf-8', newline='\n') as fh:
                cont = fh.read()

            # cleanup comments and scripts
            cont = re.sub('<!--.*?-->', "", cont, flags=re.DOTALL)
            cont = re.sub('<script.*?</script>', "", cont,
                          flags=re.DOTALL | re.IGNORECASE)

            soup = BeautifulSoup(cont, features='html.parser')

            myTitle = ""
            myBody = ""

            if lang == 'de':
                # find chapter name from dropdown
                myElement = soup.find("select", {"id": "kA"})
                myElement = myElement.find("option", {"selected": "selected"})
                myTitle = myElement.text  # chars only, no tags
                del myElement
                # print(myTitle)

                # find body text
                myElement = soup.find("div", {"class": "user-formatted-inner"})
                myBody = myElement.prettify()
                # myBody = myElement.encode()
                # myBody = str(myElement)
                del myElement

            out = f"<h1>{myTitle}</h1>\n{myBody}\n"

            with open(fileOut, mode='w', encoding='utf-8', newline='\n') as fh:
                fh.write(out)


def html_modify():
    print("html_modify")
    html_start = """<!DOCTYPE html>
<html lang="de">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="author" content="Eliezer Yudkowsky" />
<title>Harry Potter und die Methoden des rationalen Denkens</title>
</head>
<body>
"""
    html_end = "</body></html>"

    fhAll = open("output/hpmor-de.html", mode='w',
                 encoding='utf-8', newline='\n')
    fhAll.write(html_start)

    for fileIn in sorted(glob.glob("html-2-chapters-extracted/de/*.html")):
        (filePath, fileName) = os.path.split(fileIn)
        fileOut = f"html-3-cleaned/de/{fileName}"
        with open(fileIn, mode='r', encoding='utf-8', newline='\n') as fh:
            cont = fh.read()
        soup = BeautifulSoup(cont, features='html.parser')

        # find header
        myElement = soup.find("h1")
        myTitle = myElement.text  # chars only, no tags
        del myElement
        print(myTitle)

        # find body text
        myElement = soup.find("div", {"class": "user-formatted-inner"})
        # s = str(myElement)
        s = myElement.prettify()

        s = html_tuning(s)
        myElement = BeautifulSoup(s, features='html.parser')
        myBody = myElement.prettify()
        # myBody = myElement.encode()
        del myElement

        out = f"<h1>{myTitle}</h1>\n{myBody}\n"

        with open(fileOut, mode='w', encoding='utf-8', newline='\n') as fh:
            fh.write(html_start)
            fh.write(out)
            fh.write(html_end)
        fhAll.write(out)
        # break
    fhAll.write(html_end)
    fhAll.close()


def html_tuning(s: str) -> str:
    """
    cleanup spans and divs
    """
    # whitespace at start of line
    s = re.sub('\n\s+', "\n", s)
    #
    # alternatively define them via
    # <style>
    # div.user_center {	text-align: center; }
    # </style>
    #
    s = re.sub('<span class="user_normal">(.*?)</span>', r"\1", s,
               flags=re.DOTALL | re.IGNORECASE)
    s = re.sub('<span class="user_underlined">(.*?)</span>', r"<u>\1</u>", s,
               flags=re.DOTALL | re.IGNORECASE)
    s = re.sub('<span class="user_italic">(.*?)</span>', r"<i>\1</i>", s,
               flags=re.DOTALL | re.IGNORECASE)
    s = re.sub('<span class="user_bold">(.*?)</span>', r"<b>\1</b>", s,
               flags=re.DOTALL | re.IGNORECASE)
    # need to repeat b and i
    s = re.sub('<span class="user_italic">(.*?)</span>', r"<i>\1</i>", s,
               flags=re.DOTALL | re.IGNORECASE)
    s = re.sub('<span class="user_bold">(.*?)</span>', r"<b>\1</b>", s,
               flags=re.DOTALL | re.IGNORECASE)

    # cleanup divs
    s = re.sub('<div class="user_center">(.*?)</div>', r"<center>\1</center>", s,
               flags=re.DOTALL | re.IGNORECASE)
    s = re.sub('<div class="user_right">(.*?)</div>', r"<right>\1</right>", s,
               flags=re.DOTALL | re.IGNORECASE)
    s = re.sub('<div class="user_left">(.*?)</div>', r"<left>\1</left>", s,
               flags=re.DOTALL | re.IGNORECASE)
    # TODO: this is dangerous if another div is in the doc. better fix first and last line manually?
    s = re.sub('<div class="user-formatted-inner">(.*?)</div>', r"\1", s,
               flags=re.DOTALL | re.IGNORECASE)
    # 4x br -> 2x br
    s = re.sub('<br/>\s*<br/>\s*<br/>\s*<br/>', "<br/><br/>",
               s, flags=re.DOTALL | re.IGNORECASE)
    # 3x br -> 2x br
    s = re.sub('<br/>\s*<br/>\s*<br/>', "<br/><br/>",
               s, flags=re.DOTALL | re.IGNORECASE)
    # double br
    # s = re.sub('<br/>\s*<br/>', "<br/>", s, flags=re.DOTALL | re.IGNORECASE)
    # drop empty tags 3x
    s = re.sub(r'<(\w+)>\s*</\1>', "", s, flags=re.DOTALL | re.IGNORECASE)
    s = re.sub(r'<(\w+)>\s*</\1>', "", s, flags=re.DOTALL | re.IGNORECASE)
    s = re.sub(r'<(\w+)>\s*</\1>', "", s, flags=re.DOTALL | re.IGNORECASE)
    # double br again
    # s = re.sub('<br/>\s*<br/>', "<br/>", s, flags=re.DOTALL | re.IGNORECASE)

    # if more than 300 char -> use p instead of br
    s = re.sub('<br/>\n(.{200,})\n', r'<p>\n\1\n</p>', s, flags=re.IGNORECASE)
    s = re.sub('<br/>\s*<p>', "<p>", s, flags=re.DOTALL | re.IGNORECASE)
    s = re.sub('</p>\s*<br/>', "</p>", s, flags=re.DOTALL | re.IGNORECASE)

    # multiple spaces
    s = re.sub('  +', " ", s)
    # space before puctuation
    s = re.sub(' ([\.,:;])', r"\1", s)
    # space after puctuation
    s = re.sub('([a-zA-Z][\.,:;])([A-Z])', r"\1 \2", s)

    # spaces before " at lineend
    s = re.sub('\s+"\n', '"\n', s, flags=re.DOTALL | re.IGNORECASE)
    # empty lines
    s = re.sub('\n\n+', "\n", s)
    # remove linebreaks from sentences containing quotation marks
    # 3x
    s = re.sub(r'("\w[^"]+)\s+<br/>\s+([^"]+)\s+<br/>\s+([^"]+)\s+<br/>\s+([^"]+")', r'\1\2\3\4',
               s, flags=re.DOTALL | re.IGNORECASE)
    # 2x
    s = re.sub(r'("\w[^"]+)\s+<br/>\s+([^"]+)\s+<br/>\s+([^"]+")', r'\1\2\3',
               s, flags=re.DOTALL | re.IGNORECASE)
    # 1x
    s = re.sub(r'("\w[^"]+)\s+<br/>\s+([^"]+")', r'\1\2',
               s, flags=re.DOTALL | re.IGNORECASE)
    return s


download_all_chapters()
extract_chapter_text()
html_modify()

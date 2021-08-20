# import lxml.html  # pip install lxml
from bs4 import BeautifulSoup  # pip install beautifulsoup4
import os
import re
import glob
import requests

os.makedirs('html-1-download/', exist_ok=True)
os.makedirs('html-2-chapters-extracted/', exist_ok=True)
os.makedirs('html-3-cleaned/', exist_ok=True)


def download_file(url: str, filepath: str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0 ',
    }
    cont = requests.get(url, headers=headers).content
    with open(filepath, mode='wb', encoding='utf-8', newline='\n') as fh:
        fh.write(cont)


def download_chapter(chapter: int, filepath: str):
    url = f"https://www.fanfiktion.de/s/60044849000ccc541aef297e/{chapter}/"
    download_file(url=url, filepath=filepath)


def download_all_chapters():
    """Downloads into html-1-download/"""
    for chapter in range(1, 122):
        fileOut = "html-1-download/%03d.html" % chapter
        if not os.path.exists(fileOut):
            print(f"downloading chapter %03d" % chapter)
            download_chapter(chapter=chapter, filepath=fileOut)
#    del fileOut, chapter


def extract_chapter_text():
    """extract chapter text from html and writes result into html-2-chapters-extracted/"""
    for fileIn in sorted(glob.glob("html-1-download/*.html")):
        (filePath, fileName) = os.path.split(fileIn)
        fileOut = f"html-2-chapters-extracted/{fileName}"
        with open(fileIn, mode='r', encoding='utf-8', newline='\n') as fh:
            cont = fh.read()

        soup = BeautifulSoup(cont, features='html.parser')

        # find header
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

    for fileIn in sorted(glob.glob("html-2-chapters-extracted/*.html")):
        (filePath, fileName) = os.path.split(fileIn)
        fileOut = f"html-3-cleaned/{fileName}"
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

        s = html_cleanup(s)
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


def html_cleanup(s: str) -> str:
    """
    fix html
    """
    # cleanup comments and scripts
    s = re.sub('<!--.*?-->', "", s, flags=re.DOTALL)
    s = re.sub('<script.*?</script>', "", s,
               flags=re.DOTALL | re.IGNORECASE)

    # cleanup spans
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
    s = re.sub('<div class="user-formatted-inner">(.*?)</div>', r"\1", s,
               flags=re.DOTALL | re.IGNORECASE)
    # 4x br -> 2x br
    s = re.sub('<br/>\s*<br/>\s*<br/>\s*<br/>', "<br/><br/>", s, flags=re.DOTALL | re.IGNORECASE)
    # 3x br -> 2x br
    s = re.sub('<br/>\s*<br/>\s*<br/>', "<br/><br/>", s, flags=re.DOTALL | re.IGNORECASE)
    # double br
    # s = re.sub('<br/>\s*<br/>', "<br/>", s, flags=re.DOTALL | re.IGNORECASE)
    s = re.sub('<i>\s*</i>', "", s, flags=re.DOTALL | re.IGNORECASE)
    s = re.sub('<u>\s*</u>', "", s, flags=re.DOTALL | re.IGNORECASE)
    s = re.sub('<b>\s*</b>', "", s, flags=re.DOTALL | re.IGNORECASE)
    s = re.sub('<center>\s*</center>', "", s, flags=re.DOTALL | re.IGNORECASE)
    # double br again
    # s = re.sub('<br/>\s*<br/>', "<br/>", s, flags=re.DOTALL | re.IGNORECASE)

    # spaces before " at lineend
    s = re.sub('\s+"\n', '"\n', s, flags=re.DOTALL | re.IGNORECASE)

    return s


# download_all_chapters()
# extract_chapter_text()
html_modify()

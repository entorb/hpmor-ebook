import os
import re
import glob

# my helper
import helper

from bs4 import BeautifulSoup  # pip install beautifulsoup4
lang = "en-latex"
for dir in (f'html-1-download/{lang}/', f'html-3-cleaned/{lang}/'):
    os.makedirs(dir, exist_ok=True)

# download
chapter_last = 122
url_base = f"https://raw.githubusercontent.com/rjl20/hpmor/master/chapters/hpmor-chapter-<---chapter--->.tex"
for chapter in range(0+1, chapter_last+1):
    fileOut = f"html-1-download/{lang}/hpmor-chapter-%03d.tex" % chapter
    if not os.path.exists(fileOut):
        print(f"downloading chapter %03d" % chapter)
        url = url_base.replace("<---chapter--->", "%03d" % chapter)
        helper.download_file(url=url, filepath=fileOut)


def convert_tex_to_html(s: str) -> str:
    # chapter -> h1
    s = re.sub(r'\\chapter\{(.+?)\}', r"<h1>\1</h1>", s,
               flags=re.DOTALL | re.IGNORECASE)

    s = re.sub(r'\\lettrine\{(.)\}\{(.+?)\}', r"\1\2", s,
               flags=re.DOTALL | re.IGNORECASE)

    s = re.sub(r'\\emph\{(.+?)\}', r"<i>\1</i>", s,
               flags=re.DOTALL | re.IGNORECASE)

    return s


# s = "\chapter{A Day of Very Low Probability}"

# s = convert_tex_to_html(s)

# print(s)

# convert to html
fhAll = open(f"output/hpmor-{lang}.html", mode='w',
             encoding='utf-8', newline='\n')
html_start = helper.get_html_start(lang="en")
html_end = "</body></html>"
fhAll.write(html_start)

for fileIn in sorted(glob.glob(f"html-1-download/{lang}/*.tex")):
    (filePath, fileName) = os.path.split(fileIn)
    fileOut = f"html-3-cleaned/{lang}/{fileName}"
    with open(fileIn, mode='r', encoding='utf-8', newline='\n') as fh:
        cont = fh.read()
        cont = convert_tex_to_html(cont)

    with open(fileOut, mode='w', encoding='utf-8', newline='\n') as fh:
        fh.write(html_start)
        fh.write(cont)
        fh.write(html_end)
    fhAll.write(cont)
    # break

fhAll.write(html_end)
fhAll.close()

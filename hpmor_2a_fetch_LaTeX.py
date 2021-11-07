import os
import re
import glob

# my helper
import helper

# from bs4 import BeautifulSoup  # pip install beautifulsoup4
lang = "en-latex"
for dir in (f'chapters-1-download/{lang}/',):
    os.makedirs(dir, exist_ok=True)

# download
chapter_last = 122
url_base = f"https://raw.githubusercontent.com/rjl20/hpmor/master/chapters/hpmor-chapter-<---chapter--->.tex"
for chapter in range(0+1, chapter_last+1):
    fileOut = f"chapters-1-download/{lang}/hpmor-chapter-%03d.tex" % chapter
    if not os.path.exists(fileOut):
        print(f"downloading chapter %03d" % chapter)
        url = url_base.replace("<---chapter--->", "%03d" % chapter)
        helper.download_file(url=url, filepath=fileOut)

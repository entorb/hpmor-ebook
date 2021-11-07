import os
import re
import glob
import requests

from bs4 import BeautifulSoup  # pip install beautifulsoup4

# my helper
import helper

languages = ('en', 'de')


# make output dirs
os.makedirs('output', exist_ok=True)
for lang in languages:
    for dir in (f'chapters-1-download/{lang}/', f'chapters-2-extracted/{lang}/', f'chapters-3-cleaned/{lang}/'):
        os.makedirs(dir, exist_ok=True)


def download_all_chapters():
    """Downloads into chapters-1-download/<lang>/ only if fileOut does not exist"""
    chapter_last = 0
    for lang in languages:
        if lang == 'en':
            chapter_last = 122
            url_base = f"http://www.hpmor.com/chapter/<---chapter--->"
        elif lang == 'de':
            chapter_last = 121
            url_base = f"https://www.fanfiktion.de/s/60044849000ccc541aef297e/<---chapter--->/"
        for chapter in range(0+1, chapter_last+1):
            fileOut = f"chapters-1-download/{lang}/%03d.html" % chapter
            if not os.path.exists(fileOut):
                print(f"downloading chapter %03d" % chapter)
                url = url_base.replace("<---chapter--->", str(chapter))
                helper.download_file(url=url, filepath=fileOut)


if __name__ == "__main__":
    download_all_chapters()

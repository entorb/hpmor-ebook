"""
Download HTMLs.
"""
# import glob
import os

import helper

# import re
# import requests
# from bs4 import BeautifulSoup  # pip install beautifulsoup4

# my helper

languages = ("en", "de")
# , "fr"


# make output dirs
os.makedirs("output", exist_ok=True)
for lang in languages:
    for my_dir in (
        f"chapters-1-download/{lang}/",
        f"chapters-2-extracted/{lang}/",
        f"chapters-3-cleaned/{lang}/",
    ):
        os.makedirs(my_dir, exist_ok=True)


def download_all_chapters():
    """Download into chapters-1-download/<lang>/ only if fileOut does not exist."""
    chapter_last = 0
    for lang in languages:
        if lang == "en":
            chapter_last = 122
            url_base = "http://www.hpmor.com/chapter/<---chapter--->"
        elif lang == "de":
            chapter_last = 121
            url_base = (
                "https://www.fanfiktion.de/s/60044849000ccc541aef297e/<---chapter--->/"
            )
        # elif lang == "fr":
        #     chapter_last = 122
        #     url_base = f"https://www.fanfiction.net/s/6910226/<---chapter--->/"
        for chapter in range(0 + 1, chapter_last + 1):
            fileOut = "chapters-1-download/{lang}/%03d.html" % chapter
            if not os.path.exists(fileOut):
                print("downloading chapter %03d" % chapter)
                url = url_base.replace("<---chapter--->", str(chapter))
                helper.download_file(url=url, filepath=fileOut)


if __name__ == "__main__":
    download_all_chapters()

@echo off

rem echo html to epub
rem use calibre instead of pandoc, as pandoc looses the css style
rem see https://manual.calibre-ebook.com/generated/en/ebook-convert.html
echo calibre: html to epub
ebook-convert output/hpmor-en2.html output/hpmor-en2.epub --no-default-epub-cover --cover images/hpmor-en.jpg --authors "Eliezer Yudkowsky" --title "Harry Potter and the Methods of Rationality" --book-producer "Torben Menke" --pubdate 2015-03-14 --language en-US
echo calibre: epub to mobi
ebook-convert output/hpmor-en2.epub output/hpmor-en2.mobi
pause
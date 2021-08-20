# sudo apt-get install pandoc

# required for pdf
# sudo apt install texlive texlive-latex-base texlive-base texlive-lang-german texlive-latex-extra

# source is html file generated by fetch.py

# epub
echo html to markdown
pandoc -o output/hpmor-de.md    output/hpmor-de.html

echo html to epub
pandoc -o output/hpmor-de.epub  images/title.md   output/hpmor-de.md
# mobi
echo epub to mobi
pandoc -o output/hpmor-de.mobi  output/hpmor-de.epub
# markdown for simply modification
# pdf did not work from html, so started from epub instead
echo epub to pdf
pandoc -o output/hpmor-de.pdf   output/hpmor-de.epub
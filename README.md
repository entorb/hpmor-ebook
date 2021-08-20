# hpmor-translation
German translation for [Harry Potter and the Methods of Rationality](https://www.hpmor.com) by Eliezer Yudkowsky

##TODOs
- [x] find [complete translation](https://www.fanfiktion.de/s/60044849000ccc541aef297e/1/Ubersetzung-Harry-Potter-und-die-Methoden-des-rationalen-Denkens-Harry-Potter-and-the-methods-of-rationality)
- [x] fetch it
- [x] extract chapters to single files
- [x] auto-cleanup files
- [ ] manual-cleanup files
- [x] join to complete .html
- [x] convert to .epub, .mobi via [Pandoc](https://pandoc.org)
- [x] add title image
- [x] set meta data in .epub
- [ ] write preamble

## IDEAS
- [ ] convert br to p for long lines
- [ ] remove comments after download of files

## Research
### DE translations on the web
- [html by Schneefl0cke (comlete)](https://www.fanfiktion.de/s/60044849000ccc541aef297e/1/Ubersetzung-Harry-Potter-und-die-Methoden-des-rationalen-Denkens-Harry-Potter-and-the-methods-of-rationality)
- [html by Patneu (chapter 1-33)](https://www.fanfiktion.de/s/55610c610004dede273a3811/1/Harry-Potter-und-die-Methoden-der-Rationalitaet)
- [html by Jost (chapter 1-22)](https://www.fanfiktion.de/s/4cb8beb50000203e067007d0/1/Harry-Potter-und-die-Methoden-des-rationalen-Denkens)
- [html by DieFuechsin (chapter 34-78)](https://www.fanfiktion.de/s/5c793dfe000a402030774dc7/1/Harry-Potter-und-die-Methoden-der-Rationalitaet-Ubersetzung-HPMOR)
- [html von TralexHPMOR chapter 22-27](https://www.fanfiktion.de/s/59a29b7f000813c22ec1454b/1/Harry-Potter-und-die-Methoden-des-rationalen-Denkens)
- [YouTube German Audiobook (in progress)](https://www.youtube.com/watch?v=h32Ht-HUbL0&list=PLfgJSXz3-j3aYhWyR3Q5JzcI3h_eibPls)
- [pdf by elkablo](https://github.com/elkablo/hpmor), based on [Jost's translation (chapter 1-22)](https://www.fanfiktion.de/s/4cb8beb50000203e067007d0/1/Harry-Potter-und-die-Methoden-des-rationalen-Denkens) and on [rjl20's EN LaTeX PDF repo](https://github.com/rjl20/hpmor). elkablo's resulting DE-PDF can be found [here](https://blackhole.sk/~kabel/tmp/hpmor-1.pdf)
 
### other pdf projects
- [EN repo by rjl20](https://github.com/rjl20/hpmor) and [PDF](https://cdn.rawgit.com/rjl20/hpmor/0c10d2e8b6bd68e88fd2fc6e6b233140917e7314/out/hpmor.pdf) (linked at hpmor.com)
- [EN repo by xenohedron by](https://github.com/xenohedron/hpmor-xetex)
- [DE repo by elkablo](https://github.com/elkablo/hpmor) based on [rjl20's repo](https://github.com/rjl20/hpmor), resulting [DE-PDF](https://blackhole.sk/~kabel/tmp/hpmor-1.pdf)
- [Reddit post by elkablo](https://www.reddit.com/r/HPMOR/comments/gvj0x2/german_printed_version_of_book_1_anyone_interested/)

### check out EPUBs
- [epub by ikeran.org via web.archive](https://web.archive.org/web/20170624094133/http://ikeran.org/rationality.epub) (linked at hpmor.com)
- Tools
  - [Pandoc](https://pandoc.org) command line doc converter
  - [calibre](https://calibre-ebook.com) another, also OpenSource
  - [Fanfic to epub](http://ff2ebook.com/index.php)
- LaTeX -> EPUB is not a preferred way, as EPUB under the hood is html.

## OLD: TODOs for own translations
### source text fetch and convert to LaTeX
- [ ] download original EN chapter .html files
- [ ] extract chapter text from .html files
- [ ] convert html code to latex code and export 

### LaTeX setup
- [ ] base structure
- [ ] decide how to handle source and translated text in .tex file
- [ ] compile to PDF file 
- [ ] [compile to EPUB file](https://tex.stackexchange.com/questions/1551/use-latex-to-produce-epub)
- [ ] compile to MOBI file

### perform the translation to German
- [ ] use online translators to translate all chapters
- [ ] define best practice
- [ ] manually tune the translations of all chapters
- [ ] contact authors of other German in progress translations



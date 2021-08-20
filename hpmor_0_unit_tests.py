from hpmor_1_fetch_extract_convert_text import html_tuning

# de: user_center
s1 = """<br/>
 <span class="user_italic">
  Text
 </span>
 <br/>"""
s2 = """<br/>
<em>
Text
</em>
<br/>"""
assert html_tuning(s1, lang='de') == s2

# de: user_bold
s1 = """<br/>
 <span class="user_bold">
  Text
 </span>
 <br/>"""
s2 = """<br/>
<b>
Text
</b>
<br/>"""
assert html_tuning(s1, lang='de') == s2

# de: user_italic
s1 = """<br/>
 <span class="user_italic">
  Text
 </span>
 <br/>"""
s2 = """<br/>
<em>
Text
</em>
<br/>"""
assert html_tuning(s1, lang='de') == s2

# empty tags
s1 = """<br/>
<div class="user_center">
 <span class="user_bold">
  <span class="user_underlined">
  </span>
 </span>
</div>
<br/>"""
s2 = """<br/>
<br/>"""
assert html_tuning(s1, lang='de') == s2

# div center
s1 = """<div class="user_center">
 <span class="user_bold">
  <span class="user_italic">
   Text
  </span>
 </span>
 </div>"""
s2 = """<center>
<b>
<em>
Text
</em>
</b>
</center>"""
assert html_tuning(s1, lang='de') == s2

# <p style="text-align:center
s1 = """<p style="text-align:center;">
Text
</p>"""
s2 = """<p style="text-align:center;">
Text
</p>"""
assert html_tuning(s1, lang='en') == s2, s2

# convert " to lang specific
s1 = """<br/>
"Text"
<br/>"""
s2 = """<br/>
&ldquo;Text&rdquo;
<br/>"""
assert html_tuning(s1, lang='en') == s2, s2
s2 = """<br/>
&bdquo;Text&ldquo;
<br/>"""
assert html_tuning(s1, lang='de') == s2, s2

# <p style="text-align:center
s1 = '<hr noshade="noshade" size="1"/>'
s2 = '<hr/>'
assert html_tuning(s1, lang='en') == s2, s2

# s2 = html_tuning(s1, lang='en')
# print(s2)

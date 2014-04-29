# -*- coding: utf-8 -*- 
''' 
This script takes an specific format of the  EugeniBonet project DOC files, 
after converting to HTML using commandine:
soffice --headless --convert-to html --outdir HTMLs *.doc
  AND outputsa clean HTML: 
    1) only <p>, <b>, <i>, <a href...></a>
    2) All characters encoded as HTML (p.e. "&agrave;") 
'''

from tidylib import tidy_document
document, errors = tidy_document('''<p class="hello"><font>f&otilde;o <img src="bar.jpg"></font''',
    options={'numeric-entities':1})
print document
print errors

import json
import re
from pprint import pprint

def interpret_title(item):
    title_orig = re.sub(r'item.*[.]', '', item["title"], flags=re.IGNORECASE).strip()

    title = ""
    author = ""
    date_start = ""
    date_end = ""
    kind = ""

    if "/" in title_orig:
        title_orig, author = title_orig.split("/")
        myarr = re.split("\ ([a-z])",author)
        kind = ' '.join(myarr[1:])

    if  author == "": 
      author_kind = title_orig.split(",")[0]
      myarr = re.split("\ ([a-z])",author_kind)
      author = myarr[0]
      for _k in range(1, len(myarr[1:])+1):
        spc = " "
        if len(myarr[_k])==1: spc = ""
        kind += myarr[_k]+spc
      
    if "," in title_orig:
        parts = title_orig.split(",")
        title = parts[0]
        _date = " ".join(parts[1:]) # "1. May, 1950" -> "1. May 1950"
        if "-" in _date:
            date_start, date_end = _date.split("-")
        else:
            date_start = _date

    title = title_orig
    author = author.strip()
    date_start = date_start.strip()
    date_end = date_end.strip()
    kind = kind.strip()

    # print "t=%s, a=%s, d1=%s, d2=%s" % (title, author, date_start, date_end)

    item["title"] = title
    item["author"] = author
    item["date_start"] = date_start
    item["date_end"] = date_end
    item["kind"] = kind
    return item

def main():
    j = None
    with open("diaries.json") as f:
        j = json.loads(f.read())

    print len(j)
    out = []
    for item in j[:100]:
        o = interpret_title(item)
        pprint(o)
        print 
        out.append(o)

    # json.dumps(o)

main()

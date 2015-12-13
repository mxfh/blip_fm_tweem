# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
import re
#
# # Read in a page

# change accordingly
username = "diskurs"
startpage = 1
pages = 168 

# song per page
pagelength = 20

baseUrl = "http://blip.fm/" + username + "/?page="

for x in range(startpage, pages):
  html = scraperwiki.scrape(baseUrl + str(x))
  doc = lxml.html.fromstring(html)
  i = 0

  for el in doc.cssselect("a.blipTypeIcon"):
    song = el.attrib['title'].replace("\\'", "'")
    song = re.sub("^search for ","",song)
    songU = song.encode('utf8')
    print songU
    data = {
        'row': i + pagelength * (x - 1),
        'song': song
    }
    scraperwiki.sqlite.save(unique_keys=['row'], data=data)
    i+=1

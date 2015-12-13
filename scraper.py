# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
import re
#
# # Read in a page

username = "diskurs"
pages = 168 

baseUrl = "http://blip.fm/" + username + "/?page="

for x in range(1, pages):
  html = scraperwiki.scrape(baseUrl + str(x))
  doc = lxml.html.fromstring(html)
  i = 0

  for el in doc.cssselect("a.blipTypeIcon"):
    song = el.attrib['title'].replace("\\'", "'")
    song = re.sub("^search for ","",song)
    songU = song.encode('utf8')
    print songU
    data = {
        'row': i,
        'song': song
    }
    scraperwiki.sqlite.save(unique_keys=['row'], data=data)
    i+=1

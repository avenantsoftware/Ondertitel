#!/usr/bin/python
# encoding: utf-8
import hashlib, feedparser, requests, httplib, urllib

feed = feedparser.parse('http://www.addic7ed.com/rss.php?mode=hotspot')

# verstuur pushover bericht
def pushover(str):      
  conn = httplib.HTTPSConnection("api.pushover.net:443")
  conn.request("POST", "/1/messages.json",
  urllib.urlencode({
    "token": "yourtoken",
    "user": "youruserkey",
    "message": str,
    }), { "Content-type": "application/x-www-form-urlencoded" })
  conn.getresponse()
  return;

def pushover2(str):      
  conn = httplib.HTTPSConnection("api.pushover.net:443")
  conn.request("POST", "/1/messages.json",
  urllib.urlencode({
    "token": "yourtoken",
    "user": "youruserkey",
    "message": str,
    }), { "Content-type": "application/x-www-form-urlencoded" })
  conn.getresponse()
  return;

# Genereer MD5 hash van de meest recente titel en link elementen.
lasthash = hashlib.md5(feed.entries[0].link + feed.entries[0].title.encode('ascii','ignore')).hexdigest()

# locatie van ahash.txt
with open('/Users/htpc/Applications/Scripts/ahash.txt', 'r') as r:
  line = r.readline()

if line != lasthash:
  with open('/Users/htpc/Applications/Scripts/ahash.txt', 'w') as w:
    w.write(lasthash)
    # voer namen of gedeelte van naam van series in om te checken voor ondertitels
    keywords = ['Grantchester','Wallander','Vikings','True Detective','The Walking Dead','The Knick','Sherlock','Peaky Blinders','Homeland','Fargo','Endeavour','Broadchurch','Better Call Saul','Catch Fire','Leftovers','Banshee','Game of Thrones']
    nieuw = ['01x01'];
    if any(word in feed['entries'][0]['title'] for word in keywords):
      pushover(feed['entries'][0]['title'].encode('ascii','ignore'));
    if any(word in feed['entries'][0]['title'] for word in nieuw):
      pushover2(feed['entries'][0]['title'].encode('ascii','ignore'));  
 

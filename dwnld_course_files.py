#Author : Kapil Agarwal

#Download course files
#MIT 6.852: Distributed Algorithms
#Prof. Nancy Lynch

import os
import re
import urllib2
import BeautifulSoup

a=urllib2.urlopen('http://courses.csail.mit.edu/6.852/08/lecture.html').read()
b=BeautifulSoup.BeautifulSoup(a)
match = re.compile('\.(ppt|pdf)')

for link in b.findAll('a'):
  try:
    href = link['href']
    if re.search(match, href):
      os.system('wget http://courses.csail.mit.edu/6.852/08/%s'%href)
  except KeyError:
    pass

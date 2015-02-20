import xbmc
import re
import xbmcplugin
import resources.fetcher
import resources.gui
import resources.config
import BeautifulSoup

class bslzone:
  def __init__(self):
    self.gui = resources.gui.gui()

  def index(self):    
    data = resources.fetcher.fetcher().fetch(resources.config.INDEX_URL)
    soup = BeautifulSoup.BeautifulSoup(data)

    for category_list in soup.findAll("div", {"class" : "category-list"}):
      for div in category_list.findAll('div'):
        if re.compile('category-item').match(div['class']):
          link      = div.a
          title     = link.div.h2.contents[0].encode('ASCII', 'ignore')
          href      = link['href'].encode('ASCII', 'ignore')      
          xbmc.log('href: %s' % href)
          thumbnail = ''
          try:
            thumbnail = "%s%s" % (resources.config.BASE_URL, link.img['src'].encode('ASCII', 'ignore'))
            xbmc.log('thumbnail: %s' % thumbnail)
          except BaseException, err:
            xbmc.log('thumbnail error: %s' % err)        
          url       = resources.config.CATEGORY_URL % (resources.config.__plugin__, href)
          self.gui.add_folder(url, title, thumbnail)
    self.gui.end_of_folders()
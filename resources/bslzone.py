import xbmc, xbmcgui
import json
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
          thumbnail = ''
          try:
            thumbnail = "%s%s" % (resources.config.BASE_URL, link.img['src'].encode('ASCII', 'ignore'))
            xbmc.log('thumbnail: %s' % thumbnail)
          except BaseException, err:
            xbmc.log('thumbnail error: %s' % err)        
          url       = resources.config.CATEGORY_URL % (resources.config.__plugin__, href)
          self.gui.add_folder(url, title, thumbnail)
    self.gui.end_of_folders()

  def show(self, category):
    data = resources.fetcher.fetcher().fetch(category)
    soup = BeautifulSoup.BeautifulSoup(data)
    for prog_list in soup.findAll("div", {"class" : "prog-list"}):
      for div in prog_list.findAll('div'):
        if re.compile('prog-item').match(div['class']):
          link      = div.a
          title     = link.div.h2.contents[0].encode('ASCII', 'ignore')
          href      = link['href'].encode('ASCII', 'ignore')
          match     = re.search('watch\/(.*)\/', href)
          if match:
            href = match.group(1)
          thumbnail = ''
          try:
            thumbnail = "%s%s" % (resources.config.BASE_URL, link.img['src'].encode('ASCII', 'ignore'))
            xbmc.log('thumbnail: %s' % thumbnail)
          except BaseException, err:
            xbmc.log('thumbnail error: %s' % err)        
          url       = resources.config.PLAY_URL % (resources.config.__plugin__, href)
          self.gui.add_folder(url, title, thumbnail)
    self.gui.end_of_folders()

  def play(self, program):
    data          = resources.fetcher.fetcher().fetch("%s/%s" % (resources.config.INDEX_URL, program))
    soup          = BeautifulSoup.BeautifulSoup(data)
    iframe        = soup.find("iframe")
    iframe_match  = re.search('videos.bslzone.co.uk/(\d+)/player', iframe['src'])
    if iframe_match:
      video_id  = iframe_match.group(1)
      url       = self.__video_url__(video_id)
      listitem  = xbmcgui.ListItem(path = url, label = program)
      xbmc.executebuiltin("XBMC.Notification(Please Wait!,Preparing Your Video,3000)")
      xbmc.sleep(1000)
      xbmc.Player().play(url, listitem, False, -1)
      
  def __video_url__(self, video_id):
    url = resources.config.VZAAR_VIDEO_URL % video_id
    url = url + "|User-agent=" + resources.config.HTTP_USER_AGENT
    referer = resources.config.HTTP_PLAYER_REFERER % video_id
    return url + "&Referer=" + referer
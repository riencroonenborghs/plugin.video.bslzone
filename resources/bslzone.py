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
    data    = resources.fetcher.fetcher().fetch("%s/%s" % (resources.config.INDEX_URL, program))
    soup    = BeautifulSoup.BeautifulSoup(data)
    iframe  = soup.find("iframe")
    match   = re.search('videos.bslzone.co.uk/(\d+)/player', iframe['src'])
    if match:
      id = match.group(1)
      xbmc.log(resources.config.VZAAR_JSON_URL % id)
      json_response = resources.fetcher.fetcher().http_get(resources.config.VZAAR_JSON_URL % id)
      player_data = json.loads(json_response)
      ts = player_data['vz']['system']['ts'].encode('ASCII', 'ignore')
      hs = player_data['vz']['system']['hs'].encode('ASCII', 'ignore')
      smil = resources.fetcher.fetcher().http_get(resources.config.VZAAR_SMIL_URL % (id, ts, hs))
      soup = BeautifulSoup.BeautifulSoup(smil)
      rtmp = soup.smil.head.meta['base'].encode('ASCII', 'ignore')
      play_path = soup.smil.body.switch.video['src'].encode('ASCII', 'ignore')
      match = re.search('mp4\:(.*)', play_path)
      if match:
        play_path = match.group(1)
        player = 'http://view.vzaar.com/1945412/flashplayer'
        url = "rtmp://%s playpath=%s swfUrl=%s" % (rtmp, play_path, player)
        liz=xbmcgui.ListItem(program, iconImage="DefaultVideo.png", thumbnailImage='')
        liz.setInfo(type="Video", infoLabels={ "Title": program.replace('Live','')} )
        liz.setProperty("IsPlayable","true")
        pl = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        pl.clear()
        pl.add(url, liz)
        xbmc.Player(xbmc.PLAYER_CORE_MPLAYER).play(pl)
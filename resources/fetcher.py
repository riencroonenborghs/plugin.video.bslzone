import xbmc
import resources.config
import urllib2

class fetcher:
  def fetch(self, path):
    opener = urllib2.build_opener()
    urllib2.install_opener(opener)
    request = urllib2.Request(self.__build_url__(path))
    request.add_header('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16')
    try:
     response = urllib2.urlopen(request, timeout = 20)
     data     = response.read()
     response.close()
     return data
    except urllib2.HTTPError, err:
      xbmc.log("urllib2.HTTPError requesting URL: %s" % (err.code))
    else:
      return ""

  def __build_url__(self, path):
    return "%s/%s" % (resources.config.BASE_URL, path)
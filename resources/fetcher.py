import xbmc
import resources.config
import urllib2

class fetcher:
  def fetch(self, path):
    url = self.__build_url__(path)
    return self.http_get(url)

  def http_get(self, url):
    opener = urllib2.build_opener()
    urllib2.install_opener(opener)
    request = urllib2.Request(url)
    request.add_header('User-agent', resources.config.HTTP_USER_AGENT)
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
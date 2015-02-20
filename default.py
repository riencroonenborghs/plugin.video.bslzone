import cgi, urlparse
import resources.bslzone

params = cgi.parse_qs(urlparse.urlparse(sys.argv[2])[4])

if params:
  resources.bslzone.bslzone().index()
else:
  resources.bslzone.bslzone().index()
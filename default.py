import cgi, urlparse
import resources.bslzone

params = cgi.parse_qs(urlparse.urlparse(sys.argv[2])[4])

if params:
  if params['action'][0] == 'show':
    category = params['category'][0]
    resources.bslzone.bslzone().show(category)
  if params['action'][0] == 'play':
    program = params['program'][0]
    resources.bslzone.bslzone().play(program)
else:
  resources.bslzone.bslzone().index()
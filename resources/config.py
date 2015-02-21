import xbmcaddon
import sys

__plugin__    = sys.argv[0]
__id__        = int(sys.argv[1])
__name__      = "plugin.video.bslzone"
__settings__  = xbmcaddon.Addon(id = __name__)

BASE_URL      = "http://www.bslzone.co.uk"
INDEX_URL     = "watch"
CATEGORY_URL  = "%s?action=show&category=%s"
PLAY_URL      = "%s?action=play&program=%s"

VZAAR_JSON_URL = "http://view.vzaar.com/vd3/%s.json"
VZAAR_SMIL_URL = "http://view.vzaar.com/vd3/%s.smil?ts=%s&sig=%s&end"
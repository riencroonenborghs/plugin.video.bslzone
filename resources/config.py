import xbmcaddon
import sys

__plugin__    = sys.argv[0]
__id__        = int(sys.argv[1])
__name__      = "plugin.video.bslzone"
__settings__  = xbmcaddon.Addon(id = __name__)

BASE_URL      = "http://www.bslzone.co.uk"
INDEX_URL     = "watch"
CATEGORY_URL  = "%s?action=category&category=%s"
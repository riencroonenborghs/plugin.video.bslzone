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

VZAAR_VIDEO_URL = "https://view.vzaar.com/%s/video"
HTTP_USER_AGENT = "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16"
HTTP_PLAYER_REFERER = "http://videos.bslzone.co.uk/%s/player"
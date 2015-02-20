import xbmcgui, xbmcplugin
import resources.config

class gui:
  def add_list_item(self, url, title, thumbnail, icon, folder):
    listitem  = xbmcgui.ListItem(title, iconImage = icon, thumbnailImage = thumbnail)
    xbmcplugin.addDirectoryItem(handle = resources.config.__id__, url = url, listitem = listitem,  isFolder = folder)       
  def add_folder(self, url, title, thumbnail):
    self.add_list_item(url, title, thumbnail, "DefaultFolder.png", True)
  def end_of_folders(self):
    xbmcplugin.endOfDirectory(resources.config.__id__)
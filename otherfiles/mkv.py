file_path = "/Users/narendrakumar/MYSPACE/Interstellar2014)IMAXBluRayDisc1080p[Arnold].mkv"
import vlc
from time import sleep
    
movie = file_path

i = vlc.Instance()
media_player = i.media_player_new()
media = i.media_new(movie)
media_player.set_media(media)
media_player.play()
sleep(10)
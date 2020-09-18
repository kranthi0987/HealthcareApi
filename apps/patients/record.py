RTSP_LINK = r'rtsp://169.254.87.20:554/profile1'
import os
os.add_dll_directory(r'C:\Program Files (x86)\VideoLAN\VLC')
import vlc
import time
player=vlc.MediaPlayer(RTSP_LINK)
player.play()

count = 0

while count <= 100:
    count = count + 1
    time.sleep(0.2)
    player.video_set_scale(1.5)
    player.video_take_snapshot(0, './images/snapshot{0}.tmp.png'.format(count), 1920, 1080)
"""
import urllib
from urllib import request

dwn_link = 'https://www.youtube.com/watch?v=XdFUpFUDt88&list=PLqXS1b2lRpYQRJuTuoEBHVpidXQ_Tc3CT&index=6&t=902s'

file_name = 'trial_video.mp4'
urllib.request.urlretrieve(dwn_link, file_name)
"""

idx=[*range(17,57,4)]
print(idx)
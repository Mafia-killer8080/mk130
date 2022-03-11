import os, platform
try:
   import requests
except:
   os.system('pip2 install requests')
   os.system('pip2 install bs4')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from mk130 import teaching
    teaching()
elif bit == '32bit':
    from mk130 import teaching
    teaching()

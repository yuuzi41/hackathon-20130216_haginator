#!C:\Users\yhagiwara\Documents\hackathon_20130216\hackathon-20130216_haginator\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'gunicorn==0.17.2','console_scripts','gunicorn'
__requires__ = 'gunicorn==0.17.2'
import sys
from pkg_resources import load_entry_point

sys.exit(
   load_entry_point('gunicorn==0.17.2', 'console_scripts', 'gunicorn')()
)

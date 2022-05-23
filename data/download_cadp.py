"""
Please put your client_secrets.json of your project in the same folder with this script.
See how to obtain the credentials at: https://pythonhosted.org/PyDrive/quickstart.html#authentication
Usage: export PYTHONPATH=.. && python download_cadp.py
A client browser window will be opened.
"""

from analysis.pydrive import *

outputh_path="/media/tuananhn/903a7d3c-0ce5-444b-ad39-384fcda231ed/CADP/"
gauth = authenticate()

download_cadp(gauth, outputh_path)
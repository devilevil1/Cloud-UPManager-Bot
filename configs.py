# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID","3199060"))
	API_HASH = os.environ.get("API_HASH",","d67f6b73f3df9f90554442255c846f79")
	BOT_TOKEN = os.environ.get("BOT_TOKEN","5751659513:AAGSzLeALqI2u9JouXmncMNw3c-R8Sk9G88")
	GOFILE_API = os.environ.get("GOFILE_API","r2tVs13AYSpcRaR6UwPfd1nz9VhOA5HB")
	STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS","RjBvy8p62midW41")
	STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME","3eec663e2dfbda5670ac")
	SESSION_NAME = os.environ.get("SESSION_NAME", "CloudManagerBot")
	BOT_OWNER = int(os.environ.get("BOT_OWNER","1071294954"))
	LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL","-1001791902505"))
	DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
	HELP_TEXT = """
Send me any Media & Choose Upload Server,
I will Upload the Media to that server.

Currently I can Upload to:
> GoFile.io
> Streamtape.com
> Pixeldrain.com

Also I can do a lot of things from Inline!
__Check Below Buttons >>>__
"""
	PROGRESS = """
Percentage : {0}%
Done ✅: {1}
Total 🌀: {2}
Speed 🚀: {3}/s
ETA 🕰: {4}
"""

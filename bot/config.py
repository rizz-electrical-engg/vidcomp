#    Copyright (c) 2021 Danish_00
#    Improved By rizz
from decouple import config

try:
    APP_ID = config("21857983, cast=int")
    API_HASH = config("e469e84c943ce3b8b056eb6a296f2c67")
    BOT_TOKEN = config("")
    DEV = ""
    OWNER = config("833465134")
    ffmpegcode = ["-preset faster -c:v libx265 -s 854x480 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -metadata 'title=Encoded By   ⏤͟͞𝙍𝙞𝙯𝙯   (https://t.me/aboutRizzx)' -pix_fmt yuv420p -crf 30 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 1"]
    THUMBNAIL = config("THUMBNAIL", default="https://envs.sh/PvC.jpg")
except Exception as e:
    print("Environment vars Missing! Exiting App.")
    print(str(e))
    exit(1)

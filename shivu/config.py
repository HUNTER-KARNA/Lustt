class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6965147961"
    sudo_users = ["6864672519", "7710262210"]
    GROUP_ID = "-1002041586214"
    TOKEN = "6501935889:AAGJo6FN5Xrlh13H3uOJfFFB9K-u2lXrzqA"
    mongo_url = "mongodb+srv://soja11082:ZAWSN9qsi6nSBDrz@lust.6krav.mongodb.net/?retryWrites=true&w=majority&appName=lust"
    PHOTO_URL = ["https://telegra.ph/file/7e5398823512d307128a3.jpg", "https://telegra.ph/file/c45dcb207d81e97cb4f6a.jpg", "https://telegra.ph/file/0bc6d65878e8300fbf0f8.jpg", "https://telegra.ph/file/0afb45203ff162ee7227b.jpg"]
    SUPPORT_CHAT = "https://t.me/+hVnMZwUzEpIyYmI1"
    UPDATE_CHAT = "lustxUpdate"
    BOT_USERNAME = "lustXcatcherrobot"
    CHARA_CHANNEL_ID = "-1002023474262"
    api_id = "20457610"
    api_hash = "b7de0dfecd19375d3f84dbedaeb92537"
    RENDER_EXTERNAL_URL = "https://t.me/+hVnMZwUzEpIyYmI1"
    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True

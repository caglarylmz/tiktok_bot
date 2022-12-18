

from tiktok.tiktok import TikTok

with TikTok() as tiktok:
    tiktok.getBaseUrl()
    tiktok.register()
    print("Exiting....")
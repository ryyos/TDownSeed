import os
import click
import sys

from dotenv import *
from src import Instagram
from src import Tiktok
from src import write

class Main:

    url = sys.argv[1]
    
    # Memeriksa apakah URL mengandung "https://"
    if "instagram" in url:
        load_dotenv()

        instagram = Instagram()
        PATH = os.getenv('PATH_TO_SAVE')
        instagram.ex(path=PATH, post_url=url)

    elif 'tiktok' in url:
        load_dotenv()

        tiktok = Tiktok()
        PATH = os.getenv('PATH_TO_SAVE')
        tiktok.ex(path=PATH, tiktok_url=url)

if __name__ == '__main__':
    main = Main()
    main.sosmed()
    


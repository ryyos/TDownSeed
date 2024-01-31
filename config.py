import os
from src import write
from dotenv import *

def update_path(path: str):
    if not os.path.exists('.env'): write.write_str('.env', '')

    file = find_dotenv()

    set_key(file, 'PATH_TO_SAVE', path)
    os.getenv('PATH_TO_SAVE')

if __name__ == '__main__':
    update_path()
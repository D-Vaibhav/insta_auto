import logging
from dotenv import load_dotenv
from os import environ
from instagrapi import Client

def set_logger(logging_level, logging_path):
    logging.basicConfig(level = logging_level, filename = logging_path, filemode = 'w', format = '%(asctime)s - %(levelname)s - %(message)s', force = True)

    logger = logging.getLogger(__name__)
    # logger = logging.getLogger('main_pkg_logger')

    logger.info(f'logging_level is set to {logging_level}')
    logger.warning(f'explicit logger is set for the root user')

    return logger


def get_creds_from_env():
    # pip3 install python-dotenv
    load_dotenv()

    username = environ.get('USERNAME')
    password = environ.get('PASSWORD')

    return username, password



# INSTA THIN CLIENT ----------------------------------------------------------------------
def insta_login(username, password):
    # getting thin client
    insta = Client()

    insta.login(username, password)
    print(f"Great {username} is successfully logged into your's instagram profile, wooho...!!!\n")
    return insta
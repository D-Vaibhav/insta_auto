from string_stack import *

def main():
    username, password = get_creds_from_env()
    insta = insta_login(username, password)

    # ASYNC --------------------------------------------------------------------------> TO-DO
    hashtags = get_hastags_list()

    medias = get_hastags_info(insta, hashtags)

    # like_recent_hastags(insta, hashtags)

    # ASYNC --------------------------------------------------------------------------> TO-DO
    user_ids = get_user_ids(insta)
    print(f'user ids list generated from their username are below :\n {user_ids}')
    print(f'my id {insta.user_id}') # 60091742138

    # custom_message = 'hi there, this is Vaibhav Dwivedi from youtube channel : String Stack...'
    custom_message = 'test message 2 - from string_stack import package'


    send_direct_message_via_ids(insta, custom_message, user_ids)
    # send_video_via_ids(insta, video_path, user_ids)


# ====================================== PKG SETUP ======================================================
if __name__ == '__main__':
    # 1 - SETTING LOGGER from setup module inside insta package =================================================
    logging_level = logging.INFO
    logging_path = './logs/main.log'

    logger = set_logger(logging_level, logging_path)
    logger.info(f'logger is {logger}')

    # 2 - MAIN FUNCTION CALL =================================================
    main()
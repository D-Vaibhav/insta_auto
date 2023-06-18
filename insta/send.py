import logging
logger = logging.getLogger(__name__)


def send_direct_message_via_ids(insta, custom_message, user_ids):
    print(f'sending direct message ie. "{custom_message}"')
    print(f'fetched user ids by ML model : {user_ids}\n') # 60091742138

    for id in user_ids:
        insta.direct_send(custom_message, user_ids=[id])
        print(f'message sent SUCCESSFULLY to user with id = {id}')


def send_video_via_ids(insta, video_path, user_ids):
    insta.direct_send_video(video_path, [user_ids])
    print(f'video {video_path} sent SUCCESSFULLY ...!!!')
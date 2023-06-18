import logging
logger = logging.getLogger(__name__)


# DATA MODEL is supposed to be fitted here based on web scraping project -------------> TO-DO
def get_user_ids(insta):
    # https://adw0rd.github.io/instagrapi/usage-guide/direct.html
    ml_generated_ig_usernames = ['just_a_thought112', 'the_d_vaibhav', 'coderpukku', 'ujjawaldwivedi_', 'snapshotnest']
    logger.info(f'user list is {ml_generated_ig_usernames}')

    user_ids = []

    for username in ml_generated_ig_usernames:
        user_id = insta.user_id_from_username(username)
        user_ids.append(user_id)

        print(f"username is {username} and it's id is {user_id}")


    # # sending my own id
    # fetched_user_ids = insta.user_id

    return user_ids
import logging
logger = logging.getLogger(__name__)

# DATA MODEL is supposed to be fitted here based on web scraping project -------------> TO-DO
def get_hastags_list():
    hashtags = ['music', 'live', 'trending', 'indian', 'bollywood']
    return hashtags


def get_hastags_info(insta, hashtags):
    # https://adw0rd.github.io/instagrapi/usage-guide/hashtag.html

    # passing only 0th index hash tag ------------------------------------------> TO-DO
    media = insta.hashtag_info(hashtags[0]).dict()
    media_name = media['name']
    media_count = media['media_count']

    logger.info(f'media is {media}')
    print(f'total media count of {media_name} is {media_count}')

    # getting only two media posts
    amount = 2
    top_two = insta.hashtag_medias_top(hashtags[0], amount)
    logger.info(top_two[0].dict())
    logger.info(top_two[1].dict())

    return top_two


def like_recent_hastags(insta, hashtags):
    amount = 7
    medias = insta.hashtag_medias_recent(hashtags[0], amount)
    for i, media in enumerate(medias):
        insta.media_like(media.id)
        print(f'Liked post number = {i+1} of hashtag = {hashtags[0]}\n')
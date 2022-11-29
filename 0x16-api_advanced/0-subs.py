#!/usr/bin/python3
'''Contains a Reddit sub count finder'''
import requests


def number_of_subscribers(subreddit):
    '''Gets the subscriber count of a subreddit'''
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0)\
                  Gecko/20100101 Firefox/35.0'
    data = requests.get(url,
                        headers={'User-Agent': user_agent},
                        allow_redirects=False)
    try:
        return data.json()['data']['subscribers']
    except Exception:
        return 0

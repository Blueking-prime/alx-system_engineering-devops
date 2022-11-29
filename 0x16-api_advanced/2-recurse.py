#!/usr/bin/python3
'''Contains a Reddit hot post finder'''
import requests


def recurse(subreddit, hot_list=[], count=0):
    '''Gets the hottest posts of a subreddit'''
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0)\
                  Gecko/20100101 Firefox/35.0'
    data = requests.get(url,
                        headers={'User-Agent': user_agent},
                        allow_redirects=False)
    try:
        item = data.json()['data']['children'][count]['data']['title']
        hot_list.append(item)
        count += 1
        hot_list = recurse(subreddit, hot_list, count)
        return hot_list
    except Exception:
        if len(hot_list) > 0:
            return hot_list
        else:
            return None

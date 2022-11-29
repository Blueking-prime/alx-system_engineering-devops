#!/usr/bin/python3
'''Contains a Reddit top post finder'''
import requests


def top_ten(subreddit):
    '''Gets the top 10 posts of a subreddit'''
    url = 'https://www.reddit.com/r/{}/top.json'.format(subreddit)
    user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0)\
                  Gecko/20100101 Firefox/35.0'
    data = requests.get(url,
                        headers={'User-Agent': user_agent},
                        allow_redirects=False)
    try:
        j = 0
        for i in data.json()['data']['children']:
            if j == 10:
                break
            print(i['data']['title'])
            j += 1
    except Exception:
        print('None')

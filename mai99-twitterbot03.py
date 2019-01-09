import tweepy
import time

print ('Loading mai99-twitterbot03 program...')

consumer_key = 'xxxxxxxxx'
consumer_secret = 'xxxxxxxxx'
access_token = 'xxxxxxxxx'
access_token_secret = 'xxxxxxxxx'
your_account = 'xxxxxxxxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

followers = tweepy.Cursor(api.followers).items()
def following():
    print('Retrieving all your followers from twitter server...', flush=True)
    for follow in followers:
        api.create_friendship(follow.screen_name)
        print ('You just followed @' + follow.screen_name + ' now!')
        time.sleep(9)
    print('Retrieving all your followers is complete!')
    time.sleep(3)

followerlist = api.followers_ids(your_account)
friends = api.friends_ids(your_account)
def unfollow():
    print('Retrieving all the accounts you follow from twitter server...', flush=True)
    for f in friends:
        if f not in followerlist:
            api.destroy_friendship(f)
            user_details = (api.get_user(f))
            print ('You just unfollow @' + user_details.screen_name + ' now!')
            time.sleep(9)
    print('Retrieving all the accounts you follow is complete!')
    time.sleep(3)

def execute():
    if program == '1':
        following()
        print ('The mai99-twitterbot03 program will be terminated!')
        print ('<=============================================================>')
        time.sleep(3)
        exit()
    elif program == '2':
        unfollow()
        print ('The mai99-twitterbot03 program will be terminated!')
        print ('<=============================================================>')
        time.sleep(3)
        exit()
    elif program == '0':
        print ('The mai99-twitterbot03 program will be terminated!')
        print ('<=============================================================>')
        time.sleep(3)
        exit()
    else:
        print('Input error, please try again!')
        print ('<=============================================================>')
        time.sleep(3)

while True:
    print ('Enter 1 for start Auto Following')
    print ('Enter 2 for start Auto Unfollow')
    print ('Enter 0 to terminate mai99-twitterbot03 program')
    program = input('Program to be execute: ')
    execute()
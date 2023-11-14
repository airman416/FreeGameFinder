import praw
import time

reddit = praw.Reddit(
    client_id = "kgVteeNecZeI8A",
    client_secret = "R9duIi_7KV275U5kHXQnwlUADlxXvg",
#    username = YOUR_USERNAME
#    password = YOUR_PASSWORD
    user_agent = "airman416"
)

def topFindings(n):
    subreddit = reddit.subreddit('freegamefindings')
    games = []
    for submission in subreddit.new(limit=n):
        if submission.title[0] != "[":
            continue
        #print(submission.title, submission.url)
        games.append((submission.title, submission.url))
    return games
    
def newFindings():
    subreddit = reddit.subreddit('freegamefindings')
    for submission in subreddit.stream.submissions():
        print(submission.title, submission.url)
        
def newToday():
    subreddit = reddit.subreddit('freegamefindings')
    games = []
    for submission in subreddit.new(limit=10):
        minutes_since_post = (time.time() - submission.created_utc) / 60
        if minutes_since_post < 1440:
            print(submission.title)
            games.append((submission.title, submission.url))
            #return(submission.title, submission.url)
    return games

def new(hours):
    subreddit = reddit.subreddit('freegamefindings')
    games = []
    for submission in subreddit.new(limit=10):
        minutes_since_post = (time.time() - submission.created_utc) / 60
        if minutes_since_post < hours * 60:
            print(submission.title)
            games.append((submission.title, submission.url))
            #return(submission.title, submission.url)
    return games

def stream():
    subreddit = reddit.subreddit('freegamefindings')
    seen_submissions = set()
    while True:
        for submission in subreddit.new(limit=10):
            if submission.title not in seen_submissions and submission.title[0] == "[":
                seen_submissions.add(submission.title)
                print((submission.title, submission.url))
                return((submission.title, submission.url))
    
        
# for comment in reddit.subreddit("iama").stream.comments(skip_existing=True):
#     print(comment)
    
# for submission in reddit.subreddit("iama").stream.submissions():
#     print(submission)]

#print(topFindings(10))
newToday()

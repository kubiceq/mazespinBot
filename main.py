import praw
import time

reddit = praw.Reddit(
    client_id="6AhqDduz5LSvZA",
    client_secret="36lEt_0UNT68YOhryukFDQZmkN4VSw",
    user_agent="mazespin_bot_ver_1.0",
    username="congobongo420",
    password="spartak"

)
subreddit = reddit.subreddit("formula1")

for submission in subreddit.new(limit=10):
    for comment in submission.comments:
        lower_comment = comment.body.lower();

        if "mazepin" in lower_comment:
            print("---------------")
            print(lower_comment)
            comment.reply("Did you mean Mazespin?"
                          "Beep boop, I'm a bot."
                          "Please downvote me if I'm too obnoxious")
            time.sleep(600)
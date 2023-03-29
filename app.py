"""
Download comments for a public Facebook post.
"""

import facebook_scraper as fs
import json
from datetime import datetime

# get POST_ID from the URL of the post which can have the following structure:
# https://www.facebook.com/USER/posts/POST_ID
# https://www.facebook.com/groups/GROUP_ID/posts/POST_ID
POST_ID = "219149834131036"

# number of comments to download -- set this to True to download all comments
MAX_COMMENTS = 10000

# get the post (this gives a generator)
gen = fs.get_posts(
    post_urls=[POST_ID],
    options={"comments": MAX_COMMENTS, "progress": True}
)

# take 1st element of the generator which is the post we requested
post = next(gen)

# extract the comments part


#for getting only comments
comments = post['comments_full']

# Open file to add comments
f = open("posts.json", "a")

# process comments as you want...
for comment in comments:
    json_str = json.dumps(comment,default=str);
    if comments.index(comment)!=0:

        f.write(',')


        print(',')
    f.write(json_str)

    # e.g. ...print them
    print(comment)

    # e.g. ...get the replies for them
    for reply in comment['replies']:
        print(' ', reply)
        
f.close()
# Serializing json





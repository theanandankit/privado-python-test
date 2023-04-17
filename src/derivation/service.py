import requests
from .models import Comment
from .ProfileModel import Profile
from .PressInForm import PressInForm
import re
from http import cookies
from urllib.parse import unquote, urlparse

url1 = 'https://first.aspose1.com'
url2 = 'https://second.aspose2.com'
url3 = 'https://third.aspose3.com'

def add_comment(post):
    profile = Profile()
    profile_data = urlparse(url3, { id: profile.id  })
    if post:
        comment = Comment()
        comment.post = post
        comment.save()
        requests.put(url1, {'comment': comment})
        # print(comment)
    else:
        pressInForm = PressInForm()
        requests.post(url2, {'form': pressInForm})
        # print(comment)
##This program demos 3 different ways for how to use the requests module in Python.
#First, it will download an xkcd image from their site
# to the scripts working directory.
import requests

r = requests.get('https://imgs.xkcd.com/comics/password_strength.png')
with open('comic.png', 'wb') as f:
    f.write(r.content)

#Next, it will get the status code for that site.
print(r.status_code)

#Last, it will post auth tokens to a test website, and print the result.
print(r.headers)
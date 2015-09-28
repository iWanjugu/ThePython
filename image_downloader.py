__author__ = 'iWanjugu'
import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1,1000) #this renames the photo with a random number
    full_name = str(name) + ".jpg"
        #str() converts the number (name) to a string so int can be concatenated with the extension
        #giving the downloaded photos ;jpeg' extension
    urllib.request.urlretrieve(url,full_name)
        #arguments required are the url of the site and
        # what you'll name the downloaded files as

download_web_image("http://static1.squarespace.com/static/5561588fe4b0767a7f0c58c1/55632bc2e4b0c18afa44d64e/55767b1ee4b05bf4f5d6f8c7/1433828132321/Taraji-7369-2.jpg?format=1500w")
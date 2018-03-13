import random
import urllib.request


def web_image_download(url):

    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)


web_image_download("https://i.forbesimg.com/media/lists/companies/google_416x416.jpg")

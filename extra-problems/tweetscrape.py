import sys
import os
import requests
from bs4 import BeautifulSoup

# getting request

def get_request(url):
    headers = {'Accept': '*/*', 'X-User-IP': '1.1.1.1', 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Safari/605.1.15'}
    r = requests.get(url, headers=headers)

    if r.status_code != 200:
        print("We can't connect to the server")
    else:
        return r

# extracting the tweet

def extract_tweet(url):
    r = get_request(url)
    
    soup = BeautifulSoup(r.content, 'lxml')

    tweet_header_username = soup.find('a', class_="username").get_text()
    tweet_contents = soup.find('div', class_='tweet-content media-body')
    
    # setting up files
    name = "["+ tweet_header_username +"] " + tweet_contents.text.replace(":", "").replace(".", "")
    
    file_name = '%.70s' % name + ".md"
    print(file_name)

    if os.path.isfile(file_name):
        print("You already have this tweet")
        quit()
    
    f = open(file_name, "w")
    #f.write("# {}".format(file_name))
    f.write("\n\n")
    f.write("> by {}".format(tweet_header_username))
    f.write("\n\n")
    f.write("---")
    f.write("\n\n")

    tweet = tweet_contents.get_text()
    f.write(tweet)    
    f.write("\n\n")
    f.write("---")
    f.write("\n\n")
    
    f.write("")
    f.close()

# extracting thread

def extract_thread(url):
    r = get_request(url)
    
    soup = BeautifulSoup(r.content, 'lxml')

    tweet_header_username = soup.find('a', class_="username").get_text()
    tweet_contents = soup.find_all('div', class_='tweet-content media-body')
    
    # setting up files
    name = tweet_contents[0].text.replace(":", "").replace(".", "").replace("\n", "-")
    file_name = '%.70s' % name + ".md"

    if os.path.isfile(file_name):
        print("You already have this tweet")
        quit()
    
    f = open(file_name, "w")
    f.write("# {}".format(file_name))
    f.write("\n\n")
    f.write("> by {}".format(tweet_header_username))
    f.write("\n\n")
    f.write("---")
    f.write("\n\n")

    for thread in tweet_contents:
        tweet = thread.text
        f.write(tweet)    
        f.write("\n\n")
        f.write("---")
        f.write("\n\n")
    
    f.write("")
    f.close()
    #print("\n\n{} \n\nby {}".format(tweet_content, tweet_header_username))

#naval_url = "https://nitter.net/naval/status/1002103360646823936#m"
#dan_koe_url = "https://nitter.net/thedankoe/status/1673317693003378688#m"

url = sys.argv[2]

url = url.replace("twitter.com", "nitter.net")

if sys.argv[1] == "a":
    extract_tweet(url)    

if sys.argv[1] == "s":
    extract_thread(url)
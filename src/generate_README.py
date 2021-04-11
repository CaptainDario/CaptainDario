import os
import requests
import re
from datetime import date
import time

from google_play_scraper import app

debugging = True 


def insert_daKanji(readme : str):

    result = app(
        'com.DaAppLab.DaKanjiRecognizer',
        lang='en', # defaults to 'en'
        country='us' # defaults to 'us'
    )

    print("DaKanji:\n", "\tinstall:", result["installs"], "stars:", result["score"], "ratings:", result["ratings"])

    # put the playstore rating in the README
    readme = readme.replace(r"%DaKanjiAS%", "{:.2f}".format(result["score"]) + "⭐")
    # put the playstore downloads in the README
    readme = readme.replace(r"%DaKanjiAD%", result["installs"] + "️⬇️")
    
    # microsoft store rating
    readme = readme.replace("%DaKanjiDW%", "Download") 
    
    # snap store rating
    readme = readme.replace("%DaKanjiDL%", "Download") 
    
    # Mac app store rating
    readme = readme.replace("%DaKanjiDM%", "Download") 

    # github mobile stars
    rest_api = "https://api.github.com/repos/CaptainDario/DaKanji-mobile"
    page = requests.get(rest_api).json()
    stars = page["stargazers_count"]
    readme = readme.replace(r"%DaKanjiMG%", str(stars) + "⭐")

    # github desktop stars on github
    rest_api = "https://api.github.com/repos/CaptainDario/DaKanji-desktop"
    page = requests.get(rest_api).json()
    stars = page["stargazers_count"]
    readme = readme.replace(r"%DaKanjiDG%", str(stars) + "⭐")
    
    readme = readme.replace(r"%DaKanjiDG%", str(stars) + "⭐")

    return readme

def insert_daQuad(readme : str):

    result = app(
        'com.DaAppLab.DaQuad',
        lang='en', # defaults to 'en'
        country='us' # defaults to 'us'
    )

    print("DaQuad:\n", "\tinstall:", result["installs"], "stars:", result["score"], "ratings:", result["ratings"])

    # put the rating in the README
    readme = readme.replace(r"%DaQuadAS%", "{:.2f}".format(result["score"]) + "⭐")
    # put the rating in the README
    readme = readme.replace(r"%DaQuadAD%", result["installs"] + "️⬇️")
    return readme

def insert_daStairs(readme : str):

    result = app(
        'com.DaAppLab.DaStairs',
        lang='en', # defaults to 'en'
        country='us' # defaults to 'us'
    )

    print("DaStairs:\n", "\tinstall:", result["installs"], "stars:", result["score"], "ratings:", result["ratings"])

    # put the rating in the README
    readme = readme.replace(r"%DaStairsAS%", "{:.2f}".format(result["score"]) + "⭐")
    # put the rating in the README
    readme = readme.replace(r"%DaStairsAD%", result["installs"] + "️⬇️")
    return readme

def insert_youtube(readme : str):
    channel = "https://www.youtube.com/feeds/videos.xml?channel_id=UCQrQnnbsO0hCCMSGMPemPGw"
    headers= {"User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}

    page = requests.get(channel, headers=headers).content
    data = str(page)
    
    # get titles
    regex = re.compile(r'(<media:title>(.+?)</media:title>)')
    titles = regex.findall(data)
    # get urls
    regex = re.compile(r'(<media:content url="(.+?)"(.+?)/>)')
    urls = regex.findall(data)

    for i in range(5):
        readme = readme.replace("%Video{}T%".format(str(i+1)), titles[i][1])
        readme = readme.replace("%Video{}URL%".format(str(i+1)), urls[i][1])

    return readme

def insert_instructables(readme : str):

    user = "https://www.instructables.com/member/daapplab/"
    headers= {"User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}

    page = requests.get(user, headers=headers).content
    data = str(page)
    
    # get url / title
    regex = re.compile(r'(class="promoted-item-thumbnail.+?class="image-wrapper.+?href="(.+?)">)')
    titles = regex.findall(data)

    for i in range(5):
        readme = readme.replace("%Instructable{}T%".format(str(i+1)), titles[i][1][1:-1])
        
        url = "https://www.instructables.com" + titles[i][1]
        readme = readme.replace("%Instructable{}URL%".format(str(i+1)), url)

    return readme

def insert_update_date(readme : str):

    current_date = date.today().strftime(r"%B %d, %Y")
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)

    readme = readme.replace(r"%update%", " ".join([current_date,  current_time]))

    return readme



if __name__ == "__main__":

    readme = ""
    path = os.path.join(os.getcwd(), "README_template.md")

    with open(path, encoding="utf8") as f:
        readme = f.read()

    readme = insert_daKanji(readme)
    readme = insert_daQuad(readme)
    readme = insert_daStairs(readme)

    readme = insert_youtube(readme)
    readme = insert_instructables(readme)



    if(debugging):
        with open(os.path.join(os.getcwd(), "gen_README.md"), "w+", encoding="utf8") as f:
            f.write(readme)
    else:
        readme = insert_update_date(readme)
        
        with open(os.path.join(os.getcwd(), "README.md"), "w+", encoding="utf8") as f:
            f.write(readme)

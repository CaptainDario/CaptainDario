import os
from google_play_scraper import app


debugging = False


def insert_daKanji(readme : str):

    result = app(
        'com.DaAppLab.DaKanjiRecognizer',
        lang='en', # defaults to 'en'
        country='us' # defaults to 'us'
    )

    print("DaKanji:\n", "\tinstall:", result["installs"], "stars:", result["score"], "ratings:", result["ratings"])

    # put the rating in the README
    readme = readme.replace(r"%DaKanjiAS%", "{:.2f}".format(result["score"]))
    # put the rating in the README
    readme = readme.replace(r"%DaKanjiAD%", result["installs"])
    return readme

def insert_daQuad(readme : str):

    result = app(
        'com.DaAppLab.DaQuad',
        lang='en', # defaults to 'en'
        country='us' # defaults to 'us'
    )

    print("DaQuad:\n", "\tinstall:", result["installs"], "stars:", result["score"], "ratings:", result["ratings"])

    # put the rating in the README
    readme = readme.replace(r"%DaQuadAS%", "{:.2f}".format(result["score"]))
    # put the rating in the README
    readme = readme.replace(r"%DaQuadAD%", result["installs"])
    return readme

def insert_daStairs(readme : str):

    result = app(
        'com.DaAppLab.DaStairs',
        lang='en', # defaults to 'en'
        country='us' # defaults to 'us'
    )

    print("DaStairs:\n", "\tinstall:", result["installs"], "stars:", result["score"], "ratings:", result["ratings"])

    # put the rating in the README
    readme = readme.replace(r"%DaStairsAS%", "{:.2f}".format(result["score"]))
    # put the rating in the README
    readme = readme.replace(r"%DaStairsAD%", result["installs"])
    return readme


if __name__ == "__main__":

    readme = ""
    path = os.path.join(os.getcwd(), "README_template.md")

    with open(path, encoding="utf8") as f:
        readme = f.read()

    readme = insert_daKanji(readme)
    readme = insert_daQuad(readme)
    readme = insert_daStairs(readme)

    if(debugging):
        with open(os.path.join(os.getcwd(), "gen_README.md"), "w+", encoding="utf8") as f:
            f.write(readme)

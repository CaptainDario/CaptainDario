from google_play_scraper import app

result = app(
    'com.DaAppLab.DaKanjiRecognizer',
    lang='en', # defaults to 'en'
    country='us' # defaults to 'us'
)

print("install:", result["installs"])
print("stars:", result["score"])
print("ratings:", result["ratings"])

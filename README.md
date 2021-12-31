# Academic Media

## App Setup
* `git clone https://github.com/Heteroskedastic/Academic_Media.git`
* `cd Academic_Media`
* `npm install`
* `npm run build`
* `python manage.py runserver 9040`


## How to save news(using newsapi) articles in DB
* `python manage.py newsapi --endpoint top-headlines  --apiKey <api_token>  -c us`

## How to save news(using newspapers) articles in DB
* `python manage.py newspapers -u https://edition.cnn.com/world/live-news/omicron-variant-coronavirus-news-12-29-21/index.html
`



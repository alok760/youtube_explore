# youtube_explore
<img src="https://user-images.githubusercontent.com/14289201/147898972-44fef1d2-c7fa-4442-a9ca-88725ffeb116.png" width=70% >

This project can be used to explore and search youtube videos on a configured topic. 
## Try it out here https://www.video-explore.tk/

## Keyfeatures
- Uses ElasticSearch to provide fast and accurate results 
- Support for partial matches and typos in the search query
- Can use multiple API Keys, exhausted keys will be cycled automatically
- Automatic sync with Youtube every 10 minutes 
- Infinite Scroll on Dashboard
- Paginated API with sorting options

## Tech 
Frontend: ReactJS and Bootstrap
API: Django 
DB: ElasticSearch & SQLite

## API Usage
add steps how to use API here.
### Example: 
curl 'https://api.video-explore.tk/search?search=history+of+Indian+education&sort=desc&page=1&page_size=10'
Response: 

```
[
  {
    "model": "youtube_explore.video",
    "pk": "2jt3xbHYzRM",
    "fields": {
      "title": "History of Indian Education System || T Talks",
      "description": "Mana Store: https://sharemystore.com/manastoreofficial ...",
      "etag": "ZSuksJ7zkDl_jquZ7p9klwmusbA",
      "channel_id": "UCQbSl5j-XRIHJk6M63viLrQ",
      "channel_title": "T Talks",
      "published_at": "2022-01-02T13:58:57Z",
      "thumbnail_url": "https://i.ytimg.com/vi/2jt3xbHYzRM/default.jpg"
    }
  }
]
```

### Query Params

| Param | Optional | Default | Description |
| --- | --- | --- | --- |
| `search` | Optional | None | Search Query |
| `sort` | Optional | desc | asc/desc |
| `page` | Optional | 1 | page number |
| `page_size` | Optional | 10 | Items per page |



## Project Setup
### Configuration
- Edit `config.py` and add youtuve API v3 keys (1 or more)

### Docker Compose
- `docker-compose build`
- `docker-compose up`

### Manual
#### Frontend
- `npm i`
- `npm start`

#### Backend
- install https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html
- install pipenv https://pipenv.pypa.io/en/latest/install/#installing-pipenv
- `pipenv shell`
- `python manage.py migrate`
- `python manage.py crontab add`
- `python manage.py runserver`
Note: Edit `apiUrl` in `frontend/src/constants.js` and `CORS_ALLOWED_ORIGINS` in `frontend/src/constants.js` if not running on localhost

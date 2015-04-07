use the following command to download youtube channels' videos:
    $ YT_CHANNEL_ID="TWuseRGroup" MONGO_URI="mongodb://localhost:27017/dockerdata" python youtube_crawler.py
    $ YT_CHANNEL_ID="ShogunToolbox" MONGO_URI="mongodb://localhost:27017/dockerdata" python youtube_crawler.py 
    $ YT_CHANNEL_ID="PyCon2014" MONGO_URI="mongodb://localhost:27017/dockerdata" python youtube_crawler.py 
    $ YT_CHANNEL_ID="taipeipython" MONGO_URI="mongodb://localhost:27017/dockerdata" python youtube_crawler.py 
    $ YT_CHANNEL_ID="Enthought" MONGO_URI="mongodb://localhost:27017/dockerdata" python youtube_crawler.py 
    $ YT_CHANNEL_ID="iyenlung" MONGO_URI="mongodb://localhost:27017/dockerdata" python youtube_crawler.py 

youtube_crawler.py is my answer, and youtube_crawler_try.py is for test
(compare both time)

dependency:
- [PyCrawlers](https://github.com/PlaYdata/PyCrawlers)

Youtube Channels:
- TWuseRGroup
- ShogunToolbox
- PyCon2014
- taipeipython
- EnthoughtMedia (Scipy2014)#Enthought
- iyenlung

Python Videos:
- http://pyvideo.org/
    



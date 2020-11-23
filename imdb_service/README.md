## Execute the application and Access the endpoints to get hte results##

### Supported endpoint ###



## IMDB API ##

Dockerized navigation package `IMDBAPP (ResT API)`, using ``Docker, Flask, Flask-RESTful, and Ngnix``.


```
|-- _misc                        #---- Scripts used while developing(not required for this application -------#
|   |-- __init__.py
|   |-- get_details_by_imdbpyapi.py
|   |-- get_details_sav.py
|   `-- get_details_tsv_gz.py
|-- data
|   |-- README
|   |-- README.md
|   |-- dataset
|   |   |-- logs
|   |   |   |-- gunicorn-access.log
|   |   |   `-- imdb.log
|   |   |-- name.basics.sav
|   |   |-- only_movie.sav
|   |   |-- title.akas.sav
|   |   |-- title.basics.sav
|   |   |-- title.crew.sav
|   |   |-- title.episode.sav
|   |   |-- title.principals.sav
|   |   `-- title.ratings.sav
|   `-- unzip_tsv_gz.py             -  Script to unzip the data set
|-- docker-compose.yml              -  Dockercompose file to start the service
|-- imdb_proxy                      #---- NGNIX SERVICE -------#
|   |-- Dockerfile                  -  Dockerfile for NGNIX
|   |-- __init__.py
|   |-- index.html
|   `-- prod.conf
|-- imdb_service                     #---- IMDB-APP SERVICE -------#
|   |-- Dockerfile                   -  Dockerfile for IMDB
|   |-- README.md
|   |-- __init__.py
|   |-- config.py
|   |-- data
|   |   `-- imdb.db                   #---- DATABASE sqlite to store user info -------#
|   |-- gunicorn.py
|   |-- requirements.txt
|   |-- source
|   |   |-- __init__.py
|   |   |-- app.py                    #---- MAIN File for the APP ----#
|   |   |-- blk.py                    #---- BLACKLIST(user) File for the APP ----#
|   |   |-- core                      #--- Core Folder contains core modules ---#
|   |   |   |-- __init__.py
|   |   |   `-- movies_info.py        -- Module to support or requests --
|   |   |-- ext.py
|   |   |-- models
|   |   |   |-- __init__.py
|   |   |   `-- user.py               # Model file for USER
|   |   `-- resources                 #--- Resource Folder contains endpoint related modules ---#
|   |       |-- __init__.py
|   |       |-- movies.py
|   |       |-- ping.py
|   |       `-- user.py
|   `-- wsgi.py
|-- migrations
|   |-- README.md
|   |-- alembic.ini
|   |-- env.py
|   |-- script.py.mako
|   `-- versions
```


### Steps to run ###
##### Please Note: If you are running please copy the imdb-project/data/dataset to imdb-project/imdb_service/data #####
##### Because it was kept outside of the script to avoid huge image size, so ihave used the volume concept
`/path/on/host:/path/on/container`
#####
* Directly run 
/usr/bin/python3 -m flask run --port 9091

[0r]

* Open a terminal and run `docker-compose up --build`. Wait until the following output shows up on the terminal.
or 

```
Successfully tagged imdb-project_imdb_proxy:latest
Recreating imdb_app ... done
Recreating imdb_proxy ... done
Attaching to imdb_app, imdb_proxy
imdb_app      | [2020-11-22 07:24:14 +0000] [1] [INFO] Starting gunicorn 19.9.0
imdb_app      | [2020-11-22 07:24:14 +0000] [1] [INFO] Listening at: http://0.0.0.0:9090 (1)
imdb_app      | [2020-11-22 07:24:14 +0000] [1] [INFO] Using worker: gthread
imdb_app      | [2020-11-22 07:24:14 +0000] [9] [INFO] Booting worker with pid: 9
imdb_app      | [2020-11-22 07:24:14 +0000] [10] [INFO] Booting worker with pid: 10
imdb_app      | config_modeconfig_mode  developmentdevelopment
imdb_app      | 
imdb_app      | [2020-11-22 07:24:15,877] INFO in app: IMDB source is up and running
imdb_app      | [2020-11-22 07:24:15,878] INFO in app: IMDB source is up and running
``` 


3. Open the url [http://127.0.0.1:9090](http://127.0.0.1:9090) on your browser/postman, you will see the below response.
````{
message: "Welcome..!"
}
````


#### Sample Output: ####
##### Usage: http://127.0.0.1:9090/ping  (Basic api call - Health check) #####
```
{
message: "Pong..!"
}
```

##### How many movies did actor(say:Leonardo DiCaprio) star in?
##### Usage:  http://127.0.0.1:9090/movies/actor/<actor-name> #####
##### Ex:  http://127.0.0.1:9090/movies/actor/leonardo dicaprio #####

```
{
    "Movies_with_rating": {
        "HEADING": "MOVIE  ## RATING",
        "tt0108330": "This Boy's Life ## 7.3",
        "tt0108550": "What's Eating Gilbert Grape ## 7.8",
        "tt0112461": "The Basketball Diaries ## 7.3",
        "tt0114214": "The Quick and the Dead ## 6.4",
        "tt0114702": "Total Eclipse ## 6.6",
        "tt0116999": "Marvin's Room ## 6.7",
        "tt0117509": "Romeo + Juliet ## 6.7",
        "tt0119004": "Don's Plum ## 5.8",
        "tt0120338": "Titanic ## 7.8",
        "tt0120533": "Celebrity ## 6.3",
        "tt0120744": "The Man in the Iron Mask ## 6.5",
        "tt0163978": "The Beach ## 6.7",
        "tt0217505": "Gangs of New York ## 7.5",
        "tt0264464": "Catch Me If You Can ## 8.1",
        "tt0338751": "The Aviator ## 7.5",
        "tt0407887": "The Departed ## 8.5",
        "tt0450259": "Blood Diamond ## 8.0",
        "tt0758774": "Body of Lies ## 7.1",
        "tt0959337": "Revolutionary Road ## 7.3",
        "tt0993846": "The Wolf of Wall Street ## 8.2",
        "tt1130884": "Shutter Island ## 8.2",
        "tt1343092": "The Great Gatsby ## 7.2",
        "tt1375666": "Inception ## 8.8",
        "tt1433813": "Hubble 3D ## 7.7",
        "tt1616195": "J. Edgar ## 6.5",
        "tt1663202": "The Revenant ## 8.0",
        "tt1853728": "Django Unchained ## 8.4",
        "tt7131622": "Once Upon a Time... In Hollywood ## 7.6",
        "tt9114472": "Ice on Fire ## 7.4"
    },
    "Number_of_Movies": 29
}
```

##### How many movies did actor(say:Leonardo DiCaprio) star in? and What was his worst/best-rated movie?
##### Usage:  http://127.0.0.1:9090/movies/actor/<actor-name>/<best-or-worst> #####
##### Ex:  http://127.0.0.1:9090/movies/actor/leonardo dicaprio/best #####
##### Ex:  http://127.0.0.1:9090/movies/actor/leonardo dicaprio/worst #####

```
For Worst (5 movies)
{
    "Five_Worst_Rated_Movies": {
        "HEADING": "MOVIE  ## RATING",
        "tt0119004": "Don's Plum ## 5.8",
        "tt0120533": "Celebrity ## 6.3",
        "tt0114214": "The Quick and the Dead ## 6.4",
        "tt1616195": "J. Edgar ## 6.5",
        "tt0120744": "The Man in the Iron Mask ## 6.5"
    }
}

For Best (5 movies)
{
    "Five_Best_Rated_Movies": {
        "HEADING": "MOVIE  ## RATING",
        "tt1375666": "Inception ## 8.8",
        "tt0407887": "The Departed ## 8.5",
        "tt1853728": "Django Unchained ## 8.4",
        "tt1130884": "Shutter Island ## 8.2",
        "tt0993846": "The Wolf of Wall Street ## 8.2"
    }
}
```

##### What are the best-rated movies, where a single person was a writer, director, and also one of the actors?
##### Usage:   http://127.0.0.1:9090/movies/allthree #####
##### Ex:   http://127.0.0.1:9090/movies/allthree #####
* Here i have used the consolidated dataframe, to get the results bit faster, in-fact we can use this single dataset 
for all our endpoints.
* Displays TOP 25 movies

```
{
    "Top_Rated_Movies": {
        "HEADING": "MOVIE ## PERSON ## RATING",
        "2091630": "Painting a Life: Documenting an Approach to Painting ## David Kassan ## 10.0",
        "1815290": "#MostLivable ## Bhushan Gaur ## 10.0",
        "1662762": "Barcelona - Madrid ## Sergey A. ## 10.0",
        "1682433": "ONE - The Documentary ## Mike Goedecke ## 10.0",
        "2134554": "Steps in the Fire ## Andrey Hadjivasilev ## 10.0",
        "1682436": "ONE - The Documentary ## Lauren Dubac ## 10.0",
        "2239661": "Music of Survival: The Story of the Ukrainian Bandurist Chorus ## Orest Sushko ## 10.0",
        "1787549": "Love or something like that ## Shirley Frimpong-Manso ## 10.0",
        "1758782": "Closed for Storm ## Jake Williams ## 10.0",
        "1713367": "Rainaldo Graziani da Meridiano Zero al Soggetto Radicale... da Evola a Dugin ## Umberto Baccolo ## 10.0",
        "1676450": "Le Origini della Cinematografia ## Jordan River ## 10.0",
        "1739435": "Bure bareta ## Robert Bubalo ## 10.0",
        "1778748": "Sadika: The Multi-Dimensional Artist ## Farah Khadhar ## 10.0",
        "2264479": "Foster Sin ## Ray Loot ## 10.0",
        "2264480": "Foster Sin ## Kevin King ## 10.0",
        "1713368": "Ines Pedretti contro i sensi vietati, le strade del possibile ## Umberto Baccolo ## 10.0",
        "1713370": "La meta è il viaggio nella postmodernità - Murelli e Graziani a colloquio ## Umberto Baccolo ## 10.0",
        "1790164": "O Leo psahnei talento en etei 2015!! Live Performance ## Leonardo Thimo ## 10.0",
        "1243929": "The Barn Theatre: Tomorrow's Stars Today ## Phil Wurtzel ## 10.0",
        "1784014": "Mnohaya lita. Stoyko ## Vyacheslav Bihun ## 10.0",
        "1877118": "The Straight and Narrow ## Jake Yuzna ## 10.0",
        "1713371": "Neofascismo? Rispettatelo! Da giovane ebbe un futuro anche lui ## Umberto Baccolo ## 10.0",
        "2108543": "Oltre il filo ## Dorino Minigutti ## 10.0",
        "1713372": "Politica e Spiritualità nel Postmoderno ## Umberto Baccolo ## 10.0",
        "1662764": "Amber region Kaliningrad ## Sergey A. ## 10.0"
    }
}
```

##### # How many movies are longer than five hours?t #####
##### Usage:  http://127.0.0.1:9090/movies/runtime/<hours> #####
##### Ex:  http://127.0.0.1:9090/movies/runtime/7 #####
```
{
    "Movies_with_running_time": {
        "HEADING": "MOVIE  ## TIME(HH:MM)",
        "tt0003675": "The Beloved Adventurer ## 07:30",
        "tt0004052": "The Hazards of Helen ## 23:48",
        "tt0005005": "The Broken Coin ## 07:20",
        "tt0006206": "Les vampires ## 07:01",
        "tt0008284": "Mefisto ## 07:40",
        "tt0008470": "El protegido de Satán ## 08:00",
        "tt0009029": "The Eagle's Eye ## 10:00",
        "tt0009905": "Barrabas ## 08:09",
        "tt0074334": "Comment Yukong déplaça les montagnes ## 12:43",
        "tt0076147": "Hitler: A Film from Germany ## 07:22",
        "tt0089458": "Lamentations a Monument for the Dead World ## 07:17",
        "tt0090015": "Shoah ## 09:26",
        "tt0095979": "Resan ## 14:33",
        "tt0105521": "Taiga ## 08:21",
        "tt0111341": "Satantango ## 07:19",
        "tt0114186": "Prisjadim na dorozku ## 10:20",
        "tt0131597": "Split ## 11:40",
        "tt0151534": "Right of Asylum ## 11:05",
        "tt0162536": "The Photo-Drama of Creation ## 08:00",
        "tt0174864": "A Retrospection of Leningrad (1957-1990) ## 10:59",
        "tt0176691": "Expressionism in Croatian Painting ## 07:06",
        "tt0178472": "Français si vous saviez ## 07:45",
        "tt0179184": "**** ## 01:00",
        "tt0196530": "Empire ## 08:05",
        "tt0245532": "Unter der schwarzen Sturmfahne ## 04:02",
        "tt0246135": "Out 1 ## 12:09",
        "tt0253982": "Zimmermädchen... Dreimal klingeln ## 15:42",
        "tt0270523": "The Movie Orgy ## 07:00",
        "tt0270784": "Khleb - imya sushchestvitelnoe ## 09:40",
        "tt0284020": "The Cure for Insomnia ## 15:00",
        "tt0342707": "The Longest Most Meaningless Movie in the World ## 00:00",
        "tt0387271": "A Twist of Fate ## 08:50",
        "tt0389448": "Tie Xi Qu: West of the Tracks ## 09:11",
        "tt0395188": "Jeanne Marie Renée ## 12:00",
        "tt0410345": "Mystrio (Uno... dos... tres pilyos!) ## 16:39",
        "tt0424062": "Evolution of a Filipino Family ## 09:00",
        "tt0499428": "The Cloth Peddler ## 07:00",
        "tt0821950": "A Mosca cieca ## 17:15",
        "tt0843515": "Heremias: Unang aklat - Ang alamat ng prinsesang bayawak ## 09:00",
        "tt10037452": "Der fliegende Holländer ## 07:09",
        "tt10545556": "Ozalli Yillar ## 07:30",
        "tt10599470": "Israel, the Forbidden Journey ## 11:09",
        "tt10680738": "Kuriocity ## 07:41",
        "tt10798914": "Sdsdsdsdsdsds ## 10:00",
        "tt10844900": "Qw ## 23:42",
        "tt1094643": "Death in the Land of Encantos ## 09:00",
        "tt10958742": "Five-Year Diary ## 12:00",
        "tt11022238": "The Spectacular Spider-Man Trilogy (Responsibility, Repute and Requiem) ## 08:00",
        "tt11617492": "Orbius ## 09:30",
        "tt11765010": "Super Nova ## 22:05",
        "tt12176756": "Die Meistersinger von Nürnberg ## 08:15",
        "tt12176912": "Bayreuther Festspiele - Die Show Lohengrin ## 07:40",
        "tt12277054": "Carnets Filmés (Liste Complète) ## 21:23",
        "tt12416274": "#monalisa ## 11:03",
        "tt12424312": "De ma chambre d'hôtel ## 07:20",
        "tt12452858": "StabMovies: Behind the Mask ## 08:40",
        "tt12617172": "The Dominion War Chronicles ## 07:15",
        "tt12617800": "CoronaVirus: A Pandemic of the Mind ## 07:00",
        "tt1269566": "Melancholia ## 07:30",
        "tt1277455": "A Time to Stir ## 22:00",
        "tt12932540": "Alien Concubine ## 07:48",
        "tt13117718": "Gassmaniadi ## 08:00",
        "tt1356735": "Crude Oil ## 14:00",
        "tt1377817": "Welcome to New York ## 15:50",
        "tt1433078": "Amy's Night Out ## 11:15",
        "tt1447786": "Grandmother Martha ## 00:12",
        "tt1674154": "City of Eternal Spring ## 09:30",
        "tt1745901": "How Does David Lynch Do It? ## 06:00",
        "tt1757892": "The Life and Times of Allen Ginsberg Deluxe Set ## 11:20",
        "tt1806770": "American Fencer ## 12:41",
        "tt1823692": "Hollywood East ## 06:00",
        "tt1841612": "George Stevens' World War II Footage ## 07:00",
        "tt1866307": "World Peace & Prayer Day ## 16:00",
        "tt1867112": "UFOs and Close Encounters ## 08:20",
        "tt1885195": "Azgrab: The Documentary ## 03:49",
        "tt1895288": "A História de João e Zeca ## 10:05",
        "tt1910611": "Saving Julian ## 14:00",
        "tt2000421": "The New York Yankees: Fall Classic Collector's Edition 1996-2001 ## 14:25",
        "tt2008009": "The Clock ## 00:00",
        "tt2261469": "Double Fine Adventure ## 12:04",
        "tt2330754": "My Reflected Death ## 14:02",
        "tt2334994": "What Is Love? ## 09:05",
        "tt2355497": "Beijing 2003 ## 06:00",
        "tt2355499": "Chang'an Boulevard ## 10:13",
        "tt2659636": "Modern Times Forever ## 00:00",
        "tt2828546": "Sleep ## 08:00",
        "tt2846458": "The 8 Disc Matt Anderson Collection ## 11:43",
        "tt3096442": "The Soulless ## 07:30",
        "tt3201284": "Are We Famous Yet??? ## 10:25",
        "tt3317562": "Leviathan: The Story of Hellraiser and Hellbound: Hellraiser II ## 07:56",
        "tt3615052": "Empired ## 13:00",
        "tt3837350": "A 2nd generation film ## 03:17",
        "tt3963450": "NHL: Washington Capitals 10 Greatest Games ## 20:00",
        "tt3984388": "Close Up ## 08:20",
        "tt4346304": "Psychos DFLLL ## 13:00",
        "tt4390190": "Pink Noise ## 10:00",
        "tt4567170": "Breaking Yop ## 19:11",
        "tt4656672": "9 Hours ## 09:09",
        "tt4741454": "Raoul Wallenberg Tragic Hero or Agent 103? ## 12:00",
        "tt4833186": "Freedom & Unity: The Vermont Movie ## 08:40",
        "tt4842296": "A Lullaby to the Sorrowful Mystery ## 08:05",
        "tt5068890": "Hunger! ## 04:00",
        "tt5135246": "Saynatakuna: Masks ## 00:25",
        "tt5136218": "London EC1 ## 19:00",
        "tt5240738": "Ember Glow ## 11:00",
        "tt5275892": "O.J.: Made in America ## 07:47",
        "tt5305230": "CzechMate: In Search of Jirí Menzel ## 07:09",
        "tt5335720": "Animitas, 2014 ## 12:00",
        "tt5374716": "Chamisso's Shadow ## 12:00",
        "tt5375100": "Paint Drying ## 10:07",
        "tt5452954": "In Course of the Miraculous ## 09:00",
        "tt5942280": "The Nothing Movie ## 01:59",
        "tt5982192": "From Stage to Screen ## 15:00",
        "tt6086934": "World War II: Heroes & Villains ## 12:00",
        "tt6127010": "Funusion ## 00:00",
        "tt6150204": "Nieuwe Tieten ## 20:00",
        "tt6434210": "The Works and Days (of Tayoko Shiojiri in the Shiotani Basin) ## 08:00",
        "tt7017462": "Till We Age ## 08:00",
        "tt7156814": "The Innocence ## 21:00",
        "tt7321476": "h36: ## 12:00",
        "tt7442346": "Fan ## 10:23",
        "tt7521772": "24 Hour Psycho ## 00:00",
        "tt7528992": "Europa: The Last Battle ## 12:26",
        "tt7529390": "Pakistan: Education and Women ## 19:44",
        "tt7549254": "Sakhi ## 19:39",
        "tt7953946": "Early Women Filmmakers ## 10:53",
        "tt8273150": "Logistics ## 17:00",
        "tt8296608": "Dead Souls ## 08:15",
        "tt8307072": "Make Me Fly ## 10:23",
        "tt8677246": "Bullfighting Memories ## 18:20",
        "tt8690764": "Silence not silence, red not red, live not live ## 10:01",
        "tt8819192": "Women Make Film: A New Road Movie Through Cinema ## 14:00",
        "tt8842760": "Old and rare forms of craftsmanship ## 10:00",
        "tt8968058": "Cine Dreams: Future Cinema of the Mind ## 08:00",
        "tt8997670": "Wholy ## 11:00",
        "tt9047474": "La Flor ## 13:28",
        "tt9195252": "Report ## 08:00",
        "tt9552194": "The Freshman Experience ## 07:27",
        "tt9900018": "His Last Stand ## 16:30"
    }
}
```

#### Enabled ####
* Enabled JWT auth 
    - Being all are GET call, so AUTH not in use
* Enabled Logger with rotation(Will create a new log everyday)

#### ToDo ####
* TestCases


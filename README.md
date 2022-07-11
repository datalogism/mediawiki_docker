# mediawiki_docker

extends https://github.com/wikimedia/mediawiki-docker

## FIRST RUN

before all you need to be sure that docker is running : 
* ``` sudo systemctl enable docker ```
each time that you are building a new mediawiki clone you may need to : 
* delete all other container : ```docker rm -f $(docker ps -a -q)```
* delete all the volume : ```docker volume rm $(docker volume ls -q)```

Each mediawiki clone must be initialized as follow : 
* ``` sudo docker-compose -f docker-compose_begin.yml up ```
* go to http://localhost:8080/ > click on Setup Wiki
* Enter "database" as hostname / and MYSQL user name & password definied in docker-compose_begin.yml
> SAVE FILE in docker dir as the fr example

/!\ change if needed > add packages or delete some wfLoadSkin( 'MinervaNeue' ); for example get me errors

## FR example
* Maping between LocalSettings.php and LocalLanguageAdapted setting in docker-compose_fr.yml 
* sudo docker-compose -f docker-compose_fr.yml up -d --build --force-recreate 
* sudo docker run -it --rm mediawiki_custom /bin/bash 


## WHICH EXTENSION INSTALLING ?
https://fr.wikipedia.org/wiki/Special:Version

## Import

https://www.mediawiki.org/wiki/Manual:Importing_XML_dumps
https://www.mediawiki.org/wiki/Manual:ImportDump.php?tableofcontents=0

```
php importDump.php --conf ../LocalSettings.php /var/data/dumps/${lang}wiki-20220701-pages-articles-multistream.xml --username-prefix=""
files need to be decompressed... 
```

### issues 

* As said in this article : https://mindmachine.co.uk/write-up/write-ups/creating-a-local-copy-of-wikipedia/?v=86d8d92aba9e
loading an entiere wiki is very long > 14articles /sec
So for the En version it must take 6months...


## Test API

http://localhost:8080/api.php?action=query&format=json&prop=extracts&titles=1545



## TO DO 
* CAN WE AUTOMATE THE CREATION OF A WIKI ? 
php install.php --conf /var/www/html/LocalSettings_base.php --server http://localhost:8080 --pass dbpedia2022 --dbserver database --dbname my_wiki --installdbpass dbpedia2022 my_wiki wikiuser 

* Need to be tested with measure for en and fr 
-> Loading time
-> API requests answers time

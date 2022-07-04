# mediawiki_docker

extends https://github.com/wikimedia/mediawiki-docker

See https://blog.programster.org/deploy-your-own-mediawiki-wiki for more informations

## FIRST RUN
* ``` docker-compose rm --stop --force ```
* ``` sudo systemctl enable docker ```
* ``` sudo docker-compose -f docker-compose_begin.yml up ```
* go to http://localhost:8080/ > click on Setup Wiki
* Enter "database" as hostname / and MYSQL root password definied in docker-compose_begin.yml
> SAVE FILE in docker dir as the fr example
/!\ change if needed > add packages or delete some wfLoadSkin( 'MinervaNeue' ); for example get me errors
## FR example
* Maping between LocalSettings.php and LocalLanguageAdapted setting in docker-compose_fr.yml 
* sudo docker-compose -f docker-compose_fr.yml up -d --build --force-recreate 
* SUDO docker run -it --rm mediawiki_custom /bin/bash 


## WHICH EXTENSION INSTALLING ?
https://fr.wikipedia.org/wiki/Special:Version

## Import

https://www.mediawiki.org/wiki/Manual:Importing_XML_dumps
https://www.mediawiki.org/wiki/Manual:ImportDump.php?tableofcontents=0

```
var/www/html/maintenance# php importDump.php --conf ../LocalSettings.php /path_to/dumpfile.xml.gz --username-prefix=""
files need to be decompressed... 
```

## Test API

http://localhost:8080/api.php?action=query&format=json&prop=extracts&titles=1545



## TO DO 
* CAN WE AUTOMATE THE CREATION OF A WIKI ? 
php install.php --conf /var/www/html/LocalSettings_base.php --server http://localhost:8080 --pass dbpedia2022 --dbserver database --dbname my_wiki --installdbpass dbpedia2022 my_wiki wikiuser 

* Need to be tested with measure for en and fr 
-> Loading time
-> API requests answers time

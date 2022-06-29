# mediawiki_docker

extends https://github.com/wikimedia/mediawiki-docker

## FIRST RUN

* ``` sudo systemctl enable docker ```
* ``` sudo docker-compose -f docker-compose_begin.yml up ```
* docker-compose rm --stop --force

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

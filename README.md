# Mediawiki docker

extends https://github.com/wikimedia/mediawiki-docker
See https://blog.programster.org/deploy-your-own-mediawiki-wiki for more informations

## FIRST RUN : GENERATE A LocalSetting.php file

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

**An command line alternative exists !** : [use the install.php script](https://www.mediawiki.org/wiki/Manual:Install.php)

## /!\ CUSTUMIZING THE WIKI

All the extensions used in a wikipedia are generally listed into the SPecial:Version page of each wiki : 
* french one : https://fr.wikipedia.org/wiki/Special:Version

### DockerFile Settings

You will first need to install the interresting modules you want to integrate to your wiki as follow : 
https://github.com/datalogism/mediawiki_docker/blob/main/DockerFIles/Dockerfile_fr2
We generally install first basic packages for git/unzipping...
We also are installing then composer for building the modules that need to be. 
We finnaly add right for Lua engine.

Some modules need to configurated in the LocalSetting file :
* [Math]
```
$wgMathValidModes = array('source');
$wgDefaultUserOptions['math'] = 'source';
$wgMathDisableTexFilter = 'always';
```
* [TextExtracts](http://www.mediawiki.org/wiki/Extension:TextExtracts)
```
# Configuration for TextExtracts which removes noisy tags
$wgExtractsRemoveClasses = array( '.metadata', 'span.coordinates', 'span.geo-multi-punct', 'span.geo-nondefault', '#coordinates', '.reflist', '.citation', '#toc', '.tocnumber', '.references', '.reference', '.noprint');
```

* [Scribunto]

```
$wgTemplateDataUseGUI = false;
$wgScribuntoDefaultEngine = 'luastandalone'; # faster but needs configuration read http://www.mediawiki.org/wiki/Extension:Scribunto
$wgScribuntoEngineConf['luastandalone']['errorFile'] = 'lua_error.log';
```

## Updating the database schema

Some package are working on reshaped or new objects for it you may need to update de database with the following script: 
https://www.mediawiki.org/wiki/Manual:Update.php

## Loading a dump

A dump could be load with : https://www.mediawiki.org/wiki/Manual:ImportDump.php
A little wikipedia could be easily build in a day (the romanian for example), 
However with a large wiki like the English one the loading time of the entiere chapter very long (55 days at that rate to import the 55,000,000 pages (as of March 2022) in the English Wikipedia)



## Experiments made


* Maping between LocalSettings.php and LocalLanguageAdapted setting in docker-compose_fr.yml 
* sudo docker-compose -f docker-compose_fr.yml up -d --build --force-recreate 
* sudo docker run -it --rm mediawiki_custom /bin/bash 

## RO 
1091500
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

> PB : sanitized-css
> Extension:Translate + Extension:Campaigns
https://www.mediawiki.org/wiki/Extension:Wikibase_Client

## Test API

http://localhost:8080/api.php?action=query&format=json&prop=extracts&titles=1545


php importDump.php --conf ../LocalSettings.php --namespaces 10 /var/data/dumps/frwiki-20220620-pages-articles-multistream.xml

## TO DO 
* CAN WE AUTOMATE THE CREATION OF A WIKI ? 
php install.php --conf /var/www/html/LocalSettings_base.php --server http://localhost:8080 --pass dbpedia2022 --dbserver database --dbname my_wiki --installdbpass dbpedia2022 my_wiki wikiuser 

* Need to be tested with measure for en and fr 
-> Loading time
-> API requests answers time

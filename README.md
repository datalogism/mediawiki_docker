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

### LocalSetting file 

For increasing the memory capacity of the Wiki you could have to adjust the memory limit :  
```
ini_set('memory_limit', '1024M');
```
All the modules need to be activated as follow :
```
wfLoadExtension( 'CategoryTree' );
```
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
## RUNING YOUR CUSTOM DOCKER

For a french wiki : 
* Maping between LocalSettings.php and LocalLanguageAdapted setting in docker-compose_fr.yml 
```
sudo docker-compose -f docker-compose_fr.yml up -d --build --force-recreate 
```
For accesing to the container :
```
sudo docker run -it --rm mediawiki_custom /bin/bash 
```
## Updating the database schema

Some package are working on reshaped or new objects for it you may need to update de database with the following script from the container : 
https://www.mediawiki.org/wiki/Manual:Update.php

## Loading a dump

A dump could be load  from the container with (14articles /sec) :
* https://www.mediawiki.org/wiki/Manual:ImportDump.php
* https://www.mediawiki.org/wiki/Manual:Importing_XML_dumps
A little wikipedia could be easily build in a day (the romanian for example), 
However with a large wiki like the English one the loading time of the entiere chapter very long (55 days at that rate to import the 55,000,000 pages (as of March 2022) in the English Wikipedia)

For loading a dump do :
```
php importDump.php --conf ../LocalSettings.php /path_to/dumpfile.xml.gz
```

check also the option --namespaces / --skip-to that could be usefull for monitoring the load


## Experiments made

### Romanian wiki

Could be done in a day

### Loading only parsing material 

An alternative to the building of a complete could be to load only the modules and the template of a wiki :
```
> php importDump.php --conf ../LocalSettings.php --namespaces 10 /var/data/dumps/frwiki-20220620-pages-articles-multistream.xml
> php importDump.php --conf ../LocalSettings.php --namespaces 828 /var/data/dumps/frwiki-20220620-pages-articles-multistream.xml
```
I took a day for french wiki.

Unfortunatly by this way couldn't load wikibase depending data : 
https://www.mediawiki.org/wiki/Extension:Wikibase_Client

## Test API

http://localhost:8080/api.php?action=query&format=json&prop=extracts&titles=1545

## Parsing the French wiki with a mediawiki clone parser :

Using the action=parse API endpoint with contentmodel=wikitext & text=wikicode parameters,
the average parsing time of a page is equal to 0,17 sec by page it took almost 4 days for 4 087 249 pages.
 

FROM mediawiki:1.37

USER root
RUN apt-get update
RUN apt-get install -y --no-install-recommends apt-utils apt-utils git pigz pbzip2 bzip2 
#RUN mkdir -p /var/data/dumps
#COPY ./dumps /var/data/dumps/
#RUN chmod -R 755 /var/data/dumps
COPY LocalSettings_en.php /var/www/html/LocalSettings.php
COPY dumps /var/data/dumps
<<<<<<< HEAD
RUN bunzip2 /var/data/dumps/*.bz2
=======
RUN bunzip2 /var/data/*
RUN chmod -R 755 /var/data/dumps
>>>>>>> 99ce2c6dfcdec0471bdaa84b7aff80464de43a97
RUN chmod -R 755 includes
RUN chmod -R 775 extensions
RUN cd extensions && git clone https://github.com/wikimedia/mediawiki-extensions-Babel.git Babel --branch REL1_37
RUN cd extensions && git clone https://github.com/wikimedia/mediawiki-extensions-LabeledSectionTransclusion.git LabeledSectionTransclusion --branch REL1_37
RUN cd extensions && git clone https://github.com/wikimedia/mediawiki-extensions-Math.git Math --branch REL1_37
RUN cd extensions && git clone https://github.com/wikimedia/mediawiki-extensions-BiblioPlus.git BiblioPlus --branch REL1_37
RUN cd extensions && git clone https://github.com/wikimedia/mediawiki-extensions-Charinsert.git Charinsert --branch REL1_37
#RUN git clone https://gerrit.wikimedia.org/r/mediawiki/extensions/Babel.git --branch REL1_37
# LabeledSectionTransclusion
#RUN cd ./extensions && git clone https://gerrit.wikimedia.org/r/p/mediawiki/extensions/timeline.git && git clone https://gerrit.wikimedia.org/r/p/mediawiki/extensions/CharInsert.git && git clone https://gerrit.wikimedia.org/r/p/mediawiki/extensions/MobileFrontend.git && git clone https://gerrit.wikimedia.org/r/p/mediawiki/php/luasandbox.git  && git clone https://gerrit.wikimedia.org/r/p/mediawiki/extensions/GeoData.git && git clone https://gerrit.wikimedia.org/r/p/mediawiki/extensions/ExpandTemplates.git && git clone https://gerrit.wikimedia.org/r/p/mediawiki/extensions/Babel.git && git clone https://gerrit.wikimedia.org/r/p/mediawiki/extensions/Math.git && git clone https://gerrit.wikimedia.org/r/p/mediawiki/extensions/wikihiero.git && git clone https://gerrit.wikimedia.org/r/p/mediawiki/extensions/Mantle.git

# && git clone https://gerrit.wikimedia.org/r/p/mediawiki/extensions/CategoryTree.git 
# && git clone https://gerrit.wikimedia.org/mer/mediawiki/extensions/Cite.git
# && git clone https://gerrit.wikimedia.org/r/p/mediawiki/extensions/Interwiki.git 
# && git clone https://gerrit.wikimedia.org/r/p/mediawiki/extensions/SyntaxHighlight_GeSHi.git
# && git clone https://gerrit.wikimedia.org/r/p/mediawiki/extensions/InputBox.git
# && git clone https://gerrit.wikimedia.org/r/p/mediawiki/extensions/Scribunto.git
# && git clone https://gerrit.wikimedia.org/r/mediawiki/extensions/ParserFunctions.git
# && git clone https://gerrit.wikimedia.org/r/p/mediawiki/extensions/Poem.git
# && git clone https://gerrit.wikimedia.org/r/p/mediawiki/extensions/TextExtracts.git
#https://github.com/wikimedia/mediawiki-extensions-TextExtracts.git
# && git clone https://gerrit.wikimedia.org/r/p/mediawiki/extensions/ImageMap.git
RUN cd maintenance && php importDump.php --conf ../LocalSettings.php /var/data/dumps/*xml --username-prefix=""

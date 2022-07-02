FROM mediawiki:1.37

USER root
RUN apt-get update
RUN apt-get -y install git pigz pbzip2 bzip2
ADD dumps /dumps/
RUN chmod -R +x dumps
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

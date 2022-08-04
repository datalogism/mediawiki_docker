#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 14:14:12 2022

@author: cringwal
"""


        
import xml.etree.ElementTree as ET
from multiprocessing import Manager
import requests
from os.path import exists
import time

def getParsedHTML(wikicode):
    result=""
    data ={"action":"parse","format":"json","contentmodel":"wikitext","text":wikicode}
    r = requests.post(url,  data=data) 
    if(r.status_code == 200):
        result=r.json()
        result=result["parse"]["text"]["*"]
    return result 

def returnParserError(txt):
    regex = r"<strong class=\"error\">(.+?)</strong>"
    matches = re.finditer(regex, txt, re.MULTILINE)
    error_list=[]
    
    for matchNum, match in enumerate(matches, start=1):
        error=match.group()
        idx=match.start()/size
        clean_idx=round(idx,2) 
        clean_error=re.sub('<[^>]*>', '', error)
        error_list.append({"idx":clean_idx,"error":clean_error})
    return error_list
    
def saveRepport(id_,data):
    path_repport="/user/cringwal/home/Desktop/DBpedia_tests/ParseWikipedia/repport/"
    with open(path_repport+str(id_)+'.json', 'w') as outfile:
        json.dump(data, outfile)
def saveHTML(id_,title,html_content):
    path_HTML="/user/cringwal/home/Desktop/DBpedia_tests/ParseWikipedia/HTML/"
    wrapped_html='''<html>
        <head>
        <title>'''+title+'''</title>
        </head> 
        <body>
        '''+html_content+'''
        </body>
        </html>'''
    try : 
        with open(path_HTML+str(id_)+".html", 'wb') as f:
            f.write(bytes(wrapped_html, encoding='utf8'))
    except:
        return False
    return True

if __name__ == "__main__":
    file_path = "/user/cringwal/home/Desktop/GSOC/mediawiki_docker/dumps/fr/frwiki-20220620-pages-articles-multistream.xml"
    path_HTML="/user/cringwal/home/Desktop/DBpedia_tests/ParseWikipedia/HTML/"
    page = None
    tags_stack = None
    queue = queue
    index=0
    #fromidx=0
    for event, element in ET.iterparse(file_path, events=('start', 'end')):
        tag_name = element.tag.rsplit("}", 1)[-1].strip()
        if event == "start":
            if tag_name == "page":
                page = {"title": "", "text": "","id": "","ns":"-1"}
                tags_stack = []

            if page is not None:
                tags_stack.append(tag_name)
        else:  # elif event == "end"
            if page is not None:
                if tags_stack[-1] == "ns":
                    page['ns'] = element.text
                if tags_stack[-1] == "id":
                    page['id'] = element.text
                if tags_stack[-1] == "title":
                    page['title'] = element.text
                elif tags_stack[-1] == "text":
                    if(element.text and element.text!=""):
                        page['text'] = element.text
                    else:
                        page['text'] = ""
                if tags_stack[-1] == "page":
                    if(page['ns']=="0"):
                        if(page['text']!=""):
                            index += 1
                            print(index)
                            file_exists = exists(path_HTML+str(page['id'])+".html")
                            error_repport={"text":1,"parsing":[],"time":0,"saved":}
                            if(page['text']=""):
                                error_repport["text"]=0
                            else:
                                if(!file_exists):
                                    start_time = time.time()
                                    html=getParsedHTML(page['text'])
                                    saved=saveHTML(str(page['id']),str(page['title']),html)
                                    stop_time = time.time()    
                                    time_diff = stop_time - start_time
                                    repport=returnParserError(html)
                                    saveRepport(str(page['id']),repport)
                            page = None
                else:
                    del tags_stack[-1]
                    
              # we should clear element object, otherwise memory will be filled quickly
            element.clear()
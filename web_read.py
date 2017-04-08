#!/usr/bin/env python 
#coding:utf-8 

import urllib2  
response = urllib2.urlopen('http://0.0.0.0:8080/')  
html = response.read()  
print html 
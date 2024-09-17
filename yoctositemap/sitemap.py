import re
from datetime import datetime, date
from enum import Enum

from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

class YoctoSitemapWrongURL(Exception):
    pass

class YoctoSitemapWrongArguments(Exception):
    pass

class Changefreq(Enum):
    ALWAYS = 1
    HOURLY = 2
    DAILY = 3
    WEEKLY = 4
    MONTHLY = 5
    YEARLY = 6
    NEVER = 7

    def __str__(self):
        r = ''
        match self.value:
            case 1:
                r = 'always'
            case 2:
                r = 'hourly'
            case 3:
                r = 'daily'
            case 4:
                r = 'weekly'
            case 5:
                r = 'monthly'
            case 6:
                r = 'yearly'
            case 7:
                r = 'never'
        return r

class URL():
    def __init__(self, url, lastmod: datetime|str = None, changefreq: Changefreq = None, priority: float = None):
        self.url = url
        self.lastmode = lastmod
        self.changefreq = changefreq
        self.priority = priority

        if priority:
            if self.priority < 0 or self.priority > 1.0:
                raise YoctoSitemapWrongArguments("Wrong argument value: priority")


    def get_url(self):
        return self.url

    def get_last_mod(self):
        if self.lastmode:
            if isinstance(self.lastmode, datetime):
                return self.lastmode.strftime('%Y-%m-%d')
            elif isinstance(self.lastmode, date):
                return self.lastmode.strftime('%Y-%m-%d')
            else:
                return self.lastmode
        else:
            return None

    def get_changefreq(self):
        if self.changefreq:
            return str(self.changefreq)
        else:
            return None

    def get_priority(self):
        if not self.priority == None:
            return str(self.priority)
        else:
            return None

class Sitemap():
    def __init__(self):
        self.urls = []
        self.re_xml_firstline = re.compile(r'<\?xml\s+\S+\s+\?>', re.I)
        self.first_line = '<?xml version="1.0" encoding="UTF-8"?>'

    def add(self, url: URL):
        self.urls.append(url)

    def generate(self):
        urlset = Element('urlset')
        urlset.set('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')

        for url in self.urls:
            child_url = SubElement(urlset, 'url')
            url_loc = SubElement(child_url, 'loc')
            url_loc.text = url.get_url()

            if temp := url.get_last_mod():
                url_lastmod = SubElement(child_url, 'lastmod')
                url_lastmod.text = temp

            if temp := url.get_changefreq():
                url_changefreq = SubElement(child_url, 'changefreq')
                url_changefreq.text = temp

            if (temp := url.get_priority()) != None:
                url_priority = SubElement(child_url, 'priority')
                url_priority.text = temp

        reparsed = minidom.parseString(tostring(urlset, 'utf-8'))
        result = reparsed.toprettyxml(indent="  ")

        result = re.sub(self.re_xml_firstline, self.first_line, result)

        return result
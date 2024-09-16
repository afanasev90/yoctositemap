import re

from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

from yoctositemap.url import URL
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

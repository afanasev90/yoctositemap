from datetime import datetime, date

from yoctositemap.utils import Changefreq
from yoctositemap.exceptions import *
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
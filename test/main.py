from yoctositemap.sitemap import *
from yoctositemap.url import *

if __name__ == "__main__":
    print("Starting tests...")

    sm = Sitemap()
    url1 = URL("https://example.com/", datetime.now(), Changefreq.DAILY, 0.7)
    url2 = URL("https://example.com/post/1/", datetime.now(), Changefreq.YEARLY, 0.5)
    url3 = URL("https://example.com/post/2/", '2022-02-03', None, 0)

    sm.add(url1)
    sm.add(url2)
    sm.add(url3)
    #sm.generate()
    print(sm.generate())
from scrapy.cmdline import execute

import sys
import os

# print(__file__)
print(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute(['scrapy', 'crawl', 'blogs'])
execute(['scrapy', 'crawl', 'cnblog'])

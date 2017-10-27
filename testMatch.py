# -*- coding: UTF-8 -*-
import re
str = """<a id="pageNext" class="next" href="/bizhi/245_1031_2.html" title="点击浏览下一张壁纸，支持键盘'&rarr;'翻页"></a>"""
match = r"<a.*?href=(.*)?<\/a>";
print match
next = re.findall(match, str,)
print next[0]
print len(next)
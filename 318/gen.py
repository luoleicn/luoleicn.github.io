#!/usr/bin/python
#coding=utf8

header = """---
layout: github
title: 川藏线骑行多图慎入
---

# 川藏线骑行照片

点击图片跳转到下一页
"""

for i in range(2, 42):
    content ="[![image](http://www.luolei.site/source/images/318-{}.jpg)](http://www.luolei.site/318/318-{})".format(i, i + 1)
    writer = open("318-" + str(i) + ".md", "w")
    writer.write(header + "\n" + content)
    writer.close()


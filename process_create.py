#!python
print("Content-Type: text/html")
print()

import cgi
form = cgi.FieldStorage()
title = form["title"].value
description = form['description'].value

print(title, description)

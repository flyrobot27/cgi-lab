#!/usr/bin/env python3
import os
import json
print("Content-Type: text/html\r\n\r\n")
print("<!doctype html><title>Hello</title>\r\n<h2>hello world</h2>\r\n")

#Q1
jsonObject = json.dumps(dict(os.environ), indent=4)
#print(jsonObject)
print("\r\n")

#Q2
for keys, value in os.environ.items():
    if (keys == "QUERY_STRING"):
        print("<b>{0:20}</b>: {1}<br>".format(keys, value))

#Q3
for keys, value in os.environ.items():
    if (keys == "HTTP_USER_AGENT"):
        print("<b>{0:20}</b>: {1}<br>".format(keys, value))
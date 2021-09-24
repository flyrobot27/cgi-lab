#!/usr/bin/env python3
import os

def test_cookies():
    print("Set-Cookie:UserID = steven\r\n")
    print("Set-Cookie:Password = 12345\r\n")
    print("Set-Cookie:Expires = Tuesday, 31-Dec-2007 23:12:40 GMT;\r\n")
    print("Set-Cookie:Domain = www.tutorialspoint.com;\r\n")
    print("Content-type:text/html\r\n\r\n")
    print("<html>")
    print("<head>")
    print("<title>COOKIES SET - First CGI Program</title>")
    print("</head>")
    print("<body>")
    print("<h2>All Done!</h2>")
    print("</body>")
    print("</html>")

    try:
        value = os.environ["HTTP_COOKIE"]
        print("<b>{0:20}</b>: {1}<br>".format("HTTP_COOKIE", value))
    except KeyError:
        pass

test_cookies()
try:
    value = os.environ["HTTP_COOKIE"]
    print("<b>{0:20}</b>: {1}<br>".format("HTTP_COOKIE", value))
except KeyError:
    pass

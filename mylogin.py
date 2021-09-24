#!/usr/bin/env python3

import cgi

form = cgi.FieldStorage()

username = form.getvalue("username")
password = form.getvalue("password")

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - Second CGI Program</title>")
print("</head>")
print("<body>")
print("<p><b>Username</b> {0} <b>password</b> {1} </p>".format(username, password))
print("</body>")
print("</html>")
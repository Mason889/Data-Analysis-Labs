#!/usr/local/bin/python3
print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers
print("<TITLE>CGI script output</TITLE>")
print("<H1>This is my first CGI script</H1>")
import cgitb

cgitb.enable(display=0)

form = cgi.FieldStorage()
data = form.getvalue('search_query')

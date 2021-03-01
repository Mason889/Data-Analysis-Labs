#!/usr/bin/python3.8
print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers
print("<TITLE>CGI script output</TITLE>")
print("<H1>This is my first CGI script</H1>")
import cgi, cgitb

cgitb.enable()

form = cgi.FieldStorage()
query = form.getvalue('search_query')
source =  form.getvalue('seach_src')

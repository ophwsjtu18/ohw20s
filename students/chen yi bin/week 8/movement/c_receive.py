import cgi,cgitb
form=cgi.FieldStorage()
move=form.getvalue('move')
place=form.getvalue('place')


print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print("<meta charset=\"utf-8\">")
print("<title>test</title>")
print("</head>")
print("<body>")
print("<h2>%s:%s</h2>"%(move,place))
print("</body>")
print("</html>")
with open('../htdocs/'+ move +'.txt','v') as text:
    text.write(f'{place}')

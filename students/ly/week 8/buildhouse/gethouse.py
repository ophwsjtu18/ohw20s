#!C:\Users\lenovo\AppData\Local\Programs\Python\Python37\python.exe


import cgi, cgitb

form =cgi.FieldStorage()

BUILDHOUSE=form.getvalue('BUILDHOUSE')
X=form.getvalue('X')
Y=form.getvalue('Y')
Z=form.getvalue('Z')
L=form.getvalue('L')
W=form.getvalue('W')
H=form.getvalue('H')

print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print("<meta charset=\"utf-8\">")
print("<title>minecraft buildhouse</title>")
print("</head>")
print("<body>")
print("<h2>%s:%s:%s:%s:%s:%s:%s</h2>" % (BUILDHOUSE,X,Y,Z,L,W,H))
print("</body>")
print("</html>")
with open('../htdocs/'+BUILDHOUSE+'.txt','w') as f:
    f.write(X+','+Y+','+Z+','+L+','+W+','+H)

#!C:\Users\Huawei\AppData\Local\Programs\Python\Python37\python.exe
#codint=utf-8
import cgi, cgitb

form =cgi.FieldStorage()

house=form.getvalue('house')
X=form.getvalue('X')
Y=form.getvalue('Y')
Z=form.getvalue('Z')
L=form.getvalue('L')
W=form.getvalue('W')
H=form.getvalue('H')
#map=[[0.5,0.5]for x in range(10)]
#print (map)
print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print("<meta charset=\"utf-8\">")
print("<title>minecraft buildhouse</title>")
print("</head>")
print("<body>")
print("<h2>%s:%s:%s:%s:%s:%s:%s</h2>" % (house,X,Y,Z,L,W,H))
print("</body>")
print("</html>")
with open('../htdocs/'+house+'.txt','w') as f:
    f.write(X+','+Y+','+Z+','+L+','+W+','+H)

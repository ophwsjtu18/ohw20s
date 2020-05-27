#!C:\Users\dell\AppData\Local\Programs\Python\Python37\python.exe
#coding=utf-8
import cgi,cgitb
form=cgi.FieldStorage()
house_length=form.getvalue('house_length')
house_width=form.getvalue('house_width')
house_height=form.getvalue('house_height')
#map=[[0,5,0,5]for x in range(10)]
#pring(mapprint("Content-type:text/html")
print()
print("<html>")
print("<head>")
print("<meta charset=\"utf-8\">")
print("<title>moocxing</title>")
print("</head>")
print("<body>")
print("<h2>%s:%s:%s</h2>" % (house_length,house_width,house_height))
print("</body>")
print("</html>")
with open('../htdocs/house_build.txt','w') as f:
       f.write(house_length+','+house_width+','+house_height)

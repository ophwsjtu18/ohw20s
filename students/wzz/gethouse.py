#!C:\Users\knc_w\AppData\Local\Programs\Python\Python37\python.exe
#coding=utf-8
import cgi, cgitb


form = cgi.FieldStorage()

length = form.getvalue('length')
height = form.getvalue('height')
width = form.getvalue('width')
#map=[[0.5,0.5]for x in range (10)]
#print (map)
print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print("<meta charset=\"utf-8\">")
print("<title>mooc</title>")
print("</head>")
print("<body>")
print("<h2>%s:%s:%s</h2>" % (height,width,length))
print("</body>")
print("</html>")
with open('../htdocs/height.txt','w') as f1:
    f1.write(f'{height}')
with open('../htdocs/length.txt','w') as f2:
    f2.write(f'{length}')
with open('../htdocs/width.txt','w') as f3:
    f3.write(f'{width}')
    

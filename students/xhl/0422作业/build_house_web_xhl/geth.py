#!C:\Users\10369\AppData\Local\Programs\Python\Python37\python.exe
#coding=utf-8
import cgi, cgitb

form = cgi.FieldStorage()

house = form.getvalue("house")
housex = form.getvalue("housex")
housey = form.getvalue("housey")
housez = form.getvalue("housez")
#map=[[0.5,0.5]for x in range (10)]
#print (map)
print ("Content-type:text/html")
print ()
print ("<html>")
print ("<head>")
print ("<meta charset=\"utf-8\">")
print ("<title>build house</title>")
print ("</head>")
print ("<body>")
print ("<h2>(%s,%s,%s)</h2>" % (housex,housey,housez))
print ("</body>")
print ("</html>")
with open('../htdocs/house.txt','w') as f:
    f.write(f'{house}')
with open('../htdocs/x.txt','w') as f:
    f.write(f'{housex}')
with open('../htdocs/y.txt','w') as f:
    f.write(f'{housey}')
with open('../htdocs/z.txt','w') as f:
    f.write(f'{housez}')


#!C:\Users\87903\AppData\Local\Programs\Python\Python37\python.exe
#coding=utf-8
import cgi, cgitb

form=cgi.FieldStorage()

mc_move=form.getvalue('mc_move')
mc_dir=form.getvalue('mc_dir')


print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print("<meta charset=\"utf-8\">")
print("<title>myhtml</title>")
print("</head>")
print("<body>")
print("<h2>%s:%s</h2>"%(mc_move,mc_dir))
print("</body>")
print("</html>")
with open('../htdocs/'+mc_move+'.txt','w') as f:
    f.write(f'{mc_dir}')

#!C:\Users\w'm'h\AppData\Local\programs\Python\Python37\python.exe
import cgi,cgitb

form=cgi.FieldStorage()

mc_house=form.getvalue('mc_move')
mc_l=form.getvalue('mc_l')
mc_w=form.getvalue('mc_w')
mc_h=form.getvalue('mc_h')

print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print("<meta charset=\"utf_8\">")
print("<title>moocxing</title>")
print("</head>")
print("<body>")
print("<h2>%s:%s:%s:%s</h2>" % (mc_house,mc_l,mc_w,mc_h))
print("</body>")
print("</html>")
with open('../htdocs/'+mc_house+".txt",'w') as f:
    f.write(mc_l+','+mc_w+','+mc_h)

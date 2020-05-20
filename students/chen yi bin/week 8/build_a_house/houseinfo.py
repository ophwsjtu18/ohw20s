import cgi, cgitb
form = cgi.FieldStorage()
house = form.getvalue("house")
housex = form.getvalue("x")
housey = form.getvalue("y")
housez = form.getvalue("z")



print ("Content-type:text/html")
print ()
print ("<html>")
print ("<head>")
print ("<meta charset=\"utf-8\">")
print ("<title>build_a_house</title>")
print ("</head>")
print ("<body>")
print ("<h2>(%s,%s,%s)</h2>" % (x,y,z))
print ("</body>")
print ("</html>")
with open('../htdocs/house.txt','w') as file1:
    file1.write(f'{house}')
with open('../htdocs/x.txt','w') as file2:
    file2.write(f'{housex}')
with open('../htdocs/y.txt','w') as file3:
    file3.write(f'{housey}')
with open('../htdocs/z.txt','w') as file4:
    file4.write(f'{housez}')

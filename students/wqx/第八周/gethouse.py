#! D:\python3.7\python.exe
#coding = utf-8
import cgi,cgitb
form = cgi.FieldStorage()
mc_house = form.getvalue('mc_house')
mc_houselocation = form.getvalue('mc_houselocation')
#map = [[0.5,0.5]for x in range(10)]
#print(map)
print('Content-type:text/html')
print()
print('<html>')
print('<head>')
print('<meta charset=\"utf-8\">')
print('<title>moocxing</title>')
print('</head>')
print('<body>')
print('<h2>%s:%s</h2>' % (mc_house,mc_houselocation))
print('</body>')
print('</html>')
with open('../htdocs/'+mc_house+'.txt','w') as f:
    f.write(f'{mc_houselocation}')
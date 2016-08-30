# coding:utf-8
import urllib
 
domain = 'http://www.liaoxuefeng.com'      
path = r'D:\Users\ryh\Desktop\\' 
 
Input = open(r'D:\Users\ryh\Desktop\0.html', 'r')
head = Input.read()
 
f = urllib.urlopen("http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000")
home = f.read()
f.close()
 
geturl = home.replace("\n", "")
geturl = geturl.replace(" ", "")

ist = geturl.split(r'em;"><ahref="')[1:]
 
ist.insert(0, '/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000">')
 
for li in ist: 
   
    url = li.split(r'">')[0]
    url = domain + url       
    print url
    f = urllib.urlopen(url)
    html = f.read()
 

    title = html.split("<title>")[1]
    title = title.split(" - 廖雪峰的官方网站</title>")[0]
 

    title = title.decode('utf-8').replace("/", " ")
 
 
    html = html.split(r'<!-- block main -->')[0]
    html = html.split(r'<h4>您的支持是作者写作最大的动力</h4>')[0]
    html = html.replace(r'src="', 'src="' + domain)
 

    html = head + html+"</body></html>"
 
 
    output = open(path + "%d" % ist.index(li) + title + '.html', 'w')
    output.write(html)
    output.close()

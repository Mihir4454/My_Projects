import requests
import bs4
my_lst = []
url = "http://www.gseb.org/3015ecruosnepo/gen/G{x}/{y}{w}/G{x}{y}{w}{z}{v}.html"

for a in range(36,37):
    for b in range(7,8):
        for d in range(5,6):
            for c in range(7,10):
                for e in range(0,10):
                    std_url = url.format(x = a,y = b,z = c,w = d,v = e)
                    
                    req = requests.get(str(std_url))
                    soup1 = bs4.BeautifulSoup(req.text,"lxml")
                    std_data = soup1.select("span")[4].getText()[9:] 
                    if 'ELIGIBLE FOR QUALIFYING' not in std_data:
                        mydata = soup1.select("span")[1].getText()[6:] +"."+soup1.select("span")[0].getText()[9:]
                        my_lst.append(mydata)
for i in my_lst:
    f = open("student_data.txt", "a")
    f.write(str(i))
    f.write('\n')
    f.close()
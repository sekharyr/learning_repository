files = ['a.txt', 'b.txt', 'c.txt']
content=['this is terralogic','i am software engineer','work from home']

def readfile(iters):
    f = open(iters, "r")
    print(f.read())
    f.close()




def writefile(files):
    f = open(files, "a")
    f.write()
    f.close()


 map(readfile, files)


map(writefile,files,content)
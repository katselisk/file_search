import os



mydir = input('enter the path to search :')
arxio = input('give the file name to search :')

arxio = arxio.upper()

L= []
def psaxe(mydir):
    for file in os.listdir(mydir):
        file = str(file.upper())
        if file.find(arxio) >= 0:
            print(os.path.join(file))
            L.append(str(os.path.join(mydir, file)))
        
        else :
            f = f"{mydir}/{file}"
            try :
                psaxe(f)
                # print(f)
            except Exception: 
                continue
             
    return L

mylist = psaxe(mydir)

print('**'* 20)
for i in mylist:
    print(i)

input('Search completed')


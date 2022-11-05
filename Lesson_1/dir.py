import os

def print_dir(path,lvl):
    print('\t'*(lvl-1)+'|'+os.path.split(path)[-1])
    files=os.listdir(path)
    for file in files:
        if os.path.isdir(path+"\\"+file):
            print_dir(path+"\\"+file,lvl+1)
        else:
            print('\t'*lvl+file)


print_dir(r'C:\Users\Nitro5\Downloads',1)

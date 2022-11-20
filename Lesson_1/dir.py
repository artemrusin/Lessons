import os

def print_dir(path,lvl,print_all_info=False,print_part_info=False):
    files=os.listdir(path)
    print('\t'*(lvl-1)+'├'+os.path.split(path)[-1])
    if print_part_info:
        x=0
        y=0 
        for file in files:
            if os.path.isdir(path+"\\"+file):
                y+=1
            else:
                x+=1
        print('\t'*(lvl-1)+'│'+f'Файлов: {x},\n'+'\t'*(lvl-1)+f'│Папок: {y}')
        y1=y

    if print_part_info and y1==0:
        pass
    else:
        print('\t'*(lvl-1)+'└'+'─'*7+'┐')
        x=0
        y=0
        for file in files:
            if os.path.isdir(path+"\\"+file):
                files,dirs=print_dir(path+"\\"+file,lvl+1,print_part_info=print_part_info)
                x+=files
                y+=dirs+1
            else:
                print('\t'*lvl+'├'+file) if not print_part_info else 1
                x+=1
        print('\t'*(lvl-1)+'┌'+'─'*7+'┘')
    if lvl==1 and print_all_info:
        print(f'Файлов: {x},\nПапок: {y+1}') 
    else:
        return x,y

print_dir(r'C:\Users\Nitro5\Desktop\Новая папка (2)',1)


#│ └ ─ ├ ┘ ┰

#┯ ┰ ┳

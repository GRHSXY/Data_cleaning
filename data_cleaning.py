import os
path = "F:/FileRecv/大二下/大创-auto-ppt-自然语言处理/NLP/论文/txt/txt"
fileList = os.listdir(path)
#print(fileList)


new_list=[]

#for file in fileList:
#    print(file)

for file in fileList:
    if file != "data_cleaning.py":
        with open(file,encoding='UTF-16 LE',errors='ignore') as f:
            contents=f.readlines()
            for line in contents:
                if '\n' in line and len(line)==1:
                    line=line.replace('\n','')
                if ' ' in line:
                    line=line.replace(' ','')
                new_list.append(line)

        with open('a_1.txt','a',encoding='UTF-16 LE',errors='ignore') as f:
            f.writelines(new_list)
        os.remove(file)
        os.rename('a_1.txt',file)

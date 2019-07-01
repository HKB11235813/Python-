import os
import shutil
def del_emp_dir(path):
    for (root, dirs, files) in os.walk(path):
        for item in dirs:
            print('搜寻的dir为：'+item)
            if item == 'PDFS' or item == 'jpg':
                continue
            else:
                dir = os.path.join(root, item)
                try:
                    shutil.rmtree(dir)
                    #os.rmdir(dir)  #os.rmdir() 方法用于删除指定路径的目录。仅当这文件夹是空的才可以, 否则, 抛出OSError。
                    print(dir+'文件夹删除成功!')
                except Exception as e:
                    print('Exception',e)
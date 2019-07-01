import os
import shutil
from removeEmty import del_emp_dir

# shutil模块主要是用于拷贝文件

# 进入文件夹
def InFile(CLD_Path):
    Root_file = os.listdir(CLD_Path)
    for partment_list in Root_file:
        files_list = os.listdir(CLD_Path+'/'+partment_list)
        for filePersonName in files_list:
            # 开始分类文件
            #CLD(CLD_Path+'/'+partment_list+'/'+filePersonName, CLD_Path+'/'+partment_list+'/'+filePersonName)
            # 文件分类完成以后，删除空的文件夹，当执行完一次后可能清不完，请注释掉CLD一直清到控制台只打出搜寻dir和pdf
            del_emp_dir(CLD_Path+'/'+partment_list+'/'+filePersonName)

def CLD(filePersonName, rootDir):

    # 遍历这个文件夹
    for root, dirs, files in os.walk(filePersonName):
        # 如果是文件则获取类型移动
        for file in files:

            # 取得当前文件名称的格式，（切分文件名，取最后的列表元素）
            file_type = file.split('.')[-1]

            # 在rootDir(即人名文件下)创建一个以文件类型为名的文件夹
            subdir = os.path.join(rootDir, '%s' % file_type)
            print('这个文件会存入的目录:' + subdir)
            # 如果这个分类文件夹不存在则新建文件夹
            if not os.path.exists(subdir):
                os.mkdir(subdir)

            # 进入分类文件夹
            os.chdir(subdir)
            if os.path.exists(file):
                # 如果文件夹存在当前文件，则跳过
                #os.remove(file)
                continue
            else:
                # 返回之前文件夹进行归类
                print("即将返回的根目录为：" + root)
                os.chdir(root)
                # shutil.move(源文件，指定路径):递归移动一个文件
                shutil.move(file, subdir)
                print("移动"+file+"文件成功")

        # 如果当前是文件夹，则进入文件夹
        for dir in dirs:
            #如果文件夹为medical report，则直接干掉!
            if dir == 'medical report':
                medicaDir = os.path.join(root, dir)
                try:
                    shutil.rmtree(medicaDir)
                except Exception as e:
                    print('Exception', e)
            else:
                print("递归的目录为:"+root+'/'+dir)
                CLD(root+'/'+dir, rootDir)

if __name__ == '__main__':
    InFile('F:/实习工作/2. DQ045')
    InFile('F:/实习工作/3. DQ046')
    InFile('F:/实习工作/4. DQ047')
    InFile('F:/实习工作/5. DQ048')
    InFile('F:/实习工作/6. DQ049')
    InFile('F:/实习工作/7. DQ050')
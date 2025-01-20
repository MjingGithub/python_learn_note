#!/usr/bin/python
# Filename : backup_sys.py

import os
import time 

source_dir = ['D:\\4px_work\\MyNote\\AI学习\\python知识']

backup_dir ='D:\\4px_work\\MyNote\\AI学习\\python知识\\backup'

target = backup_dir+os.sep+time.strftime('%Y%m%d%H%M%S')+'.zip'

if not os.path.exists(backup_dir):
    os.mkdir(backup_dir)

# 5. 我们使用 zip 命令将文件打包成 zip 格式
zip_command = 'zip -r {0} {1}'.format(target,
' '.join(source_dir))

# 运行备份
print('Zip command is:')
print(zip_command)
print('Running:')

if os.system(zip_command)==0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')


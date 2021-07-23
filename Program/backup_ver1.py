import os
import time
# 1.The files and directories to be backup are specified in a list.
# Example on Linux: source = ['/Users/robin/notes']
source = ['C:\\Users\\50855\\PycharmProjects']
# 2.The backup must be stored in a main backup directory.
# Example on Linux:target_dir = '/Users/robin/backup'
target_dir = 'E:\\50855\\py_backup'
# 3.The files are backed up into a zip file.
# 4.The name of zip archive is the current date and time.
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') \
    + '.zip'
# Create target directory if it is not present.
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# 5.We use the zip command to put the files in a zip archive.
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

# Run the backup
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')

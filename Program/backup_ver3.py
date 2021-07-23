import os
import time
# 1.The files and directories to be backup are specified in a list.
# Example on Linux: source = ['/Users/robin/notes']
source = ['C:\\Users\\50855.PDC\\PycharmProjects\\helloworld']
# 2.The backup must be stored in a main backup directory.
# Example on Linux:target_dir = '/Users/robin/backup'
target_dir = 'E:\\50855\\py_backup'
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    print('Successful created directory.', target_dir)
# 3.The files are backed up into a zip file.
# 4.The current day is the name of the subdirectory in the main directory.
today = target_dir + os.sep + time.strftime('%Y%m%d')
# The current time is the name of the zip archive.
now = time.strftime('%H%M%S')
# The name of the zip file.
comment = input('Enter a comment -->')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
             comment.replace(' ', '_') + '.zip'
    print('Successful entered comment.', comment)
# Create the subdirectory if it isn't already there.
if not os.path.exists(today):
    os.mkdir(today)
    print('Successful created directory.', today)
# 5.We use the zip command to put the files in a zip archive.
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))
# Run the backup.
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')

import os

base = '/Users/hanjitsai/Downloads/'
dirs = os.listdir('/Users/hanjitsai/Downloads/')
for i in range(len(dirs)):
    os.system('trash ' + os.path.join(dirs[i], str(dirs[i])))

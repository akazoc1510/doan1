import os
import shutil
os.system('python camera.py')
remove_path = "runs"
if os.path.exists(remove_path):
    shutil.rmtree(remove_path)
os.system('python detect.py --source getBike.png --save-crop')
os.system('python import_data.py')
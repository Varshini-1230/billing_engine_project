#rmdir is used to delete a folder if it does not have any content
import os
#os.rmdir("new_folder")

#shutil is used to delete the folder if the folder has some content
import shutil
shutil.rmtree("new_folder")

from pathlib import Path
Path("new_folder").rmdir()


#using "with" we can open the file here it will close the file automatically
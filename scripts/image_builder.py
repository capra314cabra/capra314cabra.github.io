import os
import glob
import shutil

images = glob.glob("./contents/**/*.png") + glob.glob("./contents/**/*.svg")
for image in images:
    copy_to = os.path.basename(image)
    shutil.copyfile(image, "./publish/" + copy_to)
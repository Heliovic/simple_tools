from PIL import Image
import glob
import os
import math

src_dir = 'src'
out_dir = 'out'


def img_compress(threshold):
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    filenames = glob.glob(src_dir + '/*')
    # print(filenames)

    for filename in filenames:
        outfile_name = filename.replace(src_dir, out_dir)
        img = Image.open(filename)
        x, y = img.size
        file_size = os.path.getsize(filename)
        k = math.sqrt(file_size / (threshold * 500))
        x1 = int(x / k)
        y1 = int(y / k)
        img = img.resize((x1, y1), Image.ANTIALIAS)
        img.save(outfile_name)
        newfile_size = os.path.getsize(outfile_name)
        print('[' + outfile_name + ']', '\tSIZE:', '%.2fKB' % (newfile_size / 1024), '\tRATE:', '%.2f%%' % (newfile_size / file_size * 100))


img_compress(256)

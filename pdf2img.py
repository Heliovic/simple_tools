from pdf2image import convert_from_path
import os

src_dir = 'src'
out_dir = 'out'

if not os.path.exists(out_dir):
    os.makedirs(out_dir)
for root, dirs, filenames in os.walk(src_dir):
    for filename in filenames:
        images = convert_from_path(src_dir + '/' + filename)
        out_file_dir = out_dir + '/' + os.path.splitext(filename)[0]
        if not os.path.exists(out_file_dir):
            os.makedirs(out_file_dir)
        for idx, img in enumerate(images):
            print('[CONVERTING]', filename, 'Page:', idx + 1)
            img.save(out_file_dir + '/%s_%s.jpg' % (filename.replace('.pdf', ''), idx + 1))
        print('[DONE]', filename)

from PIL import Image

image_1 = Image.open(r'"C:\Users\Jaykumar Panchal\Pictures\Screenshots\3rd_sem_marksheet.png"')
im_1 = image_1.convert('RGB')
im_1.save(r'C:\Users\Jaykumar Panchal\Documents\python\marksheet.pdf')
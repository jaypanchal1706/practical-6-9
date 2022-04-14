""" Name = Panchal Jay Manojkumar ID = 20CE068
Generate PDF file of your 3rd Semester Mark-sheet.
 Github link = https://github.com/jaypanchal1706/practical-6-7.git """
from PIL import Image
image_1 = Image.open(r'"C:\Users\Jaykumar Panchal\Pictures\Screenshots\3rd_sem_marksheet.png"')
im_1 = image_1.convert('RGB')
im_1.save(r'C:\Users\Jaykumar Panchal\Documents\python\marksheet.pdf')
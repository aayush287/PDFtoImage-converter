'''
    This below code is use to convert pdf to jpg.
    To convert from pdf to jpg you need to run this 
    program using python 3.*
'''
# imported filedialog from tkinter as fd to select pdf
from tkinter import filedialog as fd
# Now importing covert_from_path from pdf2image to convert
# pdf to image from a selected path
from pdf2image import convert_from_path
# selecting file file from file dialog and save 
# the path of file in filename variable
filename = fd.askopenfilename()
# to define the name of image extract the name of
# pdf than store in image_name variable
path = list(map(str,filename.split('.')))
image_name = path[0]
# if filename is not null 
# convert each page of pdf to image
if filename:
    pages = convert_from_path(filename)
    count = 0
    for page in pages:
        count += 1
        page.save(image_name+count+".jpg",'JPEG')


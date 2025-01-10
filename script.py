import os 
from os import walk
from PIL import Image
from Config import Input, Output
from pathlib import Path


inputDir = str(os.path.dirname(__file__) + Input)
outputDir = str(os.path.dirname(__file__) + Output)
   
def imageConvert(path,outdir):
    print('img converter called')     
    files = os.listdir(path)
    if files:
        for file in files:
            pathfile = path + "/" + file
            if os.path.isfile(pathfile):
                        print("Is file" + path)
                        if is_valid_image_pillow(pathfile):
                            image_name = file.split('.')[0]
                            input = Image.open(path + "/" + file)
                            input = input.convert('RGBA').convert('P', palette=Image.ADAPTIVE, colors=255)
                            Path(outdir).mkdir(parents=True, exist_ok=True)
                            input.save(outdir + "/" + image_name + ".webp" ,"webp", quality=50)
                        else: 
                            print("Is not an Image: " + pathfile)   
            elif os.path.isdir(pathfile): 
                print('is dir')                
                imageConvert(path + "/" + file, outdir + "/" + file)
            else:
                 print('none')
                        
def is_valid_image_pillow(file_name):
    try:
        with Image.open(file_name) as img:
            img.verify()
            return True
    except (IOError, SyntaxError):
        return False

if __name__ == '__main__':
 
    print(inputDir)
    print(outputDir) 
    imageConvert(inputDir,outputDir)
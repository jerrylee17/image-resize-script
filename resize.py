from PIL import Image
import os, sys

basepath = "/home/ubuntu/poles-dataset/scrape/google-images-download/google_images_download/downloads/"
allpaths = {
    "desert-pole",
    "flag-pole",
    "garden-lamp-pole",
    "pole-sign",
    "street-light-pole",
    "telephone-pole",
    "traffic-sign-nature",
    "wooden-post-nature",
    "wooden-post-sand"
}

def resize(path, dirs):
    # new directory name
    # newName = path[:-1]+"-1"
    newName = "/home/ubuntu/poles-dataset/scrape/google-images-download/google_images_download/downloads/Allimages"
    try:
        os.mkdir(newName)
    except:
        print("+++DIRECTORY ALREADY EXISTS+++")
    for item in dirs: 
        if os.path.isfile(path+item):
            try:
                im = Image.open(path+item)
            except:
                continue
            # splits it to the file name (without location) and .jpg
            f, e = os.path.splitext(item)
            # resize image
            imResize = im.resize((256, 256), Image.ANTIALIAS)
            # saving image
            # index of period
            ind = item.find(".")
            imName = newName + "/" + item[ind+1:]
            # imName = newName + "/" + f + ".jpg"
            try:
                imResize.save(imName, 'JPEG', quality=90)
                print("saved image "+imName)
            except:
                print("unable to save " + imName)
            

for x in allpaths:
    path = basepath + x + "/"
    # dirs is all the items in the path
    dirs = os.listdir(path)
    resize(path, dirs)
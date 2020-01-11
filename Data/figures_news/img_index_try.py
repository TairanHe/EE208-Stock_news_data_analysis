import os
def get_img_url(number,j):
    with open("img_article/" + number + "/" + str(j) + "/" + str(j) + "_content.txt") as f:
        return  f.readline().strip()
def get_title(number,j):
    with open("img_article/" + number + "/" + str(j) + "/" + str(j) + "_content.txt") as f:
        tmp = f.readlines()
        return tmp[2].strip()
def get_content(number,j):
    with open("img_article/" + number + "/" + str(j) + "/" + str(j) + "_content.txt") as f:
        tmp = f.readlines()
        return tmp[4].strip()
def get_img_path(number,j):
    files = os.listdir("img_article/" + number + "/" + j)
    tmp=[]
    for file in files:
        if file[-3:] == "jpg":
            tmp.append("img_article/" + number + "/" + str(j) + "/" + file)
    return tmp
number = "000002"
files = os.listdir("img_article/" + number + "/")
for file in files:
    print(get_img_url(number,file))
    print(get_title(number,file))
    print(get_content(number,file))
    print(get_img_path(number,file))
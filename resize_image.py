# from PIL import Image
#
# im = Image.open('image/3.jpg')
#
# # 크기를 600x600 으로
# img2 = im.resize((59, 87))
# img2.save('image/3-(1).jpg')


from PIL import Image

im = Image.open('image/3'+'.png')

# 크기를 600x600 으로
maxsize = (59, 87.114)
im.thumbnail(maxsize, Image.ANTIALIAS)
im.save('image/3-(1)'+'.png')

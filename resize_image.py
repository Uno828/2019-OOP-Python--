# from PIL import Image
#
# im = Image.open('image/3.jpg')
#
# # 크기를 600x600 으로
# img2 = im.resize((59, 87))
# img2.save('image/3-(1).jpg')


from PIL import Image

im = Image.open('image/' + 'p' + '_emt' + '.png')

# 크기를 600x600 으로
maxsize = (100.456,100.456)
im.thumbnail(maxsize, Image.ANTIALIAS)
im.save('image/' + 'p' + '_emt' + '- 작은 버전' + '.png')

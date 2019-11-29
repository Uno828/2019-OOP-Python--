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

# 출처: https://webisfree.com/2017-08-01/python-%EC%9D%B4%EB%AF%B8%EC%A7%80-resize-thumbnail-%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0
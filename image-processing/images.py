from PIL import Image, ImageFilter

# img = Image.open('./Pokedex/pikachu.jpg')
# filtered_img = img.convert('L')
# filtered_img.save('gray.png', 'png')
# filtered_img.show()

# img.convert('L').resize((300, 300)).rotate(
#     90).show()

# Size of the image in pixels (size of orginal image)
# (This is not mandatory)

""" width, height = img.size
# Setting the points for cropped image
left = 5
top = height / 4
right = 164
bottom = 3 * height / 4
# Cropped image of above dimension
# (It will not change orginal image)
img.convert('L').crop((left, top, right, bottom)).show() """

img = Image.open('astro.jpg')
img.thumbnail((100, 100))
img.save('thumb.png')
img.show()

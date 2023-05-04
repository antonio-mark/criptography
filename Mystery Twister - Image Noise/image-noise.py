from PIL import Image

image1 = Image.open('Image.png')
image2 = Image.open('Image2.png')
result = Image.open('Image2.png') # or Image.png

print("[+]XORing the two images...")

width, height = image1.size

for h in range(height):
    for w in range(width):
        index0 = image1.getpixel((w, h))
        index1 = image2.getpixel((w, h))
        index = index0 ^ index1
        result.putpixel((w, h), index)

result.save('Result.png')


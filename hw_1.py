from PIL import Image

image_in = Image.open("hw_1_1.jpg")

print(image_in.size)

print(image_in.getpixel((0,0)))
print(image_in.getpixel((0,1)))

image_temp1 = image_in.point(lambda i : i*(1/3))


print(image_temp1.getpixel((0,0)))
print(image_temp1.getpixel((0,1)))

m_gray = Image.new("L", image_in.size)

for y in range(image_in.size[1]):
    for x in range(image_in.size[0]):
        count = image_temp1.getpixel((x,y))
        sum = count[0]+count[1]+count[2]
        m_gray.putpixel((x,y),sum)
m_gray.save("gray.jpg")
m_gray.show()




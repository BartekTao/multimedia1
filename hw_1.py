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
#m_gray.show()


#######################

'''for y in range(m_gray.size[1]):
    for x in range(m_gray.size[0]):
      oldpixel = m_gray.getpixel((x,y))
      #print(oldpixel)
      if(oldpixel<=127):
          newpixel = 0
      else:
          newpixel = 255
      m_gray.putpixel((x, y), newpixel)

m_gray.show()'''

#####################Halftone
m_gray_map = Image.new("L", ((image_in.size[0]//8)*8,(image_in.size[1]//8)*8))

map = ((0,128,32,160,8,136,40,168),
       (192,64,224,96,200,72,232,104),
       (48,176,16,144,56,184,24,152),
       (240,112,208,80,248,120,216, 88),
       (12,140,44,172,4,132,36,164),
       (204,76,236,108,196,68,228,100),
       (60,188,28,156,52,180,20,148),
       (252,124,220,92,244,116,212,84))

m_size = (image_in.size[0]//8)*(image_in.size[1]//8)

for Y in range(0, (image_in.size[1] // 8)):
    for X in range(0, (image_in.size[0] // 8)):
        for y in range(Y * 8, (Y + 1) * 8):
            for x in range(X * 8, (X + 1) * 8):
                if (m_gray.getpixel((x, y)) > map[Y % 8][X % 8]):
                    m_gray_map.putpixel((x, y), 255)
                else:
                    m_gray_map.putpixel((x, y), 0)
m_gray_map.show()





##for y in range(m_gray.size[1]):
    ##for x in range(m_gray.size[0]):




from PIL import Image

image = Image.open("sample.jpg")

print("Image Loaded Successfully")
print("Image Size:", image.size)

image.show()

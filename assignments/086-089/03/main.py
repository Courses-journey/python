"""
Assigment Soultion
"""

from PIL import Image

# Get img
elzero_image = Image.open(r"python\assignments\081-085\03\elzero-pillow.png")

# First img
croped_area = (400,0,800,400)
cropped_img = elzero_image.crop(croped_area)
cropped_img = cropped_img.convert("L")
cropped_img.show()

# second img
croped_area = (0,400,1200,800)
cropped_img = elzero_image.crop(croped_area)
cropped_img = cropped_img.convert("L")
cropped_img = cropped_img.rotate(180)
cropped_img.show()

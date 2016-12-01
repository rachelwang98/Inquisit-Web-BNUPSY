from PIL import Image, ImageDraw, ImageFont
work_dir = "/Users/Rachel 1/Documents/learning/inquisit"
r=(0,1,2,3,4)
for n in r:
    m = n * 10
    draw = ImageDraw.Draw(Image.new("RGB", size=(1000, 1000), color=(m,m,m)), mode="RGB")
    draw.text((300, 300), "G", fill=(255,255,255), font=ImageFont.truetype("/Users/Rachel 1/Documents/方正字库/FZHTJW.TTF)
    name = str(p)+".jpg"
    gray_image.save(work_dir + name,"jpg")
    gray_image = Image.open(work_dir+name)
    blank_image = Image.open(work_dir + str(p)+".jpg")
    out = blank_image.crop(box=(55, 113, 855, 913))
    out.save(work_dir + name)

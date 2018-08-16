##Pillow Library 
##pip install pillow
##Google Fonts : https://github.com/google/fonts/tree/master/apache/roboto
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def text_wrap(text, font, max_width):
    lines = []
    # If the width of the text is smaller than image width
    # we don't need to split it, just add it to the lines array
    # and return
    if font.getsize(text)[0] <= max_width:
        lines.append(text) 
    else:
        # split the line by spaces to get words
        words = text.split(' ')  
        i = 0
        # append every word to a line while its width is shorter than image width
        while i < len(words):
            line = ''         
            while i < len(words) and font.getsize(line + words[i])[0] <= max_width:                
                line = line + words[i] + " "
                i += 1
            if not line:
                line = words[i]
                i += 1
            # when the line gets longer than the max width do not append the word, 
            # add the line to the lines array
            lines.append(line)    
    return lines

    

text = input("Enter Text: ")
img = Image.open('background.jpg')

# size() returns a tuple of (width, height) 
image_size = img.size 
draw = ImageDraw.Draw(img)
# create the ImageFont instance

font = ImageFont.truetype('Roboto-Bold.ttf', size=50, encoding="unic")
lines = text_wrap(text, font, image_size[0])
line_height = font.getsize('hg')[1]
color = 'rgb(0, 0, 255)' # black color
x = 10
y = 20
for line in lines:
    # draw the line on the image
    draw.text((x, y), line, fill=color, font=font)
    
    # update the y position so that we can use it for next line
    y = y + line_height
# save the image
img.save('final_image.png', optimize=True)
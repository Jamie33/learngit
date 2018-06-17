from PIL import Image


def get_char(r,g,b,alpha):
    if alpha == 0:
        return ' '
    gray = (2126*r+7152*g+722*b)/10000
    ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
    x = int((gray/257)*len(ascii_char))
    return ascii_char[x]


def main(file_name='wm.png'):
   
    im = Image.open(file_name)
    width= im.size[0]
    height= im.size[1]
    im = im.resize((int(width/4),int(height/4)))
    width = im.size[0]
    height = im.size[1]
    txt = ''
    for x in range(height):
        for y in range(width):
            content = im.getpixel((y,x))
            txt += get_char(*content)
        txt += '\n'
    print(txt)
    write_file('output.txt',txt)


def write_file(out_file,content):
    with open(out_file,'w') as f:
        f.write(content)


if __name__ == '__main__':

    main()

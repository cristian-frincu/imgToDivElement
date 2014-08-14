import PIL
import Image
im = Image.open("Untitled.png") #Can be many different formats.
pix = im.load()
print pix[1,1]

print im.size;

f = open('workfile2.html', 'w')
f.write("<style>.p {float:left;height:1px;width:1px;}</style>");

f.write("<html><head></head><body><div style='width:"+str(im.size[0])+"px;height:"+str(im.size[1])+"px;'>");

for x in range(im.size[0]):
    for y in range (im.size[1]):
        
        f.write("<div class='p' style='background-color:rgb"+str(pix[x,y])+";'></div>");
 
f.write("</div></body></html>");
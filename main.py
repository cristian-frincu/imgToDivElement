import PIL
import Image
im = Image.open("Untitled.png") #Can be many different formats.
pix = im.load()
print pix[1,1]

print im.size;

f = open('workfile2.html', 'w')
f.write("<html><head></head><body><div style='width:12px;height:12px;'>");

for x in range(im.size[0]):
    for y in range (im.size[1]):
        
        f.write("<div style='background-color:rgb"+str(pix[x,y])+";top:"+str(y)+"px;left:"+str(x)+"px;height:1px;width:1px;float:left'></div>");

f.write("</div></body></html>");
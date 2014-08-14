import PIL
import Image
im = Image.open("earth_128.png") #Can be many different formats.
pix = im.load()



f = open('workfile2.html', 'w')

f.write("<script>$('p').hover(function(){$(this).css('top', rand(1,1000) + 'px').css('left', rand(1,1000) + 'px');});</script>");

f.write("<style>.p {float:left;height:3px;width:3px;}.p:hover{float:left;height:10px;width:10px}</style>");
f.write("<html><head></head><body><div style='width:"+str(im.size[0]*3)+"px;height:"+str(im.size[1]*3)+"px;margin:auto'>");
for y in range (im.size[1]):
    for x in range(im.size[0]):
        f.write("<div class='p' style='background-color:rgb("+str(pix[x,y][0])+","+ str(pix[x,y][1])+","+ str(pix[x,y][2])+");'></div>");
f.write("</div></body></html>");

print "Done!";
"PROJECT 3 : INFINITY FLOWER "
import turtle                                                          # turtle → used for drawing graphics on screen 🐢
import colorsys                                                        # colorsys → helps convert colors (HSV → RGB)

t= turtle.Turtle ()                                                    # creates a drawing pen (like a robot pen)
s= turtle.Screen().bgcolor('black')                                    # sets background color to black

t.speed (0)
n=70                                                                   # n → controls how fast color changes
h=0                                                                    # h → hue value (used for changing colors gradually) 
for i in range (360):
    c= colorsys.hsv_to_rgb(h,1,0.8)
    h+=1/n
    t.color(c)
    t.left(1)
    t.fd(1)                                                            # move forward a little
    for j in range (2):
        t.left(2)
        t.circle(100)                                                 # draws a circle with radius 100
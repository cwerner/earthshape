import matplotlib.patches as mpatches
from matplotlib.legend_handler import HandlerBase


class AnyObject(object):
    """Store color and patch attributes for legend
    """
    def __init__(self, color, left, right=None):
        # valid values:
        self.color = color
        self.left  = left
        self.right = right

class AnyObjectHandler(HandlerBase):
    """Custom legend handler for PFT plot
    """
    def create_artists(self, legend, ohandle,
                    x0, y0, width, height, fontsize, trans):
    
        r = []
        # if only one patch, center it
        if not ohandle.right:
            #lpos = (x0 + width*0.275, y0)
            the_width = width
            rpos = (x0, y0)
        else:
            the_width = width * 0.475
            rpos = (x0+0.525*width,y0)

        lpos = (x0, y0)
            
        r.append( mpatches.Rectangle(lpos, the_width, height, ec='black',
                   linestyle='-', fc=ohandle.color, lw=0.1, hatch=ohandle.left) )
        
        if ohandle.right:
            r.append( mpatches.Rectangle(rpos, the_width, height, ec='black',
                   linestyle='-', fc=ohandle.color, lw=0.1, hatch=ohandle.right ) )

        return r
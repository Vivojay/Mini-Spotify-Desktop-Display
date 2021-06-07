from PIL.Image import new
from colorthief import ColorThief
from matplotlib import colors
from colorharmonies import Color, complementaryColor
import colorsys

import sys

if sys.version_info < (3, 0):
    from urllib2 import urlopen
else:
    from urllib.request import urlopen

import io

from colorthief import ColorThief

sampleURL ='https://images.unsplash.com/photo-1622023585351-06eebdec74b2?ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=60'

r'''
Plan of Action:
    1) Most Dom Col
    2) Check for saturation constraint:
        if colorsys.rgb_to_hsv(*[i/255 for i in (194, 188, 186)])[1]*100 < 30:
            get color with saturation = 30 and same hue and luminance
            convert this ^ color back to rgb
    3) Get Tetradic Colors for this new rgb value
    4) Use these :-)
'''

def ctc(hex_str):
    if hex_str[0] == '#':
        hex_str = hex_str[1:]
    (r, g, b) = (hex_str[:2], hex_str[2:4], hex_str[4:])
    return '000' if 1 - (int(r, 16) * 0.299 + int(g, 16) * 0.587 + int(b, 16) * 0.114) / 255 < 0.5 else 'fff'

# With reference to "https://stackoverflow.com/questions/37765197/darken-or-lighten-a-color-in-matplotlib"
def adjust_lightness(color, amount=0.5):
    import matplotlib.colors as mc
    import colorsys
    try:
        c = mc.cnames[color]
    except:
        c = color
    c = colorsys.rgb_to_hls(*mc.to_rgb(c))
    return colorsys.hls_to_rgb(c[0], max(0, min(1, amount * c[1])), c[2])

def get_dom_color(input_url):    
    global a
    fd = urlopen(input_url)
    f = io.BytesIO(fd.read())
    color_thief = ColorThief(f)

    # Preprocessed RGB values
    rgbColors = color_thief.get_palette(color_count=3)

    # Changing Colorspaces
    hexColor = colors.to_hex([i/255 for i in rgbColors[0]])
    hsvColor = colorsys.rgb_to_hsv(*[i/255 for i in rgbColors[0]])
    domRGBColor = [int(i*255) for i in colorsys.hsv_to_rgb(*hsvColor)]

    compColor = complementaryColor(Color(domRGBColor,"",""))
    # saturationAdjustedDomColor = colors.rgb_to_hsv(compColor).tolist()
    compColor = colors.to_hex([i/255 for i in compColor])
    # saturationAdjustedcompColor = colors.rgb_to_hsv(colors.to_rgb(compColor))

    # Adjusting colour brightness for adjHexColor and adjCompColor
    if ctc(hexColor) == '000':
        adjHexColor = colors.to_hex(adjust_lightness(hexColor, 0.6))
        adjCompColor = colors.to_hex(adjust_lightness(compColor, 0.6))
    else:
        adjHexColor = colors.to_hex(adjust_lightness(hexColor, 1.4))
        adjCompColor = colors.to_hex(adjust_lightness(compColor, 1.4))

    r'''
    # return rgbColors
    if colorsys.rgb_to_hsv(*[i/255 for i in rgbColors[0]])[1]*100 < 30:
        h, s, v = colorsys.rgb_to_hsv(*[i/255 for i in rgbColors[0]])
        newHsvColor = (h, 0.3, v)
    else:
        newHsvColor = hsvColor
    '''
    # colors.to_hex(adjust_lightness('#59b4ca', 1.4))
    return (
            hexColor,
            compColor,
            ctc(hexColor),
            adjHexColor,
            adjCompColor,
            # saturationAdjustedDomColor
        )

if __name__ == '__main__':
    import json
    out=get_dom_color(sampleURL)
    print(json.dumps(out, indent=4))
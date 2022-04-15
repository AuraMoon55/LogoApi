import requests
from PIL import Image, ImageDraw, ImageFont
import os
import random
import glob
from urllib.request import urlopen

CONG = os.path.join(os.getcwd(), "config.json")


def get_word():
  s = ["asthetic", "anime", "abstract", "dark", "black"]
  return random.choice(s)

def get_bg():
  word = get_word()
  r = requests.get(f"https://testapibots1.herokuapp.com/wall/{word}")
  resp = r.json()
  resp = get_working(resp["images"])
  bg = random.choice(resp)
  resp.remove(bg)
  x = rem_perso(resp)
  return bg

def get_working(images: list):
  num = 1
  newimages = []
  for image in images:
    newname = f"res{num}.jpg"
    content = (urlopen(image)).read()
    with open(newname, "wb") as f:
      f.write(content)
      f.close()
    newimages.append(newname)
    num += 1
  return newimages

def rem_perso(images: list):
  for z in images:
    os.remove(z)
  return True

def randfont():
  fonts = glob.glob("fonts" + "/*.ttf")
  font = random.choice(fonts)
  return font

def get_colour(): 
  color = ['IndianRed', 'LightCoral', 'Salmon', 'DarkSalmon', 'LightSalmon', 'Crimson', 'Red', 'FireBrick', 'DarkRed', 'Pink', 'LightPink', 'HotPink', 'DeepPink', 'MediumVioletRed', 'PaleVioletRed', 'LightSalmon', 'Coral', 'Tomato', 'OrangeRed', 'DarkOrange', 'Orange', 'Gold', 'Yellow', 'LightYellow', 'LemonChiffon', 'LightGoldenrodYellow', 'PapayaWhip', 'Moccasin', 'PeachPuff', 'PaleGoldenrod', 'Khaki', 'DarkKhaki', 'Lavender', 'Thistle', 'Plum', 'Violet', 'Orchid', 'Fuchsia', 'Magenta', 'MediumOrchid', 'MediumPurple', 'Amethyst', 'BlueViolet', 'DarkViolet', 'DarkOrchid', 'DarkMagenta', 'Purple', 'Indigo', 'SlateBlue', 'DarkSlateBlue', 'MediumSlateBlue', 'GreenYellow', 'Chartreuse', 'LawnGreen', 'Lime', 'LimeGreen', 'PaleGreen', 'LightGreen', 'MediumSpringGreen', 'SpringGreen', 'MediumSeaGreen', 'SeaGreen', 'ForestGreen', 'Green', 'DarkGreen', 'YellowGreen', 'OliveDrab', 'Olive', 'DarkOliveGreen', 'MediumAquamarine', 'DarkSeaGreen', 'LightSeaGreen', 'DarkCyan', 'Teal', 'Aqua', 'Cyan', 'LightCyan', 'PaleTurquoise', 'Aquamarine', 'Turquoise', 'MediumTurquoise', 'DarkTurquoise', 'CadetBlue', 'SteelBlue', 'LightSteelBlue', 'PowderBlue', 'LightBlue', 'SkyBlue', 'LightSkyBlue', 'DeepSkyBlue', 'DodgerBlue', 'CornflowerBlue', 'MediumSlateBlue', 'RoyalBlue', 'Blue', 'MediumBlue', 'DarkBlue', 'Navy', 'MidnightBlue', 'Cornsilk', 'BlanchedAlmond', 'Bisque', 'NavajoWhite', 'Wheat', 'BurlyWood', 'Tan', 'RosyBrown', 'SandyBrown', 'Goldenrod', 'DarkGoldenrod', 'Peru', 'Chocolate', 'SaddleBrown', 'Sienna', 'Brown', 'Maroon', 'White', 'Snow', 'Honeydew', 'MintCream', 'Azure', 'AliceBlue', 'GhostWhite', 'WhiteSmoke', 'Seashell', 'Beige', 'OldLace', 'FloralWhite', 'Ivory', 'AntiqueWhite', 'Linen', 'LavenderBlush', 'MistyRose', 'Gainsboro', 'LightGrey', 'Silver', 'DarkGray', 'Gray', 'DimGray', 'LightSlateGray', 'SlateGray', 'DarkSlateGray', 'Black']
  colo = random.choice(color)
  return colo


def make_logo(first, last, img, colour, fnt):
  img = Image.open(img)
  fs = 250
  minwid = int(str(img.width/50).split(".")[0])
  draw = ImageDraw.Draw(img)
  Font = ImageFont.truetype(fnt, fs)
  wid = (img.width - minwid)/10
  splits = int((img.width - (2*wid))/150)
  try:
    cuts = int(str(len(first)/splits).split(".")[0])
    firsts = []
    for cut in range(cuts):
      strt = splits*(cut + 1)
      emd = splits*cut
      firsts.append(first[emd:strt])
  except:
    firsts = [first]
  try:
    cutsy = int(str(len(last)/splits).split(".")[0])
    lasts = []
    for cuty in range(cutsy):
      stry = splits*(cuty + 1)
      emdy = splits*cuty
      lasts.append(last[emdy:stry])
  except:
    lasts = [last]
  
  hei = (img.height/2) - 200
  draw.multiline_text((wid, hei), "\n".join(x for x in firsts), fill=colour, font=Font, align="center")
  draw.multiline_text(((img.width - (wid*2 + 100*(int(len(lasts)))))/2, (hei + (350*int(len(firsts))))), "\n".join(y for y in lasts), fill=colour, font=Font, align="center")
  namae = "logo.png"
  img.save(namae)
  return namae


async def get_logo(first, last):
  first = first.replace("+", " ")
  first = first.replace("%20", " ")
  last = last.replace("+", " ")
  last = last.replace("%20", " ")
  backimg = get_bg()
  colour = get_colour()
  fnt = randfont()
  logo = make_logo(first, last, backimg, colour, fnt)
  return logo

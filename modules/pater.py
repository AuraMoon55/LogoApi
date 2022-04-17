import requests
from PIL import Image, ImageDraw, ImageFont
import os
import random
import glob
from urllib.request import urlopen
import json
from telegraph import upload_file

CONG = os.path.join(os.getcwd(), "config.json")

with open(CONG, "r") as config:
  d = json.load(config)

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
  fonts = [1,2,3,4,5,6,7]
  font = random.choice(fonts)
  font = f"fonts/LoneGhoul-{font}.ttf"
  return font

def get_colour(): 
  color = ["black","white","red","green","blue","yellow","purple","brown"]
  colo = random.choice(color)
  return colo


def make_logo(first, img, colour, fnt):
  Img = Image.open(img)
  fs = 250
  minwid = int(str(Img.width/50).split(".")[0])
  draw = ImageDraw.Draw(Img)
  Font = ImageFont.truetype(fnt, fs)
  wid = (Img.width - minwid)/10
  splits = int((Img.width - (2*wid))/150)
  try:
    cuts = int(str(len(first)/splits).split(".")[0])
    firsts = []
    for cut in range(cuts):
      strt = splits*(cut + 1)
      emd = splits*cut
      firsts.append(first[emd:strt])
  except:
    firsts = [first]
  
  hei = (Img.height/2) - 200
  draw.multiline_text((wid, hei), "\n".join(x for x in firsts), fill=colour, font=Font, align="center")
  namae = "logo.png"
  Img.save(namae)
  os.remove(img)
  nama = upload_file(namae)
  nama = nama[0]
  os.remove(namae)
  return nama


async def get_logo(first):
  first = first.replace("+", " ")
  first = first.replace("%20", " ")
  backimg = get_bg()
  colour = get_colour()
  fnt = randfont()
  logo = make_logo(first, backimg, colour, fnt)
  return logo

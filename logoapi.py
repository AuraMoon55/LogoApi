from fastapi import FastAPI, Request
from modules import *
from fastapi.responses import FileResponse
import os

CONG = os.path.join(os.getcwd(), "config.json")

app = FastAPI()
"""
with open(CONG, "r") as data:
  d = json.load(data)
"""

@app.get("/")
async def home():
    return {
      "Name": "Logo Api",
      "Version": "Test",
      "Status": "Up",
      "Help": "https://testlogoapi.herokuapp.com//help",
      "Authors": "AuraMoon55"
    }

@app.get("/help")
async def get_help():
  fn = "name for first line"
  fe = "name for second line"
  return {
    "Name": "Logo Api",
    "get_logo": f"https://testlogoapi.herokuapp.com//logo?first={fn}&?last={fe}",
    "Authors": "AuraMoon55"
  }

@app.get("/logo")
async def logo_p(request: Request):
  params = request.query_params
  first = params["first"]
  last = params["last"]
  logo = await get_logo(first, last)
  return FileResponse(logo)


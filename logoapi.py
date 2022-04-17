from modules.pater import *
from dbfuncs import *
import os
from flask import Flask, render_template, request
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

CONG = os.path.join(os.getcwd(), "config.json")

app = Flask(__name__)

with open(CONG, "r") as data:
  d = json.load(data)


mongo_client = MongoClient(d['mongo'])
db = mongo_client.logoapi


@app.route("/")
async def home():
    return {
      "Name": "Logo Api",
      "Version": "Test",
      "Status": "Up",
      "Help": f"{d['name']}/help",
      "Authors": d["authors"]
    }

@app.route("/help")
async def get_help():
  fn = "text for logo"
  fe = "name for second line"
  return {
    "Name": "Logo Api",
    "get logo with preview": f"{d['name']}/logo?text={fn}",
    "Authors": d['authors'],
    "get logo link": f"{d['name']}/api/logo?api_key=your key&text={fn}",
    "get api key": f"{d['name']}/getKey?user_id=telegram user id"
  }

@app.route("/logo")
async def logo_p():
  first = request.args.get('text')
  logo = await get_logo(first)
  return render_template('post.html', logo=logo)

@app.route("/api/logo")
async def logo_api():
  first = request.args.get('text')
  api = request.args.get('api_key')
  x = await check_key(api)
  if x:
    pass
  else:
    return {
      "error": "wrong api key"
    }
  logo = await get_logo(first)
  return {
    "API": api,
    "logo": logo
  }

@app.route("/getKey")
async def getKey():
  userid = request.args.get('user_id')
  user = await get_user(userid)
  if user:
    return {
      "Key": user["key"]
    }
  else:
    key = await save_key(user_id)
    return {
      "Key": key["key"]
    }

import asyncio
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
mongo_client = MongoClient("mongodb+srv://abc:abc@cluster0.dxxoi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = mongo_client.logoapi

usersdb = db.users

async def save_key(user: int):
  ALPHA = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
  tat = str(user)
  ket = []
  for a in tat:
    a = int(a)
    a -= 1
    dig = ALPHA[int(a)]
    ket.append(dig)
  key = ket[::-1]
  key1 = key[0:5]
  key2 = key[5:8]
  key3 = key[8:]
  new_key = f"{key1}-{key2}-{key3}"
  await usersdb.insert_one({"id": user, "key": new_key})
  return {
    "key": new_key
  }

async def get_keys():
  x = await usersdb.find()
  keys = []
  for a in x:
    keys.append(a["key"])
  return keys

async def check_key(key):
  x = await get_keys()
  if key in x:
    return True
  else:
    return False

async def get_user(user):
  x = await usersdb.find()
  for a in x:
    if a["id"] == user:
      return a
    else:
      pass
  return None

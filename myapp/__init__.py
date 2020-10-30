from flask import Flask
from  bson import ObjectId
from flask_mongoengine import MongoEngine

#from pymongo import MongoClient

from datetime import datetime

app=Flask(__name__)

mongo=MongoEngine(app)

MONGODB_SETTINGS={
    'db':'local',
    'host':'localhost',
    'port':27017
}

from myapp import api, models
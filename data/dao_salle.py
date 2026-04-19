import json
import mysql.connector
from models.salle import Salle<

class DataSalle:
    def __init__(self):
        pass
    def get_connection(self):
        with open("data/config.json", "r") as f:
            config = json.load(f)

from typing import Literal


class SportsEvent:
    def __init__(self,event_name:str):
        self.event_name = event_name
        self.players = []

    def AddPlayer(self,name:str,gender:Literal["Male","Female","Others"],age:int,category=None):
        self.players.append({"name":name,"gender":gender,"age":age,"category":category})

    def GetDict(self):
        return {"name":self.event_name}
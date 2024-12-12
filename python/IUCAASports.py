from typing import Literal


class Participant:
    def __init__(self,name:str,gender:Literal["Male","Female","Others"],age:int=None):
        self.name=name
        self.gender=gender
        self.age=age
    
    def GetDict(self):
        pldict={}
        pldict["name"]=self.name
        pldict["gender"]=self.gender
        pldict["age"]=self.age
        return pldict


class Match:
    def __init__(self):
        pass



class SportsEvent:
    def __init__(self,event_name:str):
        self.event_name = event_name
        self.players:list[Participant] = []

    def AddPlayer(self,name:str,gender:Literal["Male","Female","Others"],age:int=None):
        self.players.append(Participant(name,gender,age))

    def AddMatch(self):
        pass

    def GetDict(self):
        evdict={}
        evdict["name"]=self.event_name
        evdict["participants"]=[p.GetDict() for p in self.players]

        return evdict
from typing import Literal

events = Literal["badminton","table-tennis","chess","marathon","cricket","carrom"]
bd_categories = ["mens-single","womens-single","mens-double","womens-double","mixed-double"]


class Participant:
    def __init__(self,
                 name:str,
                 gender:Literal["Male","Female","Others"],
                 age:int):
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
    _match_no=0
    def __init__(self):
        pass

        # self.date
        self._mathch_no
        # self.refree

    


class Badminton:
    def __init__(self):
        self._event_name = "badminton"
        self.pl_mens_sin:list[Participant] = []
        self.pl_womens_sin:list[Participant] = []
        self.pl_mens_dbl:list[list[Participant]] = []
        self.pl_womens_dbl:list[list[Participant]] = []
        self.pl_mixed_dbl:list[list[Participant]] = []

    def AddMensSingle(self,name:str,age:int):
        self.pl_mens_sin.append(Participant(name,"Male",age))
    
    def AddWomensSingle(self,name:str,age:int):
        self.pl_womens_sin.append(Participant(name,"Female",age))

    def AddMensDouble(self,names:list[str],ages:list[int]):
        team = []
        for n,a in zip(names,ages):
            team.append(Participant(n,"Male",a))
        self.pl_mens_dbl.append(team)

    def AddWomensDouble(self,names:list[str],ages:list[int]):
        team = []
        for n,a in zip(names,ages):
            team.append(Participant(n,"Female",a))
        self.pl_womens_dbl.append(team)


    def AddMixedDouble(self,names:list[str],ages:list[int],genders:list[Literal["Male","Female","Others"]]):
        team = []
        for n,a,g in zip(names,ages,genders):
            team.append(Participant(n,g,a))
        self.pl_mixed_dbl.append(team)


    def AddMatch(self):
        pass

    def GetDict(self):
        evdict={}
        evdict["name"]=self._event_name

        categories = {}
        categories["mens-single"]=[p.GetDict() for p in self.pl_mens_sin]
        categories["womens-single"]=[p.GetDict() for p in self.pl_womens_sin]
        categories["mens-double"] = [[team[0].GetDict(),team[1].GetDict()] for team in self.pl_mens_dbl]
        categories["womens-double"] = [[team[0].GetDict(),team[1].GetDict()] for team in self.pl_womens_dbl]
        categories["mixed-double"] = [[team[0].GetDict(),team[1].GetDict()] for team in self.pl_mixed_dbl]
        evdict["categories"] = categories
        

        return evdict
    

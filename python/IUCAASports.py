from typing import Literal
# import uuid

events = Literal["badminton","table-tennis","chess","marathon","cricket","carrom"]
bd_categories = ["mens-single","womens-single","mens-double","womens-double","mixed-double"]


class Participant:
    def __init__(self,
                 name:str,
                 gender:Literal["Male","Female","Others"],
                 age:int,
                 phone:int=None,
                 email:str=None):
        self.name=name
        self.gender=gender
        self.age=age
        self.phone=phone
        self.email=email
        # self.UID=self.genUID()
    
    def GetDict(self):
        pldict={}
        pldict["name"]=self.name
        pldict["gender"]=self.gender
        pldict["age"]=self.age
        return pldict
    
    # def genUID(self):
    #     age_group = "U18" if self.age < 18 else "18+" if self.age <= 40 else "40+"
    #     return f"{self.gender[0]}-{age_group}-{uuid.uuid4().hex[:6]}"





class Match:
    _match_no=0
    def __init__(self, date:str, time:str, event, category, participants:list[Participant], refree:str=None):
        self.date = date
        self.time = time
        self.event = event
        self.category = category
        self.participants = participants
        self.refree = refree
        Match._match_no += 1



class Badminton:
    def __init__(self):
        self._event_name = "badminton"
        self.pl_mens_sin:list[Participant]          = []
        self.pl_womens_sin:list[Participant]        = []
        self.pl_mens_dbl:list[list[Participant]]    = []
        self.pl_womens_dbl:list[list[Participant]]  = []
        self.pl_mixed_dbl:list[list[Participant]]   = []

    def AddMensSingle(self,name:str,age:int,phone:int=None,email:str=None):
        self.pl_mens_sin.append(Participant(name,"Male",age,phone,email))
    
    def AddWomensSingle(self,name:str,age:int,phone:int=None,email:str=None):
        self.pl_womens_sin.append(Participant(name,"Female",age,phone,email))

    def AddMensDouble(self,names:list[str],ages:list[int],phones:list[int]=None,emails:list[str]=None):
        team = []
        phones = phones if phones else [None]*len(names)
        emails = emails if emails else [None]*len(names)
        for n,a,p,e in zip(names,ages,phones,emails):
            team.append(Participant(n,"Male",a,p,e))
        self.pl_mens_dbl.append(team)

    def AddWomensDouble(self,names:list[str],ages:list[int],phones:list[int]=None,emails:list[str]=None):
        team = []
        phones = phones if phones else [None]*len(names)
        emails = emails if emails else [None]*len(names)
        for n,a,p,e in zip(names,ages,phones,emails):
            team.append(Participant(n,"Female",a,p,e))
        self.pl_womens_dbl.append(team)

    def AddMixedDouble(self,names:list[str],ages:list[int],genders:list[Literal["Male","Female","Others"]],phones:list[int]=None,emails:list[str]=None):
        team = []
        phones = phones if phones else [None]*len(names)
        emails = emails if emails else [None]*len(names)
        for n,a,g,p,e in zip(names,ages,genders,phones,emails):
            team.append(Participant(n,g,a,p,e))
        self.pl_mixed_dbl.append(team)


    def AddMatch(self):
        pass

    def GetDict(self):
        evdict={}
        evdict["name"]=self._event_name

        categories = {}
        categories["mens-single"]   = [p.GetDict() for p in self.pl_mens_sin]
        categories["womens-single"] = [p.GetDict() for p in self.pl_womens_sin]
        categories["mens-double"]   = [[team[0].GetDict(),team[1].GetDict()] for team in self.pl_mens_dbl]
        categories["womens-double"] = [[team[0].GetDict(),team[1].GetDict()] for team in self.pl_womens_dbl]
        categories["mixed-double"]  = [[team[0].GetDict(),team[1].GetDict()] for team in self.pl_mixed_dbl]
        evdict["categories"] = categories
        

        return evdict
    


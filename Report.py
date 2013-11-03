from datetime import datetime

class Report(object):
    def __init__(self, obj):
        self.datetime = obj.datetime
        self.location = Location(obj.location)
        self.victim = Victim(obj.victim)
        self.offenders = [Offender(x) for x in obj.offenders]
        self.witnesses = [Witness(x) for x in obj.witnesses]
        self.offense = Offense(obj.incident)
        self.evidence = Evidence(obj.evidence)
        
        pass
    
    def describe(self):
        description = ("On "+str(self.datetime)+", I responded to "+str(self.location.name)+
                ", where I made contact with the victim identified as "+self.victim.name+ "."+
                "Victim told me that "+["She", "He"][self.victim.gender=='Male']+
                " experienced "+(self.offense.status+" " if self.offense.status.lower()!='completed' else "")+self.offense.name+"."+"\n")
        
        description += self.location.describe()
        description += "\n".join([victim.describe() for victim in self.victims])+"\n"
        description += "\n".join([offender.describe()+"\n" for offender in self.offenders])+"\n"
        description += "\n".join([witness.describe()+"\n" for witness in self.witnesses])+"\n"
        description += self.offense.describe()+"\n"
        description += self.evidence.describe()+"\n"
        return description
    
class Location(object):
    def __init__(self, obj):
        name = obj.name
        state = obj.state
        zipcode = obj.zipcode
        
    
    def describe(self):
        return ""



class Person(object):
    def __init__(self, obj):
        self.name = obj.name
        self.sequence_no = obj.sequence_no  # (int 1,2,3 ...) If there are multiple victims, offenders, witnesses etc.,
        self.age = obj.age_low, obj.age_high
        self.height = obj.height_low, obj.height_high
        self.weight = obj.weight_low, obj.weight_high
        self.gender = obj.gender
        self.race = obj.race
        self.other_features = obj.other_features # list : Scars/marks/tattoos
        self.extra_info = obj.extra_info    # Descriptive field (eg., the victim was threatened by a weapon.)
    
    @property
    def pronoun(self):
        return ["She","He"][self.gender.lower()=='male']

    def describe(self):
        description = ("The "+self.person_type+(" "+self.sequence_no if self.sequence_no>1 else "")+
                       " is "+str(self.name)+", a "+str(self.gender)+", "+
                       (self.race+" looking," if self.race else "race unknown,")+
                       " around "+str(self.age[0])+"-"+str(self.age[1])+" years old."+
                       self.pronoun+" is around "+str(self.height[0])+"-"+str(self.height[1])+" tall and "+
                       "weights around "+str(self.height[0])+"-"+str(self.height[1])+" lbs."
                       )
        if self.other_features:
            description+="Other distinctive traits include "+", ".join(self.other_features)+"."
        if self.extra_info:
            description+=self.extra_info
        return description
    
class Victim(Person):
    def __init__(self, obj):
        self.person_type = 'victim'
        Person.__init__(self, obj)
        self.extra_info = obj.extra_info
        self.injury = obj.injury
        
    def describe(self):
        description = Person.describe(self)
        if self.injury:
            self.description +=self.pronoun+" suffered "+self.injury+"."
        return description
        
class Offender(Person):
    def __init__(self, obj):
        self.person_type = 'offender'
        Person.__init__(self, obj)
        self.mannerisms = obj.mannerisms
    
    def describe(self):
        description = Person.describe(self)
        if self.mannerisms:
            self.descrition+=self.pronoun+" exhibited mannerisms like "+", ".join(self.mannerisms)
        return description

class Witness(Person):
    def __init__(self, obj):
        self.person_type = 'witness'
        Person.__init__(self, obj)
    
    def describe(self):
        description = Person.describe(self)
        return description

class Offense(object):
    def __init__(self, obj):
        self.name = obj.name    # larceny/robbery/assault.
        self.status = obj.status    # attempted/completed.
        self.bias = obj.bias    # Motivation
        pass
    
    def describe(self):
        description = ("The "+(self.offense.status+" " if self.offense.status.lower()!='completed' else "")+
                       self.name+" was motivated by "+self.bias+"."
                       )
        return description


class Evidence(object):
    def __init__(self, obj):
        self.evidence_list = obj.evidence_list
        pass
    
    def describe(self):
        description = "The evidence collected include "+", ".join(self.evidence_desc)+"."
        return description


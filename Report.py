from datetime import datetime

class Report(object):
    def __init__(self, obj):
        self.datetime = obj.datetime
        self.location = Location(obj.location)
        self.victim = Victim(obj.victim)
        self.offenders = [Offender(x) for x in obj.offenders]
        self.witnesses = [Witness(x) for x in obj.witnesses]
        self.incident = Incident(obj.incident)
        pass
    
    def __repr__(self):
        return ("On "+str(self.datetime)+", I responded to the "+str(self.location)+
                ", where I made contact with the victim identified as "+self.victim.name+ "."+
                "Victim told me that "+["She", "He"][self.victim.gender=='Male']+
                " experienced "+self.incident.name)
    
class Location(object):
    def __init__(self, obj):
        pass
    
    def __repr__(self):
        return ""

class Victim(object):
    def __init__(self, obj):
        pass
    
    def __repr__(self):
        return ""

class Offender(object):
    def __init__(self, obj):
        pass
    
    def __repr__(self):
        return ""

class Witness(object):
    def __init__(self, obj):
        pass
    
    def __repr__(self):
        return ""

class Incident(object):
    def __init__(self, obj):
        pass
    
    def __repr__(self):
        return ""


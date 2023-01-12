class Fustrum(object):
    def __init__(self,r,parent):
        self.radius=r
        self.parent=parent
        self.perceptionList=[]

    def inside(self, obj):
        if hasattr(obj,'position'):
            if obj.position.distance_to(self.parent.position) < self.radius:
                return True
            return False
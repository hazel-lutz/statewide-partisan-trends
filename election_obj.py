import state_obj

class Election:

    def __init__(self, dem_vote, rep_vote, total_vote, state):
        self.dem_vote = dem_vote
        self.rep_vote = rep_vote
        self.total_vote = total_vote
        self.state = state

    def get_dem_vote(self):
        return self.dem_vote
    
    def get_rep_vote(self):
        return self.rep_vote
    
    def get_state(self):
        return self.state 

    def calc_dem_percent(self):
        return (self.dem_vote/self.total_vote)*100
    
    def calc_rep_percent(self):
        return (self.rep_vote/self.total_vote)*100

    def calc_turnout_percent(self):
        return 100*(self.total_vote/self.state.rv)

'''
Nevada = state_obj.State(3104614, 2109113)
NV_sen_22 = Election(498316, 490388, 1020850, Nevada)

print(NV_sen_22.get_rep_vote())
print(NV_sen_22.calc_dem_percent())
print(NV_sen_22.calc_turnout_percent())
'''
from random import random as rnd
import operator
import math

class Team:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank


class Match:
    def __init__(self, team_a, team_b):
        self.team_a = team_a
        self.team_b = team_b
    

    def result(self):
        win_probability = 0.5 + (self.team_b.rank - self.team_a.rank)*0.05
        x = rnd()
#        print "Getting Result"
#        print self.team_a.name + " " + str(self.team_a.rank)
#        print self.team_b.name + " " + str(self.team_b.rank)
#        print win_probability
#        print x
        if x <= win_probability:
            return self.team_a.name
        else:
            return self.team_b.name

class Tournament:
    def __init__(self):
        self.team_list = []
        self.match_list = []
        self.match_result = []
        self.result_list = []

    def add_team (self,team):
        if team not in self.team_list:
            self.team_list.append(team)

    def generate_match_list(self):
        i = 0
        self.match_list = []
        for team1 in self.team_list:
            for team2 in self.team_list[i+1:]:
                self.match_list.append(Match(team1, team2))
            i = i+1
            
        return self.match_list

    def simulate_matches(self):
        self.match_results = []
        for match in self.match_list:
            self.match_results.append((match, match.result()))
        
        return self.match_results

    def process_result(self):
        point_table = {}
        for result in match_results:
            if result[1] in point_table.keys():
                point_table[result[1]] = point_table[result[1]] + 2
            else: 
                point_table[result[1]] = 2
    
        return point_table

def sanity_check(result_list):
    game_played = {}
    for result in match_results:
        if result[0].team_a.name in game_played.keys():
            game_played[result[0].team_a.name] = game_played[result[0].team_a.name] + 1
        else: 
            game_played[result[0].team_a.name] = 1

        if result[0].team_b.name in game_played.keys():
            game_played[result[0].team_b.name] = game_played[result[0].team_b.name] + 1
        else: 
            game_played[result[0].team_b.name] = 1

    print game_played

if __name__ == '__main__':

    wc2019 = Tournament()
    wc2019.add_team(Team("ENG",  1))
    wc2019.add_team(Team("IND",  2))
    wc2019.add_team(Team("SA" ,  3))
    wc2019.add_team(Team("NZ" ,  4))
    wc2019.add_team(Team("AUS",  5))
    wc2019.add_team(Team("PAK",  6))
    wc2019.add_team(Team("BD" ,  7))
    wc2019.add_team(Team("WI" ,  8))
    wc2019.add_team(Team("SL" ,  9))
    wc2019.add_team(Team("AFG", 10))

    match_list = wc2019.generate_match_list()

    total_trial = 100
    BD_in_Semi = 0
    bd_points = 0

    for i in range(total_trial):
        match_results = wc2019.simulate_matches()
        point_table = wc2019.process_result()
        sorted_point_table = sorted(point_table.items(), key=operator.itemgetter(1), reverse = True)

        for team in sorted_point_table[0:4]:
            if team[0] == "BD":
                BD_in_Semi = BD_in_Semi + 1
                bd_points = bd_points + team[1]

    print "Chance of BD making it to semifinal " + str(BD_in_Semi*1.0/total_trial)
    print "Average points need to go to Semi:" + str(bd_points*1.0/BD_in_Semi)
    print "Average match need to win to go to Semi:" + str(int(math.ceil(bd_points*0.5/BD_in_Semi)))

#    sanity_check(match_results)

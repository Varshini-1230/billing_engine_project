def registration():
    # no_of_teams=int(input("enter no of teams:"))
    # team_name=input("enter team name:")
    # while True:
    try:
        no_of_teams=int(input("enter no of teams:"))
        if no_of_teams<2:
            print("Atleast 2 teams are required")
            no_of_teams=int(input("enter no of teams:"))
    except ValueError:
        print("please enter valid number")
        return
    #unique team names
    team_names=[]
    while len(team_names)<no_of_teams:
        team_name=input("enter team name: ").strip()
        if team_name=="":
            print("Name cannot be empty")
        elif any(team_name.lower() == name.lower() for name in team_names):
            print("team name already exist")
        else:
            team_names.append(team_name)
    print("Registered teams:",team_names)
    #cannot play against itself
    pair_count={}
    while True:
        print("Playing teams")
        team1=input("enter team 1 or stop:").strip()
        if team1.lower()=="stop":
            break
        team2=input("enter team 2:").strip()
        if team1.lower() not in [team.lower() for team in team_names] or  team2 not in [team.lower() for team in team_names]:
            print("Invalid team name")
        elif team1.lower() == team2.lower():
            print("a team cannot play against itself") 
        else:
            print("match is valid")
        #Each team must play every other team exactly twice
        pair=tuple(sorted((team1.lower(),team2.lower())))
        if pair_count.get(pair,0)>=2:
            print("teams already played twice")
        else:
            pair_count[pair]=pair_count.get(pair,0)+1
            
    return team_names
def calculate_balls(overs,balls,wickets):
    total_balls=overs*6+balls
    if wickets==10 and total_balls<120:
        total_balls=120
    return total_balls
        

def Match_details(team_names):
    matches=[]    
    while True:
        try:
            no_of_matches = int(input("Enter number of matches: "))
            if no_of_matches > 0:
                break
            else:
                print("Number of matches must be positive")
        except ValueError:
            print("Please enter a valid number")
    for i in range(no_of_matches):
        print(f"\n==========Match{i + 1} ==========")      
        while True:
            try:
                match_no = int(input("Enter match number: "))
                if match_no > 0:
                    break
                else:
                    print("Match number must be positive")
            except ValueError:
                print("Invalid match number")
        #First team name
        while True:
            team1 = input("Enter first team name: ").strip()
            if any(team1.lower()==name.lower() for name in team_names):
                break
            else:
                print("Invalid team name. Please enter a registered team.")
        while True:
            try:
                team1_runs=int(input("enter total run scored:"))
                if team1_runs>=0:
                    break
                else:
                    print("Cannot be negative")
            except(ValueError,KeyError):
                print("invalid runs")
        while True:
            try:
                team1_wickets=int(input("enter no.of wickets:"))
                if 0 <= team1_wickets <= 10:
                    break
                else:
                    print("wickets must be between 0 1nd 10")
            except(ValueError):
                print("please enter valid number")
        #first team's overs faced
        while True:
            try:
                over1=int(input("Enter competed overs:"))
                balls1=int(input("enter completed balls:"))
                if over1<0 or over1>20:
                    print("please enter overs between 0 and 20")  
                elif balls1<0 or balls1>5:
                    print("please enter balls between 0 and 5")
                elif over1==20 and balls1>0:
                    print("valid over and balls")
                else:
                    break
            except(ValueError):
                print("please enter valid overs and balls")
        print(f"{over1} overs ,{balls1} balls")
                
        #second team name
        while True:
            team2 = input("Enter second team name: ").strip()
            if not any(team2.lower() == name.lower() for name in team_names):
                print("Invalid team name.")
            elif team1.lower() == team2.lower():
                print("A team cannot play against itself.")
            else:
                break
            #total number of runs
        while True:
            try:
                team2_runs=int(input("enter total run scored:"))
                if team2_runs>=0:
                    break
                else:
                    print("Cannot be negative")
            except(ValueError,KeyError):
                print("invalid runs")
            
        while True:
            try:
                team2_wickets=int(input("enter wickets lost:"))
                if 0 <= team2_wickets <= 10:
                    break
                else:
                    print("Wickets must be between 0 and 10")
            except(ValueError,TypeError):
                print("Invalid wickets")
        # Second team's overs faced
        while True:
            try:
                over2=int(input("Enter competed overs:"))
                balls2=int(input("enter completed balls:"))
                if over2<0 or over2>20:
                    print("please enter overs between 0 and 20")  
                elif balls2<0 or balls2>5:
                    print("please enter balls between 0 and 5")
                elif over2==20 and balls2>0:
                    print("valid over and balls")
                else:
                    break
            except(ValueError):
                print("please enter valid overs and balls")
        print(f"{over2} overs ,{balls2} balls")

        for team, runs, wickets, overs, balls in[
        (team1,team1_runs,team1_wickets,over1,balls1),
        (team2,team2_runs,team2_wickets,over2,balls2)]:
            matches.append({
            "match_no":match_no,
            "team":team,
            "runs":runs,
            "wickets":wickets,
            "overs":overs,
            "balls":balls
        })
        print(matches)
        
        points_table={}
        for team in team_names:
            points_table[team]={
                "played":0,
                "won":0,
                "lost":0,
                "tie":0,
                "points":0,
                "runs_scored":0,
                "runs_conceded":0,
                "overs_faced":0,
                "overs_bowled":0,
                "nrr":0.00
            }
        # print(points_table)
        points_table[team1]["played"]+=1
        points_table[team2]["played"]+=1
        
        
        if team1_runs>team2_runs:
            print(f"Team: {team1} won")
            points_table[team1]["won"]+=1
            points_table[team1]["points"]+=2
            points_table[team2]["lost"]+=1
            
            
            
        elif team2_runs>team1_runs:
                print(f"Team: {team1} won")
                points_table[team2]["won"]+=1
                points_table[team2]["points"]+=2
                points_table[team1]["lost"]+=1
            
        elif team1_runs==team2_runs:
            print(f"Both teams tied {team1} and {team2}")
            points_table[team1]["points"]+=1
            points_table[team2]["points"]+=1
            points_table[team1]["tie"]+=1
            points_table[team2]["tie"]+=1
            
        #convert overs into legal balls for NRR
        team1_balls = calculate_balls(over1, balls1, team1_wickets)
        team2_balls = calculate_balls(over2, balls2, team2_wickets)
    
        points_table[team1]["runs_scored"]+=team1_runs
        points_table[team1]["overs_faced"]+=team1_balls
        points_table[team1]["runs_conceded"]+=team2_runs
        points_table[team1]["overs_bowled"]+=team2_balls
        
        points_table[team2]["runs_scored"]+=team2_runs
        points_table[team2]["overs_faced"]+=team2_balls
        points_table[team2]["runs_conceded"]+=team1_runs
        points_table[team2]["overs_bowled"]+=team1_balls
        
        for team in [team1,team2]:
            data=points_table[team]
            if data["overs_faced"]>0 and data["overs_bowled"]>0:
                scored_rate=data["runs_scored"]*6/data["overs_faced"]
                conceded_rate=data["runs_conceded"]*6/data["overs_bowled"]
                
                data["nrr"]=scored_rate-conceded_rate
                
        for team in [team1,team2]:
            print(f"Team {team} NRR:{points_table[team]["nrr"]:.3f}")
            
        # print(points_table)
        ranked_teams=sorted(
            team_names,
            key=lambda team:(
                points_table[team]["points"],
                points_table[team]["nrr"]
            ),reverse=True)

        print("--------CRICKET TOURNAMENT POINTS TABLE--------")
        rank=1
        for team in ranked_teams:
            data=points_table[team]
            
            print(f"Team position:{rank}")
            print(f"Team Name:{team.upper()}")
            print(f"Matches played:{data["played"]}")
            print(f"Matches won:{data["won"]}")
            print(f"Matches lost:{data["lost"]}")
            print(f"Matches Tied:{data["tie"]}")
            print(f"Total points:{data["points"]}")
            print(f"Runs Scored:{data["runs_scored"]}")
            print(f"Runs given:{data["runs_conceded"]}")
            print(f"Overs Faced:{data["overs_faced"]}")
            print(f"Overs bowled:{data["overs_bowled"]}")
            print(f"Net run rate:{data["nrr"]}")   
            
# registration()
team_name=registration()
Match_details(team_name)

# Import the random module for generating random player ratings and team selections
import random

# Quarterbacks (QB)
qb_players = {
    "Patrick Mahomes": {"team": "Kansas City Chiefs", "position": "QB", "passing_yards": 5953, "passing_touchdowns": 48, "rating": random.randint(70, 90)},
    "Jalen Hurts": {"team": "Philadelphia Eagles", "position": "QB", "passing_yards": 4280, "passing_touchdowns": 25, "rating": random.randint(70, 90)},
    "Joe Burrow": {"team": "Cincinnati Bengals", "position": "QB", "passing_yards": 5196, "passing_touchdowns": 39, "rating": random.randint(70, 90)},
    "Josh Allen": {"team": "Buffalo Bills", "position": "QB", "passing_yards": 4899, "passing_touchdowns": 38, "rating": random.randint(70, 90)},
    "Brock Purdy": {"team": "San Francisco 49ers", "position": "QB", "passing_yards": 5012, "passing_touchdowns": 26, "rating": random.randint(70, 90)},
    "Trevor Lawrence": {"team": "Jacksonville Jaguars", "position": "QB", "passing_yards": 4618, "passing_touchdowns": 30, "rating": random.randint(70, 90)},
    "Tua Tagovailoa": {"team": "Miami Dolphins", "position": "QB", "passing_yards": 3548, "passing_touchdowns": 25, "rating": random.randint(70, 90)},
    "Jared Goff": {"team": "Detroit Lions", "position": "QB", "passing_yards": 4438, "passing_touchdowns": 29, "rating": random.randint(70, 90)},
    "Dak Prescott": {"team": "Dallas Cowboys", "position": "QB", "passing_yards": 3000, "passing_touchdowns": 20, "rating": random.randint(70, 90)},
    "Lamar Jackson": {"team": "Baltimore Ravens", "position": "QB", "passing_yards": 3100, "passing_touchdowns": 22, "rating": random.randint(70, 90)}
}

# Running Backs (RB)
rb_players = {
    "Christian McCaffrey": {"team": "San Francisco 49ers", "position": "RB", "rushing_yards": 1139, "rushing_touchdowns": 8, "rating": random.randint(70, 90)},
    "Austin Ekeler": {"team": "Los Angeles Chargers", "position": "RB", "rushing_yards": 915, "rushing_touchdowns": 13, "rating": random.randint(70, 90)},
    "Josh Jacobs": {"team": "Las Vegas Raiders", "position": "RB", "rushing_yards": 1653, "rushing_touchdowns": 12, "rating": random.randint(70, 90)},
    "James Conner": {"team": "Arizona Cardinals", "position": "RB", "rushing_yards": 1538, "rushing_touchdowns": 13, "rating": random.randint(70, 90)},
    "Jahmyr Gibbs": {"team": "Detroit Lions", "position": "RB", "rushing_yards": 1525, "rushing_touchdowns": 12, "rating": random.randint(70, 90)},
    "Saquon Barkley": {"team": "New York Giants", "position": "RB", "rushing_yards": 1312, "rushing_touchdowns": 10, "rating": random.randint(70, 90)},
    "Jonathon Taylor": {"team": "Indianapolis Colts", "position": "RB", "rushing_yards": 1173, "rushing_touchdowns": 8, "rating": random.randint(70, 90)},
    "Bijan Robinson": {"team": "Atlanta Falcons", "position": "RB", "rushing_yards": 1121, "rushing_touchdowns": 2, "rating": random.randint(70, 90)},
    "Alvin Kamara": {"team": "New Orleans Saints", "position": "RB", "rushing_yards": 1040, "rushing_touchdowns": 5, "rating": random.randint(70, 90)},
    "Raheem Mostert": {"team": "Miami Dolphins", "position": "RB", "rushing_yards": 1269, "rushing_touchdowns": 11, "rating": random.randint(70, 90)}
}

# Wide Receivers 1 (WR1)
wr1_players = {
    "Justin Jefferson": {"team": "Minnesota Vikings", "position": "WR", "receiving_yards": 1600, "touchdowns": 10, "rating": random.randint(70, 90)},
    "Cooper Kupp": {"team": "Los Angeles Rams", "position": "WR", "receiving_yards": 1500, "touchdowns": 12, "rating": random.randint(70, 90)},
    "Davante Adams": {"team": "Las Vegas Raiders", "position": "WR", "receiving_yards": 1400, "touchdowns": 11, "rating": random.randint(70, 90)},
    "Ja'Marr Chase": {"team": "Cincinnati Bengals", "position": "WR", "receiving_yards": 1400, "touchdowns": 11, "rating": random.randint(70, 90)},
    "A.J. Brown": {"team": "Philadelphia Eagles", "position": "WR", "receiving_yards": 1300, "touchdowns": 9, "rating": random.randint(70, 90)},
    "CeeDee Lamb": {"team": "Dallas Cowboys", "position": "WR", "receiving_yards": 1200, "touchdowns": 8, "rating": random.randint(70, 90)},
    "Mike Evans": {"team": "Tampa Bay Buccaneers", "position": "WR", "receiving_yards": 1100, "touchdowns": 10, "rating": random.randint(70, 90)},
    "DK Metcalf": {"team": "Seattle Seahawks", "position": "WR", "receiving_yards": 1050, "touchdowns": 8, "rating": random.randint(70, 90)},
    "Keenan Allen": {"team": "Los Angeles Chargers", "position": "WR", "receiving_yards": 1000, "touchdowns": 7, "rating": random.randint(70, 90)},
    "Amon-Ra St. Brown": {"team": "Detroit Lions", "position": "WR", "receiving_yards": 950, "touchdowns": 6, "rating": random.randint(70, 90)}
}

# Wide Receivers 2 (WR2)
wr2_players = {
    "Tyreek Hill": {"team": "Miami Dolphins", "position": "WR", "receiving_yards": 1300, "touchdowns": 9, "rating": random.randint(70, 90)},
    "Stefon Diggs": {"team": "Buffalo Bills", "position": "WR", "receiving_yards": 1200, "touchdowns": 10, "rating": random.randint(70, 90)},
    "Deebo Samuel": {"team": "San Francisco 49ers", "position": "WR", "receiving_yards": 1100, "touchdowns": 8, "rating": random.randint(70, 90)},
    "Amari Cooper": {"team": "Cleveland Browns", "position": "WR", "receiving_yards": 1100, "touchdowns": 9, "rating": random.randint(70, 90)},
    "Chris Godwin": {"team": "Tampa Bay Buccaneers", "position": "WR", "receiving_yards": 900, "touchdowns": 5, "rating": random.randint(70, 90)},
    "Michael Pittman Jr.": {"team": "Indianapolis Colts", "position": "WR", "receiving_yards": 1000, "touchdowns": 6, "rating": random.randint(70, 90)},
    "Jayden Reed": {"team": "Green Bay Packers", "position": "WR", "receiving_yards": 850, "touchdowns": 5, "rating": random.randint(70, 90)},
    "DJ Moore": {"team": "Chicago Bears", "position": "WR", "receiving_yards": 900, "touchdowns": 6, "rating": random.randint(70, 90)},
    "Chris Olave": {"team": "New Orleans Saints", "position": "WR", "receiving_yards": 800, "touchdowns": 7, "rating": random.randint(70, 90)},
    "Jaylen Waddle": {"team": "Miami Dolphins", "position": "WR", "receiving_yards": 1100, "touchdowns": 8, "rating": random.randint(70, 90)}
}

# Tight Ends (TE)
te_players = {
    "Travis Kelce": {"team": "Kansas City Chiefs", "position": "TE", "receiving_yards": 1200, "touchdowns": 9, "rating": random.randint(70, 90)},
    "Mark Andrews": {"team": "Baltimore Ravens", "position": "TE", "receiving_yards": 1000, "touchdowns": 8, "rating": random.randint(70, 90)},
    "George Kittle": {"team": "San Francisco 49ers", "position": "TE", "receiving_yards": 900, "touchdowns": 7, "rating": random.randint(70, 90)},
    "Darren Waller": {"team": "Las Vegas Raiders", "position": "TE", "receiving_yards": 800, "touchdowns": 6, "rating": random.randint(70, 90)},
    "Evan Engram": {"team": "Jacksonville Jaguars", "position": "TE", "receiving_yards": 850, "touchdowns": 5, "rating": random.randint(70, 90)},
    "Dallas Goedert": {"team": "Philadelphia Eagles", "position": "TE", "receiving_yards": 700, "touchdowns": 5, "rating": random.randint(70, 90)},
    "Dalton Kincaid": {"team": "Buffalo Bills", "position": "TE", "receiving_yards": 650, "touchdowns": 6, "rating": random.randint(70, 90)},
    "T.J. Hockenson": {"team": "Detroit Lions", "position": "TE", "receiving_yards": 600, "touchdowns": 4, "rating": random.randint(70, 90)},
    "Sam LaPorta": {"team": "Detroit Lions", "position": "TE", "receiving_yards": 550, "touchdowns": 4, "rating": random.randint(70, 90)},
    "Jake Ferguson": {"team": "Dallas Cowboys", "position": "TE", "receiving_yards": 500, "touchdowns": 5, "rating": random.randint(70, 90)}
}

# List of positions
positions = ["QB", "RB", "WR1", "WR2", "TE"]

# Dictionary to store all teams
teams = {}

# Dictionary to store all players
all_players = {}

def generate_random_team(team_name):
    """
    Generates a random team by selecting players for each position.

    Args:
        team_name (str): The name of the team to be generated.

    Returns:
        dict: A dictionary representing the team with players assigned to positions.
    """
    team = {
        "Team Name": team_name,
        "Score": 0,
        "Wins": 0,
        "Losses": 0
    }
    for position in positions:
        players_in_position = list(all_players[position].keys())
        if players_in_position:
            selected_player = random.choice(players_in_position)
            team[position] = all_players[position].pop(selected_player)
    return team

def create_cpu_teams():
    # Creates CPU teams with predefined names and adds them to the teams dictionary.
    cpu_team_names = ["Loud and Stroud", "Sherlock Mahomes", "Just the Tua Us", 
                      "Dak to the Future", "Inglorious Staffords", "Get Goff My Lawn", 
                      "Wentz Upon a Time"]

    for cpu_name in cpu_team_names:
        if cpu_name not in teams:
            teams[cpu_name] = generate_random_team(cpu_name)

def create_teams(player_name):
    """
    Creates a user's team and CPU teams.

    Args:
        player_name (str): The name of the user's team.
    """
    team = {
        "Team Name": player_name,
        "Score": 0,
        "Wins": 0,
        "Losses": 0
    }
    
    teams[player_name] = team
    create_cpu_teams()  # Create CPU teams after the user's team is created

def initialize_all_players():
    """
    Initializes the all_players dictionary with player data for each position.
    """
    global all_players
    all_players = {
        "QB": qb_players.copy(),
        "RB": rb_players.copy(),
        "WR1": wr1_players.copy(),
        "WR2": wr2_players.copy(),
        "TE": te_players.copy()
    }

# Initialize all players at the start
initialize_all_players()
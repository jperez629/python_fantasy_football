import random
from team_management import teams, all_players, positions, generate_random_team, initialize_all_players
from match_simulation import simulate_matches
from standings import display_standings

# Global variables to manage game state
team_name = None
players_drafted = False
season_started = False
team_viewed = False
current_week = 1
total_weeks = 10

def show_menu():
    # Displays the main menu of the Fantasy Football game.
    print(" _________________________________________________________________________________")
    print("|          |  10  |  20  |  30  |  40  |  50  | 40  | 30  | 20  | 10  |          |")
    print("|          |      |      |      |      |      |     |     |     |     |          |")
    print("|    P     |      |      |      |      |      |     |     |     |     |     P    |")
    print("|    Y     |      |      |      |      |      |     |     |     |     |     Y    |")
    print("|    T     |      |      |      |      |      |     |     |     |     |     T    |")
    print("|    H     |      |      |  FANTASY FOOTBALL LEAGUE |     |     |     |     H    |")
    print("|    O     |      |      |      |      |      |     |     |     |     |     O    |")
    print("|    N     |      |      |      |      |      |     |     |     |     |     N    |")
    print("|          |      |      |      |      |      |     |     |     |     |          |")
    print("|          |      |      |      |      |      |     |     |     |     |          |")
    print("|________________________________________________________________________________|")
    print("1) Name Your Team")
    print("2) Draft Players")
    print("3) View Team")
    print("4) Start Season")
    print("5) Quit")

def create_your_team():
    # Allows the user to create their team by entering a team name.
    global team_name, players_drafted, season_started, team_viewed
    if team_name:
        print("Team already created! You cannot create another team.")
        return
    new_team_name = input("Enter your team name: ")
    if new_team_name in teams:
        print("Team name already exists! Please choose a different name.")
        return
    print(f"Team {new_team_name} created!")
    team_name = new_team_name
    teams[new_team_name] = {"Score": 0, "Wins": 0, "Losses": 0}
    players_drafted = False
    season_started = False
    team_viewed = False

def draft_players():
    # Allows the user to draft players for their team by selecting players for each position.
    global players_drafted, all_players
    if not team_name:
        print("You need to create a team first!")
        return
    if players_drafted:
        print("Players already drafted!")
        return
    print(f"\n{team_name}, it's time to draft your players!")

    drafted_team = {"QB": None, "RB": None, "WR1": None, "WR2": None, "TE": None}

    for position in positions:
        print(f"\nDrafting for position: {position}")
        available_players = list(all_players[position].keys())
        if not available_players:
            print(f"No available players left for position: {position}")
            continue
        random.shuffle(available_players)
        drafted_player_name = available_players[0]
        drafted_player_stats = all_players[position].pop(drafted_player_name)

        print(f"You have drafted: {drafted_player_name}")
        print(f"Stats - Team: {drafted_player_stats['team']}, Rating: {drafted_player_stats['rating']}")

        drafted_team[position] = {'name': drafted_player_name, **drafted_player_stats}

    teams[team_name] = drafted_team
    players_drafted = True

def view_team():
    # Displays the user's team roster.
    global team_viewed
    if not team_name:
        print("You need to create and draft a team first!")
        return
    if team_viewed:
        print("Team already viewed. You're ready to start the season!")
        return
    else:
        print(f"\n{team_name} Roster:")
        for position, player in teams[team_name].items():
            if player:
                print(f"{position}: {player['name']} - Rating: {player['rating']}")
            else:
                print(f"{position}: Not yet drafted")
        team_viewed = True

def start_season():
    # Starts the season by simulating matches each week and displaying standings.
    global season_started, current_week, total_weeks, players_drafted

    if not players_drafted:
        print("You need to draft your players before starting the season!")
        return

    if season_started:
        if current_week > total_weeks:
            display_end_of_season_awards(teams)
            return "season_end"
        else:
            print(f"\nWeek {current_week} matches:")
            simulate_week_matches()
            display_standings(teams)
            current_week += 1
            return
    else:
        print("\nSeason is starting... Good luck!")
        cpu_team_names = ["Loud and Stroud", "Sherlock Mahomes", "Just the Tua Us", 
                          "Dak to the Future", "Inglorious Staffords", "Get Goff My Lawn", 
                          "Wentz Upon a Time"]

        # Create CPU teams
        for cpu_name in cpu_team_names:
            if cpu_name not in teams:
                teams[cpu_name] = generate_random_team(cpu_name)

        # Simulate each week of the season
        total_weeks = 10
        for week in range(1, total_weeks + 1):
            print(f"\nWeek {week} matches:")
            simulate_week_matches()
            display_standings(teams)

            if week == total_weeks:
                display_end_of_season_awards(teams)
                return "season_end"
        
        season_started = True
        current_week = 1
        return

def display_end_of_season_awards(teams):
    # Displays the end of season awards and final leaderboard.
    print("\n--- End of Season Awards ---")
    top_scorer = max(teams.items(), key=lambda x: x[1]['Score'])
    print(f"Top Scorer: {top_scorer[0]} with {top_scorer[1]['Score']} points")
    toilet_bowl_champion = max(teams.items(), key=lambda x: x[1]['Losses'])
    print(f"Toilet Bowl Champion: {toilet_bowl_champion[0]}")
    print("\n--- Final Leaderboard ---")
    display_standings(teams)

def simulate_week_matches():
    # Simulates matches for a week by randomly pairing teams and updating scores and standings.
    team_names = list(teams.keys())
    random.shuffle(team_names)

    for i in range(0, len(team_names), 2):
        if i + 1 < len(team_names):
            team1 = team_names[i]
            team2 = team_names[i + 1]
            simulate_matches(teams[team1], teams[team2])

def display_menu():
    # Main function to display the menu and handle user choices.
    global current_week, total_weeks
    while True:
        show_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            create_your_team()
        elif choice == '2':
            if team_name:
                draft_players()
            else:
                print("Please create a team first!")
        elif choice == '3':
            if team_name:
                view_team()
            else:
                print("Please create a team first!")
        elif choice == '4':
            if team_name:
                result = start_season()
                if result == "season_end":
                    while True:  
                        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
                        if play_again == "yes":
                            reset_game()
                            break  # Restart the game
                        elif play_again == "no":
                            print("Exiting game. Goodbye!")
                            exit()
                        else:
                            print("Invalid choice. Please try again.")
            else:
                print("Please create a team first!")
        elif choice == '5':
            print("Exiting game. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2/3/4/5).")

def reset_game():
    # Resets the game to its initial state for a new playthrough.
    global team_name, players_drafted, season_started, team_viewed, current_week
    team_name = None
    players_drafted = False
    season_started = False
    team_viewed = False
    current_week = 1
    teams.clear()
    initialize_all_players()  # Reinitialize all players when resetting the game
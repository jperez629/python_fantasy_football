from menu import display_menu
from team_management import teams, initialize_all_players
from match_simulation import simulate_matches
from standings import display_standings
import random

def simulate_week():
    """
    Simulates the matches for a week by shuffling the teams
    and pairing them for matches.
    """
    team_names = list(teams.keys())
    random.shuffle(team_names)  # Shuffle for random matchups

    for i in range(0, len(team_names), 2):
        if i + 1 < len(team_names):
            team1 = teams[team_names[i]]
            team2 = teams[team_names[i + 1]]
            simulate_matches(team1, team2)

def display_end_of_season_awards(teams):
    """
    Displays the end of season awards, including the top scorer
    and the toilet bowl champion.
    """
    print("\n--- End of Season Awards ---")
    top_scorer = max(teams.items(), key=lambda x: x[1]['Score'])
    print(f"Top Scorer: {top_scorer[0]} with {top_scorer[1]['Score']} points")
    toilet_bowl_champion = max(teams.items(), key=lambda x: x[1]['Losses'])
    print(f"Toilet Bowl Champion: {toilet_bowl_champion[0]}")
    print("\n--- Final Leaderboard ---")
    display_standings(teams)

def main():
    # Main function to initialize players and display the main menu.
    initialize_all_players()
    display_menu()

if __name__ == "__main__":
    main()


def display_standings(teams):
    """
    Displays the standings of the teams, sorted by Wins and then by Score.
    
    Args:
        teams (dict): A dictionary of teams with their respective data (Wins, Losses, Score).
    """
    # Convert teams dictionary to a list of tuples for sorting
    team_list = [(team_name, data) for team_name, data in teams.items()]

    # Sort the team list first by Wins and then by Score in case of a tie
    sorted_standings = sorted(team_list, key=lambda x: (x[1].get("Wins", 0), x[1].get("Score", 0)), reverse=True)

    # Display the standings
    for i, (team_name, data) in enumerate(sorted_standings, start=1):
        wins = data.get("Wins", 0)
        losses = data.get("Losses", 0)
        score = data.get("Score", 0)
        print(f"{i}. {team_name} - Wins: {wins}, Losses: {losses}, Score: {score}")
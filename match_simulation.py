import random

def simulate_matches(team1, team2):
    """
    Simulates a match between two teams by calculating the performance
    of players in each position and updating the team scores and records.
    """
    # Initialize scores for both teams
    team1_score = 0
    team2_score = 0

    # List of positions to be simulated
    positions = ["QB", "RB", "WR1", "WR2", "TE"]

    # Simulate performance for each position
    for position in positions:
        player1 = team1.get(position, {})
        player2 = team2.get(position, {})

        # Simulate player performance using player ratings and random factor
        player1_performance = calculate_performance(player1)
        player2_performance = calculate_performance(player2)

        # Update team scores based on player performance
        team1_score += player1_performance
        team2_score += player2_performance

    # Update team records based on match outcome
    update_team_records(team1, team2, team1_score, team2_score)

def calculate_performance(player):
    """
    Calculates the performance of a player based on their rating and a random factor.
    
    Args:
        player (dict): A dictionary containing player attributes, including 'rating'.
        
    Returns:
        int: The calculated performance score for the player.
    """
    if player:
        base_performance = player.get('rating', 0)
        random_factor = random.randint(0, 100)
        return base_performance + random_factor
    return 0

def update_team_records(team1, team2, score1, score2):
    """
    Updates the records of two teams based on the scores of their match.
    
    Args:
        team1 (dict): A dictionary representing the first team.
        team2 (dict): A dictionary representing the second team.
        score1 (int): The score of the first team.
        score2 (int): The score of the second team.
    """
    # Update the cumulative scores
    team1['Score'] = team1.get('Score', 0) + score1
    team2['Score'] = team2.get('Score', 0) + score2

    # Update wins and losses based on the match outcome
    if score1 > score2:
        team1['Wins'] = team1.get('Wins', 0) + 1
        team2['Losses'] = team2.get('Losses', 0) + 1
    elif score2 > score1:
        team2['Wins'] = team2.get('Wins', 0) + 1
        team1['Losses'] = team1.get('Losses', 0) + 1

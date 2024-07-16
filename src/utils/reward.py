def calculate_reward(prev_state, current_state, action):
    reward = 0
    
    # Reward for moving right (progressing)
    if current_state['player_x'] > prev_state['player_x']:
        reward += 1
    
    # Reward for defeating enemies
    if current_state['enemies_defeated'] > prev_state['enemies_defeated']:
        reward += 10
    
    # Penalty for taking damage
    if current_state['player_health'] < prev_state['player_health']:
        reward -= 5
    
    # Large reward for reaching a new area or defeating a boss
    if current_state['area'] != prev_state['area']:
        reward += 100
    
    return reward
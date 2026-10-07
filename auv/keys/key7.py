import math

s = input("Enter target string: ").strip()

keys = {
    "1": {"x": 0.0, "y": 38.0}, "2": {"x": 19.0, "y": 38.0}, "3": {"x": 38.0, "y": 38.0}, "4": {"x": 57.0, "y": 38.0},
    "5": {"x": 76.0, "y": 38.0}, "6": {"x": 95.0, "y": 38.0}, "7": {"x": 114.0, "y": 38.0}, "8": {"x": 133.0, "y": 38.0},
    "q": {"x": 0.0, "y": 19.0}, "w": {"x": 19.0, "y": 19.0}, "e": {"x": 38.0, "y": 19.0}, "r": {"x": 57.0, "y": 19.0},
    "t": {"x": 76.0, "y": 19.0}, "y": {"x": 95.0, "y": 19.0}, "u": {"x": 114.0, "y": 19.0}, "i": {"x": 133.0, "y": 19.0},
    "a": {"x": 0.0, "y": 0.0}, "s": {"x": 19.0, "y": 0.0}, "d": {"x": 38.0, "y": 0.0}, "f": {"x": 57.0, "y": 0.0},
    "g": {"x": 76.0, "y": 0.0}, "h": {"x": 95.0, "y": 0.0}, "j": {"x": 114.0, "y": 0.0}, "k": {"x": 133.0, "y": 0.0},
}

finger_names = ["left middle", "left index", "right index", "right middle"]

def get_dist(k1, k2):
    """Calculates distance between two key names"""
    p1, p2 = keys[k1], keys[k2]
    return math.hypot(p1["x"] - p2["x"], p1["y"] - p2["y"])

def is_valid_state(state):
    """
    Enforces physical limitations of the human hands.
    state = (left_middle_key, left_index_key, right_index_key, right_middle_key)
    """
    k_lm, k_li, k_ri, k_rm = state
    
    # 1. NO CROSSING: Ensure strict left-to-right ordering on the X-axis
    x_lm = keys[k_lm]["x"]
    x_li = keys[k_li]["x"]
    x_ri = keys[k_ri]["x"]
    x_rm = keys[k_rm]["x"]
    
    if not (x_lm <= x_li < x_ri <= x_rm):
        return False
        
    # 2. MAX STRETCH: Distance between fingers on the same hand cannot exceed 85
    if get_dist(k_lm, k_li) > 85.0:
        return False
        
    if get_dist(k_ri, k_rm) > 85.0:
        return False
        
    return True

# 1. Setup Viterbi Initial State
initial_state = ("a", "s", "j", "k")
current_layer = {initial_state: (0.0, None, None)}
trellis = [current_layer]

valid_string = [ch for ch in s if ch in keys]

# 2. Build the Trellis (Forward Pass)
for char in valid_string:
    next_layer = {}
    
    for state, (cost, _, _) in current_layer.items():
        for f_idx in range(4):
            # Simulate moving one finger to the target character
            move_cost = get_dist(state[f_idx], char)
            
            # Create the new state
            new_state_list = list(state)
            new_state_list[f_idx] = char
            new_state = tuple(new_state_list)
            
            # Toss out the state immediately if it breaks physical rules
            if not is_valid_state(new_state):
                continue
                
            total_cost = cost + move_cost
            
            if new_state not in next_layer or total_cost < next_layer[new_state][0]:
                next_layer[new_state] = (total_cost, state, f_idx)
                
    current_layer = next_layer
    trellis.append(current_layer)

# 3. Backtrack to find the optimal path
if not current_layer:
    print("No valid string provided or no physically possible paths found.")
else:
    best_final_state = min(current_layer.keys(), key=lambda s: current_layer[s][0])
    
    path = []
    curr_state = best_final_state
    
    for t in range(len(valid_string), 0, -1):
        cost, prev_state, f_idx = trellis[t][curr_state]
        path.append((valid_string[t-1], finger_names[f_idx]))
        curr_state = prev_state
        
    path.reverse()
    
    for idx, (ch, fname) in enumerate(path):
        print(f"Step {idx + 1}: '{ch}' pressed by {fname}")
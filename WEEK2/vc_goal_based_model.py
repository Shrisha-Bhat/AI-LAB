def goal_based_vacuum(current_location, room_states):
    goal_state = {"A": "Clean", "B": "Clean"}
    print(f"Start Location: {current_location} | Status: {room_states}")
    actions = []
    if room_states["A"] == "Dirty" and room_states["B"] == "Dirty":
        actions = ["Suck", "Right", "Suck"] if current_location == "A" else ["Suck", "Left", "Suck"]
    elif room_states["A"] == "Dirty" and room_states["B"] == "Clean":
        actions = ["Suck"] if current_location == "A" else ["Left", "Suck"]
    elif room_states["A"] == "Clean" and room_states["B"] == "Dirty":
        actions = ["Suck"] if current_location == "B" else ["Right", "Suck"]
    print(f"Goal Plan: {actions}")
    for action in actions:
        print(f"Action: {action}")
        if action == "Suck":
            room_states[current_location] = "Clean"
        elif action == "Right":
            current_location = "B"
        elif action == "Left":
            current_location = "A"
    print(f"End Location: {current_location} | Status: {room_states}")
    if room_states == goal_state:
        print("Goal Achieved!")
goal_based_vacuum(current_location="A", room_states={"A": "Dirty", "B": "Dirty"})

import random
import time

# Initialize game variables
days = 0
group_size = 4
food = 10  # Initial food stock (units)
water = 10  # Initial water stock (units)
health = [100] * group_size  # Health for each group member
scavenging_status = [False] * group_size  # Track whether a member is out scavenging
scavenging_days_left = [0] * group_size  # Days left until each member returns
prepared_defense = False  # Track if defense was prepared for the day
scavenges_in_row = 0  # Track how many days in a row members have gone scavenging
morale = [100] * group_size  # Morale for each group member

# Track how many days without food or water
days_without_food = [0] * group_size
days_without_water = [0] * group_size

# Bandit attack variables
base_defense_chance = 80  # Base percentage chance to defend the shelter successfully
min_defense_chance = 20  # Minimum defense chance after health and days reduce it
bandit_frequency_increase = 0.05  # Increase in raid probability later in the game

# List of special events with reduced resource changes
events = [
    {"event": "💧 A water pipe burst, water wasted!", "water_change": -1, "food_change": 0, "health_change": 0},
    {"event": "🍞 Found extra food while scavenging!", "water_change": 0, "food_change": 1, "health_change": 0},
    {"event": "🤒 One member got sick from radiation.", "water_change": 0, "food_change": 0, "health_change": -15},
    {"event": "🌧️ Rainwater collected!", "water_change": 1, "food_change": 0, "health_change": 0},
    {"event": "🥫 Tough times, food spoiled!", "water_change": 0, "food_change": -1, "health_change": 0},
    {"event": "☢️ Radiation levels dropped slightly, health improved.", "water_change": 0, "food_change": 0, "health_change": 5},
]

# Hunger and thirst status stages
hunger_stages = ["🍽️ Filled", "🥗 Normal", "😋 Craving", "🍵 Hungry", "🥴 Starving"]
thirst_stages = ["💦 Hydrated", "🚰 Normal", "🥤 Thirsty", "🧊 Parched", "💧 Dehydrated"]

def display_status():
    """Display the current status of the group."""
    print(f"\n🌄 Day {days}:")
    print(f"🍞 Food remaining: {food} units")
    print(f"💧 Water remaining: {water} units")
    
    # Display health, hunger, thirst, and morale status for each member
    for i in range(group_size):
        hunger_status = hunger_stages[min(days_without_food[i] // 2, 4)]  # Stage based on days without food
        thirst_status = thirst_stages[min(days_without_water[i], 4)]  # Stage based on days without water
        print(f"👤 Member {i + 1}:")
        print(f"   💪 Health: {health[i]}")
        print(f"   🍽️ Hunger: {hunger_status}")
        print(f"   💧 Thirst: {thirst_status}")
        print(f"   😊 Morale: {morale[i]}")
        print()  # Blank line for separation

    print(f"🔄 Scavenging status: {scavenging_status}")
    print(f"⏳ Days until scavengers return: {scavenging_days_left}")
    print(f"🛡️ Defense prepared: {prepared_defense}")

def ration_resources():
    """Allow the player to choose whether to give food and water to each group member."""
    global food, water, days_without_food, days_without_water
    
    print("\n🧑‍🍳 Time to ration food and water.")
    for i in range(group_size):
        if scavenging_status[i]:
            continue  # Skip members that are out scavenging
        
        # Food decision
        give_food = input(f"   🍞 Give food to member {i + 1}? (yes/no): ").lower()
        if give_food == 'yes' and food >= 0.5:
            food -= 0.5
            days_without_food[i] = 0  # Reset days without food
        else:
            days_without_food[i] += 1
        
        # Water decision
        give_water = input(f"   💧 Give water to member {i + 1}? (yes/no): ").lower()
        if give_water == 'yes' and water >= 0.5:
            water -= 0.5
            days_without_water[i] = 0  # Reset days without water
        else:
            days_without_water[i] += 1

def update_health_and_morale():
    """Update health based on how long each member has gone without food or water and decrease morale."""
    global morale
    for i in range(group_size):
        if scavenging_status[i]:
            continue  # Skip members that are out scavenging
        
        # Health impact of hunger
        if days_without_food[i] > 7:  # Start losing health after 7 days without food
            health[i] -= (days_without_food[i] - 7) * 2  # Lose 2 health for each day past 7

        # Health impact of thirst
        if days_without_water[i] > 4:  # Start losing health after 4 days without water
            health[i] -= (days_without_water[i] - 4) * 5  # Lose 5 health for each day past 4

        # Make sure health doesn't drop below 0
        health[i] = max(0, health[i])

        # Morale decrease
        if group_size == 1:
            morale[i] -= 7  # Fixed decrease if only one member
        else:
            morale[i] -= random.randint(1, 6)  # Daily decrease

        # Ensure morale stays within bounds
        morale[i] = max(0, morale[i])

        # Check if morale is zero or less, if so, member leaves the shelter
        if morale[i] <= 0:
            print(f"❌ Member {i + 1} has left the shelter due to despair.")
            health[i] = 0  # Considered as dead
        
def apply_event():
    """Apply a random event that affects resources or health, and display the changes."""
    global food, water, health
    event = random.choice(events)
    print(f"\n📅 Special event: {event['event']}")

    # Track changes
    food_change = event["food_change"]
    water_change = event["water_change"]
    health_change = event["health_change"]

    # Apply changes to resources
    food_before = food
    water_before = water
    food += food_change
    water += water_change
    
    # Make sure food and water don't drop below 0
    food = max(0, food)
    water = max(0, water)
    
    # Display food and water changes
    if food_change != 0:
        print(f"   🍞 Food changed by {food_change} units (Now: {food}).")
    if water_change != 0:
        print(f"   💧 Water changed by {water_change} units (Now: {water}).")

    # Apply health changes to all group members
    for i in range(group_size):
        if health_change != 0:
            old_health = health[i]
            health[i] = max(0, health[i] + health_change)
            print(f"   👤 Member {i + 1}'s health changed from {old_health} to {health[i]}.")

def morale_increase():
    """Apply morale changes based on the outcomes of the day."""
    global morale
    for i in range(group_size):
        # Increase morale based on positive events or conditions
        if random.random() < 0.2:  # 20% chance to boost morale
            boost = random.randint(5, 10)
            morale[i] += boost
            morale[i] = min(100, morale[i])  # Ensure morale doesn't exceed 100
            print(f"   🎉 Member {i + 1}'s morale increased by {boost}.")

def check_game_over():
    """Check if the game is over due to all members perishing."""
    if all(h <= 0 for h in health):
        print("🚫 Game Over! All group members have perished.")
        return True
    
    return False

def send_for_scavenging():
    """Send a group member out for scavenging."""
    global scavenging_status, scavenging_days_left, scavenges_in_row

    if any(scavenging_status):
        print("❌ Someone is already out scavenging. Only one person can go at a time.")
        return

    print("\n🎒 Choose a member to send scavenging (1-4):")
    for i in range(group_size):
        if not scavenging_status[i]:  # Only show available members
            print(f"   👤 Member {i + 1}: Health = {health[i]}, Morale = {morale[i]}")
    
    member_choice = int(input("> ")) - 1
    
    if scavenging_status[member_choice]:
        print("❌ That member is already out scavenging.")
    elif morale[member_choice] < 40:
        print(f"👤 Member {member_choice + 1} refuses to scavenge due to low morale.")
    else:
        scavenging_status[member_choice] = True
        scavenging_days_left[member_choice] = random.randint(2, 5)  # Random return time
        scavenges_in_row += 1
        print(f"✅ Member {member_choice + 1} sent out to scavenge for {scavenging_days_left[member_choice]} days.")

# Main game loop
while True:
    # New day
    days += 1
    display_status()

    # Daily choice menu
    print("\n🔄 What would you like to do today?")
    print("   1. Check supplies and statuses.")
    print("   2. Send someone scavenging.")
    print("   3. Ration food and water.")
    print("   4. Prepare defenses.")
    print("   5. Boost morale.")
    print("   6. End the day.")
    
    choice = int(input("> "))
    
    if choice == 1:
        display_status()
        continue
    elif choice == 2:
        send_for_scavenging()
    elif choice == 3:
        ration_resources()
    elif choice == 4:
        prepared_defense = True
        print("🛡️ Defense prepared for the day.")
    elif choice == 5:
        morale_increase()
    elif choice == 6:
        print("🕰️ Day ended.")
    
    # End of day updates
    update_health_and_morale()
    apply_event()
    
    if check_game_over():
        break

    # Reset daily modifiers
    prepared_defense = False

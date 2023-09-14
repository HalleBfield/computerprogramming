def print_my_name(name):
    print(name)

    print_my_name("Halle B")

def trip_planner(start, end, duration, mode ='car'):
    print(f"it looks like you're starting your trip from {start}")
    print(f"you are planning to get to {end}")
    print(f"it should take you about {duration} hours")
    print(f"I see you are taking a {mode}")

trip_planner('paradigm','bearlake', 3)

trip_planner('megaplex', 'disneyland', 2 ,'plane')

trip_planner('great harvest', 'lake powell', 4,)
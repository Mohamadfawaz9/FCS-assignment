def employee():
    while True:
        s = '''Hello! Please enter:
        1. To go to the drivers' menu.
        2. To go to the cities' menu.
        3. To exit the system.'''
        print(s)
        entry = input("Enter 1, 2 or 3 according to the above options: ")
        if entry == "1":
            pass
        elif entry == "2":
            pass
        elif entry == "3":
            return

# Add the cities to the graph
class Cities:
    def __init__(self):
        self.graph = {}

    def add_city(self):
        s = '''Please enter:
        1. If you want to add a city with a driver.
        2. If you want to add a neighbouring city with a delivery guy.
        3. If you don't want to add cities or want to go back to main menu'''
        print(s)
        while True:
            answer = input("Enter 1, 2 or 3 according to the above options: ")
            if answer == "1":
                n_city = input("Enter the city name: ")   # n_city as "new city"
                if n_city not in self.graph:
                    self.graph[n_city] = []
                else:
                    print(s)
            elif answer == "2":
                city = input("Enter the name of the main city: ")
                nhb_city = input("Enter the neighbouring city: ")  # nhb_city as "neighbouring city"
                if nhb_city not in self.graph:
                    self.graph[nhb_city] = []
                    self.graph[nhb_city].append([city])
                else:
                    self.graph[city].append(nhb_city)
            elif answer == "3":
                return

    def delete_city(self):
        s = '''Please enter:
        1. To delete a city
        2. to go back to main menu'''
        print(s)
        ans = input("Enter 1 or 2 according to the above options: ")
        while True:
            if ans == "1":
                city = input("Enter the name of the city to remove: ")
                if city in self.graph:
                    del(self.graph[city])
                else:
                    print("This entry is not correct. Please try again or enter '2' if you want to go back to main menu")
            elif ans == "2":
                return

    def print_cities(self):
        s = '''Hello! Please enter:
        1. If you just want to see the registered cities in the system.
        2. If you want to see the connections between the cities.
        3. If you want to go back to main menu.'''
        print(s)
        while True:
            entry = input("Enter a number from the above options according to what you want: ")
            if entry == "1":
                for key in self.graph:
                    print(key, end = " - ")  #this one only prints the keys (the registered cities)
                return
            elif entry == "2":
                print(self.graph)    # this one prints all the keys with their values (the cities and the ones it has connections with)
                return
            elif entry == "3":
                return
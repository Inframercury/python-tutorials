class Client:
    def __init__(self, user_name):
        self.user_name = user_name

    def __repr__(self):
        return self.user_name

    def __hash__(self):
        return hash(self.user_name)

    def __eq__(self, other):
        if self.user_name == other.user_name:
            return True
        else:
            return False


clients = set()

fish1 = Client(user_name="catfish")
clients.add(fish1)
fish2 = Client(user_name="catfish")
clients.add(fish2)
print(clients)
print(fish1 == fish2)


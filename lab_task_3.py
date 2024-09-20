# model base refliex agent
class agent:
    def __init__(self):
        self.heater_state=False
        self.rooms={}
    def sense(self,room,temperature):
        self.rooms[room]=temperature
    def act(self):
        for room ,temperature in self.rooms.items():
            if temperature<22 and not self.heater_state:
                print("turning heater on in room:",room)
                self.heater_state=True
            elif temperature>22 and self.heater_state:
                print("turning heater off in room:",room)
                self.heater_state=False
    def run(self):
        while True:
            self.sense("living room: ",20)
            self.sense("bedroom: ",18)
            self.act()
agent1=agent()
agent1.run()

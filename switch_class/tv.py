# TV Class
class Tv:
    def __init__(self):
        self.power = False
        self.muted = False
        self.current_volume = 5
        self.min_volume = 0
        self.max_volume = 10
        self.current_channel = 5
        self.channel_list = [1,2,3,4,5,6,7,8,9,10]
        
    # define some methods
    def power_on(self):
        self.power = True
        
    def power_off(self):
        self.power = False
    
    def mute(self):
        self.muted = not self.muted
        
    def increase_volume(self):
        if self.current_volume > self.min_volume:
            self.current_volume += 1
    
    def reduce_volume(self):
        if self.current_volume < self.max_volume:
            self.current_volume -= 1
            
    def change_channel(self, new_channel):
        if new_channel in self.channel_list:
            self.current_channel = new_channel
        else:
            print("Please Select a valid channel from: ", self.channel_list)
    
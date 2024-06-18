class DimmerSwitch:
    def __init__(self):
        self.switch_is_on = False
        self.brightness = 0
        
    def turn_on(self):
        self.switch_is_on = True
        
    def turn_off(self):
        self.switch_is_on = False
        
    def increase_brightness(self):
        if self.brightness < 10:
            self.brightness += 1
    def reduce_brightness(self):
        if self.brightness > 0:
            self.brightness  -= 1
            
    def show_status(self):
        print("Is the switch on?: ", self.switch_is_on)
        print("what is the brightness of the switch?: ", self.brightness)
                

# create an object of this class
dimmer = DimmerSwitch()
# let's switch it on and increase the brightness 3 times
dimmer.turn_on()
dimmer.increase_brightness()
dimmer.increase_brightness()
dimmer.increase_brightness()
dimmer.show_status()
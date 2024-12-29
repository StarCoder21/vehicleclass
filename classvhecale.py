class vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
modelx=vehicle(240,18)

print("model max speed is ",modelx.max_speed)
print("models mileage is ",modelx.mileage)
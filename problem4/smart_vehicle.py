# Base Class
class Vehicle:
    def start(self):
        print("Vehicle started.")

    def stop(self):
        print("Vehicle stopped.")

# Subclass
class Car(Vehicle):
    def play_music(self):
        print("Playing music...")

# Electric Mixin
class ElectricMixin:
    def start(self):
        print("Performing battery check...")
        super().start()

# Autopilot Mixin
class AutopilotMixin:
    def start(self):
        print("Running sensor calibration...")
        super().start()

# Tesla using Multiple Inheritance
class Tesla(AutopilotMixin, ElectricMixin, Car):
    pass


# --------- TESTING THE SYSTEM ----------
my_car = Tesla()

print("\n--- Starting Tesla ---")
my_car.start()

print("\n--- Using Features ---")
my_car.play_music()

print("\n--- Stopping Tesla ---")
my_car.stop()

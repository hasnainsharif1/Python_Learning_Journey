class animal:
    def speak(self):
        print(f"Animals make sounds")
    
class dog(animal):
    def bark(self):
        print(f"Dog Bark!")
    
dog01 = dog()
dog01.speak()
dog01.bark()
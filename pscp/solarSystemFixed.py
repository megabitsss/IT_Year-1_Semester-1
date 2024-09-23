"""Solar System"""
def main(orbit):
    """Finding the hottest and coolest planets"""
    orbit = " " + orbit + " "
    sun_index = orbit.find(" Sun ") + 1 #Starts at 'S'
main(input())

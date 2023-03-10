car_status = ""

while car_status != "quit":
    car_status_previous = car_status[:]
    car_status = input("> ").lower()

    if car_status == "start":
        if car_status == car_status_previous:
            print("Car already started!")
        else:
            print("Car started... Ready to go!")
    elif car_status == "stop":
        if car_status == car_status_previous:
            print("Car already stopped!")
        else:
            print("Car stopped.")
    elif car_status == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit""")
    elif car_status == "quit":
        break
    else:
        print("Sorry, I don't understand that!")
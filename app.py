car_status = ""

while car_status != "quit":
    car_status = input("> ").lower()
    if car_status == "start":
        print("Car started... Ready to go!")
    elif car_status == "stop":
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
def on_forever():
    if Kitronik_Move_Motor.read_sensor(Kitronik_Move_Motor.LfSensor.LEFT) < 80:
        Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.LEFT, 25)
    elif Kitronik_Move_Motor.read_sensor(Kitronik_Move_Motor.LfSensor.RIGHT) < 80:
        Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.RIGHT, 25)
    else:
        Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.FORWARD, 20)
basic.forever(on_forever)

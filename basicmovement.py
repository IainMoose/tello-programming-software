from djitellopy import Tello

tello = Tello()

tello.connect()
tello.takeoff()

tello.move_left(100)
tello.rotate_counter_clockwise(90)

tello.rotate.counter_clockwise(180)
tello.move_forward(100)

tello.rotate_clockwise(90)
tello.rotate_clockwise(30)
tello.rotate_clockwise(90)

tello.move_backward(100)
tello.rotate_clockwise(90)

tello.move_right(10)

tello.flip_forward()

tello.land_()
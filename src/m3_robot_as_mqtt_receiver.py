"""
Using a Brickman (robot) as the receiver of messages.
"""

# Same as m2_fake_robot_as_mqtt_sender,
# but have the robot really do the action.
# Implement just FORWARD at speeds X and Y is enough.

import mqtt_remote_method_calls as com
import time
import math
import ev3dev.ev3 as ev3


class Motor(object):
    WheelCircumference = 1.3 * math.pi

    def __init__(self, port, motor_type='wheel'):
        # port must be 'A', 'B', 'C', or 'D'.  Use 'arm' as motor_type for Arm.
        if motor_type == 'wheel':
            self._motor = ev3.LargeMotor('out' + port)
        else:
            self._motor = ev3.MediumMotor('out' + port)

    def turn_on(self, speed):  # speed must be -100 to 100
        self._motor.run_direct(duty_cycle_sp=speed)

    def turn_off(self):
        self._motor.stop(stop_action="brake")

    def get_position(self):  # Units are degrees (that the motor has rotated).
        return self._motor.position

    def reset_position(self):
        self._motor.position = 0


class DriveSystem(object):
    """
    Controls the robot's motion via GO and STOP methods,
        along with various methods that GO/STOP under control of a sensor.
    """

    def __init__(self):
        """
        What comes in:  Two (optional) sensors.
        What goes out:  Nothing, i.e., None.
        Side effects:
          -- Stores the (optional) sensors.
          -- Constructs two Motors (for the left and right wheels).
        Type hints:
          :type color_sensor:              ColorSensor
          :type infrared_proximity_sensor: InfraredProximitySensor
        """
        self.left_motor = Motor('B')
        self.right_motor = Motor('C')

    def go(self, left_wheel_speed, right_wheel_speed):
        self.left_motor.turn_on(left_wheel_speed)
        self.right_motor.turn_on(right_wheel_speed)


class DelegateThatReceives(object):

    def forward(self, left_speed, right_speed):
        print("Message received!", "forward_button", left_speed, right_speed)
        drive_system = DriveSystem()
        drive_system.go(left_speed, right_speed)


def main():

    name1 = input("Enter one name (subscriber): ")
    name2 = input("Enter another name (publisher): ")

    my_delegate = DelegateThatReceives()  # This is creating a new object
    mqtt_client = com.MqttClient(my_delegate)  # This assigns mqtt_client to the object MqttClient(my_delegate) defined
    # in the com file
    mqtt_client.connect(name1, name2)
    time.sleep(1)  # Time to allow the MQTT setup.
    print()

    while True:
        time.sleep(0.01)  # Time to allow message processing


main()

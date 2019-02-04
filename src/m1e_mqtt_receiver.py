""" A simple example of using MQTT for RECEIVING messages. """

import mqtt_remote_method_calls as com
import time


class DelegateThatReceives(object):

    def say_it(self, message):
        print("Message received!", message)


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

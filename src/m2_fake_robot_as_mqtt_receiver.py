# DONE: Copy the code in
#     m1e_mqtt_receiver.py
# as your starting point, pasting its code here.

# Then modify the code so that it receives messages from your
#    m2_tkinter_as_mqtt_sender.py
# module and PRINTS them.
import mqtt_remote_method_calls as com
import time


class DelegateThatReceives(object):

    def forward(self, left_speed, right_speed):
        print("Message received!", "forward_button", left_speed, right_speed)


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

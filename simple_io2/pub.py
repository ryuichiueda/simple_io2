import rclpy, random
from rclpy.node import Node
from std_msgs.msg import Float64

class Talker(Node):
    def __init__(self):
        super().__init__("pub")
        self.pub = self.create_publisher(Float64, "uniform_rand", 10)
        self.create_timer(1, self.cb)


    def cb(self):
        msg = Float64()
        msg.data = random.uniform(0.0, 1.0)
        self.pub.publish(msg)


def main():
    rclpy.init()
    talker = Talker()
    rclpy.spin(talker)

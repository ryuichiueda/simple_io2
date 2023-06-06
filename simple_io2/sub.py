import rclpy, random
from rclpy.node import Node
from std_msgs.msg import Float64

class Listener(Node):
    def __init__(self):
        super().__init__("sub")
        self.pub = self.create_subscription(Float64, "uniform_rand", self.cb, 10)


    def cb(self, msg):
        self.get_logger().info("Listen: %f" % msg.data)


def main():
    rclpy.init()
    listener = Listener()
    rclpy.spin(listener)

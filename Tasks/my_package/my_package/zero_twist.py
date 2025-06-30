import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist

class ZeroTwist(Node):
    def __init__(self):
        super().__init__('zero_twist')

        # Create publisher
        self.twist_pub = self.create_publisher(Twist, 'twist', 10)

        # Create subscriber
        self.sub = self.create_subscription(String, 'is_stopped', self.is_stopped_callback, 10)

    def is_stopped_callback(self, msg):
        if msg.data.strip().lower() == 'true':
            zero_twist = Twist()  # All fields default to 0.0
            self.twist_pub.publish(zero_twist)
            self.get_logger().info("Published zero Twist message.")
        else:
            self.get_logger().info("Received 'false'; no message published.")

def main(args=None):
    rclpy.init(args=args)
    node = ZeroTwist()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

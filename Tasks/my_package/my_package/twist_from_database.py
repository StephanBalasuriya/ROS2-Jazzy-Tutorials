import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import csv
import os

class TwistFromDatabase(Node):
    def __init__(self):
        super().__init__('twist_from_database')

        # Publisher setup
        self.publisher_ = self.create_publisher(Twist, 'twist_from_database', 20)

        # File reading
        csv_path = '/home/stephan/ros2_ws/src/my_package/my_package/values.csv'  
        if not os.path.isfile(csv_path):
            self.get_logger().error(f"File not found: {csv_path}")
            return

        with open(csv_path, 'r') as file:
            reader = csv.reader(file)
            self.twist_values = [row for row in reader if len(row) == 6]

        if not self.twist_values:
            self.get_logger().warn("No valid data found in CSV.")
            return

        self.index = 0
        self.timer = self.create_timer(0.1, self.publish_twist)  # 10 Hz

    def publish_twist(self):
        if self.index >= len(self.twist_values):
            self.get_logger().info("Finished publishing all twist values.")
            self.destroy_timer(self.timer)
            return

        data = [float(value.strip()) for value in self.twist_values[self.index]]

        msg = Twist()
        msg.linear.x = data[0]
        msg.linear.y = data[1]
        msg.linear.z = data[2]
        msg.angular.x = data[3]
        msg.angular.y = data[4]
        msg.angular.z = data[5]

        self.publisher_.publish(msg)
        self.get_logger().info(f"Published Twist: {msg}")
        self.index += 1


def main(args=None):
    rclpy.init(args=args)
    node = TwistFromDatabase()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

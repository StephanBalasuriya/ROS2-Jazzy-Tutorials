import rclpy
from rclpy.node import Node

class ParamReader(Node):
    def __init__(self):
        super().__init__('param_reader')

        # Declare the parameter (in case it's not set externally)
        self.declare_parameter('robot_name', 'default_bot')

        # Get the parameter value
        robot_name = self.get_parameter('robot_name').get_parameter_value().string_value

        # Print to terminal
        self.get_logger().info(f"Robot name: {robot_name}")

def main(args=None):
    rclpy.init(args=args)
    node = ParamReader()
    rclpy.spin_once(node)  # Only need one spin to read and print
    node.destroy_node()
    rclpy.shutdown()

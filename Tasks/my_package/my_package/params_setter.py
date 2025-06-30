import rclpy
from rclpy.node import Node

class ParamSetter(Node):
    def __init__(self):
        super().__init__('params_setter')
        param = 'example_param'
        value = 'some_value'
        self.declare_parameter(param, value)
        self.get_logger().info(f"Set parameter: {param} = {value}")

def main(args=None):
    rclpy.init(args=args)
    node = ParamSetter()
    rclpy.spin_once(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
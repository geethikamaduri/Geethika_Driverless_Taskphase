import rclpy
from rclpy.node import Node
from taskone_interfaces.msg import RT2String
from std_msgs.msg import Int32

class PalindromeChecker(Node):
    def __init__(self):
        super().__init__('palindrome_checker')
        self.result_publisher = self.create_publisher(Int32,'palindrome_result',10)
        self.subscription = self.create_subscription(RT2String,'input_string',self.check_palindrome,10)

    def check_palindrome(self, msg):
        text = msg.data
        result = Int32()
        if text == text[::-1]:
            result.data = 1
        else:
            result.data = 0

        self.result_publisher.publish(result)
        self.get_logger().info(f'{text} -> {result.data}')


def main(args=None):
    rclpy.init(args=args)
    node = PalindromeChecker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

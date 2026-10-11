import rclpy
from rclpy.node import Node
from taskone_interfaces.msg import RT2String
from std_msgs.msg import Int32, String


class PalindromeChecker(Node):
    def __init__(self):
        super().__init__('palindrome_checker')

        self.string_subscription = self.create_subscription(
            RT2String,
            '/input_string',
            self.check_palindrome,
            10
        )

        self.result_publisher = self.create_publisher(
            Int32,
            '/palindrome_result',
            10
        )

        self.response_subscription = self.create_subscription(
            String,
            '/palindrome_response',
            self.receive_response,
            10
        )

    def check_palindrome(self, msg):
        text = msg.data
        result = Int32()
        result.data = 1 if text == text[::-1] else 0

        self.get_logger().info(
            f'Input: {text} | Palindrome: {result.data}'
        )
        self.result_publisher.publish(result)

    def receive_response(self, msg):
        self.get_logger().info(f'Response from Node 3: {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    node = PalindromeChecker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

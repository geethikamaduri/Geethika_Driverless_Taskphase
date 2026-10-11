import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String

class ResponseNode(Node):
    def __init__(self):
        super().__init__('response_node')
        self.subscription = self.create_subscription(Int32, 'palindrome_result', self.send_response, 10)
        self.publisher = self.create_publisher(String, 'palindrome_response', 10)

    def send_response(self, msg):
        response = String()

        if msg.data == 1:
            response.data = 'Yes'
        else:
            response.data = 'No'

        self.publisher.publish(response)
        self.get_logger().info(f'Response:{response.data}')

def main(args=None):
    rclpy.init(args=args)
    node = ResponseNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
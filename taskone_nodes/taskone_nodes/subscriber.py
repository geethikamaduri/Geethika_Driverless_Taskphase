import rclpy
from rclpy.node import Node
from taskone_interfaces.msg import TaskOne


class TaskOneSubscriber(Node):
    def __init__(self):
        super().__init__('taskone_subscriber')
        self.subscription = self.create_subscription(
            TaskOne, 'taskone', self.listener_callback, 10
        )

    def listener_callback(self, msg):
        speed = msg.ang_vel * msg.radius
        self.get_logger().info(
            f'Longitudinal speed: {speed} m/s'
        )


def main(args=None):
    rclpy.init(args=args)
    node = TaskOneSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

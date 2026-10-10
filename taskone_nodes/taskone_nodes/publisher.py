import rclpy
from rclpy.node import Node
from taskone_interfaces.msg import TaskOne


class TaskOnePublisher(Node):
    def __init__(self):
        super().__init__('taskone_publisher')

        self.publisher_ = self.create_publisher(
            TaskOne, 'taskone', 10
        )

        self.ang_vel = float(input("Enter angular velocity: "))
        self.radius = float(input("Enter wheel radius: "))

        self.timer = self.create_timer(1.0, self.publish_values)

    def publish_values(self):
        msg = TaskOne()
        msg.ang_vel = self.ang_vel
        msg.radius = self.radius

        self.publisher_.publish(msg)

        self.get_logger().info(
            f'Published ang_vel={msg.ang_vel}, radius={msg.radius}'
        )


def main(args=None):
    rclpy.init(args=args)
    node = TaskOnePublisher()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

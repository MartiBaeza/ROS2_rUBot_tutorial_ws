import rclpy
# import the Node module from ROS2 Python library
from rclpy.node import Node

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('move_turtle')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.subscription = self.create_subscription(Pose,'/turtle1/pose',self.pose_callback,10)
        self.subscription  # prevent unused variable warning
        self.get_logger().info('Init completat')

    def pose_callback(self, msg):
        twist = Twist()
        if msg.x > 7.0 or msg.y > 7.0:
            twist.linear.x = 0.0
            twist.angular.z = 0.0
        else:
            twist.linear.x = 0.2
            twist.angular.z = 0.1
        self.publisher_.publish(twist)


def main(args=None):
    # initialize the ROS communication
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main() #call the main function
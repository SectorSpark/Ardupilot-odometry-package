#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Quaternion
import math

class ExternalOdomPublisher(Node):
    def __init__(self):
        super().__init__('external_odom_pub')
        self.pub = self.create_publisher(Odometry, '/mavros/odometry/out', 10)
        self.timer = self.create_timer(1/30.0, self.timer_callback)  # 30 Hz
        self.t = 0.0

    def timer_callback(self):
        msg = Odometry()

        radius = 2.0
        angular_speed = 0.05  # rad/s
        x = radius * math.cos(angular_speed * self.t)
        y = radius * math.sin(angular_speed * self.t)
        z = 2.0

        vx = radius * angular_speed * math.sin(angular_speed * self.t)
        vy = -radius * angular_speed * math.cos(angular_speed * self.t)

        yaw = math.atan2(vy, vx) + math.pi

        q = Quaternion()
        q.w = math.cos(yaw/2)
        q.x = 0.0
        q.y = 0.0
        q.z = math.sin(yaw/2)

        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "odom"
        msg.child_frame_id = "base_link"

        msg.pose.pose.position.x = x
        msg.pose.pose.position.y = y
        msg.pose.pose.position.z = z
        msg.pose.pose.orientation = q

        msg.pose.covariance = [0.25 if i%7==0 else 0.0 for i in range(36)]
        msg.twist.covariance = [0.25 if i%7==0 else 0.0 for i in range(36)]

        msg.twist.twist.linear.x = vx
        msg.twist.twist.linear.y = vy
        msg.twist.twist.linear.z = 0.0
        msg.twist.twist.angular.z = angular_speed

        self.pub.publish(msg)
        self.t += 1/30.0

def main(args=None):
    rclpy.init(args=args)
    node = ExternalOdomPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


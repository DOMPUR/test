#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import cv2
import numpy as np

class DashboardNode(Node):
    def __init__(self):
        super().__init__('dashboard_node')
        self.create_subscription(Twist, '/cmd_vel', self.vel_callback, 10)
        self.create_subscription(Odometry, '/odom', self.odom_callback, 10)
        
        self.current_vel = 0.0
        self.pos_x = 0.0
        self.pos_y = 0.0
        self.window_name = "FossBot - Dashboard na zywo"
        
        cv2.namedWindow(self.window_name)
        self.timer = self.create_timer(0.1, self.update_dashboard)
        self.get_logger().info("Dashboard uruchomiony.")

    def vel_callback(self, msg):
        self.current_vel = msg.linear.x
        
    def odom_callback(self, msg):
        self.pos_x = msg.pose.pose.position.x
        self.pos_y = msg.pose.pose.position.y
        
    def update_dashboard(self):
        img = np.ones((300, 500, 3), dtype=np.uint8) * 30
        cv2.putText(img, 'DASHBOARD FOSSBOT', (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 255), 2)
        cv2.putText(img, f'Predkosc liniowa: {self.current_vel:.2f} m/s', (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        cv2.putText(img, f'Pozycja X: {self.pos_x:.2f} m', (10, 160), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 100, 100), 2)
        cv2.putText(img, f'Pozycja Y: {self.pos_y:.2f} m', (10, 220), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 100, 100), 2)
        
        cv2.imshow(self.window_name, img)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    node = DashboardNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        cv2.destroyAllWindows()
        cv2.waitKey(1)  # Wymuszenie fizycznego zamknięcia okna
        rclpy.shutdown()

if __name__ == '__main__':
    main()

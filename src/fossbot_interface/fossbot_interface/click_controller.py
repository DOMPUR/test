#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import cv2
import numpy as np

class ClickController(Node):
    def __init__(self):
        super().__init__('click_controller')
        self.declare_parameter('linear_speed', 0.5)
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.window_name = "FossBot - Panel Sterowania"
        self.image_height = 480
        self.image_width = 640
        self.display_image = np.ones((self.image_height, self.image_width, 3), dtype=np.uint8) * 40
        
        cv2.line(self.display_image, (0, self.image_height // 2), (self.image_width, self.image_height // 2), (0, 255, 0), 2)
        cv2.putText(self.display_image, 'KLIKNIJ TUTAJ: PRZOD', (150, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(self.display_image, 'KLIKNIJ TUTAJ: TYL', (150, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        cv2.namedWindow(self.window_name)
        cv2.setMouseCallback(self.window_name, self.mouse_callback)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.get_logger().info("Wezel sterowania uruchomiony.")

    def timer_callback(self):
        cv2.imshow(self.window_name, self.display_image)
        cv2.waitKey(1)

    def mouse_callback(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            twist = Twist()
            speed = self.get_parameter('linear_speed').value
            
            if y < (self.image_height / 2):
                self.get_logger().info("Kliknieto GORE -> PRZOD")
                twist.linear.x = speed   
            else:
                self.get_logger().info("Kliknieto DOL -> TYL")
                twist.linear.x = -speed  
                
            self.publisher_.publish(twist)
            feedback_img = self.display_image.copy()
            cv2.circle(feedback_img, (x, y), 20, (0, 0, 255), -1)
            cv2.imshow(self.window_name, feedback_img)
            cv2.waitKey(100)

def main(args=None):
    rclpy.init(args=args)
    node = ClickController()
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

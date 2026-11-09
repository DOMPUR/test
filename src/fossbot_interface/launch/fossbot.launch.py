import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import launch_ros.actions

def generate_launch_description():
    # Pobranie ścieżki do paczki z symulacją FossBota
    fossbot_sim_dir = get_package_share_directory('fossbot_educational_description')
    
    # Zdefiniowanie akcji uruchomienia zewnętrznego pliku launch
    fossbot_sim_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(fossbot_sim_dir, 'launch', 'single.launch.py')
        )
    )

    return LaunchDescription([
        # 1. Uruchomienie symulacji FossBota
        fossbot_sim_launch,

        # 2. Węzeł klikania (Twój interfejs)
        launch_ros.actions.Node(
            package='fossbot_interface',
            executable='click_controller',
            name='click_controller',
            parameters=[
                {'linear_speed': 0.8}
            ]
        ),
        
        # 3. Węzeł dashboardu (Twój podgląd)
        launch_ros.actions.Node(
            package='fossbot_interface',
            executable='dashboard_node',
            name='dashboard_node'
        )
    ])

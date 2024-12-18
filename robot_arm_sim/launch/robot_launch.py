from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    robot_arm_sim_dir = get_package_share_directory('robot_arm_sim')  # Nome del pacchetto
    urdf_file = os.path.join(robot_arm_sim_dir, 'urdf', 'prova1.urdf')


    return LaunchDescription([
        # Avvia Gazebo
        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so'],
            output='screen'
        ),
       
           # Launch the robot
        Node(
            package='gazebo_ros', 
            executable='spawn_entity.py',

            arguments=[
                '-entity', 'test_robot',
                '-file', urdf_file,
                ],
            output='screen'
        )
    
    
    
    ])



from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim_plus',
            namespace='',
            executable='turtlesim_plus_node.py',
            name='turtlesim_plus'
        ),
        Node(
            package='lab3',
            namespace='',
            executable='killer.py',
            name='killer'
        ),
        Node(

            package='lab3',
            namespace='',
            executable='eater.py',
            name='eater'
        )
    ])
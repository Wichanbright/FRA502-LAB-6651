from launch import LaunchDescription
from launch_ros.actions import Node
name_eater='black_cat'
name_killer='balck_revo'
def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim_plus',
            namespace='',
            executable='turtlesim_plus_node.py'
        ),
        Node(
            package='lab3',
            namespace=name_killer,
            executable='killer.py',
            parameters=[{'rate':10.0,'namet':name_eater}]
        ),
        Node(

            package='lab3',
            namespace=name_eater,
            executable='eater.py',
            parameters=[{'rate':10.0}]
        )
    ])
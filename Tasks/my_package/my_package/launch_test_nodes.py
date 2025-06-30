from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import TimerAction
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        # Node: chatter.py
        Node(
            package='tests',
            executable='chatter.py',
            name='test_chatter',
            output='screen',
            remappings=[
                ('/chatter', '/test/chatter')
            ]
        ),

        # Node: listener.py
        Node(
            package='tests',
            executable='listener.py',
            name='listener',
            output='screen'
        ),

        # One-time publisher to /twist topic using ros2 CLI
        TimerAction(
            period=2.0,  # delay to make sure system is ready
            actions=[
                ExecuteProcess(
                    cmd=[
                        'ros2', 'topic', 'pub', '-1',  # publish once
                        '/twist',
                        'geometry_msgs/Twist',
                        "{linear: {x: 0.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}"
                    ],
                    output='screen'
                )
            ]
        )
    ])

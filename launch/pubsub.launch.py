import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():
    pub = launch_ros.actions.Node(
             package='simple_io2',
             executable='pub', )
    sub = launch_ros.actions.Node(
            package='simple_io2',
            executable='sub',
            output='screen', )

    return launch.LaunchDescription([pub, sub])

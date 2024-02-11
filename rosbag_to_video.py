import argparse
import cv2
from ros import rosbag
from sensor_msgs.msg import Image
from cv_bridge import CvBridge


def extract_video(bag_path, topic_name, video_path, first_image_path, width, height):
    print('Opening bag')
    bag = rosbag.Bag(bag_path)

    # OpenCV bridge to convert ROS Image messages to OpenCV images
    bridge = CvBridge()

    # Video writer setup
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(video_path, fourcc, 20.0, (width, height))  # Adjust the resolution if needed

    print('Reading video frames and saving to video file')
    frame_count = 0

    first_image_saved = False

    for topic, msg, stamp in bag.read_messages(topics=[topic_name]):
        if msg._type == 'sensor_msgs/Image':
            frame_count += 1
            # Convert ROS Image message to OpenCV image
            cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

            # Save the first image separately
            if not first_image_saved:
                cv2.imwrite(first_image_path, cv_image)
                first_image_saved = True

            # Write the frame to the video file
            video_writer.write(cv_image)

    bag.close()
    video_writer.release()
    print('Done. %d video frames written to %s' % (frame_count, video_path))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert ROS video bag file to video file')
    parser.add_argument('-source', dest='bag_path', required=True, help='ROS bag file path')
    parser.add_argument('-topic', dest='topic_name', required=True, help='Video topic name')
    parser.add_argument('-output', dest='video_path', required=True, help='Output video file path')
    parser.add_argument('-first_image', dest='first_image_path', help='Path to save the first image')
    parser.add_argument('-width', dest='width', type=int, default=960, help='Width of the video frames (default: 960)')
    parser.add_argument('-height', dest='height', type=int, default=600, help='Height of the video frames (default: 600)')

    args = parser.parse_args()

    extract_video(args.bag_path, args.topic_name, args.video_path, args.first_image_path, args.width, args.height)
# ROS Bag to Video Converter

Converts video data from ROS bag files containing sensor_msgs/Image messages to a video file.

## Overview

This Python script extracts video frames from ROS bag files, specifically from messages of type `sensor_msgs/Image`, and compiles them into a video file. The script is designed to be a helpful tool for working with ROS bag files containing video data.

## Features

- Extracts video frames from specified ROS bag file and topic.
- Compiles the video frames into an MP4 video file.
- Saves the first image as an optional separate file for debugging purposes.
- Adjustable video frame dimensions.

## Requirements

- Python 3
- ROS (Robot Operating System)
- `rosbag` Python package
- `opencv-python` Python package

## Usage

```bash
python your_script_name.py -source <bag_file_path> -topic <video_topic_name> -output <output_video_file_path> [-first_image <first_image_file_path>] [-width <video_frame_width>] [-height <video_frame_height>]
```

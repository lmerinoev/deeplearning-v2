from datetime import timedelta
import cv2
import numpy as np
import os

SAVING_FRAMES_PER_SECOND = 1

# Format time delta
# 00:00:20:05
def format_timedelta(td):
    result = str(td)
    try:
        result, ms = result.split(".")
    except ValueError:
        return result + ".00".replace(":", "-")
    ms = int(ms)
    ms = round(ms / 1e4)
    return f"{result}.{ms:02}".replace(":", "-")

# Return list of durations where to save the frames
def saving_frames (cap, saving_fps):
    save = []
    # clip duration by dividing # of frames by # of frames per second
    clip_duration = cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS)

    # np.arrage() to make floating-point steps
    for i in np.arange(0, clip_duration, 1 / saving_fps):
        save.append(i)
    return save

 # Main 
def main(video_file):
    filename, _ = os.path.splitext(video_file)
    filename += "-opencv"

    # make a folder with the name of the video file
    # this is where images will be saved
    if not os.path.isdir(filename):
        os.mkdir(filename)
    # read the video filename
    cap = cv2.VideoCapture(video_file)
    # get FPS of video
    fps = cap.get(cv2.CAP_PROP_FPS)
    saving_frames_per_second = min(fps, SAVING_FRAMES_PER_SECOND)

    # get list of duration spots to save
    saving_frames_durations = saving_frames(cap, saving_frames_per_second)

    # start loop
    count = 0 
    myCount = 1
    while True:
        is_read, frame = cap.read()
        if not is_read:
	    #break with no frames to read
            break
        frame_duration = count / fps
        try:
	    # get the earliest duration to save
            closest_duration = saving_frames_durations[0]
        except IndexError:
	    # the list is empty, all duration frames were saved
            break
        if frame_duration >= closest_duration:
	    # save frame
            frame_duration_formatted = format_timedelta(timedelta(seconds=frame_duration))
            cv2.imwrite(os.path.join(filename, f"frame_{myCount}.jpg"), frame)
            myCount = myCount + 1
            print("My count is: " + str(myCount)) 
	    # drop the duration spot from the list
            try:
                saving_frames_durations.pop(0)
            except IndexError:
                pass
	#increment the frame count
        count += 1

if __name__ == "__main__":
    import sys
    video_file = sys.argv[1]
    main(video_file)

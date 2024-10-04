import cv2
import os

def Getframe(path):

    #setup
    video = cv2.VideoCapture(path)
    f_cnt = 0
    out_cnt = 1
    success = 1

    #get video fps
    fps = video.get(cv2.CAP_PROP_FPS)

    #check if input invaid
    while(True):
        GoalFPS = int(input(f"Goal FPS (Max:{fps}):"))
        if GoalFPS <= fps and GoalFPS > 0:
            break

    goal_fps = int(fps / GoalFPS)

    #make folder
    folder_name = f"{path}_frameOutput"

    while True:
        if os.path.exists(folder_name):
            folder_name = f"{folder_name}_1"
        else:
            break

    os.makedirs(folder_name)

    #output img
    while True:
        success, image = video.read()

        if success:
            if f_cnt % goal_fps ==0:
                output_path = f"{folder_name}/{path}_{out_cnt:08d}.png"
                cv2.imwrite(output_path, image)
                out_cnt += 1
        else:
            break

        f_cnt += 1

    print(f"DONE: {out_cnt} FILES HAS BEEN OUTPUT TO PATH: '{folder_name}/'")       
    input("Press Enter to continue...")

if __name__ == "__main__":
    fileName = input("Video Filename:")
    Getframe(fileName)

# Video read and write


import cv2

def read_write_video():
    # Requirement: ffmpeg package
    cap = cv2.VideoCapture(0)
    out = cv2.VideoWriter('Resources/output.mp4',
                          cv2.VideoWriter_fourcc('m','p','4','v'), # important
                          30.0,
                          (int(cap.get(3)),int(cap.get(4))))

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            gray = cv2.cvtColor(src=frame, code=1)

            out.write(gray)

            cv2.imshow('frame', gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    read_video()
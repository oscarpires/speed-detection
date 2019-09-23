import dlib
import cv2


def track_cars(frame_object):
    trackers = []
    labels = []
    counter = 0

    for (_x, _y, _w, _h) in frame_object.cars:
        x = int(_x)
        y = int(_y)
        w = int(_w)
        h = int(_h)

        tracker = dlib.correlation_tracker()

        rect = dlib.rectangle(x, y, x + w, y + h)
        tracker.start_track(frame_object.image_processed, rect)

        trackers.append(tracker)
        labels.append(counter)

        counter = counter + 1
        print("New tracked car")

    for t in trackers:
        l = labels.pop(0)

        pos = t.get_position()
        startX = int(pos.left())
        startY = int(pos.top())
        endX = int(pos.right())
        endY = int(pos.bottom())
        cv2.rectangle(frame_object.image, (startX, startY), (endX, endY), (0, 255, 0), 2)
        cv2.putText(frame_object.image, 'id: ' + str(l), (startX, startY - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.45,
                    (0, 255, 0), 2)

    return trackers
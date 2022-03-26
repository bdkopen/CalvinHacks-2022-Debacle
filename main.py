# CalvinHacks 2022 - Implemented by Braden Kopenkoskey
# Credit to the face_recognition library and examples
# https://github.com/ageitgey/face_recognition

import face_recognition
import cv2
import numpy as np
from turret import Turret
import argparse

parser = argparse.ArgumentParser(description='Display Visualization')
parser.add_argument('visualize', metavar='V', type=int, nargs='+',
                    help='a boolean integer for data visualization')
args = parser.parse_args()

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
braden_image = face_recognition.load_image_file("bdkopen.png")
braden_face_encoding = face_recognition.face_encodings(braden_image)[0]

daveeid_image = face_recognition.load_image_file("daveeeid2.jpg")
daveeid_face_encoding = face_recognition.face_encodings(daveeid_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    braden_face_encoding,
    daveeid_face_encoding,
]
known_face_names = [
    "Braden Kopenkoskey",
    "Daveeid"
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

myTurret = Turret()

while True:

    ####################################
    # Camera Imaging
    ####################################

    # Grab a single frame of video
    ret, frame = video_capture.read()

    scale_size = 1

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=1/scale_size, fy=1/scale_size)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Target"

            #     # # If a match was found in known_face_encodings, just use the first one.
            #     # if True in matches:
            #     #     first_match_index = matches.index(True)
            #     #     name = known_face_names[first_match_index]

            # # Or instead, use the known face with the smallest distance to the new face
            # face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)

            # best_match_index = np.argmin(face_distances)
            # if matches[best_match_index]:
            #     name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    # Display the results
    # for (top, right, bottom, left), name in zip(face_locations, face_names):
    #     # Scale back up face locations since the frame we detected in was scaled to 1/4 size
    #     top *= scale_size
    #     right *= scale_size
    #     bottom *= scale_size
    #     left *= scale_size

    #     # Draw a box around the face
    #     cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    #     # Draw a label with a name below the face
    #     cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
    #     font = cv2.FONT_HERSHEY_DUPLEX
    #     cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    # cv2.imshow('Video', frame)

    #Only visualize if parameter is 1
    if(args.visualize[0] == 1):
        #Show downscaled
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            # top *= scale_size
            # right *= scale_size
            # bottom *= scale_size
            # left *= scale_size

            # Draw a box around the face
            cv2.rectangle(small_frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            # cv2.rectangle(small_frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)

            box_width = right - left
            box_height = bottom - top
            line_length = 7
            line_thickness = 3
            cv2.rectangle(small_frame, (left - line_length, bottom - round(box_height/2) - line_thickness), (left + line_length, bottom - round(box_height/2) + line_thickness), (0, 0, 255), cv2.FILLED)
            cv2.rectangle(small_frame, (right - line_length, bottom - round(box_height/2) - line_thickness), (right + line_length, bottom - round(box_height/2) + line_thickness), (0, 0, 255), cv2.FILLED)
            cv2.rectangle(small_frame, (left + round(box_width/2) - line_thickness, top + line_length), (left + round(box_width/2) + line_thickness, top - line_length), (0, 0, 255), cv2.FILLED)
            cv2.rectangle(small_frame, (left + round(box_width/2) - line_thickness, bottom + line_length), (left + round(box_width/2) + line_thickness, bottom - line_length), (0, 0, 255), cv2.FILLED)
            # font = cv2.FONT_HERSHEY_DUPLEX
            # cv2.putText(small_frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('Video', small_frame)

    if(len(face_locations)):
        print(face_locations)

    # If face location say it is centered
    if(not len(face_locations)):
        face_locations = [(-1, -1, -1, -1)]
        #face_locations = -1

    #This is on a 160 x 120 
    face_locations_obj_top = face_locations[0][0]
    face_locations_obj_right = face_locations[0][1]
    face_locations_obj_bottom = face_locations[0][2]
    face_locations_obj_left = face_locations[0][3]

    face_locations_obj_face_width = face_locations[0][1] - face_locations[0][3]
    face_locations_obj_face_height = face_locations[0][0] - face_locations[0][2]

    print(face_locations_obj_left)

    face_locations_obj_face_center_x = face_locations_obj_left + face_locations_obj_face_width/2
    face_locations_obj_face_center_y = face_locations_obj_top + face_locations_obj_face_height/2

    ####################################
    # Motor Logic
    ####################################

    #How many pixels of tolerance we want to give as error
    tolerance = 5


    dx = 0
    dy = 0
    if(face_locations[0][0] != -1):
        # Check horizontal position
        if(face_locations_obj_face_center_x > (640/scale_size)/2 - tolerance and face_locations_obj_face_center_x < (640/scale_size)/2 + tolerance):
            print("Basically centered horizontally!")
        elif(face_locations_obj_face_center_x > (640/scale_size)/2):
            print("Move to the right")
            dx = 10
        elif(face_locations_obj_face_center_x < (640/scale_size)/2):
            print("Move to the left")
            dx = -10
        else:
            print("This line should never be reached")

        # Check vertical position
        if(face_locations_obj_face_center_y > (480/scale_size)/2 - tolerance and face_locations_obj_face_center_y < (480/scale_size)/2 + tolerance):
            print("Basically centered vertically!")
        elif(face_locations_obj_face_center_y > (480/scale_size)/2):
            print("Move down")
            dy = -10
        elif(face_locations_obj_face_center_y < (480/scale_size)/2):
            print("Move up")
            dy = 10
        else:
            print("This line should never be reached")
    
    myTurret.adjust(dx, dy)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
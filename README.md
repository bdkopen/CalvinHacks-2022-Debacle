# Team Debacle's Automatic Targeting Nerf Blaster

## Inspiration
Nerf blasters are really cool and would be even cooler if automated!

## What it does
Automatically targets and fires a Nerf blaster using facial recognition.

## How we built it
We built it using a Raspberry PI with the help of facial recognition libraries. We are using stepper motors driven by a power supply to change the position and angle of the Nerf Blaster and another stepper motor with a cam to pull the trigger. We also 3D printed parts to mount the Nerf Blaster to a robotic arm that was driven by gear boxes.

## Challenges we ran into
We had difficulties connecting the Raspberry PI to the school internet. The default network manager does not allow for complex network certificates so we had to install a more advanced network manager. We also encountered an issue where all of our stepper motor drives were shorted and broke, leaving us unable to run our motors for a large duration of the project.

## Accomplishments that we're proud of
We're proud of the custom 3D printed parts we designed that held the Nerf Blaster tightly. We also are proud of the facial recognition software being able to identify faces.

## What we learned
When doing electrical circuits, the process should be taken slow and precautions should be made to stop mistakes. In our case, we decide to put all 3 stepper motor drivers in at once rather then testing them one at time. Because of this, we had to learn of our mistake by losing 3 stepper motor drivers instead of just one.

We also learned that SD cards can have slow write speeds. This led to issues where we accidentally corrupted the SD cards leading to increased delays. We learned how to better work with SD cards in Raspberry Pis to avoid this type of issue in the future.

## What's next for Debacle
Refine the facial recognition so that it is more accurate. Additionally, it would be cool to have the turret only target certain people or exclude certain people, therefore differentiating between targets.

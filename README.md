# Team Debacle's Automatic Targeting Nerf Blaster

## Inspiration
Nerf blasters are cool, but they'd be even cooler if automated!

## What it does
Our project can automatically locate someone with facial recognition, target them with our turret, and fire a Nerf blaster at them.

## How we built it
Our hardware is driven by a Raspberry Pi. We are using stepper motors driven by a power supply to change the position and angle of the Nerf Blaster and another stepper motor with a cam to pull the trigger. We also used a 3D printer to create parts to mount the Nerf Blaster to a robotic arm that was driven by gear boxes.
Our software consists of several pieces of Python code. We used a [facial recognition library](https://github.com/ageitgey/face_recognition) to target a person's face, and used a convenient [input library](https://github.com/zeth/inputs) which gave us the ability to control the blaster turret using an Xbox controller. Our mechanical systems were also controlled by Python code.

## Challenges we ran into
We had difficulties connecting Raspbian, the stock Raspberry Pi operating system, to Calvin's eduroam network. The default network manager does not allow for complex network certificates so we had to install a more advanced network manager which automated some of the steps involved. An additional issue arose when our stepper motor controllers shorted out, causing an unfortunately long span of time during which we could not work on the mechanical aspects of our turret.

## Accomplishments that we're proud of
We're definitely very proud of the custom 3D printed parts we designed that held the Nerf Blaster tightly. We're also proud of how we were able to integrate facial recognition with a webcam into our design.

## What we learned
In order to prevent mistakes when dealing with circuitry, the process should be slow and filled with plenty of precaution. In our case, we decided to put all 3 stepper motor controllers in at once rather then testing them one at time. As a result, all three of these controllers shorted out, rather than potentially just one that would have been lost had we tested one at a time.

We also learned that we should be careful to take account of all potential bottlenecking factors. One particularly annoying one in our case was the write speed of the SD cards in our Raspberry Pis. Due to their relatively low write speeds, we encountered several delays as we waited for disk images to be written to the cards. Additionally, in our haste, the data on the cards was corrupted multiple times, which only increased delays. Because of these experiences, we've learned how to work more efficiently and carefully with this sort of potential bottleneck in order to avoid these issues in the future.

## What's next for Debacle
We'd like to refine the facial recognition so that it is more accurate. Additionally, it would be cool to have the turret only target certain people or exclude certain people, thereby differentiating between targets.

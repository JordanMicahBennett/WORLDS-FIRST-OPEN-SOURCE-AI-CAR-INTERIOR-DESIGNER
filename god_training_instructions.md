Notes by God Bennett

1. Library utilized: Image Generator Generative Adversarial Neural Network library. https://github.com/shivamswarnkar/Image-Generator

2. The library above doesn't mention on their github page training dataroot folder naming convention, but quickly digging starting from their training code, we end up at the source library DCGAN, where comments in the code indicate training data should exist as "real" and "fake" images of interiors crucially in folders named "1" and "0" respectively. 

Without following this convention, training is not possible out of the box.

i. Set python36 path:
path=C:\Users\Jordan\AppData\Local\Programs\Python\Python36

ii. Train (Save a generated image every 5 epochs to intermediately view progress)

ii.a) Download [pre-trained model](https://drive.google.com/drive/folders/1pfjUbH3T-CfFB7Hmkxpm5UJ473QfzjST), and place in directory of the image gen files, where train.py resides. 

ii.b) Download dataset [dataset_image_gen.zip](https://drive.google.com/drive/folders/1pfjUbH3T-CfFB7Hmkxpm5UJ473QfzjST), and unzip to somewhere, then set --dataroot below to that path

ii.c)
COMMAND:
python train.py --save_every 5 --dataroot C:/Users/Jordan/Downloads/God/RobotizeJa/Ai-Car-Interior-Designer/dataset_image_gen --num_epochs 0

iii. Inference/Generation (cmd is ran in admin to avoid permission denied rights to checkpoints):

iii.a) Set your path below

iii.b) 
COMMAND:
python generate.py --netG C:/Users/Jordan/Downloads/God/RobotizeJa/Ai-Car-Interior-Designer/Image-Generator-master/checkpoints/netG.pth --n 64
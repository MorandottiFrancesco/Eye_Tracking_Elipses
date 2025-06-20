# Eye_Tracking_Elipses
Use a novel approach at finding the pupil in eye videos. The general idea is to derive 5 values to be used as outputs for a neural network that shall find the pupil and track both position and size.

Elipses are used to fit the black pulil. the parameters are (X,Y) of the center of the elipse, (Axis_Maj,Axis_Min,Incline) for the geometrical constrains of the elipse. The next step, not yet developed, is to train a DNN to fetch those 5 parameters out of each of the video frames. The deterministic approach followed in this repository, before the AI is used, enhances accuracy by using a frame-to-frame algorithm that will not be used for the AI development itself, since is should then be able to find the pupil in each frame without knowledge of the previous frames.

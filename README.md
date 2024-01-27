# FlyspotConverter

Hello flyers!
For how awesome FlySpot is, their video format sucks. You can use this script to convert .avi to .mp4 using [ffmpeg](https://ffmpeg.org/).

## Prerequisites
- python & pip
- ffmpeg -> `brew install ffmpeg`

## Required changes
- `converter.py` line 29: change to folder, where all of your videos are

## How it works
Download/clone/fork this repo or `converter.py`. Specify the folder, in which you have all the videos. Folder is the same for .avi and .mp4 videos, names of the videos will be the same. Execute the script (`python converter.py`) or by passing parameters (`python converter.py TOP desk centerline`). Script takes the parameters and matches pattern in the video names, e.g. if you'd like to convert only centerline videos, or you'd like to convert only videos from certain time. If you won't specify any parameters, centerline and desk videos will be converted - feel free to change it on lines 23 and 24. Script goes through all the .avi files in the folder and converts all of them, that match the specified pattern. Once the conversion is done, all .avis are deleted. If you'd like to retain the files and not delete them, comment out (`#`) the line 9. ffmpeg conversion is done in series, so the conversion can take quite a bit, but when I tried it in parallel (with 50+ videos) , it almost fried my computer. After it finishes the last conversion, console will log number of converted and deleted files.

In case you find any bugs, let me know or fix them in a PR.

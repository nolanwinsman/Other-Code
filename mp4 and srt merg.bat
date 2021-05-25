@echo off
REM grabs the name of the file and saves it in the variable input
set /p input=Paste the file name as STRING with quotes 
REM uses ffmpeg to merge the srt and mp4 file
ffmpeg -i %input%.mp4 -i %input%.srt -c copy -c:s mov_text "output.mp4"
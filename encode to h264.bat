DO (
MKDIR Old_Files
)

FOR /F "tokens=*" %%G IN ('dir /b *.mkv') DO (
	ffmpeg -i "%%G" -vcodec libx264 -acodec aac "h264_%%G"
	move "%%G" "Old_Files"
		)
FOR /F "tokens=*" %%G IN ('dir /b *.mp4') DO (
	ffmpeg -i "%%G" -vcodec libx264 -acodec aac "h264_%%G"
	move "%%G" "Old_Files"
		)


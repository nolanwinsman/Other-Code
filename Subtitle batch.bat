DO (
MKDIR Encoded_Files
)
FOR /F "tokens=*" %%G IN ('dir /b *.mkv') DO (
	ffmpeg -i "%%G" -vn -an -codec:s:0.1 srt "%%G.srt"
	ffmpeg -i "%%G" -vf "subtitles=%%G.srt" "%%GEncoded.mkv"
	move *"%%~nG" "Encoded_Files"
		)



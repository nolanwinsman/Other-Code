@echo off
rem two loops that convert every .webm and m4a file into mp3
FOR /F "tokens=*" %%G IN ('dir /b *.webm') DO ( rem for every .webm file, convert said .webm file to .mp3
	ffmpeg -i "%%G" -acodec mp3 "%%~nG.mp3"
		del *"%%~nG.webm"
	)
FOR /F "tokens=*" %%G IN ('dir /b *.m4a') DO ( /rem for every .m4a file, convert said .m4a file to .mp3
	ffmpeg -i "%%G" -acodec mp3 "%%~nG.mp3"
		del *"%%~nG.m4a"
	)

FOR /F "tokens=*" %%G IN ('dir /b *.mp3') DO ( rem move every .mp3 file into the folder "Converted_Files"
	move *"%%~nG.mp3" "Converted_Files"
	)
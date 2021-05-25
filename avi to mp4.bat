echo
setlocal enabledelayedexpansion
DO (
Print "Make sure there are no other .mp4 files in the directory"
MKDIR Old_Files
)
FOR /F "tokens=*" %%G IN ('dir /b *.avi') DO (
	ffmpeg -i "%%G" -strict -2 "%%G.mp4"
	move "%%G" "Old_Files"
		)

@for /f "delims=" %%i in ('dir /b *.mp4')  do (
    set fname=%%~ni
    set fname=!fname:~0,-4!.mp4
    ren "%%i" "!fname!"
)

endlocal


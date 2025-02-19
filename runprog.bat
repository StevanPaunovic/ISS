@echo off

REM Pfad zur Anaconda-Installation anpassen, falls nötig
set ANACONDA_PATH=C:\Users\steva\miniconda3

REM Erstes Fenster: detectlive.py
start "Anaconda Prompt - YOLO_detect" cmd /k "%ANACONDA_PATH%\Scripts\activate.bat && conda activate mm && python YOLO_detect.py"

REM Wartezeit, um sicherzustellen, dass detectlive.py gestartet wurde
timeout /t 10 /nobreak

REM Zweites Fenster: analyse.py
start "Anaconda Prompt - verhaltenserkennung" cmd /k "%ANACONDA_PATH%\Scripts\activate.bat && conda activate mm && python verhaltenserkennung.py"

REM Drittes Fenster: verhaltenserkennung.py (für gefundene frames)


exit
Das Programm bedient sich eines virtuellen Environments in miniconda3
Desweiteren müssen ultralytics und mmaction2 installiert werden. 
Folgende Links beinhalten Dokumentationen, die eine schnelle Installation ermöglichen.
https://mmaction2.readthedocs.io/en/latest/get_started/overview.html
https://docs.ultralytics.com/de/quickstart/


Das Programm kann mit folgendem Befehl gestartet werden:
runprog.bat

Wenn das Programm gestartet wurde, werden 2 Kommandofenster geöffnet und ein drittes Fenster, mit der Anzeige der Kamera.
Die interne Kamera des Computers wird aktiviert und führt eine Personenerkennung durch.
Wenn eine Person erkannt wurde, speichert das Programm alle Frames, auf denen die Person zu sehen ist.
Wenn 4 sekunden keine Person erkennbar ist wird die analyse der gespeicherten Frames, abzüglich der 4 "leeren" Sekunden, gestartet
Das Ergebnis der Personenerkennung wird in Log.txt gespeichert.
Das Ergebnis der Verhaltenserkennung wird in verhaltenslog.txt gespeichert. 



Die Datei "wortzaehler.py" wurde verwendet, um die Vorkommnisse der Klassen aus den Log-Dateien effizient auszulesen.

Der Ordner "data" beinhaltet alle in der Arbeit analysierten Videos, sowie alle Ergebnisse der Verhaltenserkennung.

# Projekti i tretë në lëndën "Siguria ne Internet" <br><br>
## Zhvillimi i një aplikacioni që mundëson SQL Injection Teste të Automatizuar në një URL të caktuar <br>
**SQL Injection** është një teknikë e injektimit të kodit përmes SQL query duke shtuar të dhëna nga pjesa e përdoruesit në aplikacionin e cenueshëm të uebit. Është një nga teknikat më të zakonshme dhe më të rrezikshme të hakimit në ueb.<br><br>
Një injektim i  suksesshëm i SQL mund të shkaktojë shumë dëme të mëdha në bazën e të dhënave të një aplikacioni në internet.Për shembull, mund të lexojë të dhëna të ndjeshme si fjalëkalimet e përdoruesit nga baza e të dhënave, të shtojë, modifikojë dhe madje të fshijë të dhënat e përdoruesëve të një ueb aplikacioni të caktuar.<br><br>
Qëllimi kryesor i zhvillimit të një aplikacioni të tillë i cili mundëson SQL Injection Teste të Automatizuara në një URL të caktuar është që një perdoruesi të ia 
mundësoj që ta testojë një website se a është i  sigurtë apo jo në lidhje me sulmet SQL Injection. <br>

### Veglat e përdorura:
```
Editori: VisualStudio 2019
Gjuha programuese: Python
Sistemi Operativ: Windows/Linux
```
### Hapat e ekzekutimit:
**Hapi 1:** Klonimi i projektit nga GitHub-i përmes komandës së mëposhtme.
```
git clone https://github.com/Alberiana/IS2022-Gr17
```
**Hapi 2:** Hyrja tek **root directory** i projektit të klonuar.<br>
**Hapi 3:** Importimi i moduleve të mëposhtme të cilat nevojiten për ekzekutimin e aplikacionit.
```
import tkinter
import re
import unittest
import htmltestrunner
import ddt
import data
import unpack
```
Për implementimin e moduleve përdoret komanda vijuese:
```
pip install <module> or pip3 install <module>
```
**Hapi 4:** Ekzekutimi.
Komanda për ekzekutimin e programit:
```
python3 sqlinjectiontester.py
```
<br>
Pamja e programit pas ekzekutimit të **sqlinjectiontester.py**:<br>
https://github.com/Alberiana/IS2022-Gr17/blob/main/Images/1.PNG
<br>
Pamja e programit pas vendosjes së një URL të një website të caktuar dhe testimit të saj:<br>
https://github.com/Alberiana/IS2022-Gr17/blob/main/Images/2.PNG <br>
https://github.com/Alberiana/IS2022-Gr17/blob/main/Images/3.PNG
<br>
<br>
### Testimi:
Për testimin e mëtutjeshem të programit të zhvilluar, ekzekutojmë file **pageTesting.py**.Pas ekzekutimit shfaqet një **Html file** i cili tregon statusin e të gjitha testimeve të cilat janë të pranishme tek file **pages.txt**.<br>
https://github.com/Alberiana/IS2022-Gr17/blob/main/Images/6.PNG
<br>
Në pjesen e terminalit:<br>
https://github.com/Alberiana/IS2022-Gr17/blob/main/Images/4.PNG
<br>
https://github.com/Alberiana/IS2022-Gr17/blob/main/Images/5.PNG
<br>

### Punuan: <br>
Ky applikacion është zhvilluar krahas hulumtimeve të shumëta nga studentët e vitit të tretë në Fakultetin e Inxhinierisë Elektrike dhe Kompjuterike, drejtimi Inxhinieri Kompjuterike në lëndën "Siguria në Internet".
<br><br>
<ul>
   <li>Arlinda Kastrati @arlindakastrati</li>
   <li>Alberiana Tofaj @Alberiana</li>
   <li>Elsa Vitija @elsavitija</li>
   <li>Elona Rashica @Elona-Rashica</li>
</ul>

### Referencat:
https://www.thepythoncode.com/code/sql-injection-vulnerability-detector-in-python <br>
https://github.com/x4nth055/pythoncode-tutorials/tree/master/ethical-hacking/sql-injection-detector <br>
https://cyberpersons.com/2016/11/15/combine-python-graphical-user-interface-sql-injection/ <br>


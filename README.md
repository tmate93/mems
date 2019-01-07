# A régi golyójáték újraalkotása a Raspberry PI és Sense Hat segítségével

Ez a pythonban íródott program az elterjedt játék újragondolása, átemelése modern környezetbe a Raspberry PI és annak Sense Hat kiegészítőjének segítségével

# Működése:

A program a Sense Hat inerciális mérőegységének (IMU) segítségével, a készülék tengelyek mentén való elmozdálásának mérésével mozgatja a "golyót" az előre megadott labirintusban
. a golyó koordinátáinak és a mért elmozdulásának felhasználásával teszteli, hogy az szabadon mozoghat-e az adott irányba, vagy falnak, csapdának esetleg a célnak ütközne-e, és ezen események alapján dönti el a mozgatás eredményét (sorrendben): <br><br> 
letiltja a golyó mozgását,<br><br>
levon életet amennyiben még van, és visszaállítja a kezdőállapotba a játékost, ha elfogyott az összes élet jelzi a játék végét és kilép a programból,<br><br>
illetve írja ki a győzelmet jelző szöveget és lép ki a programból,<br><br>
A játék nagy méretű pályák kezelésére alkalmas és annak a megfelelő részletét jeleníti meg a készülék led kijelzőjén.
Van lehetőség a pálya módosítására a kódon belül a "maze" változó tartalmának megváltoztatásával az előre definiált elemek használatának segítségével

# Használata:

Másoljuk át a marble mappát a PI-re tetszőleges helyre, majd a main.py file elindításával indul a játék. A készülék döntésével irányítható a golyó (fehérrel jelölve a kijelzőn). A játék célja, hogy átnavigáljunk a labirintuson a csapdák (a kijelzőn pirossal jelölve) kikerülésével és eljussunk a célba (zölddel jelölve).

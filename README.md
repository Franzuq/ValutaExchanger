Valutakonverterare

Skapad av Francis Chew | 2025-05-03

Beskrivning
Jag har koncentrerat mig på fyra primära kurselement under mitt projekt:

 1: Integration av API för att få aktuella växelkurser från ExchangeRate.host i realtid och ge korrekta och uppdaterade valutakonverteringar

 2. Använd Flask för webbutveckling för att skapa ett användarvänligt gränssnitt som gör det enkelt att konvertera och se historik.

 3. Filhantering genom att spara transaktioner i JSON-format, som visar hur man kan lagra data utan en databas.

 4: Grundläggande säkerhet, inklusive inputvalidering och varningar om användning av API-nyckeln

Jag valde dessa ögonblick eftersom de bidrar till skapandet av en effektiv applikation som löser ett verkligt problem.  API:et tillhandahåller pålitlig data, flaska möjliggör ett effektivt gränssnitt och filhanteringen sparar historik enkelt.  Säkerhet blev grundläggande för att skydda användardata.  Jag valde att undvika ytterligare komponenter, såsom databaser, eftersom de inte var nödvändiga för projektets storlek.


Krav
- Python 3.8 eller senare
- Installerad Flask, Requests och datetime:
  pip install flask requests
- Tillgång till internet (API-anrop krävs)
- API-nyckel (redan inkluderad):
  - Max 1000 anrop/månad
  - Varning: Dela inte denna nyckel med andra

Starta applikationen
1. Kör huvudfilen:
   python ValutaExchanger.py
2. Öppna i webbläsare:
   http://localhost:80

Obs:  
- Öppna inte HTML-filen direkt – den kräver Flask-servern
- En conversion_history.json skapas automatiskt för att spara data

Användarguide

Valutakonvertering
1. Ange belopp (siffror)
2. Välj "Från valuta"
3. Välj "Till valuta"
4. Klicka på "Konvertera"

Historikvisning
Klicka på "Visa Historik" för att se:
- Datum/tid
- Belopp
- Valutapar (Från → Till)
- Resultat

Avsluta
Stäng terminalfönstret eller tryck:
Ctrl + C

Felsökning
- Kontrollera installation:
  pip list | grep -E "flask|requests"
- Port 80 upptagen? Testa:
  netstat -ano | findstr :80
- Kontrollera internetanslutning

Projektstruktur
projekt/
├── ValutaExchanger.py     # Huvudapplikation
├── README.md              # Denna fil
├── requirements.txt       # Vilka python paket som krävs  
├── conversion_history.json # Sparad data
└── templates/
    └── index.html         # Webbgränssnitt

Tips: För säkerhetsuppdateringar, byt API-nyckel regelbundet.
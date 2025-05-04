#Francis Chew 2025-05-03

from flask import Flask, render_template, request
from datetime import datetime
import requests, json

# Skapa Flask-applikationen
app = Flask(__name__)

# Dictionary med tillgängliga valutor och deras fullständiga namn
CURRENCIES = {
    'SEK': 'Svensk krona',
    'EUR': 'Euro',
    'USD': 'Amerikansk dollar',
    'GBP': 'Brittiskt pund',
    'JPY': 'Japansk yen',
    'CAD': 'Kanadensisk dollar',
    'AUD': 'Australisk dollar',
    'CHF': 'Schweizisk franc',
    'CNY': 'Kinesisk yuan',
    'NOK': 'Norsk krona',
    'DKK': 'Dansk krona',
    'TRY': 'Turkisk lira',
    'RUB': 'Rysk rubel',
    'INR': 'Indisk rupie',
    'BRL': 'Brasiliansk real',
    'ZAR': 'Sydafrikansk rand',
    'MXN': 'Mexikansk peso',
    'SGD': 'Singapore-dollar',
    'HKD': 'Hongkong-dollar',
    'NZD': 'Nyzeeländsk dollar'
}

# API-URL för valutakonvertering
API_URL = "https://api.exchangerate.host/convert?access_key=a10162be35858348be07dbea4b4c824d"
# Filnamn för att spara konverteringshistorik
HISTORY_FILE = 'conversion_history.json'

def save_conversion(amount, from_curr, to_curr, result):
    """Sparar en lyckad valutakonvertering till historikfilen"""
    try:
        # Försök läsa befintlig historik
        try:
            with open(HISTORY_FILE, 'r') as f:
                history = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # Om filen inte finns eller är tom, skapa en tom lista
            history = []
        
        # Lägg till ny konvertering i historiken
        history.append({
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  # Nuvarande tidpunkt
            'amount': amount,                                      # Belopp att konvertera
            'from_currency': from_curr,                            # Från valuta
            'to_currency': to_curr,                                # Till valuta
            'result': result                                       # Konverteringsresultat
        })
        
        # Spara den uppdaterade historiken till fil
        with open(HISTORY_FILE, 'w') as f:
            json.dump(history, f, indent=2)  # Använd indent för läsbar JSON
    except Exception as e:
        # Logga fel om det uppstår problem med filhantering
        print(f"Kunde inte spara historik: {e}")

def get_conversion_history():
    """Hämtar hela konverteringshistoriken från fil"""
    try:
        with open(HISTORY_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Returnera tom lista om filen inte finns eller är ogiltig
        return []
    except Exception as e:
        # Logga andra fel som uppstår vid filläsning
        print(f"Kunde inte läsa historik: {e}")
        return []
    
@app.route('/', methods=['GET', 'POST'])
def index():
    """Huvudroute som hanterar både visning och hantering av formuläret"""
    result = None          # Variabel för konverteringsresultat
    show_history = None    # Flagga för att visa historik
    history = None         # Variabel för att lagra historikdata

    try:
        if request.method == 'POST':
            # Hantera valutakonvertering
            if 'amount' in request.form:
                from_currency = request.form['from_currency']
                to_currency = request.form['to_currency']
                amount = float(request.form['amount'])

                # Parametrar för API-anropet
                params = {
                    'from': from_currency,
                    'to': to_currency,
                    'amount': amount
                }
                try:
                    # Gör API-anrop för valutakonvertering
                    response = requests.get(API_URL, params=params)
                    data = response.json()
                    result = data.get('result', 'Fel vid hämtning av data')
                    
                    # Spara endast lyckade konverteringar
                    if not isinstance(result, str) or not result.startswith('Fel:'):
                        save_conversion(amount, from_currency, to_currency, result)
                except Exception as e:
                    # Hantera fel från API-anropet
                    result = f"Fel: {str(e)}"
            
            # Hantera förfrågan om att visa historik
            elif 'show_history' in request.form:
                show_history = True
                history = get_conversion_history()
            
        # Rendera mallen med alla nödvändiga data
        return render_template('index.html', 
                            currencies=sorted(CURRENCIES.items()),
                            result=result,
                            show_history=show_history,
                            history=history)
    except Exception as ex:
        # Fånga oväntade fel i huvudlogiken
        print(ex)
        
# Starta Flask-applikationen
app.run(host="0.0.0.0", port=80)

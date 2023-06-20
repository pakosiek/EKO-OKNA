from flask import Flask, render_template, request, jsonify, send_file
import csv
import requests
from bs4 import BeautifulSoup
import re
import io

app = Flask(__name__)

class PagineGialleApp:
    def __init__(self):
        self.csv_file = open('Klienci bramy - Arkusz1.csv', 'a', newline='', encoding='utf-8')
        self.csv_writer = csv.writer(self.csv_file, delimiter=',')
        self.existing_data = self.load_data()

    def load_data(self):
        try:
            with open('Klienci bramy - Arkusz1.csv', 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                existing_data = list(reader)
        except FileNotFoundError:
            existing_data = []
        return existing_data

    def validate_url(self, url):
        if not url.startswith('https://www.paginegialle.it'):
            return False
        return True

    def check_duplicate_entry(self, url):
        for data_entry in self.existing_data:
            if data_entry and data_entry[0] == url:
                return True
        return False

    def save_data(self, data_entry):
        self.csv_writer.writerow(data_entry)
        self.existing_data.append(data_entry)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data', methods=['POST'])
def get_data():
    url = request.form['url']

    pagine_gialle = PagineGialleApp()

    if not pagine_gialle.validate_url(url):
        return jsonify({'error': 'Błędny link'})

    if pagine_gialle.check_duplicate_entry(url):
        return jsonify({'error': 'Ta firma już została wpisana!'})

    response = requests.get(url)
    html_code = response.content

    soup = BeautifulSoup(html_code, 'html.parser')

    piva_element = soup.find('strong', string='P. IVA')
    if piva_element:
        piva = piva_element.next_sibling.strip().replace(':', '')
    else:
        return jsonify({'error': 'Na pewno wpisałeś dobry link?'})

    h1_element = soup.find('h1', {'class': 'scheda-azienda__companyTitle'})
    if h1_element:
        company_name = h1_element.text.strip()
    else:
        return jsonify({'error': 'Na pewno wpisałeś dobry link?'})

    address_element = soup.find('div', {'class': 'scheda-azienda__companyAddress'})
    if address_element:
        address_lines = [line.strip() for line in address_element.stripped_strings]
        address = ' '.join(address_lines)
    else:
        return jsonify({'error': 'Na pewno wpisałeś dobry link?'})

    email_pattern = r'"email":"([^"]+)"'
    email_match = re.search(email_pattern, html_code.decode('utf-8'))

    if email_match:
        email = email_match.group(1)
    else:
        email = 'Nie znaleziono adresu e-mail'

    data_entry = [url, company_name, address, piva, email]
    pagine_gialle.save_data(data_entry)

    return jsonify({'success': 'Dane zostały zapisane'})

@app.route('/download_data')
def download_data():
    with open('Klienci bramy - Arkusz1.csv', 'r', newline='', encoding='utf-8') as file:
        return send_file(
            io.StringIO(file.read()),
            mimetype='text/csv',
            as_attachment=True,
            attachment_filename='Klienci_bramy_Arkusz1.csv'
        )

if __name__ == '__main__':
    app.run()

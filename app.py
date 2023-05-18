from flask import Flask, render_template

app = Flask(__name__)

# Konfiguracja ikony favicon
@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

# Strona główna
@app.route('/')
def home():
    return render_template('index.html')

# O mnie
@app.route('/about')
def about():
    return render_template('aboutme.html')

# Galeria
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

# Kontakt
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Obsługa stron błędów
@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', error_code='404', error_message='Page not found'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('error.html', error_code='500', error_message='Internal Server Error'), 500

if __name__ == '__main__':
    app.run(debug=True)

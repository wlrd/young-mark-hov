from app import app
import chainz

@app.route('/')
@app.route('/index')
def index():
    file = open('./lyrics.txt')
    m = chainz.Markov(file)
    return m.generate_markov_text()


from flask import Flask
from flask import jsonify
from flask import render_template

from sqlalchemy.orm import sessionmaker
from model import Server, Monitoring, engine


DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 


@app.route('/json')
def data_for_server():
    server = session.query(Server).first()
    all_recs = session.query(Monitoring).filter(Monitoring.server == server).all()

    pings = []
    for rec in all_recs:
        pings.append(rec.ping)

    return jsonify({"x": pings,
                    "y": [str(i) for i in range(len(pings))]})
    

app.run()

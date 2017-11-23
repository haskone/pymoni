import re
import subprocess

from sqlalchemy.orm import sessionmaker
from model import Server, Monitoring, engine
# from threading import Thread

DBSession = sessionmaker(bind=engine)
session = DBSession()

def make_monitoring(id):
    server = session.query(Server).filter(Server.id == id).first()
    ping = subprocess.Popen(["ping", "-c", "3", server.ip],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    out, error = ping.communicate()
    out = out.strip()        
    s = out.decode().split("\n")[-1]    
    groups = re.search(r'([0-9]+\.[0-9]+)\/([0-9]+\.[0-9]+)', s)
    ping_value = groups.group(2)   
    monitor = Monitoring(ping=ping_value,
                         server=server)
    session.add(monitor)
    session.commit()

servers = session.query(Server).all()
for server in servers:
    make_monitoring(server.id)
    # TODO: should be wiht thread or asyncio
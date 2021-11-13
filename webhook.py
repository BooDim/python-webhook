import json
from pprint import pprint


def webhook(session):
    action = session['action']

    if action == 'event1':
       
        session['variable1'] = 'count'

   
    return json.dumps(session)

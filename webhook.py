import json
from pprint import pprint


def webhook(session):
    action = session['action']

    if action == 'event1':
        num_u = session['num_u']
        number = [int(i) for i in ' '.join(session['number']).split()]
        count = 0
        for i in range(len(number)):
            if num_u[i] == number[i]:
                count += 1
        session['variable1'] = 'count'

    elif action == 'event2':
        print('Received request from event2 action')
        session['variable2'] = "value2"

    elif action == 'event3':
        print('Received request from event3 action')
        session['variable3'] = "value3"

    else:
        print('Unknown action. Session data:')
        pprint(session)
        action = session['action']

        session['text'] = f'Webhook recieved a request, but couldn\'t handle the action' \
                          f'{action}.'

    return json.dumps(session)
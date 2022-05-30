import os

class SessionsRead:
    def __init__(self):
        self.sessions = []
        for session in os.listdir('sessions'):
            if session[-7:] == 'session':
                session = open(f'sessions/{session}', 'r')
                self.sessions.append(session.read())

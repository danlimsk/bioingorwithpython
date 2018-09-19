### Example 6-3: Sending email

import smtplib
import socket                   # just for socket.err

def sendmsg(fromaddr, toaddr,
            username=None, password=None,
            subject='', msg='',
            hostname='localhost', port=25):

    # Destination can be a single username or a sequence of them
    dest = toaddr if type(toaddr) == str else ', '.join(toaddr)

    msg = '''To: {1}
From: {0}
Subject: {2}
Content-Type: text/plain; charset="us-ascii"

'''.format(fromaddr, dest, subject) + msg

    connection = None
    try:
        connection = smtplib.SMTP()
        connection.connect(hostname, port)
        if username:
            connection.login(username, password)
        connection.sendmail(fromaddr, dest, msg)
        print('\nMessage sent from {}:\nto: {}'.
              format(fromaddr, dest),
              file=sys.stderr)
    except smtplib.SMTPConnectError as err:
        print('Attempted connection to {} on port {} failed',
              format(hostname, port),
              file=sys.stderr)
    except smtplib.SMTPAuthenticationError as err:
        print('Authentication for user', username, 'failed',
              'Invalid username-password combination?',
              sep='\n',
              file=sys.stderr)
    except socket.error as err:
        print('Socket error:', err, file=sys.stderr)
    finally:
        if connection:
            try:
                connection.quit()
            except smtplib.SMTPServerDisconnected:
                pass            # can't quit an unconnected SMTP

### Example 6-10: Using the string template facility to email a form letter

import string
from ch06_03 import sendmsg

def broadcast(subject, filename, substitutions, receivers):
    with open(filename) as file:
        message = string.Template(file.read()).substitute(substitutions)
    for receiver in receivers:
        sendmsg('your-program',
                receiver,
                subject=subject,
                msg=message
                )

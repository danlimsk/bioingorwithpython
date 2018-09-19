### Example 6-4: A minimal logging example

import datetime
import logging

LOG_FILENAME = '../output/logging.out'

# This directs the logging facility to use the named file and to
# ignore any requests for log entries with a level less than DEBUG
logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO)

# This appends an entry to the logfile
logging.info("This message was logged at {}."
             .format(datetime.datetime.now().strftime('%H:%M')))

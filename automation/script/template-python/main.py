import os
import logging
if __name__ == "__main__":

    logging.info ('')
    logging.info ('Main script:')
    logging.info ('ENV CM_VAR1: {}'.format(os.environ.get('CM_VAR1','')))
    logging.info ('')

    exit(0)

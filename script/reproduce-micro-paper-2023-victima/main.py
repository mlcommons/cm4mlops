import os
import logging
if __name__ == "__main__":

    logging.info ('')
    logging.info ('Main script:')
    logging.info ('Experiment: {}'.format(os.environ.get('CM_EXPERIMENT','')))
    logging.info ('')

    exit(0)

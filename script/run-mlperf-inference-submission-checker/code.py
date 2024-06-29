# Developer: Grigori Fursin

import os
import pandas
import logging
def main():
    logging.info ('=========================================================')

    logging.info ('Searching for summary.csv ...')

    if os.path.isfile('summary.csv'):
        logging.info ('Converting to json ...')

        import pandas

        df = pandas.read_csv('summary.csv').T

        logging.info ('')
        logging.info (df)
        logging.info ('')

        df.to_json('summary.json', orient='columns', indent=4)

    logging.info ('=========================================================')

if __name__ == '__main__':
    main()

# Taken from https://github.com/mlcommons/croissant/pull/564/files (@mkuchnik)

import os
import mlcroissant as mlc
import logging
def main():
    
    url = os.environ.get('CM_PRINT_CROISSANT_URL', '')

    if url=='':
        logging.error ('Error: --url is not specified')
        exit(1)
    
    ds = mlc.Dataset(url)
    metadata = ds.metadata.to_json()

    logging.info ('')
    logging.info ('Croissant meta data URL: {}'.format(url))
    logging.info ('')
    logging.info (f"{metadata['name']}: {metadata['description']}")

    logging.info ('')
    for x in ds.records(record_set="default"):
        logging.info(x)

if __name__ == '__main__':
    main()

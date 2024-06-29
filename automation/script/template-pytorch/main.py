import os
import logging
import torch

if __name__ == "__main__":

    logging.info ('')
    logging.info ('Main script:')
    logging.info ('ENV CM_VAR1: {}'.format(os.environ.get('CM_VAR1','')))
    logging.info ('ENV USE_CUDA: {}'.format(os.environ.get('USE_CUDA','')))
    logging.info ('')
    logging.info ('PyTorch version: {}'.format(torch.__version__))
    logging.info ('')

    exit(0)

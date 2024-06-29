import os
import logging
from cmind import utils
    
# Pring help about script
def print_help(i):

    meta = i.get('meta', '')
    path = i.get('path', '')

    if len(meta)==0 and path=='':
        return {'return':0}

    logging.info ('')
    logging.info ('Help for this CM script ({},{}):'.format(meta.get('alias',''), meta.get('uid','')))

    logging.info ('')
    logging.info ('Path to this automation recipe: {}'.format(path))

    variations = meta.get('variations',{})
    if len(variations)>0:
        logging.info ('')
        logging.info ('Available variations:')
        logging.info ('')
        for v in sorted(variations):
            logging.info ('  _'+v)

    input_mapping = meta.get('input_mapping', {})
    if len(input_mapping)>0:
        logging.info ('')
        logging.info ('Available flags mapped to environment variables:')
        logging.info ('')
        for k in sorted(input_mapping):
            v = input_mapping[k]

            logging.info ('  --{}  ->  --env.{}'.format(k,v))

    input_description = meta.get('input_description', {})
    if len(input_description)>0:
        # Check if has important ones (sort)
        sorted_keys = []
        all_keys = sorted(list(input_description.keys()))

        for k in sorted(all_keys, key = lambda x: input_description[x].get('sort',0)):
            v = input_description[k]
            if v.get('sort',0)>0:
                sorted_keys.append(k)
        
        
        logging.info ('')
        logging.info ('Available flags (Python API dict keys):')
        logging.info ('')
        for k in all_keys:
            v = input_description[k]
            n = v.get('desc','')

            x = '  --'+k
            if n!='': x+='  ({})'.format(n)

            logging.info (x)

        if len(sorted_keys)>0:
            logging.info ('')
            logging.info ('Main flags:')
            logging.info ('')
            for k in sorted_keys:
                v = input_description[k]
                n = v.get('desc','')

                x = '  --'+k

                d = None
                if 'default' in v:
                    d = v.get('default','')

                if d!=None:
                    x+='='+d

                c = v.get('choices',[])
                if len(c)>0:
                    x+='   {'+','.join(c)+'}'

                if n!='': x+='   ({})'.format(n)

                logging.info (x)



    logging.info ('')
    x = input ('Would you like to see a Python API with a list of common keys/flags for all scripts including this one (y/N)? ')

    x = x.strip().lower()

    skip_delayed_help = False if x in ['y','yes'] else True

    r = {'return':0}

    if skip_delayed_help: 
        r['skip_delayed_help'] = True

    return r

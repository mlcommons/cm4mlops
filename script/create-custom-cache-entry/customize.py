from cmind import utils
import os
import shutil

def preprocess(i):

    # CM script internal variables
    env = i['env']

    extra_cache_tags = []
    if env.get('CM_EXTRA_CACHE_TAGS','').strip() == '':
        print ('')
        extra_cache_tags_str = input('Enter extra tags for the custom CACHE entry separated by comma: ')

        extra_cache_tags = extra_cache_tags_str.strip().split(',')

    return {'return':0, 'add_extra_cache_tags':extra_cache_tags}

def postprocess(i):

    env = i['env']

    cur_dir = os.getcwd()

    x = ''
    env_key = env.get('CM_CUSTOM_CACHE_ENTRY_ENV_KEY', '')
    if env_key != '': x = env_key+'_'
    
    env['CM_CUSTOM_CACHE_ENTRY_{}PATH'.format(x)] = cur_dir
    env['CM_CUSTOM_CACHE_ENTRY_PATH'] = cur_dir

    return {'return': 0}

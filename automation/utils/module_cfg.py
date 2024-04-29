﻿import os
import cmind
import copy

base_path={}
base_path_meta={}

##################################################################################
def load_cfg(i):

    tags = i.get('tags','')
    artifact = i.get('artifact','')

    key = i.get('key', '')
    key_end = i.get('key_end', [])

    ii={'action':'find',
        'automation':'cfg'}
    if artifact!='':
        ii['artifact']=artifact
    elif tags!='':
        ii['tags']=tags

    r=cmind.access(ii)
    if r['return']>0: return r

    lst = r['list']

    prune = i.get('prune',{})
    prune_key = prune.get('key', '')
    prune_key_uid = prune.get('key_uid', '')
    prune_meta_key = prune.get('meta_key', '')
    prune_meta_key_uid = prune.get('meta_key_uid', '')
    prune_uid = prune.get('uid', '')
    prune_list = prune.get('list',[])
    
    # Checking individual files inside CM entry
    selection = []
 
    if i.get('skip_files', False):
        for l in lst:
             meta = l.meta
             full_path = l.path

             meta['full_path']=full_path

             add = True
             
             if prune_key!='' and prune_key_uid!='':
                 if prune_key_uid not in meta.get(prune_key, []):
                     add = False
             
             if add:
                 selection.append(meta)
    else:
        for l in lst:
            path = l.path

            main_meta = l.meta

            skip = False
            
            if prune_meta_key!='' and prune_meta_key_uid!='':
                if prune_meta_key_uid not in main_meta.get(prune_meta_key, []):
                    skip = True
            
            if skip:
                continue
            
            all_tags = main_meta.get('tags',[])

            files = os.listdir(path)

            for f in files:
                if key!='' and not f.startswith(key):
                    continue

                if f.startswith('_') or (not f.endswith('.json') and not f.endswith('.yaml')):
                    continue

                if len(key_end)>0:
                    skip = True
                    for ke in key_end:
                        if f.endswith(ke):
                            skip = False
                            break
                    if skip:
                        continue

                full_path = os.path.join(path, f)

                full_path_without_ext = full_path[:-5]

                r = cmind.utils.load_yaml_and_json(full_path_without_ext)
                if r['return']>0:
                    print ('Warning: problem loading file {}'.format(full_path))
                else:
                    meta = r['meta']

                    # Check base
                    r = process_base(meta, full_path)
                    if r['return']>0: return r
                    meta = r['meta']
                    
                    uid = meta['uid']

                    # Check pruning
                    add = True

                    if len(prune)>0:
                        if prune_uid!='' and uid != prune_uid:
                            add = False
                            
                        if add and len(prune_list)>0 and uid not in prune_list:
                            add = False

                        if add and prune_key!='' and prune_key_uid!='' and prune_key_uid != meta.get(prune_key, None):
                            add = False

                    if add:
                        meta['full_path']=full_path

                        add_all_tags = copy.deepcopy(all_tags)
                        
                        name = meta.get('name','')
                        if name=='':
                            name = ' '.join(meta.get('tags',[]))
                        name = name.strip()
                        meta['name'] = name

                        file_tags = meta.get('tags', '').strip()
                        if file_tags=='':
                            if name!='':
                                add_all_tags += [v.lower() for v in name.split(' ')]
                        else:
                            add_all_tags += file_tags.split(',')
                            
                        meta['all_tags']=add_all_tags

                        meta['main_meta']=main_meta

                        selection.append(meta)

    return {'return':0, 'lst':lst, 'selection':selection}

##################################################################################
def process_base(meta, full_path):

    global base_path, base_path_meta

    _base = meta.get('_base', '')
    if _base != '':
        name = ''

        filename = _base
        full_path_base = os.path.dirname(full_path)
 
        if not filename.endswith('.yaml') and not filename.endswith('.json'):
            return {'return':1, 'error':'_base file {} in {} must be .yaml or .json'.format(filename, full_path)}
        
        if ':' in _base:
            x = _base.split(':')
            name = x[0]

            full_path_base = base_path.get(name, '')
            if full_path_base == '':
                
                # Find artifact
                r = cmind.access({'action':'find',
                                  'automation':'cfg',
                                  'artifact':name})
                if r['return']>0: return r

                lst = r['list']

                if len(lst)==0:
                    if not os.path.isfile(path): 
                        return {'return':1, 'error':'_base artifact {} not found in {}'.format(name, full_path)}

                full_path_base = lst[0].path
            
                base_path[name] = full_path_base
            
            filename = x[1]
       
        # Load base
        path = os.path.join(full_path_base, filename)

        if not os.path.isfile(path): 
            return {'return':1, 'error':'_base file {} not found in {}'.format(filename, full_path)}
            
        if path in base_path_meta:
            base = copy.deepcopy(base_path_meta[path])
        else:
            path_without_ext = path[:-5]

            r = cmind.utils.load_yaml_and_json(path_without_ext)
            if r['return']>0: return r

            base = r['meta']

            base_path_meta[path]=copy.deepcopy(base)

        for k in meta:
            v = meta[k]

            if k not in base:
                base[k]=v
            else:
                if isinstance(v, str):
                    # Only merge a few special keys and overwrite the rest
                    if k in ['tags','name']:
                        base[k] += meta[k]
                    else:
                        base[k] = meta[k]

                elif type(v) == list:
                    for vv in v:
                        base[k].append(vv)
                elif type(v) == dict:
                    base[k].merge(v)

        meta = base

    return {'return':0, 'meta':meta}

##################################################################################
def select_cfg(i):

    self_module = i['self_module']
    tags = i['tags']
    alias = i.get('alias', '')
    title = i.get('title', '')

    # Check if alias is not provided 
    r = self_module.cmind.access({'action':'find', 'automation':'cfg', 'tags':'basic,docker,configurations'})
    if r['return'] > 0: return r
        
    lst = r['list']

    selector = []

    for l in lst:
        p = l.path

        if alias != '':
            for ext in ['.json', '.yaml']:
                p1 = os.path.join(p, alias+ext)
                if os.path.isfile(p1):
                    selector.append({'path':p1, 'alias':alias})
                    break

        else:
            files = os.listdir(p)

            for f in files:
                if not f.startswith('_cm') and (f.endswith('.json') or f.endswith('.yaml')):
                    selector.append({'path':os.path.join(p, f), 'alias':f[:-5]})

    if len(selector) == 0:
        return {'return':16, 'error':'configuration was not found'}

    select = 0
    if len(selector) > 1:
        xtitle = ' ' + title if title!='' else ''
        print ('')
        print ('Available{} configurations:'.format(xtitle))
        
        print ('')

        for s in range(0, len(selector)):
            ss = selector[s]

            path = ss['path']

            full_path_without_ext = path[:-5]

            r = cmind.utils.load_yaml_and_json(full_path_without_ext)
            if r['return']>0:
                print ('Warning: problem loading configuration file {}'.format(path))

            meta = r['meta']
            ss['meta'] = meta

            alias = ss['alias']
            name = meta.get('name','')

            x = name
            if x!='': x+=' '
            x += '('+alias+')'
            
            print ('{}) {}'.format(s, x))
        
        print ('')
        select = input ('Enter configuration number of press Enter for 0: ')

        if select.strip() == '': select = '0'

    select = int(select)

    if select<0 or select>=len(selector):
        return {'return':1, 'error':'selection is out of range'}

    ss = selector[select]

    return {'return':0, 'selection':ss}

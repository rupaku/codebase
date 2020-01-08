''' convert this dictionary into a flattened dictionary where the key is separated by ‘_’ in case of the nested key to be started.'''

def flatten_dict(d):
    flat_dict={}
    def looping(dict1,keystring=''):
        for k,v in dict1.items():
            if k!='':
                if keystring!='':
                    k=keystring+'.'+k
            else:
                k=keystring
            if type(v)!=dict:
                print('adding to flat '+str(k)+' :'+str(v))
                flat_dict[k]=v
            else:
                print('recurse and build '+str(k))
                looping(v,k)
    looping(d)
    return flat_dict

dict1={'key1':
           {'key2':
                {'key3':1}
            },
           'key4':
               {'key5':
                    {'key6':2}
               },
           'key7':
                {'key8':
                    {'key9':3, 'key10': 4}
                }
       }

print(flatten_dict(dict1))

#output
# recurse and build key1
# recurse and build key1.key2
# adding to flat key1.key2.key3 :1
# recurse and build key4
# recurse and build key4.key5
# adding to flat key4.key5.key6 :2
# recurse and build key7
# recurse and build key7.key8
# adding to flat key7.key8.key9 :3
# adding to flat key7.key8.key10 :4
# {'key1.key2.key3': 1, 'key4.key5.key6': 2, 'key7.key8.key9': 3, 'key7.key8.key10': 4}


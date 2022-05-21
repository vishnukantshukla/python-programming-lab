def value(**a):
    st=f'''
     Name={ a.get('name')}
    section={a.get('section')}
    cpi={a.get('cpi')}    
    '''
    return st

dct={'name':'vishnukant shukla ','section':'H'}
out=value(**dct)
print(out)
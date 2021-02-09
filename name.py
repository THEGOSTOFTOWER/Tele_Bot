def con_name(lst, type, name):
    if type == 'street':
        return lst['улица'][(lst.index(f'*.{name[0]}'))]
    else:
        return lst['дом'][(lst.index(f"*.{' '.join(name)}"))]

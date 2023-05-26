# se pueden modificar, no tienen un orden, no puede tener elementos duplicados
# no tiene un par key = value

# CREATE
set_countries = {'col', 'mex', 'bol', 'col'}
set_from_string = set('Camilo')

# READ
print(set_countries)
print(set_from_string)
print(len(set_countries))
print('col' in set_countries)
print('pe' in set_countries)

# UPDATE
set_countries.add('pe')
set_countries.update({'AR', 'CL', 'pe'})

# DELETE
set_countries.remove('pe')
set_countries.discard('sp')
set_countries.clear()


# OPERATIONS
set_latam = {'CO', 'PE', 'AR', 'BR'}
set_otros = {'SP', 'BR', 'TR'}

set_union = set_latam.union(set_otros)
print(set_union)
print(set_latam | set_otros)

set_interseccion = set_latam.intersection(set_otros)
print(set_interseccion)
print(set_latam & set_otros)

set_difference = set_latam.difference(set_otros)
print(set_difference)
print(set_latam - set_otros)

set_difference_sym = set_latam.symmetric_difference(set_otros)
print(set_difference_sym)
print(set_latam ^ set_otros)
import own_mod
import utils
import random



def run():
    keys, values = own_mod.get_population()
    print(keys, values)

    result_suma = utils.suma(3)
    print(result_suma)

    result_multiplication = utils.multiplicar(3)
    print(result_multiplication)

if __name__ == '__main__': #si es ejecutado desde la terminal se ejecuta, si no , no
    run()

data = [
    {
        'name' : 'camilo'
    }
]
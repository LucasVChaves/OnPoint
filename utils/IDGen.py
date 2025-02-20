import random

class IDGen():
    @staticmethod
    def gen_id(seed: str):
        # a seed pode ser o nome, PIN, email, qualquer coisa unica
        random.seed(seed)
        # o intervalo eh [a,b)
        return random.randint(1000, 10001)

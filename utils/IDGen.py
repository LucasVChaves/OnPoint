import hashlib

class IDGen():
    @staticmethod
    def gen_id(seed: str):
        # Garante um ID fixo e determinístico baseado na seed (ex: PIN, email, etc.)
        hash_value = int(hashlib.sha256(seed.encode()).hexdigest(), 16)
        return 1000 + (hash_value % 9000)  # Mantém o ID entre 1000 e 9999

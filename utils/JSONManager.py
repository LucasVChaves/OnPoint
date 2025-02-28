import os
import json
from utils.State import State  # Importando o Enum State

class JSONManager:
    data_dir = os.path.abspath(os.getcwd()) + '/data/'

    # Carregar um único objeto com base no ID
    def load_from_json(self, category: str, id: str):
        if not category or not id:
            raise ValueError("Todos argumentos devem ser passados")

        file_path = self.data_dir + f'{category}.json'

        if not os.path.exists(file_path):
            raise FileNotFoundError(f'Arquivo JSON pra categoria {category} não encontrado em {file_path}')

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            raise ValueError(f'Erro ao decodificar o JSON para a categoria {category}.')

        for obj in data:
            if obj.get('id') == id:
                # Garantindo que o estado seja um valor do Enum
                if obj.get('state'):
                    obj['state'] = State[obj['state'].upper()]  # Converte o estado para o enum correspondente
                return obj

        return None

    # NOVA FUNÇÃO: Carregar todos os objetos de uma categoria
    def load_all_from_json(self, category: str):
        if not category:
            raise ValueError("A categoria deve ser informada.")

        file_path = self.data_dir + f'{category}.json'

        if not os.path.exists(file_path):
            raise FileNotFoundError(f'Arquivo JSON para categoria {category} não encontrado em {file_path}')

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                # Garantindo que o estado de todos os objetos seja convertido para o enum
                for obj in data:
                    if obj.get('state'):
                        obj['state'] = State[obj['state'].upper()]  # Converte o estado para o enum correspondente
                return data
        except json.JSONDecodeError:
            raise ValueError(f'Erro ao decodificar o JSON para a categoria {category}.')

    # Salvar ou atualizar um objeto no JSON
    def save_to_json(self, category: str, id: str, new_object):
        if not category or not id:
            raise ValueError("Todos argumentos devem ser passados")

        data = []
        file_path = self.data_dir + f'{category}.json'

        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                raise ValueError(f"Erro ao acessar o JSON da categoria {category}")

        # Verificar se o ID já existe e atualizar
        for i, obj in enumerate(data):
            if obj.get('id') == id:
                data[i] = new_object  # Atualiza o objeto existente
                break
        else:
            data.append(new_object)  # Se não existir, adiciona um novo

        try:
            with open(file_path, 'w', encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
                return True
        except Exception as e:
            print(f"Erro ao salvar no arquivo JSON de {category}: {e}")
            return False

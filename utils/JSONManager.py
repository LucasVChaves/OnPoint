import os
import json

class JSONManager:
    data_dir = os.path.abspath(os.getcwd()) + '/data/'

    def load_from_json(self, category: str, id: str):
        if not category or not id:
            raise ValueError("Todos argumentos devem ser passados")

        file_path = self.data_dir + f'{category}.json'

        if not os.path.exists(file_path):
            raise FileNotFoundError(f'Arquivo JSON pra categoria {category} nao encontrado em {file_path}')

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            raise ValueError(f'Erro ao decodificar o JSON para a categoria {category}.')

        for obj in data:
            if obj.get('id') == id:
                return obj

        return None

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

        for i, obj in enumerate(data):
            if obj.get('id') == new_object['id']:
                data[i] = new_object
                break;
            else:
                data.append(new_object)

        try:
            with open(file_path, 'w', encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
                return True
        except Exception as e:
            print(f"Erro ao salvar no arquivo JSON de {category}: {e}")
            return False



loader = JSONManager()
print(loader.load_from_json(category="employee", id="1"))

updated_employee =  {'id': '1', 'name': 'Testinho', 'role': 'gerente'}
loader.save_to_json(category='employee', id='1', new_object=updated_employee)
print(loader.load_from_json(category="employee", id="1"))

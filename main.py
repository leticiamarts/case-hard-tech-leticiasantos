import requests
import json

class Api_Requests():

    def __init__(self):
        self.r = requests.get("https://rickandmortyapi.com/api/character")
        self.data = json.loads(self.r.content)
        self.results = self.data['results'] 
        # dados_indentados = json.dumps(data, indent=4)
        # print(dados_indentados)


#Classe criada para representar a lista de alguns personagens de Rick and Morty
class List_Characters():

    # Construtor
    def __init__(self, name): # Atribuir name a lista
        self.name = name
        self.characters = []

    # Método para adicionar personagens na lista
    def add_character(self, character):
        self.characters.append(character)

    # Método para imprimir name de determinada lista
    def print_name_list(self):
        print('\n##################{}##################\n'.format(self.name))


    # Método para printar a lista de personagens do filme
    def print_characters_list(self):
        for character in self.characters:
            print('{}\n'.format(character['name']))

    # Método para printar name, gênero e espécie de personagens da lista
    def print_character_gender(self):
        for character in self.characters:
            print('Name: {} - Gender: {} - Species: {}'.format(
                character['name'], character['gender'], character['species']))

    # Método para printar personagens vivos
    def print_alive(self):
        for character in self.characters:
            if character['status'] == 'Alive':
                print('{} - {}\n'.format(character['name'], character['status']))

    #Método para printar personagens mortos
    def print_dead(self):
        for character in self.characters:
            if character['status'] == 'Dead':
                print('{} - {}\n'.format(character['name'], character['status']))

    # Método para deletar personagens mortos da lista
    def pop_dead(self):
        for character in self.characters:
            if character['status'] == 'Dead':
                for i, j in enumerate(self.characters):
                    if j['status'] == 'Dead':
                        self.characters.pop(i)
        return

    # Método para alterar nome de personagem
    def change_character_name(self, name):
        name = name[len(name)::-1]
        return name
        


if __name__ == '__main__':
    api_r = Api_Requests()

    human_list = List_Characters("LISTA HUMANOS")
    alien_list = List_Characters("LISTA ALIENS")

    for character in api_r.results:
        # print(results)
        registro_character = {}
        registro_character['name'] = character['name']
        registro_character['id'] = character['id']
        registro_character['status'] = character['status']
        registro_character['species'] = character['species']
        registro_character['gender'] = character['gender']

        if character['species'] == 'Alien':
            alien_list.add_character(registro_character)
        else:
            human_list.add_character(registro_character)

        
    human_list.print_name_list()
    human_list.print_characters_list()
    
    
    alien_list.print_name_list()
    alien_list.print_characters_list()

    print("Characters - Genders - Species")
    human_list.print_character_gender()
    alien_list.print_character_gender()

    print("\n---ALIVE---\n")
    human_list.print_alive()
    alien_list.print_alive()

    print("\n---DEAD---\n")
    human_list.print_dead()
    alien_list.print_dead()

    print("\n---Deletando os mortos da lista---\n")

    human_list.pop_dead()
    alien_list.pop_dead()

    print("\n---Alterando nome de um Personagem e Pritando as listas novamente---\n")
    human_list.print_name_list()
    human_list.characters[0]['name'] = human_list.change_character_name(human_list.characters[0]['name'])
    human_list.print_characters_list()

    alien_list.print_name_list()
    alien_list.print_characters_list()

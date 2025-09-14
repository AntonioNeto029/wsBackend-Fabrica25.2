# Projeto para o Desafio da Fábrica de Software

O projeto consiste em uma Pokédex desenvolvida com o FrameWork Django, aonde o usuário consegue fazer buscas em tempo real por uma API, e também consegue montar sua propria Pokédex!

## Funcionalidades

### Pokémons

- **Criação de Pokémons:** Registo de novos Pokémons no banco de dados local. Ao criar, o sistema busca automaticamente a imagem oficial da PokéAPI para enriquecer os dados.
- **Listagem de Pokémons:** Visualização de todos os Pokémons "capturados", com as suas respectivas imagens e detalhes.
- **Atualização e Exclusão:** Edição dos dados e exclusão de registos, com uma página de confirmação para evitar exclusões acidentais.

---

### Treinadores

- **Criação de Treinadores:** Registo de novos treinadores.
- **Listagem de Treinadores:** Visualização de todos os treinadores registados.
- **Atualização e Exclusão:** Edição e exclusão de treinadores.

---

### Integração com a PokéAPI

- **Busca em Tempo Real:** Uma funcionalidade de busca na página inicial que consulta a PokéAPI e exibe os dados de qualquer Pokémon (imagem, tipo, habilidades, etc.) sem a necessidade de o salvar na Pokédex local.

---

## Tecnologias Utilizadas

- **Backend:** Python, Django
- **Comunicação com API:** Biblioteca `requests`
- **API Externa:** [PokéAPI V2](https://pokeapi.co/)
- **Frontend:** HTML, CSS (com estilos no template)
- **Banco de Dados:** SQLite 3 (padrão do Django para desenvolvimento)

---

## Autor

- **Antonio Ramos de Araujo Neto**

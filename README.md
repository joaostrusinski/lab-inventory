# Sistema de Gerenciamento de Equipamentos de Laboratório

![Static Badge](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Static Badge](https://img.shields.io/badge/licen%C3%A7a-MIT-blue)

Um sistema web front-end para gerenciar e visualizar os equipamentos de um laboratório de testes de rede, substituindo o controle manual por planilhas.

![Screenshot do Projeto] https://imgur.com/a/dJ9WIJk

## 📋 Sobre o Projeto

Este projeto foi criado para atender à necessidade de um laboratório de redes e homologações da Vivo, com o objetivo de centralizar e facilitar a consulta de equipamentos que estão em uso em diferentes cenários de teste. A interface permite visualizar rapidamente o status de cada porta, VLANs associadas e observações importantes, além de permitir o cadastro dinâmico de novos equipamentos.

## ✨ Funcionalidades (Front-end)

-   **Visualização em Tabela:** Exibe todos os equipamentos e suas configurações em uma tabela clara e organizada.
-   **Filtro em Tempo Real:** Um campo de busca que filtra a tabela dinamicamente conforme o usuário digita.
-   **Cadastro Dinâmico:** Um formulário que permite adicionar novas linhas à tabela sem precisar recarregar a página.
-   **Validação de Dados:** Campos numéricos no formulário de cadastro só aceitam números, garantindo a integridade dos dados inseridos.
-   **Interface Responsiva:** O layout se adapta a diferentes tamanhos de tela.

## 🚀 Tecnologias Utilizadas

O front-end deste projeto foi construído utilizando as seguintes tecnologias:

-   **HTML5:** Para a estrutura semântica do conteúdo.
-   **CSS3:** Para a estilização, utilizando Flexbox para um layout moderno.
-   **JavaScript (Vanilla):** Para toda a interatividade, manipulação do DOM e validação de dados, sem a necessidade de frameworks externos.

## 🔧 Como Executar o Projeto (Front-end)

Atualmente, o projeto é apenas front-end, então não requer um servidor complexo para ser executado.

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    ```
2.  **Navegue até a pasta do projeto:**
    ```bash
    cd seu-repositorio
    ```
3.  **Abra o arquivo principal:**
    -   Simplesmente abra o arquivo `index.html` no seu navegador de preferência.
    -   **(Recomendado)** Se você usa o Visual Studio Code, instale a extensão [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) e clique em "Go Live" no canto inferior direito para iniciar um servidor de desenvolvimento local.

## 🛣️ Próximos Passos (Roadmap)

A fase atual compreende apenas a interface do usuário. Os próximos passos para tornar este um projeto completo são:

-   [ ] **Desenvolvimento do Backend:** Criar uma API utilizando **Python** e o micro-framework **Flask**.
-   [ ] **Integração com Banco de Dados:** Substituir os dados estáticos por um banco de dados (provavelmente SQLite para começar) para persistir as informações.
-   [ ] **Criação de Endpoints:** Desenvolver as rotas da API para:
    -   `GET /equipamentos`: Listar todos os equipamentos.
    -   `POST /equipamentos`: Salvar um novo equipamento.
    -   `PUT /equipamentos/<id>`: Editar um equipamento existente.
    -   `DELETE /equipamentos/<id>`: Remover um equipamento.
-   [ ] **Conexão Front-end e Backend:** Fazer com que o JavaScript se comunique com a API para carregar e salvar os dados de verdade.

## 👤 Autor

-   **[Seu Nome Completo]**
-   **GitHub:** `[link para o seu perfil do GitHub]`
-   **LinkedIn:** `[link para o seu perfil do LinkedIn]`

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

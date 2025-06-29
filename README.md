
# Projeto - TechSistem

## Instruções de Instalação do Backend:

1. **Instale o Docker**  
   Baixe e instale o [Docker Desktop](https://www.docker.com/products/docker-desktop) ou a versão tradicional do Docker, dependendo do seu sistema operacional.

2. **Clone o repositório**  
   Clone o repositório para o seu computador com o seguinte comando:

   ```bash
   git clone https://github.com/BigHobbit1/Seminario-C214
   ```

3. **Acesse a pasta do projeto**  
   Abra o terminal e navegue até a pasta do projeto com o comando:

   ```bash
   cd Seminario-C214
   ```

4. **Construa a imagem Docker**  
   Execute o comando para construir as imagens necessárias:

   ```bash
   docker-compose build
   ```

5. **Suba os containers**  
   Após a construção, inicie os containers com o comando:

   ```bash
   docker-compose up -d
   ```

6. **Acesse a API**  
   Agora, a API estará funcionando. Acesse a documentação da API através do seguinte link:  
   [http://localhost:8000/docs](http://localhost:8000/docs)

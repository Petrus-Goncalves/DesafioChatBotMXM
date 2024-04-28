# ChatBot: Leitor de PDF's

## Introdução
------------
O aplicativo 'ChatBot: Leitor de PDF's' é uma aplicação Python que permite conversar com vários documentos PDF. Você pode fazer perguntas sobre o conteúdo contido nos PDFs e, usando linguagem natural, o aplicativo fornecerá respostas com base nos documentos fornecidos. Este aplicativo utiliza um modelo de linguagem natural para gerar respostas precisas para as perguntas fornecidas. 
Obs: note que o aplicativo só responderá à perguntas relacionadas aos PDFs carregados.

## Funcionamento
------------
O aplicativo segue estes passos para fornecer as respostas:

1. Carregamento dos arquivos PDFs: O aplicativo faz a leitura de documentos PDF e extrai o seu conteúdo de texto.

2. Fragmentação de Texto: O texto extraído é dividido em partes menores que podem ser processadas de forma mais eficaz pelo modelo de linguagem.

3. Modelo de Linguagem: O aplicativo utiliza um modelo de linguagem para gerar representações vetoriais (embeddings) das partes fragmentadas do texto.

4. Correspondência de Similaridade: Quando você faz uma pergunta, o modelo de linguagem transforma sua pergunta em uma base vetorial e à compara com o banco de dados vetoriais gerados no passo '3'. E assim, identifica os fragmentos que mais possuam uma similaridade semântica.

5. Geração de Resposta: As partes selecionadas são passadas para o modelo de linguagem, que gera uma resposta com base no conteúdo previamente carregados dos PDFs.

## Dependências e Instalações
------------
Para instalar o aplicativo ChatBot: Leitor de PDF's, siga estes passos:

1. Clone este repositório para sua máquina local.

2. Instale as dependências necessárias executando o seguinte comando:
   ```
      pip install -r requirements.txt
   ```

3. Obtenha uma chave de API da OpenAI e adicione-a ao arquivo .env no diretório do projeto.
   ```
      OPENAI_API_KEY = sua_chave_de_api
   ```

## Utilização
------------
Para utilização do "ChatBot: Leitor de PDF's", siga os passos abaixo:

1. Certifique-se de ter instalado as dependências necessárias e adicionado a chave de API da OpenAI ao arquivo .env.

2. Execute o arquivo main.py usando o CLI do Streamlit com o comando:
   ```
      streamlit run app.py
   ```

3. O aplicativo será iniciado em seu navegador padrão, exibindo a interface do usuário.

4. Carregue os documentos PDF no aplicativo seguindo as instruções fornecidas na própria página.

5. Faça perguntas sobre os PDFs carregados usando o chat.

## Declarações Finais
------------
Este repositório destina-se à elaboração de um desafio proposto pela empresa MXM-Sistemas, o qual consiste na criação de um chatbot que seja direcionado à arquivos PDF's previamente carregados. Assim, gerando suas respostas restritas a esse banco de dados.
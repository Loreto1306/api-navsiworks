Esta API foi desenvolvida em Python utilizando Flask com o objetivo de automatizar o processo de criação de Reviews no Autodesk Navisworks, a partir de dados estruturados enviados por um servidor PHP. O sistema estabelece uma integração entre uma aplicação web (PHP) e o ambiente desktop do Navisworks por meio de automação com bibliotecas nativas da Autodesk (controls.dll, api.dll).

⚙️ Como Funciona
Requisição Inicial (PHP ➜ API Python):
Um script em PHP realiza uma requisição GET para verificar se a API Flask está ativa e pronta para receber dados.

Envio de Dados (PHP ➜ Python):
Após a confirmação, o PHP envia um payload em JSON contendo informações para a criação de um review, como caminho dos arquivos .nwd, título do review, observações e demais metadados necessários.

Execução da Automação (Python ➜ Navisworks):
O script Python (api-call.py) processa os dados recebidos e utiliza a API de automação do Navisworks (via controls.dll e api.dll) para abrir os arquivos .nwd, gerar os reviews desejados e compilar os resultados conforme solicitado.

Resposta ao Servidor (Python ➜ PHP):
Ao final do processo, a API retorna um JSON para o servidor PHP com a confirmação da execução ou, em caso de erro, detalhes sobre a falha.

📁 Estrutura dos Arquivos
client.php – Script PHP responsável por iniciar a comunicação com a API Python e enviar os dados de review.

api-call.py – Responsável por receber os dados JSON, processar a automação no Navisworks e retornar o resultado.

app.py – API Flask que expõe os endpoints necessários para comunicação entre PHP e Python/Navisworks.

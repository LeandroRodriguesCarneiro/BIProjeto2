# BIProjeto2
## Configurando ambiente virtual
Inicialmente é necessário criar o ambiente virtual. Para criá-lo, basta usar o seguinte comando.

- No Linux, utilizando o bash:

Para criar o ambiente virtual:

    python3 -m venv myenv

Para iniciar o ambiente virtual:

    source myenv/bin/activate
    
- No Windows, utilizando o PowerShell:

Para criar o ambiente virtual:

    python -m venv venv

Para iniciar o ambiente virtual:

    venv/Scripts/activate.ps1

Utilize o comando para instalar as bibliotecas necessárias do projeto após iniciar o ambiente virtual.

    pip install -r requirements.txt

Observação: pode ser necessário utilizar outros comandos para criar o ambiente virtual. Se ocorrer algum problema, favor pesquisar como configurar a máquina para uso dos ambientes virtuais do Python.

Basta utilizar o seguinte comando para iniciar o projeto:

    python manage.py runserver
# 🚀 JWT HTML5 Login Page

Este projeto é uma **tela de login** desenvolvida em **HTML5**, **CSS**, e **JavaScript**, com uma API **backend** implementada em **Python** usando **Flask** e **JWT** para autenticação.

## 🛠️ Funcionalidades

- **Tela de Login**: Interface estilizada com HTML5, CSS e JavaScript.
- **Autenticação JWT**: API em Flask que autentica usuários e gera tokens JWT.
- **CORS**: Suporte para chamadas de API cross-origin.

## 🌐 Como Funciona

1. **Frontend**: A tela de login é construída com HTML5 e estilizada com CSS. A interação com o backend é realizada via JavaScript.
2. **Backend**: A API em Flask processa as credenciais de login e gera um token JWT válido por 1 hora se as credenciais forem corretas.

## 📁 Estrutura do Projeto

- **`index.html`**: Página de login com HTML5, CSS e JavaScript.
- **`app.py`**: Código Python para o backend Flask que autentica usuários e gera tokens JWT.
- **`login.json`**: Dados de login para autenticação (usuário e senha).
  
### Código do Backend

```python
# app.py
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import jwt
import datetime
import json

app = Flask(__name__)
CORS(app)

# Chave secreta para JWT
SECRET_KEY = '123'

# Dados de login (para fins de exemplo, use um banco de dados real em produção)
with open('login.json', 'r') as file:
    login_data = json.load(file)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username == login_data['username'] and password == login_data['password']:
        token = jwt.encode({
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1),
            'iat': datetime.datetime.utcnow()
        }, SECRET_KEY, algorithm='HS256')
        return jsonify({'token': token})
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('', path)

if __name__ == '__main__':
    app.run(debug=True)
```

## 📸 Imagens do Projeto

### 🖼️ Tela de Login
![Tela de Login](https://github.com/evolucaoit/JWT_HTML5_Login_page/blob/main/chrome_vsXtrPuksc.png?raw=true)
*A visualização completa da tela de login do projeto.*

### ✔️ Mensagem de Sucesso
![Mensagem de Sucesso](https://github.com/evolucaoit/JWT_HTML5_Login_page/blob/main/chrome_qrgjZYXB1H.png?raw=true)
*Mensagem exibida após um login bem-sucedido.*

### 📷 Print da Tela de Login
![Print da Tela de Login](https://github.com/evolucaoit/JWT_HTML5_Login_page/blob/main/chrome_wtMdGygxcb.png?raw=true)
*Um print detalhado da tela de login.*

## 🔗 Links Úteis

### 🌐 Portfólio
[Evolução IT](https://github.com/evolucaoit)
*Explore mais projetos e detalhes sobre o portfólio.*

### 🛠️ Outro Repositório
[Chaos4455](https://github.com/chaos4455)
*Confira outros repositórios e projetos.*

### 💼 LinkedIn
[Elias Andrade](https://br.linkedin.com/in/itilmgf)
*Conecte-se no LinkedIn para mais informações e networking.*


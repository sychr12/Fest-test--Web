# FesttestWeb



---
## 📡 Descrição do Projeto

Este é um aplicativo web que realiza testes de velocidade da internet, medindo:

* Velocidade de **download** (em Mbps)
* Velocidade de **upload** (em Mbps)
* **Latência** (ping, em ms)

O aplicativo foi desenvolvido com:

* **Frontend**: HTML5, CSS3 e JavaScript
* **Backend**: Python com Flask
* **Biblioteca de teste de velocidade**: `speedtest-cli`

---

## ⚙️ Funcionalidades

1. **Teste de Velocidade Automático**: O teste é executado automaticamente ao carregar a página.
2. **Visualização Gráfica**:

   * Barras animadas para download e upload
   * Barra de progresso para ping
3. **Repetição de Teste**: Botão para repetir o teste manualmente.
4. **Design Responsivo**: Layout que se adapta a diferentes tamanhos de tela.
5. **Feedback Visual**:

   * Animações durante o teste
   * Cores que indicam o status da conexão

---

## ▶️ Como Executar o Projeto

### Pré-requisitos

* Python 3.x instalado
* Pip (gerenciador de pacotes do Python)

### Instalação

1. Clone o repositório:

   ```bash
   git clone [URL_DO_REPOSITORIO]
   cd [NOME_DO_DIRETORIO]
   ```

2. Instale as dependências:

   ```bash
   pip install flask speedtest-cli
   ```

3. Execute o aplicativo:

   ```bash
   python app.py
   ```

4. Acesse no navegador:

   ```
   http://localhost:5000
   ```

---

## 📁 Estrutura de Arquivos

* `app.py`: Contém a lógica do servidor Flask e a integração com a biblioteca `speedtest-cli`.
* `templates/index.html`: Página HTML principal com a interface do usuário.
* `static/style.css`: Estilos CSS da aplicação.

---

## 🎨 Personalização

Você pode personalizar:

* **Cores**: Altere os códigos hexadecimais no arquivo CSS.
* **Velocidade Máxima**: Modifique o valor `150` no JavaScript para ajustar a escala das barras.
* **Tempo de Animação**: Edite as durações no CSS.

---

## 🚀 Possíveis Melhorias

1. Adicionar histórico de testes
2. Implementar gráficos de tendência
3. Suportar múltiplos servidores de teste
4. Incluir comparação com médias regionais
5. Adicionar modo claro/escuro

---

## ⚠️ Limitações

* O teste pode ser afetado por outros dispositivos/processos na rede
* A precisão depende da qualidade da conexão com os servidores do `speedtest`
* Em conexões muito rápidas (>150 Mbps), as barras podem ultrapassar o limite visual

---

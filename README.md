# FesttestWeb - Teste de Velocidade de Internet Completo

![Captura de Tela do FesttestWeb](https://via.placeholder.com/800x500/48eb91/ffffff?text=FesttestWeb+Speed+Test) *(Exemplo de imagem - substitua pela real)*

## 🌐 Visão Geral

O FesttestWeb é uma ferramenta avançada para teste de velocidade de internet que oferece métricas precisas e visualização intuitiva. Desenvolvido com tecnologias modernas, ele permite:

- Testes completos de download/upload
- Análise de latência e qualidade de conexão
- Seleção de servidores específicos
- Visualização gráfica dos resultados

## 🛠 Tecnologias Utilizadas

### Frontend
- **HTML5** (Estrutura semântica)
- **CSS3** (Design responsivo com Flexbox/Grid)
- **JavaScript** (Lógica e interações)
- **Chart.js** (Visualização de dados)
- **Font Awesome** (Ícones)

### Backend
- **Python** (Lógica do servidor)
- **Flask** (Framework web)
- **Speedtest-CLI** (Medições de velocidade)
- **Ping3** (Análise de latência)

## ⚡ Funcionalidades Principais

1. **Teste Completo de Velocidade**
   - Download (Mbps)
   - Upload (Mbps)
   - Ping/Latência (ms)
   - Jitter (variação de latência)
   - CPING (ping personalizado)

2. **Seleção de Servidores**
   ```mermaid
   graph TD
   A[Servidor Automático] --> B[Otimização]
   B --> C[Melhor Performance]
   D[Servidor Manual] --> E[Teste Específico]
   ```

3. **Visualização Interativa**
   - Barras animadas de download/upload
   - Gráfico de ping escalável
   - Cores indicativas de qualidade

4. **Informações de Rede**
   - Detecção automática de IP
   - Identificação do provedor (ISP)
   - Localização aproximada

## 🖥 Como Executar

### Pré-requisitos
- Python 3.8+
- Pip instalado
- Conexão com internet

### Instalação
```bash
git clone https://github.com/seu-usuario/festtestweb.git
cd festtestweb
pip install -r requirements.txt
```

### Execução
```bash
python app.py
```

Acesse no navegador: `http://localhost:5000`

## 📊 Métricas Medidas

| Métrica       | Descrição                          | Valores Ideais       |
|---------------|------------------------------------|----------------------|
| Download      | Velocidade de recebimento de dados | >50 Mbps (residencial) |
| Upload        | Velocidade de envio de dados       | >20 Mbps (residencial) |
| Ping          | Tempo de resposta                  | <30 ms (ótimo)       |
| Jitter        | Variação do ping                   | <5 ms (estável)      |
| CPING         | Ping customizado para Google       | <20 ms               |

## 🎨 Design e Interface

![Diagrama de Interface](https://via.placeholder.com/600x400/10b981/ffffff?text=UI+Design)

- **Cores Principais**:
  - Verde (`#48eb91`) para conexões boas
  - Amarelo para conexões regulares
  - Vermelho para conexões ruins

- **Elementos Interativos**:
  - Barras de progresso animadas
  - Botão de repetição de teste
  - Seleção de servidores

## 🌟 Recursos Avançados

1. **Multi-Servidor**
   - Lista de servidores brasileiros pré-configurados:
     - Claro, Vivo, TIM, Oi
     - Algar Telecom, Sercomtel
     - Provedores regionais

2. **Análise de Jitter**
   - 10 medições consecutivas de ping
   - Cálculo da variação média

3. **Detecção de Localização**
   - Integração com IP-API.com
   - Exibe cidade, país e provedor

## 📂 Estrutura de Arquivos

```
festtestweb/
├── app.py              # Lógica principal do servidor
├── templates/
│   └── index.html      # Página web principal
├── static/
│   └── style.css       # Estilos CSS
├── requirements.txt    # Dependências
└── README.md           # Documentação
```

## 🚀 Melhorias Futuras

- [ ] Histórico de testes
- [ ] Comparação com médias regionais
- [ ] Exportação de resultados (PDF/CSV)
- [ ] Modo escuro/claro
- [ ] Teste de estabilidade prolongada

## 📝 Licença

Este projeto está licenciado sob a licença MIT - consulte o arquivo [LICENSE](LICENSE) para detalhes.

---

**Desenvolvido por**: Luiz Felipe  
**Contato**: exemplo@email.com  
**Versão**: 1.0.0

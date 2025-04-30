# Tradutor Automático PT ↔ EN

Este é um projeto de **tradução automática** entre **Português (PT)** e **Inglês (EN)** utilizando modelos pré-treinados da **Hugging Face** e uma interface web simples com **Gradio**.

O projeto utiliza os modelos da Hugging Face, como o `Helsinki-NLP/opus-mt-en-ROMANCE` para tradução de **Inglês para Português** e `Helsinki-NLP/opus-mt-ROMANCE-en` para tradução de **Português para Inglês**.

## 🔥 Funcionalidades

- Tradução automática de **textos** entre **Português e Inglês**.
- Interface web simples e interativa utilizando o **Gradio**.
- Backend utilizando o **Transformers** da Hugging Face para tradução.

## 📋 Como Rodar o Projeto Localmente

### 1. **Clonando o Repositório**

Primeiro, clone o repositório para sua máquina local:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

# 2. Configurar o Ambiente Virtual 
Para garantir que as dependências do projeto sejam instaladas corretamente, crie um ambiente virtual. 
Para sistemas baseados em Unix (Linux/macOS): 
```bash
python3 -m venv venv
source venv/bin/activate

Para Windows: 
python -m venv venv
venv\Scripts\activate
```

# 3. Instalar Dependências 
Após ativar o ambiente virtual, instale as dependências necessárias: 
pip install -r requirements.txt

O arquivo requirements.txt inclui as seguintes dependências principais: * gradio: Para construir a interface web interativa. *
transformers: Para carregar os modelos de tradução da Hugging Face. * torch: Para rodar os modelos de tradução (necessário para a
biblioteca transformers). 

# 4. Rodar o Servidor Local 
Com as dependências instaladas, basta rodar o arquivo app.py para iniciar a interface web: 
python app.py

Isso iniciará o servidor localmente, e você verá um link na saída do terminal, que pode ser acessado no seu navegador. 
# 5. Acessando a Interface Web 
Depois de rodar o comando acima, abra o navegador e acesse o seguinte link: 
http://127.0.0.1:7860

Agora, você pode digitar um texto em Português ou Inglês e selecionar o idioma de origem e destino para ver a tradução em tempo
real! 

## 🚀 Como Funciona 
# Backend (Lógica de Tradução) 
O backend usa a biblioteca Transformers da Hugging Face para carregar os modelos de tradução: * Helsinki-NLP/opus-mt-en
ROMANCE: Tradução de Inglês para Português. * Helsinki-NLP/opus-mt-ROMANCE-en: Tradução de Português para Inglês. 
A entrada do texto é tokenizada e passada para o modelo de tradução, que gera a tradução do texto conforme o par de idiomas
selecionado. 

# Interface Web (Frontend) 
Gradio é utilizado para criar uma interface web simples onde o usuário pode digitar o texto a ser traduzido e selecionar os idiomas de
origem e destino. 
O resultado da tradução é exibido em tempo real na própria interface web. 

# ⚙️ Tecnologias Usadas 

Python 3.x
Gradio (para construir a interface web)
Hugging Face Transformers (para carregar os modelos de tradução)
PyTorch (para rodar os modelos de tradução)
Helsinki-NLP/opus-mt (modelos pré-treinados de tradução automática)🌍 Deploy Gratuito 
Você pode rodar este projeto localmente ou fazer o deploy para plataformas gratuitas como: * Hugging Face Spaces: Hospedagem
rápida e fácil de modelos e interfaces. * Google Colab: Para protótipos rápidos. * Replit: Para rodar e compartilhar o código em
tempo real.

# 🚧 Roadmap 
Adicionar suporte a mais idiomas.
Melhorar a interface com mais opções de customização.
Otimizar o tempo de resposta da tradução.
Implementar suporte para tradução de múltiplos idiomas ao mesmo tempo. 

# 💡 Contribuições 
Sinta-se à vontade para contribuir com o projeto! Caso tenha sugestões de melhorias ou queira adicionar novas funcionalidades,
basta abrir uma issue ou enviar um pull request. 

# 🔗 Links Úteis 
Transformers: https://huggingface.co/transformers/
Gradio: https://gradio.app/
Helsinki-NLP Models: https://huggingface.co/models
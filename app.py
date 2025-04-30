import gradio as gr
from transformers import MarianMTModel, MarianTokenizer

# Modelos substitutos atualizados
MODEL_MAP = {
    ("Português", "Inglês"): ("Helsinki-NLP/opus-mt-ROMANCE-en", ">>en<<"),
    ("Inglês", "Português"): ("Helsinki-NLP/opus-mt-en-ROMANCE", ">>pt<<")
}

# Função de tradução
def traduzir(texto, idioma_origem, idioma_destino):
    if idioma_origem == idioma_destino:
        return texto  # Sem tradução

    config = MODEL_MAP.get((idioma_origem, idioma_destino))
    if not config:
        return "Tradução não suportada."

    model_name, lang_token = config
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    # Adiciona o token do idioma de destino ao texto
    texto = f"{lang_token} {texto}"
    tokens = tokenizer(texto, return_tensors="pt", padding=True, truncation=True)
    translated = model.generate(**tokens)
    return tokenizer.decode(translated[0], skip_special_tokens=True)

# Interface Gradio
iface = gr.Interface(
    fn=traduzir,
    inputs=[
        gr.Textbox(label="Texto para traduzir", lines=5, placeholder="Digite aqui..."),
        gr.Dropdown(choices=["Português", "Inglês"], label="Idioma de origem", value="Português"),
        gr.Dropdown(choices=["Português", "Inglês"], label="Idioma de destino", value="Inglês")
    ],
    outputs=gr.Textbox(label="Tradução"),
    title="Tradutor Automático PT ↔ EN",
    description="Traduz textos automaticamente entre Português e Inglês usando modelos atualizados da Hugging Face 🤖"
)

# Executa a interface
if __name__ == "__main__":
    iface.launch()

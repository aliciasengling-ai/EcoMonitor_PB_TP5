from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

MODELO = "google/flan-t5-small"

print("Carregando modelo de inteligencia artificial...")

tokenizer = AutoTokenizer.from_pretrained(MODELO)
model = AutoModelForSeq2SeqLM.from_pretrained(MODELO)

model.eval()

texto = """
Renewable energy helps reduce greenhouse gas emissions.
Solar and wind energy are important alternatives to fossil fuels.
These technologies contribute to environmental sustainability.
"""

prompt = "Summarize the following text: " + texto

inputs = tokenizer(
    prompt,
    return_tensors="pt",
    truncation=True,
    max_length=512
)

with torch.inference_mode():
    outputs = model.generate(
        **inputs,
        max_new_tokens=100
    )

resultado = tokenizer.decode(
    outputs[0],
    skip_special_tokens=True
)

print("\nModelo carregado com sucesso!")
print("\nTexto original:")
print(texto)
print("\nResumo gerado pela IA:")
print(resultado)
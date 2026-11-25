import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from functools import lru_cache

MODELO = "google/flan-t5-small"


@lru_cache(maxsize=1)
def carregar_modelo():
    tokenizer = AutoTokenizer.from_pretrained(
        MODELO,
        local_files_only=True
    )

    model = AutoModelForSeq2SeqLM.from_pretrained(
        MODELO,
        local_files_only=True
    )

    model.eval()

    return tokenizer, model


def processar_texto(texto):
    tokenizer, model = carregar_modelo()

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
            max_new_tokens=100,
            max_time=30,
            num_beams=4
        )

    resultado = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return resultado
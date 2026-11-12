"""1. adım: Claude ile bölüm senaryosu üretir (bolum.json).

Kullanım:  python senaryo.py "konu" [cikti.json]
ANTHROPIC_API_KEY (veya `ant auth login`) gerekir. Anahtar yoksa hazır bolum.json kullanılır.
"""
import json
import sys

import anthropic
from pydantic import BaseModel


class Bolum(BaseModel):
    baslik: str
    sunucu: str
    cumleler: list[str]


SISTEM = (
    "Sen 'Tuhaf Ama Gerçek' adlı Türkçe video podcast'in yazarısın. Sunucu Defne, kurgusal bir "
    "yapay zekâ karakteri; sıcak, meraklı ve esprili konuşur. Sadece doğrulanabilir gerçekleri kullan, "
    "emin olmadığın ayrıntıyı yazma. 8-12 kısa, konuşma dilinde cümle yaz (toplam ~45-60 sn). "
    "İlk cümle selam ve program adı, ikincisi şaşırtıcı kanca, sonra hikâye, bir 'Peki ama nasıl?' "
    "anı, gündelik bir benzetmeyle açıklama ve kısa bir kapanış. Sağlık, hukuk, finans tavsiyesi verme."
)


def main() -> None:
    konu = sys.argv[1] if len(sys.argv) > 1 else "Londra'da araba eriten gökdelen (2013)"
    cikti = sys.argv[2] if len(sys.argv) > 2 else "bolum.json"
    client = anthropic.Anthropic()
    response = client.beta.messages.parse(
        model="claude-opus-5-5",
        max_tokens=16000,
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
        output_config={"effort": "medium"},
        system=SISTEM,
        messages=[{"role": "user", "content": f"Konu: {konu}"}],
        output_format=Bolum,
    )
    if response.stop_reason == "refusal":
        sys.exit("Model bu konuyu yazmayı reddetti; başka bir konu deneyin.")
    bolum = response.parsed_output
    with open(cikti, "w", encoding="utf-8") as f:
        json.dump(bolum.model_dump(), f, ensure_ascii=False, indent=2)
    print(f"{cikti} yazıldı: {len(bolum.cumleler)} cümle")


if __name__ == "__main__":
    main()

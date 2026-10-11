# Ses Niteliklerini Kodlayan Bir Yazılım Sistemi

Bu depo, yazıya ses performansını kodlayacak minimalist bir prototip ve notasyon sistemine odaklanır.

Amaç:
- metin üzerinde konuşma dinamiğini yazılı olarak göstermek
- ses şiddeti, perde, süre ve konuşma biçimini ayrı işaretlerle ifade etmek
- metni hem insan için okunabilir hem de bilgisayar için ayrıştırılabilir tutmak

## Ana fikir

Geleneksel metin yalnızca sözcükleri ifade eder. Bu sistem, yazının yanında şu bilgileri de saklar:

- ses şiddeti: çok düşük, normal, yüksek, bağırma, çığlık
- perde / tona: düşük, orta, yüksek, nota bazlı ifade
- süre: normal, uzatılmış, çok uzatılmış
- konuşma modu: normal, fısıltı, sessiz dudak hareketi, bağırma

## Temel notasyon ilkeleri

- yatay çizgi: temel metin satırı
- dikey çizgiler: ses şiddeti ve perde yönü
- sessiz dudak hareketi: başında ve sonunda yukarı yönlü işaret
- uzatma: harf/hece/kelime üzerinde gösterilir
- dalgalı uzatma: ~ sembolüyle gösterilir

## Notasyon örneği

```text
Ahmet, neredesin?
  │   │
  v=5 v=7
  p=C4 p=D4
  t=600ms t=800ms
```

Bu örnek, metnin içinde konuşma performansını tanımlayan bir kodlama biçiminin basit sürümünü gösterir.

## Repo içeriği

- `notation_system.py`: notasyon modelini ve işaretleme kurallarını tanımlar
- `editor.py`: örnek editör arayüzü ve tuş kontrolü
- `sample_text.txt`: örnek metin
- `example.json`: örnek veri modeli
- `requirements.txt`: bağımlılıklar

## Çalıştırma

```bash
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
# veya .venv\Scripts\activate  # Windows
pip install -r requirements.txt
python editor.py
```

## Not

Bu repo, üretim düzeyinde tam bir TTS sistemi değildir; ilk uygulanabilir prototip ve notasyon sistemi tasarımına odaklanır.

Amaç, yazı ile konuşma performansını eşleştiren bir editör ve kodlama modelini somutlaştırmaktır.

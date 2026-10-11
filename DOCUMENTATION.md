# Ses Niteliklerini Kodlayan Bir Yazılım Sistemi

Bu belge, sistemin temel tasarım ve kullanım kuralını açık şekilde anlatır. Amaç, yazının yanında konuşma performansını da tanımlayan bir notasyon mekanizması kurmaktır.

## 1. Amaç

Geleneksel metin, sadece dilsel içeriği taşır. Bu sistem ise metnin yanında şu bilgileri de taşır:

- ses şiddeti
- ses perdesi / tonu
- süre / uzatma
- konuşma biçimi
- sessiz dudak hareketi

Bu sayede metin, yalnızca insanlar için değil, bilgisayarlar için de doğrudan işlenebilir bir performans tanımı haline gelir.

## 2. Temel ilke

Metin ve performans ayrıdır:

- metin = dilsel içerik
- performans = konuşma davranışı

Bu ayrım, aynı sözcüğün farklı seslendirme biçimlerine izin verir.

## 3. Notasyon sistemi

### 3.1 Temel satır

Yazı metni, yatay temel çizgi üzerinde yazılır.

```text
Ahmet, neredesin?
-------------------
```

Bu çizgi, metnin ana satırını temsil eder.

### 3.2 Ses şiddeti

Ses şiddeti, metnin üzerinde veya altında yer alan dikey çizgilerle gösterilir.

- tek dikey çizgi = çok düşük / fısıltı
- iki dikey çizgi = düşük / duyulabilir normal seviye
- üç çizgi = orta düşük
- dört çizgi = orta
- beş çizgi = yüksek
- altı çizgi = çok yüksek / bağırma
- yedi çizgi = çığlık / en yüksek şiddet

Örnek:

```text
Ahmet
  |||||
```

Bu örnek, kelimenin orta-üst şiddetli şekilde söylenmesini ifade eder.

### 3.3 Ses tonu / perde

Aynı kelimenin altına veya üstüne eklenen aşağı yönlü dikey çizgiler, tonu temsil eder.

- düşüş = alçak ton
- yükseliş = yüksek ton
- 7 farklı seviye

Örnek:

```text
Ahmet
  ||||
  ||||
```

Bu, sesin daha yüksek bir ton aralığına sahip olduğunu gösterir.

### 3.4 Sessiz dudak hareketi

Eğer metin sesi duyulmadan dudak hareketiyle çekilecekse:

- kelimenin başı ve sonu, yukarı yönlü işaretle çevrelenir

Örnek:

```text
↑ Ahmet ↓
```

Bu gösterim, işitilebilir konuşma yoksa fakat dudak hareketi var demektir.

### 3.5 Uzatma

Uzatma, kelime veya hece üzerine eklenen işaretlerle gösterilir.

- tek çizgi = normal uzatma (yaklaşık 2 kat)
- tek çizgi + tek nokta = daha uzun uzatma
- tek çizgi + iki nokta = daha uzun
- tek çizgi + tek nokta + iki nokta = maksimum tanımlı uzatma

Örnek:

```text
Aaaahmet
     .
```

 veya çok daha sade biçim:

```text
Ahmet—
```

### 3.6 Dalgalı uzatma

Daha fazla ve düzensiz uzatma için `~` sembolü kullanılır.

Örnek:

```text
A~hmet
```

Bu, okuyucuya göre esnek ve doğal bir uzatma çizgisi oluşturur.

## 4. Kullanım örnekleri

### 4.1 Normal konuşma

```text
Ahmet, neredesin?
-------------------
```

### 4.2 Yüksek ses / bağırma

```text
Ahmet, neredesin?
||||||| 
```

### 4.3 Fısıltı

```text
↑ Ahmet ↓
```

### 4.4 Uzatılmış konuşma

```text
Ahmet----
```

### 4.5 Sessiz dudak hareketi

```text
↑ Neredesin ↓
```

## 5. Veri modeli

Her kelime/parça için şu alanlar kullanılabilir:

```json
{
  "text": "Ahmet",
  "volume": 5,
  "pitch": "C4",
  "duration_ms": 600,
  "mode": "normal",
  "extension": 1,
  "silent_lip": false
}
```

Bu yapı, yazıdan ses üretimi için yeterli bir veri taşıyıcısıdır.

## 6. Uygulama fikri

Bu sistemin ilk versiyonu doğrudan bir editör olarak düşünülür:

- metni yaz
- seçili kelimeyi işaretle
- tuşlarla ses şiddetini ve tonunu ayarla
- işaretler otomatik eklenir
- çıktı PDF veya JSON olarak saklanır

## 7. Hedef

Bu sistemin asıl hedefi şudur:

- yazının insanlar için okunabilirliği korunur
- sessizlik, yükselme, düşüş, fısıltı, bağırma ve uzatma ayrıntıları açık biçimde yazıya aktarılır
- bilgisayar bunları ayrıştırabilir ve gerektiğinde ses üretimi için kullanabilir

## 8. Sonuç

Bu belge, ses performansını metin içinde kodlayan minimalist ve uygulanabilir bir gösterim yaklaşımı tanımlar. Tasarım, metnin insan okuruna anlaşılır kalmasını hedeflerken, aynı zamanda bilgisayar tarafından işlenebilir bir veri yapısı üretebilir.

Bu notasyon sistemi, daha sonra metinden sese çevirme ya da sesli konuşma için işlenebilir bir kodlama katmanı haline getirilebilir.


# 🤖 Chatbot AI SMK - Flask + OpenRouter + Bootstrap

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-lightgrey?logo=flask)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Development-yellow)

Chatbot ini adalah proyek pembelajaran **Kecerdasan Artifisial (AI)** untuk siswa **SMK**, dibangun menggunakan framework **Flask**, dengan integrasi model **LLM** dari **OpenRouter**. Antarmuka dirancang seperti **ChatGPT**, lengkap dengan bubble chat, highlight kode, dan dukungan rumus matematika.

---

## ✨ Fitur

- 🧠 Chat dengan model LLM seperti `gpt-4o`, `mistral`, dll melalui OpenRouter API
- 💬 Antarmuka real-time dengan Bootstrap (tampilan mirip ChatGPT)
- 🔍 Highlight otomatis untuk kode Python, HTML, dsb (Prism.js)
- 📐 Mendukung rumus matematika via MathJax
- 📱 Responsif di perangkat mobile & desktop
- 🎓 Cocok untuk proyek edukasi SMK/SMA bidang AI dan pemrograman

---

## 📦 Teknologi yang Digunakan

- Python 3.10+
- Flask
- Bootstrap 5
- Prism.js
- MathJax
- OpenRouter API

---

## 🚀 Instalasi

```bash
# 1. Clone repository
git clone https://github.com/username/chatbot-ai-smk.git
cd chatbot-ai-smk

# 2. Buat virtual environment
python -m venv venv
# Aktifkan:
source venv/bin/activate        # Linux / Mac
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install flask requests

# 4. Jalankan aplikasi
python app.py
```

Akses di browser:
```
http://localhost:5000
```

---

## 🔑 Konfigurasi API OpenRouter

1. Daftar ke [https://openrouter.ai/](https://openrouter.ai/)
2. Dapatkan API Key
3. Ganti baris di `app.py`:
```python
OPENROUTER_API_KEY = "sk-or-v1-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

> 💡 Gunakan model gratis seperti `mistralai/mistral-7b-instruct`, atau upgrade jika ingin akses GPT-4o.

---

## 🖼️ Cuplikan Tampilan

| Chat Responsive         | Kode Python Otomatis |
|------------------------|----------------------|
| ![chat-preview](https://i.imgur.com/zGVZfOq.png) | ![code-preview](https://i.imgur.com/OysNN8f.png) |

---

## 🧪 Contoh Pertanyaan yang Bisa Diajukan

- `Buatkan program Python penjumlahan`
- `Apa itu LLM dan bagaimana kerjanya?`
- `Contoh list dan dictionary di Python`
- `Tampilkan rumus luas segitiga`
- `Jelaskan AI di industri pariwisata`

---

## 📁 Struktur Folder

```
chatbot-ai-smk/
├── app.py
├── templates/
│   └── index.html
├── static/          # optional untuk CSS/JS tambahan
├── venv/            # virtual environment
└── README.md
```

---

## 🧑‍🏫 Cocok Digunakan untuk

- Pembelajaran AI dan LLM di SMK
- Demo coding Python interaktif
- Modul integrasi API eksternal (OpenRouter)
- Proyek Ujian atau Uji Kompetensi Keahlian

---

## 📄 Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).  
Silakan digunakan, dikembangkan, atau dimodifikasi untuk keperluan edukasi maupun proyek pribadi.

---

## 🙋‍♂️ Kontributor

Dikembangkan oleh **Azis (guru SMK)** dengan bantuan AI dan komunitas pembelajaran terbuka.  
Terima kasih juga untuk [OpenRouter.ai](https://openrouter.ai/) dan [Prism.js](https://prismjs.com/).

---

## 📬 Kontak

Jika ada pertanyaan, saran, atau ingin berkolaborasi, silakan hubungi melalui GitHub Issues atau email.

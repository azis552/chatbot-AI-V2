🤖 Chatbot AI SMK - Berbasis Flask + OpenRouter + Bootstrap
Chatbot AI ini dibuat untuk membantu siswa SMK berinteraksi dengan model AI berbasis LLM (Large Language Model) menggunakan OpenRouter API. Tampilan dirancang menyerupai ChatGPT, lengkap dengan highlight kode, respons real-time, dan dukungan rumus matematika (MathJax).

✨ Fitur Utama
✅ Antarmuka ala ChatGPT (responsive, clean, mobile-friendly)

🧠 Menggunakan model AI via OpenRouter (seperti GPT-4o, Mistral, Claude)

🧮 Mendukung input/output kode Python dan rumus matematika

⚡ Realtime Chat UI (tanpa reload)

🎓 Siap digunakan untuk pembelajaran AI di SMK/SMA/Umum

📦 Teknologi yang Digunakan
Python Flask

OpenRouter API

Bootstrap 5

Prism.js (highlight sintaks kode)

MathJax (render rumus)

🚀 Instalasi & Menjalankan
Clone repositori ini

bash
Copy
Edit
git clone https://github.com/nama-anda/chatbot-flask-smk.git
cd chatbot-flask-smk
Buat virtual environment dan aktifkan

bash
Copy
Edit
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
Install dependencies

bash
Copy
Edit
pip install flask requests
Jalankan aplikasi

bash
Copy
Edit
python app.py
Akses di browser

arduino
Copy
Edit
http://localhost:5000
🔑 Konfigurasi API OpenRouter
Buka app.py, lalu ganti:

python
Copy
Edit
OPENROUTER_API_KEY = "sk-or-v1-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
dengan API Key kamu dari:
🔗 https://openrouter.ai/

⚠️ Untuk penggunaan gratis, pastikan token masih aktif dan model yang dipilih mendukung free tier.

🖼️ Cuplikan Antarmuka
Tampilan chat mirip ChatGPT:

Bubble kiri-kanan (bot dan user)

Blok kode dengan warna sintaks

Scroll otomatis

Responsif di mobile dan desktop

🧪 Contoh Pertanyaan untuk Dicoba
Buatkan program Python untuk menghitung luas lingkaran

Apa itu LLM dan bagaimana cara kerjanya?

Tampilkan contoh struktur data list di Python

Bagaimana menghitung volume balok?

Tampilkan rumus luas segitiga

📁 Struktur Folder
cpp
Copy
Edit
├── app.py
├── templates/
│   └── index.html
├── static/  (jika kamu ingin tambahkan)
├── venv/
└── README.md


📌 Lisensi
Proyek ini dibuat untuk keperluan edukasi dan pembelajaran. Bebas digunakan untuk SMK/SMA dan pengembangan personal.
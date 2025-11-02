# kdxPOS API (FastAPI)

FastAPI tabanlı backend servisidir. Satış, stok, kullanıcı, rapor ve lisans doğrulama işlemlerini yönetir.

## Kurulum

```bash
cd pos-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

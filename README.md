# kdxPOS Platform

**kdxPOS**, KronosDX tarafından geliştirilen, öncelikle eczaneler için tasarlanmış; daha sonra market, perakende ve farklı sektörlere genişleyebilen modüler bir satış noktası (POS) platformudur.

---

## 🧱 Bileşenler

| Klasör | Açıklama |
|--------|-----------|
| `pos-ui/` | React tabanlı kasiyer ekranı (dokunmatik uyumlu) |
| `pos-api/` | FastAPI backend — satış, stok, kullanıcı işlemleri |
| `gateway/` | Barkod, yazıcı, Ingenico POS, çekmece entegrasyonu |
| `admin-cms/` | Vue + Django tabanlı yönetim paneli |
| `sync-agent/` | Bulut yedekleme ve senkronizasyon ajanı |
| `monitoring/` | Prometheus + Grafana + Alertmanager stack |
| `k3s-manifests/` | k3s ortamında deployment YAML dosyaları |
| `docker/` | Lokal geliştirme / container build ayarları |
| `docs/` | Diyagramlar, API dokümantasyonu, kurulum notları |

---

HP Engage Pro (Rocky Linux)
├── k3s master
│ ├── pos-ui Pod (React / Nginx)
│ ├── pos-api Pod (FastAPI / Python)
│ ├── db Pod (Postgres)
│ ├── gateway Pod (Python)
│ ├── admin-cms Pod (Vue / Django)
│ ├── sync-agent CronJob
│ └── monitoring stack (Prometheus + Grafana + Alertmanager)


## Data Flow
1. Kasiyer barkod okutma → `pos-ui`
2. `pos-ui` → `pos-api` ürün & satış işlemi
3. `pos-api` → `db` kaydı
4. `pos-api` ↔ `gateway` (Ingenico / Yazıcı)
5. Gün sonu → `sync-agent` → Cloud backup
6. `monitoring` stack: pod health, resource usage, error rate


## 🧠 Teknoloji Yığını

- **Frontend:** React (Vite)  
- **Backend:** FastAPI (Python 3.11+)  
- **Database:** PostgreSQL  
- **Container Runtime:** Podman / containerd  
- **Orkestrasyon:** k3s  
- **Monitoring:** Prometheus, Grafana, Alertmanager  
- **OS:** Rocky Linux (RHEL türevi)


🧾 İletişim

KronosDX Dijital & Bilişim Teknolojileri Ltd. Şti.
📍 İstanbul, Türkiye
🌐 https://kronosdx.com
---

## ⚙️ Hızlı Başlangıç

### Backend (pos-api)
```bash
cd pos-api
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

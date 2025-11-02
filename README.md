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

## 🧠 Teknoloji Yığını

- **Frontend:** React (Vite)  
- **Backend:** FastAPI (Python 3.11+)  
- **Database:** PostgreSQL  
- **Container Runtime:** Podman / containerd  
- **Orkestrasyon:** k3s  
- **Monitoring:** Prometheus, Grafana, Alertmanager  
- **OS:** Rocky Linux (RHEL türevi)

---

## ⚙️ Hızlı Başlangıç

### Backend (pos-api)
```bash
cd pos-api
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

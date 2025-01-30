# restaurant-tracking-system
Basic Desktop App Without Database Software Dependency
# Restaurant Takip Sistemi

## Açıklama
Bu, QtPy ile oluşturulmuş basit bir restoran takip sistemidir. Kullanıcıların:
- `fiyatlistesi.txt` dosyasından öğe fiyatlarını güncellemesini,
- Siparişleri `log.txt` dosyasına kaydetmesini,
- Herhangi bir veritabanı bağlantısı olmadan çalışmasını sağlar.

## Özellikler
- **Fiyat Yönetimi:** Fiyatlar `fiyatlistesi.txt` dosyasında saklanır ve kolayca güncellenebilir.
- **Sipariş Kaydı:** Siparişler `log.txt` dosyasına kaydedilir.
- **Hafif:** Veritabanı bağımlılığı yok; tamamen metin dosyaları ile çalışır.

## Kurulum
    
    git clone https://github.com/yourusername/restaurant-tracking-system.git
    cd restaurant-tracking-system
    pip install -r requirements.txt
    

## Kullanım
    
    python mainwindow.py
    

## Dosya Yapısı
    
    restaurant-tracking-system/
    │── fiyatlar.ui
    │── fiyatlar_ui.py
    │── fiyat_listesi/
    │   ├── flist.txt
    │   ├── log.txt
    │── form.ui
    │── form_ui.py
    │── requirements.txt
    │── RestoranTakip.py
    │── RestoranTakip.pyproject
    │── RestoranTakip.pyproject.user
    │── ui_fiyatlar.py
    │── ui_form.py
    


---

# Restaurant Tracking System

## Description
This is a simple restaurant tracking system built with QtPy. It allows users to:
- Update item prices from `fiyatlistesi.txt`
- Log orders into `log.txt`
- Operate without any database connection

## Features
- **Price Management:** Prices are stored in `fiyatlistesi.txt` and can be updated easily.
- **Order Logging:** Orders are recorded in `log.txt` for tracking.
- **Lightweight:** No database dependency; works entirely with text files.

## Installation
    
    git clone https://github.com/yourusername/restaurant-tracking-system.git
    cd restaurant-tracking-system
    pip install -r requirements.txt
    

## Usage
    
    python mainwindow.py
    

## File Structure
    
    restaurant-tracking-system/
    │── fiyatlar.ui
    │── fiyatlar_ui.py
    │── fiyat_listesi/
    │   ├── flist.txt
    │   ├── log.txt
    │── form.ui
    │── form_ui.py
    │── requirements.txt
    │── RestoranTakip.py
    │── RestoranTakip.pyproject
    │── RestoranTakip.pyproject.user
    │── ui_fiyatlar.py
    │── ui_form.py
    

## License
This project is licensed under the GNU General Public License v3. Built using QtPy and intended as a hobby project; it is not meant for serious business use. This application is not officially supported.


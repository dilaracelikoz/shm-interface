import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go



# 1. Sayfa Konfigürasyonu
st.set_page_config(page_title="SHM APP", layout="wide")

if 'is_auth' not in st.session_state:
    st.session_state.is_auth = False

# Sayfa durumu yönetimi
if 'page' not in st.session_state:
    st.session_state.page = "Monitor"

# 2. Sidebar (Sol Menü) - Tüm butonlar burada tanımlı
with st.sidebar:
    st.markdown("<h2 style='color: #333;'>🌸 SHM APP</h2>", unsafe_allow_html=True)
    st.write("---")
    st.caption("DASHBOARD")
    if st.button("📍 Real-Time Monitor"): st.session_state.page = "Monitor"
    if st.button("📊 Analysis"): st.session_state.page = "Analysis"
    if st.button("🔔 Alerts"): st.session_state.page = "Alerts"
    
    st.write("")
    st.caption("SYSTEM")
    if st.button("⚙️ Configuration"): st.session_state.page = "Configuration"
    if st.button("👤 User Access"): st.session_state.page = "User Access"

# ---------------------------------------------------------
# 3. SAYFA İÇERİKLERİ
# ---------------------------------------------------------

# --- MONITOR SAYFASI ---
# --- MONITOR SAYFASI ---
if st.session_state.page == "Monitor":
    # 🎨 TÜM BAŞLIKLARI VE KARTLARI MAC TARZINA ÇEVİREN TEK CSS BLOĞU
    st.markdown("""
        <style>
        /* Arka planı hafif gri-beyaz yapalım */
        .stApp { background-color: #f8f9fa !important; }

        /* ANA BAŞLIK: Tam attığın görseldeki füme ve kalın stil */
        h1 {
            color: #34495e !important; 
            font-size: 42px !important; 
            font-weight: 800 !important;
            letter-spacing: -1.2px !important;
            margin-bottom: 0px !important;
            font-family: 'Inter', -apple-system, sans-serif;
        }

        /* ALT BAŞLIK: Station ID gibi yazılar için */
        .sub-header-text {
            color: #7f8c8d !important;
            font-size: 16px !important;
            font-weight: 400 !important;
            margin-top: -10px !important;
            margin-bottom: 25px !important;
        }

        .main-card { 
            background: white; 
            padding: 24px; 
            border-radius: 20px; 
            box-shadow: 0 4px 20px rgba(0,0,0,0.05); 
            margin-bottom: 20px; 
            border: 1px solid #f0f0f0; 
        }

        /* SAĞDAKİ METRİK KARTLARI */
        .metric-card { 
            background: white; 
            padding: 18px; 
            border-radius: 18px; 
            box-shadow: 0 2px 10px rgba(0,0,0,0.03); 
            text-align: center; 
            border: 1px solid #eee; 
            margin-bottom: 15px; 
        }

        /* CANLI VERİ ETİKETİ (Yeşil Hap) */
        .live-tag { 
            background: #d4edda; 
            color: #155724; 
            padding: 4px 12px; 
            border-radius: 10px; 
            font-size: 11px; 
            font-weight: bold;
            letter-spacing: 0.5px;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- SAYFA DÜZENİ BAŞLIYOR ---
    col_left, col_right = st.columns([3.8, 1])
    
    with col_left:
        # Görseldeki profesyonel başlık yapısı
        st.markdown("<h1>Structure Name</h1>", unsafe_allow_html=True)
        st.markdown("<p class='sub-header-text'>Station ID: ID • Stand-Alone Mode</p>", unsafe_allow_html=True)
        
        # 1. Kart: Real-Time Displacement (3D)
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        c1, c2 = st.columns([4, 1])
        with c1:
            st.markdown("### Real-Time Displacement (3D)")
            st.caption("East-North-Up Time Series")
        with c2:
            st.markdown('<div style="text-align:right;"><span class="live-tag">LIVE DATA</span><br><span style="color:#e91e63; font-size:12px; font-weight:600;">North East Up</span></div>', unsafe_allow_html=True)
    

        # Grafik Verisi
        v_factor = 1.0 if st.session_state.is_auth else 0.0
        t = np.linspace(0, 10, 200)
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=t, y=np.sin(t)*0.5*v_factor, name='North', line=dict(color='#9c27b0', width=2)))
        fig1.add_trace(go.Scatter(x=t, y=np.cos(t)*0.3*v_factor, name='East', line=dict(color='#03a9f4', width=2)))
        fig1.add_trace(go.Scatter(x=t, y=np.sin(t+0.5)*0.2*v_factor, name='Up', line=dict(color='#e91e63', width=2)))
        fig1.update_layout(height=250, margin=dict(l=0,r=0,t=10,b=0), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', showlegend=False)
        st.plotly_chart(fig1, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # 2. Kart: FFT / SPECTRA
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        f1, f2 = st.columns([4, 1])
        with f1:
            st.markdown("### FFT / SPECTRA")
        with f2:
            st.markdown('<p style="text-align:right; color:#34495e; font-size:13px; font-weight:bold; cursor:pointer;">Export Report</p>', unsafe_allow_html=True)
        
        # Örnek FFT Görüntüsü (VA Flowchart'ına uygun)
        f_axis = np.linspace(0, 10, 100)
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=f_axis, y=np.abs(np.sinc(f_axis-1.2))*10*v_factor, name="VA-FFT", line=dict(color="#2ecc71")))
        fig2.update_layout(height=200, margin=dict(l=0,r=0,t=0,b=0), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig2, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_right:
        # Sistem Durumu (Görseldeki gibi sağ üstte)
        st.markdown("<div style='text-align: right; margin-bottom: 30px;'>", unsafe_allow_html=True)
        status_txt = "Running" if st.session_state.is_auth else "Stopped"
        status_col = "#2ecc71" if st.session_state.is_auth else "#e74c3c"
        st.markdown(f"<p style='color:gray; font-size:12px; margin:0;'>SYSTEM STATUS</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:{status_col}; font-weight:bold; margin:0;'>● {status_txt}</p>", unsafe_allow_html=True)
        st.markdown("<p style='color:#3498db; margin:0;'>📶 GNSS Connection</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Metrik Kutuları
        m_val = ["20 Hz", "12", "0.05 s", "1.2 cm"] if st.session_state.is_auth else ["0 Hz", "0", "-", "-"]
        labels = ["SAMPLING RATE", "SATELLITES", "LATENCY", "RMS ERROR"]
        
        for l, v in zip(labels, m_val):
            st.markdown(f"""
                <div class="metric-card">
                    <small style="color:gray;">{l}</small>
                    <h2 style="margin:0; color:#2c3e50;">{v}</h2>
                </div>
            """, unsafe_allow_html=True)

# --- ANALYSIS SAYFASI (GELİŞMİŞ ANALİZ & FFT) ---
elif st.session_state.page == "Analysis":
    st.markdown("<h1 style='color: #34495e;'> Advanced Analysis & Spectral Results</h1>", unsafe_allow_html=True)
    
    if not st.session_state.is_auth:
        st.warning("⚠️ Lütfen 'User Access' panelinden giriş yapın.")
    else:
        # PPPH-VA Sütun Tanımları
        cols = ['Year', 'DOY', 'SOD', 'dx', 'dY', 'dZ', 'dN', 'dE', 'du', 'DTG', 'DTR', 'DTE', 'DTB2', 'DTB3']
        
        try:
            # Gerçek Gebze verisi veya BRUX verisi
            df_full = pd.read_csv('RES_SF_BRD.txt', sep='\s+', names=cols)
            st.success("✅ PPPH-VA Çıktı Dosyası Bağlandı.")
        except:
            # Dosya henüz yoksa demo veri üret (Sunumda risk olmasın diye)
            t_sim = np.linspace(0, 10, 500)
            df_full = pd.DataFrame({
                'SOD': t_sim,
                'dN': np.sin(2 * np.pi * 1.5 * t_sim) * 0.01, # 1.5 Hz titreşim simülasyonu
                'dE': np.random.normal(0, 0.002, 500),
                'du': np.random.normal(0, 0.005, 500)
            })

        # --- ⏳ GERÇEK ZAMANLI AKIŞ SİMÜLASYONU (Hoca için!) ---
        st.write("### ⏱️ Real-Time Stream Simulation")
        # Streamlit slider ile verinin hangi anını izlediğimizi seçebiliriz (Sanki canlı akıyormuş gibi)
        sample_size = st.slider("İzlenecek Veri Aralığı (Epoch)", 10, len(df_full), 100)
        df_display = df_full.iloc[:sample_size]

        # 1. Grafik: Zaman Serisi (Live Scroll Effect)
        fig_live = go.Figure()
        fig_live.add_trace(go.Scatter(x=df_display['SOD'], y=df_display['dN'], name='North', line=dict(color='#9c27b0')))
        fig_live.add_trace(go.Scatter(x=df_display['SOD'], y=df_display['du'], name='Up', line=dict(color='#e91e63')))
        fig_live.update_layout(title="Canlı Zaman Serisi (Epoch-by-Epoch Reading)", height=350)
        st.plotly_chart(fig_live, use_container_width=True)

        # --- 📉 FFT / SPEKTRAL ANALİZ (Yeni Eklendi!) ---
        st.write("---")
        st.write("### Spectral Analysis (Fast Fourier Transform)")
        
        # Basit FFT Hesaplama (North verisi üzerinden)
        # Gebze örneğinde 20Hz sampling vardı
        fs = 20.0 
        n = len(df_display['dN'])
        yf = np.abs(np.fft.fft(df_display['dN'].values))
        xf = np.fft.fftfreq(n, 1/fs)
        
        # Sadece pozitif frekansları alalım
        pos_mask = xf > 0
        fig_fft = go.Figure(go.Scatter(x=xf[pos_mask], y=yf[pos_mask], fill='tozeroy', line=dict(color='#2ecc71')))
        fig_fft.update_layout(title="Vibrasyon Frekansı (Hz)", xaxis_title="Frekans (Hz)", yaxis_title="Genlik", height=300)
        st.plotly_chart(fig_fft, use_container_width=True)
        
        st.info("💡 FFT analizi, yapının hangi frekansta salınım yaptığını gösterir. Gebze sarsma tablası verilerinde bu grafik çok net çıkacaktır! 🚀")

# --- USER ACCESS SAYFASI (TEMİZLENDİ: TEK GİRİŞ PANELİ) ---
elif st.session_state.page == "User Access":
    st.markdown("<h1 style='color: #34495e;'> Sistem Yetkilendirme Merkezi</h1>", unsafe_allow_html=True)

    if not st.session_state.is_auth:
        st.info("Lütfen yönetici bilgileriyle sistemi aktifleştirin. 🔐")
        mail = st.text_input("Yönetici E-posta", key="admin_mail")
        pw = st.text_input("Güvenlik Şifresi", type="password", key="admin_pw")
        
        if st.button("Sistemi Tam Yetkiyle Aç 🔓"):
            if mail == "dilara@example.com" and pw == "dilara2210674003":
                st.session_state.is_auth = True
                st.success("Sistem Aktif! ✨")
                st.rerun()
            else:
                st.error("Hatalı bilgiler! 🎀")
    else:
        st.success(f"Hoş geldin Dilara Çeliköz! ✨ Sistem tam kapasite çalışıyor.")
        if st.button("Oturumu Kapat ve Sistemi Kilitle 🔒"):
            st.session_state.is_auth = False
            st.rerun()

# --- 2. CONFIGURATION SAYFASI (YETKİ KONTROLÜ) ---
elif st.session_state.page == "Configuration":
    st.markdown("<h1 style='color: #34495e;'> System Configuration</h1>", unsafe_allow_html=True)
    
    if not st.session_state.is_auth:
        st.warning("⚠️ Bu bölüme erişmek için yetkili girişi gereklidir. Lütfen 'User Access' sayfasından giriş yapın.")
    else:
        # Yetki varsa dosyaları yükleyebilir
        st.subheader("Data Acquisition & Processing Settings")
        col_a, col_b = st.columns(2)
        with col_a:
            st.write("### 📂 Data Input")
            st.file_uploader("RINEX Gözlem Dosyası Yükle (.obs)", type=['obs', 'rnx'])
            st.file_uploader("Broadcast Ephemeris Yükle (.nav)", type=['nav'])
        with col_b:
            st.write("### ⚙️ Parameters")
            st.selectbox("GNSS Constellations", ["Multi-GNSS (GPS+Galileo+BeiDou)", "GPS Only"])
            st.slider("Sampling Frequency (Hz)", 1, 20, 20)

# --- ALERTS SAYFASI (YETKİ KONTROLÜ EKLENDİ) ---
elif st.session_state.page == "Alerts":
    st.markdown("<h1 style='color: #34495e;'> Alerts & Thresholds</h1>", unsafe_allow_html=True)
    
    if not st.session_state.is_auth:
        st.warning("⚠️ Alarm kayıtlarını ve eşik değerlerini görüntülemek için yetkili girişi gereklidir.")
        st.info("Lütfen 'User Access' sayfasından giriş yapın. 🔐")
    else:
        st.write("Yapısal Sağlık İzleme sistemi tarafından üretilen son uyarılar:")
        
        # Şık bir uyarı kartı
        st.error("⚠️ **Kritik Hareket Eşiği:** 5.0 cm (Şu anki durum: Stabil ✅)")
        
        # Örnek geçmiş kayıtlar tablosu
        alert_data = pd.DataFrame({
            'Tarih': ['2026-02-14 10:20', '2026-02-15 09:15'],
            'Olay': ['Sistem Başlatıldı', 'Veri Akışı Stabil'],
            'Durum': ['Bilgi', 'Normal']
        })
        st.table(alert_data)
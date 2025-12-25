import streamlit as st
import random
from streamlit_mic_recorder import speech_to_text

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="İlim Alp_Bot Macerası", page_icon="🛡️", layout="centered")

# --- DURUM (STATE) YÖNETİMİ ---
if 'toplam_puan' not in st.session_state:
    st.session_state.toplam_puan = 0
if 'yapilan_gorevler' not in st.session_state:
    st.session_state.yapilan_gorevler = []

# --- PUAN EKLEME FONKSİYONU ---
def gorevi_tamamla(anahtar, miktar):
    if anahtar not in st.session_state.yapilan_gorevler:
        st.session_state.toplam_puan += miktar
        st.session_state.yapilan_gorevler.append(anahtar)
        st.balloons()
        st.toast(f"🌟 Muhteşem! '{anahtar}' rozetini kazandın!", icon="✅")

# --- GELİŞMİŞ GÖRSEL STİL (CSS) ---
st.markdown("""
    <style>
    /* Ana Arka Plan */
    .main { background: linear-gradient(135deg, #e8f5e9 0%, #f1f8e9 100%); font-family: 'Segoe UI', sans-serif; }
    
    /* Kart Tasarımı (Cam Efekti) */
    .glass-card {
        background: rgba(255, 255, 255, 0.8);
        border-radius: 25px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
        backdrop-filter: blur(4px);
        margin-bottom: 20px;
    }
    
    /* Puan ve Rütbe Kutusu */
    .stat-box {
        background: #1b5e20;
        color: white;
        padding: 15px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 10px;
    }

    /* Rozet Stili */
    .badge {
        display: inline-block;
        padding: 10px;
        margin: 5px;
        background: white;
        border-radius: 50%;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        width: 60px; height: 60px;
        text-align: center; font-size: 25px;
        border: 2px solid #4caf50;
    }

    /* Buton Güzelleştirme */
    div.stButton > button {
        background: linear-gradient(90deg, #2e7d32, #66bb6a);
        color: white; border-radius: 30px; border: none;
        font-weight: bold; padding: 15px 30px; font-size: 18px;
        width: 100%; transition: 0.3s ease;
    }
    div.stButton > button:hover { transform: translateY(-3px); box-shadow: 0 10px 20px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# --- VERİ SETİ ---
bilgi_sozlugu = {
    "namaz": {"tanim": "Kalbimizi huzurla dolduran en güzel buluşma. ✨", "gorev": "Ezanı kalbinle dinle.", "puan": 20, "icon": "🕋"},
    "edep": {"tanim": "Güzel ahlakın en şık elbisesidir. 🌸", "gorev": "Büyüğüne nazikçe selam ver.", "puan": 15, "icon": "💎"},
    "sadaka": {"tanim": "Gülümsemek bile bir hazinedir. 😊", "gorev": "Bugün 3 kişiye gülümse.", "puan": 10, "icon": "🎁"},
    "merhamet": {"tanim": "Şefkat dolu bir kalbe sahip olmaktır. ❤️", "gorev": "Kuşlar için su bırak.", "puan": 20, "icon": "🐾"},
    "israf": {"tanim": "Emanetleri korumak, boşa harcamamaktır. 💧", "gorev": "Tabağındaki yemeği bitir.", "puan": 15, "icon": "🌊"}
}

# --- YAN MENÜ (PRO PANELİ) ---
with st.sidebar:
    st.markdown("<div class='stat-box'><h3>🌟 Alp_Bot Profil</h3></div>", unsafe_allow_html=True)
    st.metric("Puanın", f"{st.session_state.toplam_puan} ⭐")
    
    p = st.session_state.toplam_puan
    rutbe, emoji = ("Yeni Alp", "🌱") if p < 40 else ("Bilge Yolcu", "📚") if p < 100 else ("Edep Kahramanı", "🛡️")
    st.markdown(f"<p style='text-align:center; font-weight:bold;'>Rütben: {rutbe} {emoji}</p>", unsafe_allow_html=True)
    
    st.write("---")
    st.write("🏅 **Kazandığın Rozetler:**")
    cols = st.columns(3)
    for i, g in enumerate(st.session_state.yapilan_gorevler):
        with cols[i % 3]:
            st.markdown(f"<div class='badge'>{bilgi_sozlugu[g]['icon']}</div>", unsafe_allow_html=True)
    
    if st.button("🔄 Sıfırla"):
        st.session_state.clear()
        st.rerun()

# --- ANA EKRAN ---
st.markdown("<h1>🛡️ İlmi Alp_Bot Macerası</h1>", unsafe_allow_html=True)

# İlerleme Çubuğu (Görselleştirilmiş)
prog_val = len(st.session_state.yapilan_gorevler) / len(bilgi_sozlugu)
st.write(f"📊 Koleksiyonun: {len(st.session_state.yapilan_gorevler)} / {len(bilgi_sozlugu)}")
st.progress(prog_val)

# Giriş Alanı
c1, c2 = st.columns([1, 4])
with c1:
    voice = speech_to_text(language='tr', start_prompt="🎤", stop_prompt="⏹️", key='stt')
with c2:
    query = st.text_input("", value=voice if voice else "", placeholder="Örn: Namaz, Edep, Merhamet...").lower()



# Sonuç Ekranı
if query:
    found = False
    for k, v in bilgi_sozlugu.items():
        if k in query:
            found = True
            st.markdown(f"""
                <div class="glass-card">
                    <h2 style='color:#2e7d32;'>{v['icon']} {k.upper()}</h2>
                    <p style='font-size:18px;'>{v['tanim']}</p>
                    <div style='background:#f1f8e9; padding:15px; border-radius:15px; border-left:5px solid #2e7d32;'>
                        <b>🏆 Kahramanlık Görevi:</b><br>{v['gorev']}
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            if k in st.session_state.yapilan_gorevler:
                st.success("🌟 Bu rozeti zaten kazandın ve başarına ekledin!")
            else:
                st.button(f"🚀 Görevi Yaptım (+{v['puan']} Puan)", on_click=gorevi_tamamla, args=(k, v['puan']))

# Günün Hadisi Kartı
st.markdown("""
    <div style='background: #fff3e0; padding: 20px; border-radius: 20px; text-align: center; border: 1px dashed #ff9800;'>
        <b>✨ Günün İlhamı</b><br>
        <i>"Sizin en hayırlınız, ahlakı en güzel olanınızdır."</i>
    </div>
    """, unsafe_allow_html=True)
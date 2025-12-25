import streamlit as st
import random

# Sayfa Yapılandırması
st.set_page_config(page_title="Dijital Empati Asistanı", page_icon="🤝")

# --- VERİ SETİ VE MANTIK ---
kabalik_sozlugu = {
    "aptal": "bu fikrin üzerine biraz daha düşünmelisin",
    "saçma": "mantığını anlayamadığım",
    "kötü": "geliştirilmeye açık",
    "beceriksiz": "henüz yeterli tecrübede değil",
    "nefret": "pek hoşlanmadığım",
    "rezil": "beklentinin altında"
}

islami_uyarilar = [
    "Mümin, diliyle kimseyi incitmeyen kimsedir. (Hadis-i Şerif)",
    "Kavlü'n-Leyyin: Yumuşak ve nazik bir üslup kullanmayı dene.",
    "Hüsn-ü Zan: Karşındakinin niyetini iyiye yormak seni de rahatlatır."
]

# --- ARAYÜZ TASARIMI ---
st.title("🤝 Dijital Empati Asistanı")
st.subheader("Değerler Eğitimi ve Yapay Zeka Projesi")
st.write("Bu uygulama, yazdığınız mesajları analiz ederek daha nazik ve ahlaki değerlere uygun hale getirir.")

st.divider()

# Kullanıcı Girişi
user_text = st.text_area("Mesajınızı buraya yazın:", placeholder="Örn: Bu yaptığın çok aptalca...")

if st.button("Analiz Et"):
    if user_text:
        mesaj = user_text.lower()
        tespit_edilenler = []
        yeni_mesaj = mesaj

        # Analiz Süreci
        for anahtar, deger in kabalik_sozlugu.items():
            if anahtar in mesaj:
                tespit_edilenler.append(anahtar)
                yeni_mesaj = yeni_mesaj.replace(anahtar, f"**{deger}**")

        if tespit_edilenler:
            st.warning(f"⚠️ Mesajınızda sert ifadeler bulundu: {', '.join(tespit_edilenler)}")
            
            # Değerler Eğitimi Kartı
            with st.expander("Neden Değiştirmeliyim?"):
                st.info(random.choice(islami_uyarilar))
            
            st.success("✨ Önerilen Yeni Mesaj:")
            st.write(yeni_mesaj.capitalize())
        else:
            st.balloons()
            st.success("🌟 Harika! Mesajınız nezaket kurallarına ve değerlerimize uygun.")
    else:
        st.error("Lütfen bir metin girin.")

st.sidebar.info("Bu proje TÜBİTAK 2204-A Değerler Eğitimi kategorisi için geliştirilmiştir.")
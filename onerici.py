import streamlit as st
import random

# Sayfa Yapılandırması (Modern Görünüm İçin)
st.set_page_config(page_title="Mood Music", page_icon="🎵", layout="centered")

# Senin Linklerin (Aynı Sözlük Yapısı)
sarkilar = {
    "Rap": ["https://www.youtube.com/watch?v=IT8XvzIfi4U", "https://www.youtube.com/watch?v=fCeiUX59_FM"],
    "Metal": ["https://www.youtube.com/watch?v=XtjSYv1Qh1M"],
    "Pop": ["https://www.youtube.com/watch?v=H7mxXm0Avts"],
    "Rock": ["https://www.youtube.com/watch?v=CD-E-LDc384"],
    "Classic": ["https://www.youtube.com/watch?v=OCUSalQf-jY"],
    "Arabesk": ["https://youtu.be/lYNMQBKDhwg"],
    "Jazz": ["https://www.youtube.com/watch?v=oHRNrgDIJfo"]
}

# Tasarım: Başlık ve Açıklama
st.title("🎵 Akıllı Müzik Önerici")
st.markdown("Seçimlerini yap, senin için en uygun şarkıyı bulalım!")

# Yan yana kolonlar oluşturarak modern bir görünüm sağlayalım
col1, col2 = st.columns(2)

with col1:
    akt = st.selectbox("Şu an ne yapıyorsun?", ["Spor", "Ders/Odaklanma", "Parti/Eğlence", "Yolculuk", "Dinlenme/Uyku"])

with col2:
    ruh = st.selectbox("Nasıl hissediyorsun?", ["Enerjik/Neşeli", "Öfkeli/Gergin", "Melankolik/Hüzünlü", "Sakin/Huzurlu"])

# Buton
if st.button("Bana Şarkı Öner!", use_container_width=True):
    # Karar Ağacı Mantığı
    tavsiye = ""
    if akt == "Spor":
        tavsiye = "Metal" if ruh == "Öfkeli/Gergin" else "Rap"
    elif akt == "Ders/Odaklanma":
        tavsiye = "Classic"
    elif akt == "Parti/Eğlence":
        tavsiye = "Pop"
    elif akt == "Yolculuk":
        tavsiye = "Rock"
    elif akt == "Dinlenme/Uyku":
        tavsiye = "Jazz" if ruh == "Sakin/Huzurlu" else "Arabesk"

    # Sonucu Göster
    st.success(f"Senin için seçilen tür: **{tavsiye}**")
    link = random.choice(sarkilar[tavsiye])
    
    # WEB'İN GÜCÜ: Videoyu direkt sayfanın içine gömelim!
    st.video(link)
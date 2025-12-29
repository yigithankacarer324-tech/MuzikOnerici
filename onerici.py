import streamlit as st
import random

# Sayfa Yapılandırması (Modern Görünüm İçin)
st.set_page_config(page_title="Mood Music", page_icon="🎵", layout="centered")

# Senin Linklerin (Aynı Sözlük Yapısı)
sarkilar = {
    "Rap": ["https://www.youtube.com/watch?v=fCeiUX59_FM&list=RDfCeiUX59_FM&start_radio=1","https://youtu.be/3GiO2hfzbZY?si=KAa-PhCLHI8UKlb5","https://youtu.be/Ze0o7ulhsk4?si=5PAx76kVP4O7OVZ8","https://www.youtube.com/watch?v=lTVhSzDRrRg","https://www.youtube.com/watch?v=EF38XQ5o4EM&list=RDEF38XQ5o4EM&start_radio=1","https://www.youtube.com/watch?v=0xji3PXYSxU&list=RD0xji3PXYSxU&start_radio=1","https://www.youtube.com/watch?v=gXkfiZgqmJA&list=RDgXkfiZgqmJA&start_radio=1","https://www.youtube.com/watch?v=g3zAzfySfsY&list=RDg3zAzfySfsY&start_radio=1","https://www.youtube.com/watch?v=Ui-gMJ_Dsjc&list=RDUi-gMJ_Dsjc&start_radio=1","https://www.youtube.com/watch?v=uDuFEM-ofZY&list=RDuDuFEM-ofZY&start_radio=1","https://www.youtube.com/watch?v=U87R2Dzk57M&list=RDU87R2Dzk57M&start_radio=1","https://www.youtube.com/watch?v=_6xxK2lYhTc&list=RD_6xxK2lYhTc&start_radio=1","https://www.youtube.com/watch?v=phaJXp_zMYM&list=RDphaJXp_zMYM&start_radio=1","https://www.youtube.com/watch?v=9FIwhBAsUnY&list=RD9FIwhBAsUnY&start_radio=1"],
    "Metal": ["https://youtu.be/hmpJqJLsR48?si=CPoGrnq_trIeDLLn","https://www.youtube.com/watch?v=XtjSYv1Qh1M&list=RDXtjSYv1Qh1M&start_radio=1","https://youtu.be/86URGgqONvA?si=1h5-wdnU_9i6kuyS","https://youtu.be/6xjJ2XIbGRk?si=92yDGxkbzBcmpWKA","https://youtu.be/8aQRq9hhekA?si=ZpKHWizMN0Rdgb8I","https://youtu.be/L397TWLwrUU?si=9tVw_UdzPABcHLCH","https://www.youtube.com/watch?v=orwgEEaJln0&list=RDorwgEEaJln0&start_radio=1","https://www.youtube.com/watch?v=iVvXB-Vwnco&list=RDiVvXB-Vwnco&start_radio=1","https://www.youtube.com/watch?v=eqEgHWlHad4&list=RDeqEgHWlHad4&start_radio=1","https://www.youtube.com/watch?v=_U8X6XvS3EI&list=RD_U8X6XvS3EI&start_radio=1"],
    "Pop": ["https://www.youtube.com/watch?v=H7mxXm0Avts","https://www.youtube.com/watch?v=NAHRpEqgcL4","https://www.youtube.com/watch?v=6dYWe1c3OyU","https://www.youtube.com/watch?v=ETxmCCsMoD0","https://www.youtube.com/watch?v=qFy5GEymMz4","https://www.youtube.com/watch?v=CGNcI0Fsl9c","https://www.youtube.com/watch?v=0TFNGRYMz1U","https://www.youtube.com/watch?v=sCz-efrkir8","https://www.youtube.com/watch?v=6aFJErFRQuY","https://www.youtube.com/watch?v=ozkIhToWUPs","https://www.youtube.com/watch?v=uc2UEfWjvo8","https://www.youtube.com/watch?v=pidPpEA4F-g","https://www.youtube.com/watch?v=dJ8PfMwEWxU","https://www.youtube.com/watch?v=IT8XvzIfi4U"],
    "Rock": ["https://www.youtube.com/watch?v=CD-E-LDc384","https://www.youtube.com/watch?v=StZcUAPRRac&ab_channel=RammsteinOfficial","https://www.youtube.com/watch?v=Ckom3gf57Yw&ab_channel=WarnerRecordsVault","https://www.youtube.com/watch?v=GkPna4xPJmE&ab_channel=SystemOfADown-Topic","https://www.youtube.com/watch?v=Q2FvEb59lQY&ab_channel=Haggard-Topic","https://www.youtube.com/watch?v=VvYRYCIAKZo&ab_channel=HAGGARDOfficial","https://www.youtube.com/watch?v=3V4VQogwKZA","https://www.youtube.com/watch?v=x-xTttimcNk","https://www.youtube.com/watch?v=IBtGmxU1wzs","https://www.youtube.com/watch?v=qgaRVvAKoqQ&list=RDqgaRVvAKoqQ&start_radio=1","https://www.youtube.com/watch?v=jxi17F3z0Xw","https://www.youtube.com/watch?v=x9HH5aFy9Ew","https://youtu.be/3DgfKdnUBkA?si=gBi1ooxsxed8uQga","https://www.youtube.com/watch?v=Kn_uLF4KHgY","https://youtu.be/w1G5Xn6400s?si=Cb8HW5AmP2FmvktO"],
    "Classic": ["https://www.youtube.com/watch?v=OCUSalQf-jY","https://www.youtube.com/watch?v=YusS_XgkRgE&list=RDYusS_XgkRgE&start_radio=1","https://www.youtube.com/watch?v=FDTGPChTtEw&list=RDFDTGPChTtEw&start_radio=1","https://www.youtube.com/watch?v=GRxofEmo3HA","https://www.youtube.com/watch?v=K2iC1aCPbKA","https://www.youtube.com/watch?v=HWqKPWO5T4o"],
    "Arabesk": ["https://youtu.be/lYNMQBKDhwg?si=sVmWjZmONoiKQnhP","https://www.youtube.com/watch?v=bmFaaLLF56c","https://youtu.be/ccYt6LEQtP8?si=o_5JatTS2TCt3HDq","https://youtu.be/wtOHNhG0EZc?si=NDZZlnCyULuY531E","https://www.youtube.com/watch?v=YbI6J338xxw","https://youtu.be/wtOHNhG0EZc?si=NDZZlnCyULuY531E","https://www.youtube.com/watch?v=cVL7Gvlm59A","https://www.youtube.com/watch?v=7hp-nwyHe24","https://www.youtube.com/watch?v=6pYgGItOqtE","https://www.youtube.com/watch?v=D2C3dBE7BtM","https://www.youtube.com/watch?v=AQWgp4Xav-E&list=RDAQWgp4Xav-E&start_radio=1","https://www.youtube.com/watch?v=BzcAXC-xGFg&list=RDBzcAXC-xGFg&start_radio=1","https://www.youtube.com/watch?v=BzcAXC-xGFg&list=RDBzcAXC-xGFg&start_radio=1","https://www.youtube.com/watch?v=MoxHg_2HaU4&list=RDMoxHg_2HaU4&start_radio=1"],
    "Jazz": ["https://www.youtube.com/watch?v=oHRNrgDIJfo","https://www.youtube.com/watch?v=1fpvmQBsGyE&list=RD1fpvmQBsGyE&start_radio=1","https://www.youtube.com/watch?v=DXq-XdyGehk","https://www.youtube.com/watch?v=eNbpq_95blM&list=RDeNbpq_95blM&start_radio=1","https://www.youtube.com/watch?v=SrnWp5O0DEs","https://www.youtube.com/watch?v=tO4dxvguQDk","https://www.youtube.com/watch?v=vmDDOFXSgAs","https://www.youtube.com/watch?v=b4wSrqPqKqU","https://www.youtube.com/watch?v=JErVP6xLZwg","https://www.youtube.com/watch?v=zqNTltOGh5c","Leonard Cohen - Dance Me to the End of Love (Official Video)"]
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
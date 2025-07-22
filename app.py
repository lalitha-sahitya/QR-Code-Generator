import streamlit as st
import qrcode
from io import BytesIO

st.set_page_config(page_title="QR Code Generator", page_icon="🔗")

st.title("QR Code Generator")

data = st.text_input("Enter the URL or Text:")
filename = st.text_input("Enter a file name (e.g., myqr.png):")

if st.button("Generate QR Code"):
    if data and filename:
        qr = qrcode.QRCode(box_size=10, border=4)
        qr.add_data(data)
        img = qr.make_image(fill_color='black', back_color='white')

        buf = BytesIO()
        img.save(buf, format='PNG')
        buf.seek(0)
        st.image(buf, caption="Generated QR Code", use_container_width=False)
        st.download_button(
            label="Download QR Code",
            data=buf,
            file_name=filename if filename.endswith('.png') else filename + '.png',
            mime="image/png"
        )
    else:
        st.warning("Please enter both URL/text and filename.")
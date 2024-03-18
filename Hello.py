import folium
from selenium import webdriver
from PIL import Image
from io import BytesIO
import streamlit as st

# Criar um mapa com o Folium
m = folium.Map(location=[-30, -55], zoom_start=10)

# Adicionar marcadores, polígonos, etc., conforme necessário
folium.Marker([-30.05, -55.1], popup='Marker 1').add_to(m)
folium.Marker([-29.95, -54.9], popup='Marker 2').add_to(m)
folium.Polygon(locations=[[-30.1, -55.2], [-30.1, -54.8], [-29.9, -54.8], [-29.9, -55.2]], color='blue', fill=True).add_to(m)

# Renderizar o mapa em HTML
mapa_html = m._repr_html_()

# Configurar o webdriver do Selenium
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Executar o Chrome em modo headless (sem janelas visíveis)
driver = webdriver.Chrome(options=options)

# Abrir uma página temporária e renderizar o HTML do mapa usando o webdriver
driver.get('about:blank')
driver.execute_script('document.write(\'{}\');'.format(mapa_html))

# Capturar a tela do navegador
screenshot_bytes = driver.get_screenshot_as_png()

# Fechar o webdriver
driver.quit()

# Converter a imagem capturada em um objeto Image do Pillow
img = Image.open(BytesIO(screenshot_bytes))

# Mostrar a imagem no Streamlit
st.image(img, caption='Mapa capturado', use_column_width=True)

# Salvar a imagem em um arquivo temporário
img_path = 'mapa_capturado.png'
img.save(img_path)

# Exibir o link para o arquivo no Streamlit
st.markdown(f'Download do mapa capturado: [Download](data:image/png;base64,{base64.b64encode(open(img_path, "rb").read()).decode()})', unsafe_allow_html=True)

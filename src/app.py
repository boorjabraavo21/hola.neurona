import streamlit as st

st.title("¡Hola neurona! :sunglasses:")

tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y sesgo"])
y = 0

with tab1:
    w = st.slider("Peso", 0.0, 5.0, 0.0)
    x = st.number_input("Introduzca el valor de la entrada")
    y = x * w
    if st.button("Calcular la salida", key="button_1"):
        st.write(f"La salida de la neurona es {y}")
with tab2:
    col1, col2 = st.columns(2)
    with col1:
        w0 = st.slider("Peso w0", 0.0, 5.0, 0.0, key=0)
        x0 = st.number_input("Entrada x0", key="input_1")
    with col2:
        w1 = st.slider("Peso w1", 0.0, 5.0, 0.0, key=1)
        x1 = st.number_input("Entrada x1", key="input_2")
    y = x0 * w0 + x1 * w1
    if st.button("Calcular la salida", key="button_2"):
        st.write(f"La salida de la neurona es {y}")
with tab3:
    col1, col2, col3 = st.columns(3)
    with col1:
        w0 = st.slider("Peso w0", 0.0, 5.0, 0.0, key=3)
        x0 = st.number_input("Entrada x0", key="input_3")
    with col2:
        w1 = st.slider("Peso w1", 0.0, 5.0, 0.0, key=4)
        x1 = st.number_input("Entrada x1", key="input_4")
    with col3:
        w2 = st.slider("Peso w2", 0.0, 5.0, 0.0, key=5)
        x2 = st.number_input("Entrada x2", key="input_5")
    b = st.number_input("Introduce el valor del sesgo")
    y = x0 * w0 + x1 * w1 + x2 * w2 + b
    if st.button("Calcular la salida", key="button_3"):
        st.write(f"La salida de la neurona es {y}")
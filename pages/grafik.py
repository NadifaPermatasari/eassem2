import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.title("Aplikasi Grafik Histogram dan Boxplot")
    
    # Mengambil input dataset dari pengguna
    uploaded_file = st.file_uploader("Unggah file CSV", type="csv")
    
    if uploaded_file is not None:
        # Membaca dataset dari file CSV
        df = pd.read_csv(uploaded_file)
        
        # Menampilkan dataset
        st.subheader("Dataset")
        st.write(df)
        
        # Menampilkan grafik histogram
        st.subheader("Histogram")
        column = st.selectbox("Pilih kolom", df.columns)
        fig, ax = plt.subplots()
        ax.hist(df[column], bins='auto')
        st.pyplot(fig)
        
        # Menampilkan grafik boxplot
        st.subheader("Boxplot")
        st.write('note : jika muncul error didapatkan bahwa data tidak bisa direalisaikan dalam bentuk boxplot')
        fig, ax = plt.subplots()
        ax.boxplot(df[column])
        st.pyplot(fig)

if __name__ == "__main__":
    main()
    print(plt.boxplot)
    print(plt.hist)

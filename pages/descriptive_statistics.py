import streamlit as st
import numpy as np
import pandas as pd

def main():
    st.title("Aplikasi Statistika Deskriptif")
    
    # Mengambil input dataset dari pengguna
    uploaded_file = st.file_uploader("Unggah file CSV dengan catatan tanpa judul langsung data", type="csv")
    
    if uploaded_file is not None:
        # Membaca dataset dari file CSV
        df = pd.read_csv(uploaded_file)
        
        # Menampilkan dataset
        st.subheader("Dataset")
        st.write(df)
        
        # Mencari statistika deskriptif
        st.subheader("Statistika Deskriptif")
        st.write("Jumlah Data:", df.shape[0])
        st.write("Mean:", df.mean())
        st.write("Median:", df.median())
        st.write("Standar Deviasi:", df.std())
        st.write("Minimum:", df.min())
        st.write("Maksimum:", df.max())
        st.write("Kuartil 1:", df.quantile(0.25))
        st.write("Kuartil 3:", df.quantile(0.75))

if __name__ == "__main__":
    main()
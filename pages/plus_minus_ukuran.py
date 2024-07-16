import streamlit as st
import pandas as pd

def main():
    st.title("Kekurangan dan Kelebihan Ukuran Dalam Statistika Deskriptif")
    
    # Membuat data frame
    data = {
        'Ukuran': ['Mean', 'Median', 'Modus', 'Range', 'Varians'],
        'Kelebihan': ['Ukuran simpel yang mewakili sekelompok data', 'Tidak terpengaruh nilai ekstrim', 'Bagus untuk menunjukkan karakteristik tertentu', 'Ukuran simpel untuk melihat keseluruhan data', 'Bisa mewakili keragaman setiap data'],
        'Kekurangan': ['Terpengaruh nilai ekstrim', 'Tidak mencerminkan jumlah', 'Tidak selalu menunjukkan nilai terendah', 'Kurang bisa mendeskripsikan lebih jauh', 'Perhitungan cukuo rumit']
    }
    df = pd.DataFrame(data)
    
    # Menampilkan tabel
    st.write(df)

if __name__ == "__main__":
    main()
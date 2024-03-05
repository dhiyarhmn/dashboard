import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Memuat data
day_df = pd.read_csv("main_data.csv")  

day_df.to_csv("main_data.csv", index=False)

# Mengonversi kolom 'dteday' menjadi format datetime
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

def visualize_data(df):
    palet_warna_pastel = ['paleturquoise', 'pink']  
    st.subheader("Distribusi jumlah peminjaman sepeda oleh pengguna yang sudah terdaftar selama 2011 sampai 2012")

    # Plot pengguna terdaftar per bulan 
    registered_users_df = df.groupby(by=["yr", "mnth"])["registered"].sum().reset_index()
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(x='mnth', y='registered', hue='yr', data=registered_users_df, estimator=sum, marker='o', ax=ax, palette=palet_warna_pastel)

    handles = [plt.Line2D([0], [0], color=palet_warna_pastel[0], marker='o', linestyle='None', markersize=10),
               plt.Line2D([0], [0], color=palet_warna_pastel[1], marker='o', linestyle='None', markersize=10)]
    labels = ['2011', '2012']
    ax.legend(title='Tahun', loc='upper left', handles=handles, labels=labels)

    plt.title('Distribusi Jumlah Peminjaman Sepeda oleh Pengguna yang Sudah Terdaftar')
    plt.xlabel('Bulan')
    plt.ylabel('Jumlah Peminjaman Sepeda oleh Pengguna Terdaftar')
    st.pyplot(fig)
    st.write('Dari visualisasi diatas dapat dilihat bahwa distribusi jumlah peminjaman sepeda oleh pengguna yang sudah terdaftar per bulan dan tahun, yaitu jumlah penyewaan sepeda lebih tinggi pada tahun 2012 dibandingkan dengan 2011 karena setelah dilihat dari diagramnya, warna pink lebih banyak daripada warna biru jumlah peminjaman sepeda oleh pengguna terdaftar. Sehingga dapat disimpulkan bahwa distribusi jumlah peminjaman sepeda oleh pengguna yang sudah terdaftar pada tahun 2011 dan 2012 adalah lebih banyak jumlah peminjaman sepeda oleh pengguna yang sudah terdaftar pada tahun 2012')
    
    st.write('')

    st.subheader("Perubahan Jumlah Peminjaman Sepeda berdasarkan Kondisi Cuaca selama 2011 sampai 2012")

    # Plot perubahan penyewaan sepeda berdasarkan kondisi cuaca 
    weather_df = df.groupby(by=['yr', 'weathersit']).agg({"cnt": "sum"}).reset_index()

    weather_df['weathersit'] = weather_df['weathersit'].astype(str)

    weather_df['yr'] = weather_df['yr'].astype(str)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='weathersit', y='cnt', hue='yr', data=weather_df, estimator=sum, ax=ax, palette=palet_warna_pastel)

    plt.title('Perubahan Jumlah Peminjaman Sepeda berdasarkan Kondisi Cuaca')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Jumlah Peminjaman Sepeda')

    legend = ax.legend(title='Tahun', loc='upper right')
    legend.set_title('Tahun')
    legend.get_texts()[0].set_text('2011')
    legend.get_texts()[1].set_text('2012')
    st.pyplot(fig)
    
    st.write('Dari visualisasi diatas dapat dilihat bahwa perubahan peminjaman sepeda berdasarkan kondisi cuaca pada tahun 2011 dan 2012, yaitu pada cuaca 1 lebih banyak peminjaman sepeda pada tahun 2012 daripada tahun 2011, pada cuaca 2 lebih banyak peminjaman sepeda pada tahun 2012 daripada tahun 2011, pada cuaca 3 lebih banyak peminjaman sepeda pada tahun 2011 daripada tahun 2012. Sehingga dapat disimpulkan bahwa terdapat perubahan peminjaman sepeda berdasarkan kondisi cuaca. Jumlah peminjaman sepeda yang tertinggi terdapat pada cuaca 1 tahun 2012 dan jumlah peminjaman sepeda terendah terdapat pada cuaca 3 tahun 2012')

# Navigasi sidebar
st.sidebar.markdown("<h1 style='text-align: center; color: pink;'>Penyewaan Sepeda</h1><br>", unsafe_allow_html=True)
nav_selection = st.sidebar.selectbox("Navigation", ["Home", "Data Overview", "Visualizations"])

if nav_selection == "Home":
    st.title("Selamat Datang Di Dashboard Penyewaan Sepeda")
    st.write('')
    st.write('')
    st.image("sepeda.jpg", caption="", use_column_width=True)
elif nav_selection == "Data Overview":
    st.title('Dashboard Penyewaan Sepeda')
    st.write('')
    st.header('Day Dataset')
    st.write(day_df.head())
elif nav_selection == "Visualizations":
    st.title('Dashboard Penyewaan Sepeda')
    st.write('')
    visualize_data(day_df)
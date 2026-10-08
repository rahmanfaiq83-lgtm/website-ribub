import streamlit as st
from streamlit_extras.let_it_rain import rain
import time

# -----------------------------------------------------------------------------
# KONFIGURASI HALAMAN & TEMA (Bikin Gemes)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Love Journey: Kita 👩‍❤️‍👨",
    page_icon="💖",
    layout="wide" # Pakai layout wide biar lebih lega
)

# Custom CSS untuk tema warna Pink & Merah yang ngejreng tapi rapi
st.markdown("""
    <style>
    /* Warna Background Utama */
    .stApp {
        background-color: #ffe5ec;
    }
    
    /* Gaya Judul Utama (H1) */
    h1 {
        color: #ff0a54;
        text-align: center;
        font-family: 'Arial Black', gadget, sans-serif;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        background: -webkit-linear-gradient(#ff0a54, #ff758f);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Gaya Subheader (H2) */
    h2, .stSubheader {
        color: #c9184a !important;
        border-bottom: 2px solid #ff758f;
        padding-bottom: 10px;
    }

    /* Gaya Kartu Profil (Pop-up style) */
    .profile-card {
        background: rgba(255, 255, 255, 0.9);
        padding: 25px;
        border-radius: 25px;
        box-shadow: 0 10px 20px rgba(255, 75, 143, 0.3);
        border: 2px solid #ffb3c1;
        text-align: center;
        transition: transform 0.3s;
        margin-bottom: 20px;
    }
    .profile-card:hover {
        transform: scale(1.03);
    }

    /* Sidebar Styling */
    .css-1cd4s4 {
        background-color: #ffb3c1 !important;
    }
    
    /* Stylling untuk pesan berjalan */
    .marquee {
        background-color: #ff0a54;
        color: white;
        padding: 10px;
        font-weight: bold;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    
    /* Tombol Kustom */
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #c9184a;
        transform: translateY(-3px);
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# SIDEBAR NAVIGATION (Bikin Rame & Terstruktur)
# -----------------------------------------------------------------------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3616/3616215.png", width=100)
    st.title("💖 Menu Cinta")
    selected_page = st.radio("Cari Tahu Tentang Kita:", ["🏠 Beranda Utama", "📸 Galeri Foto Bucin", "🎶 Playlist Kenangan", "💌 Pesan Rahasia"])
    st.markdown("---")
    st.write("Dibuat dengan ❤️ oleh [Nama Kamu]")

# -----------------------------------------------------------------------------
# FUNGSI EFEK HUJAN HATI (Bikin Meriah)
# -----------------------------------------------------------------------------
def play_heart_rain():
    rain(
        emoji="💖",
        font_size=54,
        falling_speed=5,
        animation_length="forever", # Biar ngerain terus
    )

# -----------------------------------------------------------------------------
# MAIN CONTENT BERDASARKAN NAVIGASI
# -----------------------------------------------------------------------------

if selected_page == "🏠 Beranda Utama":
    play_heart_rain() # Jalankan efek hati jatuh
    st.title("👩‍❤️‍👨 Welcome to Our Love Journey! 👨‍❤️‍👩")
    
    # Teks Berjalan (Marquee)
    st.markdown("""
        <marquee class="marquee">
            💖 Selamat datang di situs resmi ke-bucin-an kita! 💖 Hari ini hari yang indah karena ada kamu! 💖 Happy Always! 💖
        </marquee>
    """, unsafe_allow_html=True)

    # Backsound (Tarik ke atas biar langsung jalan)
    # Ganti "lagu.mp3" sesuai nama filemu
    st.audio("lagu.mp3", autoplay=True)

    st.markdown("---")
    
    # Bagian Profil dengan Layout 2 Kolom
    col1, space, col2 = st.columns([10, 1, 10])

    with col1:
        st.markdown('<div class="profile-card">', unsafe_allow_html=True)
        # Ganti dengan nama file foto kamu
        st.image("aku.jpg", caption="Sang Pangeran 😎", use_container_width=True)
        st.subheader("Namaku")
        st.write("Suka bikin kamu ketawa, hobi fotoin kamu diem-diem, dan paling jago bikin rindu.")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="profile-card">', unsafe_allow_html=True)
        # Ganti dengan nama file foto pacar kamu
        st.image("dia.jpg", caption="Sang Putri ✨", use_container_width=True)
        st.subheader("Namanya")
        st.write("Pemilik senyum terlaris, alasan utamaku semangat tiap hari, dan pawang hatiku.")
        st.markdown('</div>', unsafe_allow_html=True)

    # Tombol Interaktif
    st.markdown("---")
    st.write("<h3 style='text-align: center; color: #c9184a;'>Seberapa sayang aku sama kamu?</h3>", unsafe_allow_html=True)
    if st.button("Klik untuk Tahu Jawabannya!", use_container_width=True):
        st.balloons() # Efek balon melambung
        st.success("GAK ADA OBATNYA! SAYANG BANGET BANGET BANGET! ❤️❤️❤️")

elif selected_page == "📸 Galeri Foto Bucin":
    st.title("📸 Galeri Momen Indah Kita")
    st.write("Kumpulan foto-foto acak tapi bermakna yang pernah kita abadikan.")
    
    # Layout Grid Foto yang Rame (3 Kolom)
    # Ganti URL placeholder dengan nama file foto kamu di folder yang sama
    g1, g2, g3 = st.columns(3)
    with g1:
        st.markdown('<div class="profile-card">', unsafe_allow_html=True)
        st.image("https://via.placeholder.com/400x400.png?text=Momen+1", caption="Kencan Pertama ❤️")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="profile-card">', unsafe_allow_html=True)
        st.image("https://via.placeholder.com/400x500.png?text=Momen+4", caption="Candid Lucu 😂")
        st.markdown('</div>', unsafe_allow_html=True)

    with g2:
        st.markdown('<div class="profile-card">', unsafe_allow_html=True)
        st.image("https://via.placeholder.com/400x500.png?text=Momen+2", caption="Jalan-Jalan Bareng 🚗")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="profile-card">', unsafe_allow_html=True)
        st.image("https://via.placeholder.com/400x400.png?text=Momen+5", caption="Makan Enak 🍕")
        st.markdown('</div>', unsafe_allow_html=True)

    with g3:
        st.markdown('<div class="profile-card">', unsafe_allow_html=True)
        st.image("https://via.placeholder.com/400x400.png?text=Momen+3", caption="Ulang Tahun 🎉")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="profile-card">', unsafe_allow_html=True)
        st.image("https://via.placeholder.com/400x500.png?text=Momen+6", caption="Malam Minggu 🌙")
        st.markdown('</div>', unsafe_allow_html=True)

elif selected_page == "🎶 Playlist Kenangan":
    st.title("🎶 Lagu-Lagu yang 'Kita Banget'")
    st.write("Playlist audio biar suasananya makin syahdu.")

    # Tambah beberapa pemutar audio (file harus ada di folder)
    t1, t2 = st.tabs(["🎵 Lagu Utama", "📻 Lagu Cadangan"])
    
    with t1:
        st.subheader("Dengerin ini kalau lagi kangen:")
        st.audio("lagu.mp3")
        st.write("**Judul Lagu:** Lagu Favorit Kita")
        st.write("**Deskripsi:** Lagu ini ngenalin banyak kenangan pas kita pertama ketemu.")

    with t2:
        st.subheader("Dengerin ini kalau lagi pengen *happy*:")
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3") # Contoh link online
        st.write("**Judul Lagu:** Lagu Ceria Kita")

elif selected_page == "💌 Pesan Rahasia":
    st.title("💌 Pesan Spesial Untukmu")
    
    st.markdown('<div class="profile-card">', unsafe_allow_html=True)
    st.subheader("Klik tombol di bawah untuk melihat pesan")
    
    pesan = st.text_input("Masukkan 'Kata Sandi Cinta' (Tanya Aku dulu):", type="password")
    
    if pesan == "sayang": # Ganti kata sandinya sesuai keinginan
        st.markdown("---")
        st.markdown("""
        ### ❤️ Sayangku... ❤️
        
        Terima kasih sudah memilihku untuk menjadi teman perjalananmu. 
        Tiap hari bersamamu adalah anugerah terbesar buatku. Aku janji bakal terus berusaha 
        bikin kamu bahagia, ngejaga kamu, dan jadi orang pertama yang selalu mendukungmu.
        
        *I love you, now and always.* ❤️
        """)
        st.heart() # Efek detak jantung
    elif pesan != "":
        st.error("Sandi salah! Cobain tanya aku lagi ya 😜")
    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# FOOTER (Bikin Rapi)
# -----------------------------------------------------------------------------
st.markdown("---")
st.markdown("<p style='text-align: center; color: #888;'>&copy; 2024 - Our Love Story | Terus Bahagia Bersama ❤️</p>", unsafe_allow_html=True)
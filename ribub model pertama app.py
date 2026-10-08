import streamlit as st

# -----------------------------------------------------------------------------
# Konfigurasi Halaman Web
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Our Journey 💕",
    page_icon="💖",
    layout="centered"
)

# Custom CSS untuk mempercantik tampilan (Warna Tema & Font)
st.markdown("""
    <style>
    .main {
        background-color: #fff0f3;
    }
    h1 {
        color: #ff4b4b;
        text-align: center;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .stSubheader {
        color: #ff758f;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Header / Judul
# -----------------------------------------------------------------------------
st.title("💖 Our Story & Journey 💖")
st.write("<p style='text-align: center; color: #555;'>Tempat kita menyimpan kenangan dan di jauhkan oleh jarak ldr hufftt.</p>", unsafe_allow_html=True)

st.divider()

# -----------------------------------------------------------------------------
# Profil Kita (Foto & Deskripsi)
# -----------------------------------------------------------------------------
st.header("👩‍❤️‍👨 Tentang Kita")
col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    # Ganti 'foto_aku.jpeg' dengan nama file fotomu nanti
    st.image("aku.jpeg", caption="gua 😎", use_container_width=True)
    st.subheader("Fa'iq")
    st.write("Suka gangguin kamu,dan jahilin kamu tiada hari tanpa bikin kamu bete rorr.")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    # Ganti 'foto_doi.jpeg' dengan nama file foto pacarmu nanti
    st.image("wnge.jpeg", caption="Kamu ✨", use_container_width=True)
    st.subheader("Ribub")
    st.write("Sosok terfavorit yanng tiap hari marah dan suka bete tapi cayang kooo,apalagi pas haid huuu mau diterkam aku.")
    st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# -----------------------------------------------------------------------------
# Galeri Kenangan / Moment
# -----------------------------------------------------------------------------
st.header("📸 Galeri Momen Indah")
st.write("Kumpulan foto-foto momen terbaik.")

# Grid Foto (3 Kolom)
g1, g2, g3 = st.columns(3)

with g1:
    st.image("date.jpeg", caption="dating💕")

with g2:
    st.image("momen best.jpeg", caption="best moment🚗")

with g3:
    st.image("graduate.jpeg", caption="graduate🎉")

st.divider()

# -----------------------------------------------------------------------------
# Pesan Manis / Pesan Rahasia
# -----------------------------------------------------------------------------
st.header("💌 Pesan Untukmu")
with st.expander("Klik untuk membuka pesan rahasia..."):
    st.write("""
        Terima kasih sudah selalu ada dan menjadi bagian terindah dalam hidupku. 
        Semoga kita bisa terus lewati LDR yang pahit ini yaa ❤️
    """)

# Footer sederhana
st.markdown("---")
st.markdown("<p style='text-align: center; color: #888;'>Dibuat dengan ❤️ dengan cinta</p>", unsafe_allow_html=True)
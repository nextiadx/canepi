# import streamlit
import streamlit as st

# Input data Nilai
nilaiPAI_S1 = st.number_input("Masukkan Nilai PAI Semester 1", min_value=1, max_value=100, step=1)
nilaiPAI_S2 = st.number_input("Masukkan Nilai PAI Semester 2", min_value=1, max_value=100, step=1)
nilaiPAI_S3 = st.number_input("Masukkan Nilai PAI Semester 3", min_value=1, max_value=100, step=1)
nilaiPAI_S4 = st.number_input("Masukkan Nilai PAI Semester 4", min_value=1, max_value=100, step=1)
nilaiPAI_S5 = st.number_input("Masukkan Nilai PAI Semester 5", min_value=1, max_value=100, step=1)

nilaiPKN_S1 = st.number_input("Masukkan Nilai PKN Semester 1", min_value=1, max_value=100, step=1)
nilaiPKN_S2 = st.number_input("Masukkan Nilai PKN Semester 2", min_value=1, max_value=100, step=1)
nilaiPKN_S3 = st.number_input("Masukkan Nilai PKN Semester 3", min_value=1, max_value=100, step=1)
nilaiPKN_S4 = st.number_input("Masukkan Nilai PKN Semester 4", min_value=1, max_value=100, step=1)
nilaiPKN_S5 = st.number_input("Masukkan Nilai PKN Semester 5", min_value=1, max_value=100, step=1)

nilaiBIndo_S1 = st.number_input("Masukkan Nilai Bahasa Indonesia Semester 1", min_value=1, max_value=100, step=1)
nilaiBIndo_S2 = st.number_input("Masukkan Nilai Bahasa Indonesia Semester 2", min_value=1, max_value=100, step=1)
nilaiBIndo_S3 = st.number_input("Masukkan Nilai Bahasa Indonesia Semester 3", min_value=1, max_value=100, step=1)
nilaiBIndo_S4 = st.number_input("Masukkan Nilai Bahasa Indonesia Semester 4", min_value=1, max_value=100, step=1)
nilaiBIndo_S5 = st.number_input("Masukkan Nilai Bahasa Indonesia Semester 5", min_value=1, max_value=100, step=1)

nilaiMTK_S1 = st.number_input("Masukkan Nilai Matematika Semester 1", min_value=1, max_value=100, step=1)
nilaiMTK_S3 = st.number_input("Masukkan Nilai Matematika Semester 2", min_value=1, max_value=100, step=1)
nilaiMTK_S2 = st.number_input("Masukkan Nilai Matematika Semester 3", min_value=1, max_value=100, step=1)
nilaiMTK_S4 = st.number_input("Masukkan Nilai Matematika Semester 4", min_value=1, max_value=100, step=1)
nilaiMTK_S5 = st.number_input("Masukkan Nilai Matematika Semester 5", min_value=1, max_value=100, step=1)

nilaiIPA_S1 = st.number_input("Masukkan Nilai IPA Semester 1", min_value=1, max_value=100, step=1)
nilaiIPA_S2 = st.number_input("Masukkan Nilai IPA Semester 2", min_value=1, max_value=100, step=1)
nilaiIPA_S3 = st.number_input("Masukkan Nilai IPA Semester 3", min_value=1, max_value=100, step=1)
nilaiIPA_S4 = st.number_input("Masukkan Nilai IPA Semester 4", min_value=1, max_value=100, step=1)
nilaiIPA_S5 = st.number_input("Masukkan Nilai IPA Semester 5", min_value=1, max_value=100, step=1)

nilaiIPS_S1 = st.number_input("Masukkan Nilai IPS Semester 1", min_value=1, max_value=100, step=1)
nilaiIPS_S2 = st.number_input("Masukkan Nilai IPS Semester 2", min_value=1, max_value=100, step=1)
nilaiIPS_S3 = st.number_input("Masukkan Nilai IPS Semester 3", min_value=1, max_value=100, step=1)
nilaiIPS_S4 = st.number_input("Masukkan Nilai IPS Semester 4", min_value=1, max_value=100, step=1)
nilaiIPS_S5 = st.number_input("Masukkan Nilai IPS Semester 5", min_value=1, max_value=100, step=1)

nilaiBIng_S1 = st.number_input("Masukkan Nilai Bahasa Inggris Semester 1", min_value=1, max_value=100, step=1)
nilaiBIng_S2 = st.number_input("Masukkan Nilai Bahasa Inggris Semester 2", min_value=1, max_value=100, step=1)
nilaiBIng_S3 = st.number_input("Masukkan Nilai Bahasa Inggris Semester 3", min_value=1, max_value=100, step=1)
nilaiBIng_S4 = st.number_input("Masukkan Nilai Bahasa Inggris Semester 4", min_value=1, max_value=100, step=1)
nilaiBIng_S5 = st.number_input("Masukkan Nilai Bahasa Inggris Semester 5", min_value=1, max_value=100, step=1)

nilaiAkreditasiSekolah = st.number_input("Masukkan Nilai Akreditasi Sekolah", min_value=1, max_value=100, step=1)
indeksSekolah = st.number_input("Masukkan Indeks Sekolah", min_value=1, max_value=100, step=1)

# Kalkulasi rata rata masing-masing mapel
ratarataPAI = (nilaiPAI_S1 + nilaiPAI_S2 + nilaiPAI_S3 + nilaiPAI_S4 + nilaiPAI_S5) / 5
ratarataPKN = (nilaiPKN_S1 + nilaiPKN_S2 + nilaiPKN_S3 + nilaiPKN_S4 + nilaiPKN_S5) / 5
ratarataBIndo = (nilaiBIndo_S1 + nilaiBIndo_S2 + nilaiBIndo_S3 + nilaiBIndo_S4 + nilaiBIndo_S5) / 5
ratarataMTK = (nilaiMTK_S1 + nilaiMTK_S2 + nilaiMTK_S3 + nilaiMTK_S4 + nilaiMTK_S5) / 5
ratarataIPA = (nilaiIPA_S1 + nilaiIPA_S2 + nilaiIPA_S3 + nilaiIPA_S4 + nilaiIPA_S5) / 5
ratarataIPS = (nilaiIPS_S1 + nilaiIPS_S2 + nilaiIPS_S3 + nilaiIPS_S4 + nilaiIPS_S5) / 5
ratarataBIng = (nilaiBIng_S1 + nilaiBIng_S2 + nilaiBIng_S3 + nilaiBIng_S4 + nilaiBIng_S5) / 5

# Kalkulasi rata rata nilai mapel keseluruhan
ratarataRapor = (ratarataPAI + ratarataPKN + ratarataBIndo + ratarataMTK + ratarataIPA + ratarataIPS + ratarataBIng) / 7

# kalkulasi Nilai Akhir
nilaiAkhirMentah = 0.5 * ratarataRapor + 0.2 * nilaiAkreditasiSekolah + 0.3 * indeksSekolah

nilaiAkhir = round(nilaiAkhirMentah)
# Print hasil
st.text(f"Nilai Akhir PPDB Anda Adalah {nilaiAkhir}")
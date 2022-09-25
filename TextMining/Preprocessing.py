"""
TUGAS 1 Pre-Processing pada Text Mining
Nama    : Christian Arthur
NIM     : 205150207111008
Kelas   : Text-Mining TIF-A
Jurnal  : https://j-ptiik.ub.ac.id/index.php/j-ptiik/article/view/9524
"""
from ctypes import resize
import spacy
# nlp = spacy.load('en_core_web_sm')
nlp=spacy.blank("id")


raw_data="Modified K-Nearest Neighbour (MK-NN) telah banyak digunakan untuk melakukan klasifikasi berbagai macam objek. Dalam melakukan klasifikasi, MK-NN menghitung jarak k tetangga terdekatnya pada data latih. Perbedaan K-Nearest Neighbour (K-NN) dengan M-KNN terdapat pada proses perhitungan validitas seluruh data latih dan weight voting. Tahapan perhitungan algoritme MK-NN yaitu menghitung jarak antar data latih, menghitung nilai validitas data latih, menghitung jarak antara data latih dengan data uji, dan menghitung weight voting. Hasil weight voting terbesar diambil sejumlah k yang digunakan. Dari hasil weight voting yang diambil, kelas dari nilai weight voting terbesar merupakan kelas penyakit dari data uji. Data tanaman kentang (Solanum tuberosum L) yang digunakan sebanyak 115 data latih dan data uji dengan 7 jenis penyakit dan 23 gejala penyakit. Akurasi sistem ini bergantung pada nilai k dan total data latih yang digunakan. Semakin besar nilai k maka semakin akurasi semakin kecil karena nilai validitas yang didapatkan semakin kecil. Semakin banyak data latih yang digunakan maka akurasi semakin tinggi karena selisih nilai Euclidian antar kelas semakin besar. Akurasi sistem terbaik didapatkan dari nilai k=4 dan total data latih sebanyak 45 yaitu 97.142857%."
result=[]
print("sebelum preprocess:"," {}".format(raw_data),sep="\n")
# 1. Case folding
hasil_cf=str.lower(raw_data)

# 2. Tokenizing, filtering, dan lemmatizing

# Tokenizing
doc=nlp(hasil_cf)
for word in doc:
    # Filtering(menghilangkan tanda baca dan stop word)
    if not word.is_punct and not word.is_stop:
        result.append(word.text)
        # Lemmatizing pada library ini tidak berfungsi sehingga hanya berhenti di filtering stop words
        # result.append(word.lemma_) # method yang tidak berjalan
        

print()
print("setelah preprocess:"," ".join(result),sep="\n")
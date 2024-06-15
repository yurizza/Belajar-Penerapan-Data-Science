# Proyek Akhir : Menyelesaikan Permasalahan Edutech

### Pemahaman Bisnis

Jaya Jaya Institut, sebuah institusi pendidikan terkemuka yang telah beroperasi sejak tahun 2000, memiliki reputasi yang sangat baik dalam mencetak lulusan berkualitas tinggi. Namun, institusi ini menghadapi tantangan serius dengan tingginya angka dropout siswa, yang dapat merusak reputasi dan efisiensi operasionalnya. Dengan mengidentifikasi siswa yang berpotensi untuk dropout lebih awal, Jaya Jaya Institut dapat memberikan bimbingan dan dukungan yang diperlukan untuk meningkatkan retensi siswa dan memastikan kelulusan mereka, sehingga mempertahankan reputasi institusi serta meningkatkan kepuasan dan keberhasilan siswa.

### Rumusan Masalah

Bagaimana Jaya Jaya Institut dapat mendeteksi lebih awal siswa yang berpotensi dropout sehingga dapat diberikan bimbingan khusus untuk meningkatkan retensi dan keberhasilan akademik siswa? Pertanyaan ini dapat diuraikan menjadi beberapa sub-masalah yang lebih spesifik:
1. Apa faktor-faktor utama yang menyebabkan tingginya tingkat dropout siswa di Jaya Jaya Institut?
2. Bagaimana motivasi belajar, kesejahteraan psikologis, dukungan akademik, dan lingkungan sosial saat ini mempengaruhi retensi siswa di institusi ini?
3. Strategi apa yang dapat diterapkan oleh manajemen untuk meningkatkan motivasi dan retensi siswa?
4. Apa saja best practice dalam manajemen pendidikan yang dapat diadopsi oleh Jaya Jaya Institut untuk mengurangi tingkat dropout?

## Lingkup Proyek

1. **Pengumpulan Data:** Mengumpulkan data siswa, termasuk informasi pribadi, prestasi akademik, kehadiran, dan keterlibatan ekstrakurikuler.
2. **Analisis Data Awal:** Menganalisis data untuk mengidentifikasi tren dan pola yang berkaitan dengan dropout.
3. **Rekayasa Fitur:** Membuat fitur baru berdasarkan analisis data untuk meningkatkan performa model prediksi.
4. **Pemodelan dan Prediksi:** Membangun model machine learning untuk memprediksi kemungkinan dropout siswa.
5. **Pembuatan Dasbor Bisnis:** Membuat dasbor interaktif untuk memonitor faktor-faktor yang mempengaruhi dropout.
6. **Pembuatan Aplikasi Streamlit:** Mengembangkan aplikasi web dengan Streamlit untuk memprediksi kemungkinan dropout siswa.
7. **Dokumentasi dan Pelaporan:** Mendokumentasikan seluruh proses proyek dan menyusun laporan hasil analisis.
8. **Rekomendasi Tindakan:** Memberikan rekomendasi tindakan kepada manajemen berdasarkan temuan dari analisis.
9. **Implementasi Program Intervensi:** Merancang dan menerapkan program bimbingan khusus untuk siswa yang teridentifikasi berisiko tinggi dropout.
10. **Evaluasi dan Pemantauan:** Melakukan evaluasi berkala terhadap efektivitas program intervensi dan model prediksi, serta melakukan penyesuaian yang diperlukan untuk meningkatkan hasil.

Melalui lingkup proyek ini, diharapkan Jaya Jaya Institut dapat memahami lebih baik faktor-faktor yang memengaruhi dropout siswa dan dapat mengambil tindakan yang sesuai untuk meningkatkan retensi dan keberhasilan akademik siswa.

## Persiapan

### Sumber

[Tautan ke Sumber Data](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md)

### Instalasi

1. **Pastikan Python terinstal**
   - Pastikan Python versi 3.x terinstal di sistem Anda. Anda dapat mengunduh dan menginstalnya dari [python.org](https://www.python.org/).

2. **Buat lingkungan virtual**
   - Buat lingkungan virtual untuk mengisolasi dependensi proyek. Jalankan perintah berikut di terminal Anda:
     ```bash
     python -m venv env
     ```

3. **Aktifkan lingkungan virtual**
   - Untuk Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - Untuk macOS/Linux:
     ```bash
     source env/bin/activate
     ```

4. **Pasang dependensi menggunakan `requirements.txt`**
   - Pastikan Anda berada di direktori proyek yang sama dengan file `requirements.txt`, lalu jalankan perintah berikut:
     ```bash
     pip install -r requirements.txt
     ```

Dengan langkah-langkah di atas, Anda telah siap untuk memulai proyek dengan lingkungan yang bersih dan terisolasi.

### Struktur Direktori Proyek

```
HR-Attrition-Analytics
├───data
│       data.csv
│       df_final.csv
│
├───image
│       feature_importances.png
|       logo.png
│
├───model
│       best_standard_scaler.pkl
│       best_trained_model.pkl
│
├───app.py
├───notebook.ipynb
├───README.md
├───requirements.txt
├───yuriza-dashboard.png
├───yuriza-video.mp4
```

## Persiapan Notebook

Untuk mempersiapkan Notebook dan melanjutkan langkah-langkah yang Anda sebutkan, berikut adalah beberapa langkah yang dapat Anda ikuti:

### Langkah 1: Buka Notebook Jupyter
1. Buka terminal atau command prompt.
2. Ketik perintah `jupyter notebook` dan tekan Enter. Ini akan membuka antarmuka Notebook Jupyter di browser web Anda.

### Langkah 2: Lakukan Analisis Data Eksploratif (EDA)
1. Baca dataset yang Anda miliki ke dalam notebook.
2. Lakukan eksplorasi data untuk memahami struktur, pola, dan statistik penting.
3. Identifikasi atribut-atribut yang mungkin berperan penting dalam pembentukan model machine learning.

### Langkah 3: Skalasi Atribut dengan StandardScaler
1. Identifikasi atribut yang memerlukan skala, terutama jika terdapat atribut numerik yang memiliki rentang nilai yang berbeda.
2. Gunakan scaler seperti `StandardScaler` dari scikit-learn untuk melakukan skala pada atribut numerik.
   
### Langkah 4: Buat Model dengan Random Forest
1. Pisahkan data menjadi atribut (fitur) dan target.
2. Bagi data menjadi set pelatihan dan pengujian.
3. Buat model Random Forest menggunakan `RandomForestClassifier` dari scikit-learn.
4. Definisikan grid search CV untuk mendapatkan parameter terbaik.
5. Latih model menggunakan data pelatihan.
6. Evaluasi kinerja model menggunakan data pengujian.
7. Cek feature importance dari model yang terbentuk.
8. Simpan model dan encoder ke dalam folder model.

### Langkah 5: Buat Streamlit GUI untuk Klasifikasi Karyawan
1. Buat file Python baru untuk membuat aplikasi Streamlit.
2. Impor library yang diperlukan seperti pandas, joblib, sklearn, dan streamlit.
3. Muat model dan encoder yang telah disimpan sebelumnya.
4. Buat antarmuka pengguna menggunakan elemen-elemen Streamlit.
5. Tentukan logika untuk mengklasifikasikan student berdasarkan input pengguna.

### Langkah 6: Jalankan Streamlit
1. Jalankan perintah `streamlit run nama_file.py` di terminal atau command prompt, di mana `prediction.py` adalah nama file Python yang berisi kode Streamlit.
     ```bash
     streamlit run app.py
     ```

## Pembuatan Dasbor

- Manfaatkan [Looker Studio](https://lookerstudio.google.com/)
- Simpan tangkapan layar sebagai `<username>-dashboard.png`

## Dokumentasi

- Dokumentasikan proses dalam `readme.md`

## Dasbor Bisnis

Hasil pemodelan machine learning menunjukkan beberapa kolom yang memiliki dampak signifikan pada dropout, ditampilkan dalam Looker Studio.

[Tautan ke Dasbor Bisnis](https://lookerstudio.google.com/reporting/d3421a48-4500-4221-a7ee-105154cb8460)

Dasbor tersebut memperlihatkan hubungan antara beberapa kolom dan Dropout atau Graduate.

### Isi Dashboard

1. **Key Performance Indicators (KPI)**

   KPI merupakan metrik-metrik utama yang digunakan untuk mengukur kinerja dan efektivitas berbagai aspek yang berhubungan dengan karyawan. Berikut adalah penjelasan singkat mengenai beberapa KPI yang penting:

   - **Total Student**
     - **Definisi**: Jumlah total siswa yang terdaftar di Jaya Jaya Institut pada saat ini.
     - **Fungsi**: Menyediakan gambaran tentang ukuran institusi dan populasi siswa saat ini.

   - **Persentase Gender**
     - **Definisi**: Perbandingan persentase siswa perempuan dan laki-laki di institusi.
     - **Fungsi**: Memahami demografi siswa secara gender untuk perencanaan kebijakan pendidikan dan dukungan siswa.

   - **Dropout Rate**
     - **Definisi**: Persentase siswa yang tidak menyelesaikan pendidikan mereka di Jaya Jaya Institut.
     - **Fungsi**: Indikator untuk mengevaluasi efektivitas program pendidikan dan identifikasi masalah yang mempengaruhi retensi siswa.

2. **Bar Chart: Scholarship Holder vs Status**

   Grafik batang ini membandingkan jumlah siswa penerima beasiswa dengan status mereka (dropout atau graduate). Informasi ini membantu dalam melihat apakah penerimaan beasiswa berhubungan dengan tingkat retensi siswa.

3. **Gender vs Status**

   Grafik ini memperlihatkan perbandingan antara gender siswa dengan status mereka (dropout atau graduate). Analisis ini dapat memberikan wawasan tentang apakah ada perbedaan dalam tingkat retensi antara siswa perempuan dan laki-laki.

4. **Curricular Units 1st Enrolled vs Status**

   Grafik ini menunjukkan hubungan antara unit kurikuler yang diambil pada semester pertama dengan status siswa (dropout atau graduate). Informasi ini membantu dalam memahami apakah pilihan mata pelajaran awal mempengaruhi keputusan siswa untuk tetap berada di institusi.

5. **Curricular Units 1st Sem Credited vs Status**

   Grafik ini menggambarkan hubungan antara jumlah unit kurikuler yang diakui pada semester pertama dengan status siswa (dropout atau graduate). Analisis ini dapat mengungkap apakah kemajuan akademis awal berpengaruh terhadap retensi siswa.

6. **Curricular Units 2nd Enrolled vs Status**

   Grafik ini membandingkan jumlah unit kurikuler yang diambil pada semester kedua dengan status siswa (dropout atau graduate). Data ini membantu dalam memahami apakah keberlanjutan perkembangan akademis mempengaruhi keputusan siswa untuk tetap melanjutkan studi.

7. **Previous Qualification Grade vs Status**

   Grafik ini menunjukkan hubungan antara nilai kualifikasi sebelumnya dengan status siswa (dropout atau graduate). Informasi ini dapat memberikan wawasan tentang seberapa kuat hubungan antara kualifikasi sebelumnya dengan keberhasilan siswa di institusi ini.

Dengan menggunakan dashboard ini, Jaya Jaya Institut dapat memantau dan menganalisis data untuk memahami faktor-faktor yang mempengaruhi dropout siswa, serta mengambil tindakan yang sesuai untuk meningkatkan retensi dan keberhasilan akademik siswa.

### Kesimpulan

#### Faktor Utama yang Mempengaruhi Dropout Siswa:

Berdasarkan analisis data, faktor-faktor utama yang mempengaruhi tingkat dropout siswa di Jaya Jaya Institut meliputi:
- Status sebagai penerima beasiswa (Scholarship Holder)
- Gender siswa
- Unit kurikuler yang diambil pada semester pertama (Curricular Units 1st Enrolled)
- Kemajuan akademis pada semester pertama (Curricular Units 1st Sem Credited)
- Unit kurikuler yang diambil pada semester kedua (Curricular Units 2nd Enrolled)
- Nilai kualifikasi sebelumnya (Previous Qualification Grade)

#### Model Prediksi dan Akurasi:

Sebuah model prediksi menggunakan algoritma Random Forest telah dikembangkan dan disesuaikan dengan menggunakan grid search CV untuk tuning hyperparameter. Model ini mencapai akurasi sebesar 90% dalam memprediksi siswa yang berisiko dropout, dengan 53 siswa yang sebenarnya dropout namun diprediksi lulus.

#### Business Dashboard:

Dashboard bisnis telah dirancang untuk memberikan visibilitas terhadap faktor-faktor yang mempengaruhi dropout siswa. Dashboard ini mencakup Key Performance Indicators (KPIs) seperti Total Student, Persentase Gender, dan Dropout Rate. Selain itu, dashboard juga menyajikan visualisasi seperti Bar Chart untuk Scholarship Holder VS Status dan Gender VS Status untuk memberikan pemahaman yang lebih dalam terhadap faktor-faktor tersebut.

### Rekomendasi Tindakan

- **Penguatan Dukungan Akademik:** Menyediakan program pembinaan dan mentoring untuk siswa penerima beasiswa dan siswa dengan kemajuan akademis yang menurun.
  
- **Pemantauan Kemajuan Akademis:** Implementasikan sistem pemantauan kemajuan akademis secara teratur untuk mengidentifikasi siswa yang memerlukan intervensi lebih lanjut.
  
- **Perbaikan Kurikulum dan Pembelajaran:** Evaluasi dan diversifikasi kurikulum untuk memastikan relevansi dan keterlibatan siswa, terutama pada mata pelajaran awal yang mempengaruhi keputusan awal siswa untuk melanjutkan pendidikan.
  
- **Kolaborasi dengan Orang Tua dan Stakeholder:** Melibatkan orang tua dan stakeholder dalam mendukung pendidikan siswa dan mendapatkan wawasan tentang faktor-faktor yang mempengaruhi keberhasilan siswa.
  
- **Pengembangan Program Keseimbangan Kehidupan:** Menyediakan program kesejahteraan siswa yang mendukung kesehatan mental dan emosional mereka, serta membantu dalam menjaga keseimbangan antara kehidupan akademis dan non-akademis.

Dengan mengimplementasikan rekomendasi ini, diharapkan Jaya Jaya Institut dapat mengurangi tingkat dropout siswa dan meningkatkan kesuksesan serta keberlanjutan pendidikan siswa mereka.

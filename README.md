# Proyek Akhir : Menyelesaikan Permasalahan Human Resources

## Pemahaman Bisnis

Jaya Jaya Maju adalah sebuah perusahaan multinasional yang didirikan pada tahun 2000 dan kini telah memiliki lebih dari 1000 karyawan yang tersebar di seluruh negeri. Meskipun perusahaan ini telah berkembang menjadi entitas bisnis yang besar, Jaya Jaya Maju masih menghadapi tantangan signifikan dalam mengelola karyawannya. Salah satu masalah utama yang dihadapi adalah tingginya tingkat pergantian karyawan (attrition rate) yang mencapai lebih dari 10%. Tingginya tingkat pergantian karyawan ini menunjukkan adanya masalah dalam manajemen sumber daya manusia, yang mungkin mencakup kepuasan kerja, keseimbangan kehidupan kerja, pengembangan karir, atau budaya organisasi. Masalah ini tidak hanya berdampak pada produktivitas dan efisiensi operasional perusahaan, tetapi juga menimbulkan biaya tambahan terkait rekrutmen dan pelatihan karyawan baru, serta berpotensi mengganggu stabilitas dan keberlanjutan bisnis Jaya Jaya Maju di masa depan.

Jika tingkat pergantian karyawan ini terus meningkat, perusahaan dapat menghadapi beberapa konsekuensi serius. Pertama, biaya yang dikeluarkan untuk rekrutmen dan pelatihan karyawan baru akan terus meningkat, menguras sumber daya finansial yang seharusnya dapat digunakan untuk pengembangan bisnis atau inovasi. Kedua, seringnya pergantian karyawan dapat mengganggu kontinuitas dan konsistensi operasional, yang berpotensi menurunkan kualitas layanan atau produk yang dihasilkan. Hal ini dapat berdampak negatif pada reputasi perusahaan di mata pelanggan dan mitra bisnis.

Selain itu, tingginya attrition rate dapat menimbulkan dampak jangka panjang yang lebih serius, seperti menurunnya moral dan semangat kerja di kalangan karyawan yang masih bertahan. Mereka mungkin merasa tidak aman dalam pekerjaan mereka atau kehilangan kepercayaan pada manajemen perusahaan. Jika situasi ini tidak segera diatasi, perusahaan dapat mengalami kesulitan dalam menarik talenta baru yang berkualitas, karena calon karyawan mungkin melihat perusahaan sebagai tempat kerja yang tidak stabil. Dalam jangka panjang, hal ini bisa menghambat pertumbuhan dan perkembangan Jaya Jaya Maju, mengurangi daya saingnya di pasar, dan akhirnya mengancam kelangsungan bisnisnya.

## Rumusan Masalah

Bagaimana Jaya Jaya Maju dapat mengurangi tingkat pergantian karyawan yang tinggi untuk meningkatkan produktivitas, efisiensi operasional, dan stabilitas bisnisnya di masa depan.
Pertanyaan ini dapat diuraikan menjadi beberapa sub-masalah yang lebih spesifik:
1. Apa faktor-faktor utama yang menyebabkan tingginya tingkat pergantian karyawan di Jaya Jaya Maju?
2. Bagaimana kepuasan kerja, keseimbangan kehidupan kerja, pengembangan karir, dan budaya organisasi saat ini mempengaruhi retensi karyawan di perusahaan?
3. Strategi apa yang dapat diterapkan oleh manajemen untuk meningkatkan kepuasan dan retensi karyawan?
4. Apa saja best practice dalam manajemen sumber daya manusia yang dapat diadopsi oleh Jaya Jaya Maju untuk mengurangi attrition rate?

## Lingkup Proyek

1. **Pengumpulan Data:** Mengumpulkan data karyawan, termasuk informasi pribadi, performa, dan kehadiran.
2. **Analisis Data Awal:** Menganalisis data untuk mengidentifikasi tren dan pola yang berkaitan dengan atrisi.
3. **Rekayasa Fitur:** Membuat fitur baru berdasarkan analisis data untuk meningkatkan performa model prediksi.
4. **Pemodelan dan Prediksi:** Membangun model machine learning untuk memprediksi kemungkinan atrisi karyawan.
5. **Pembuatan Dasbor Bisnis:** Membuat dasbor interaktif untuk memonitor faktor-faktor yang mempengaruhi atrisi.
6. **Pembuatan Aplikasi Streamlit:** Mengembangkan aplikasi web dengan Streamlit untuk memprediksi atrisi karyawan baru.
7. **Dokumentasi dan Pelaporan:** Mendokumentasikan seluruh proses proyek dan menyusun laporan hasil analisis.
8. **Rekomendasi Tindakan:** Memberikan rekomendasi tindakan kepada manajemen berdasarkan temuan dari analisis.

Melalui lingkup proyek ini, diharapkan Jaya Jaya Maju dapat memahami lebih baik faktor-faktor yang memengaruhi atrisi karyawan dan dapat mengambil tindakan yang sesuai untuk meningkatkan retensi karyawan.

## Persiapan

### Sumber

[Tautan ke Sumber Data](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)

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
│       employee_data.csv
│       new_employee_data.csv
│
├───image
│       logo.png
│
├───model
│       encoder.pkl
│       trained_model.pkl
│
├───README.md
├───notebook.ipynb
├───notebook.py
├───prediction.py
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

### Langkah 3: Encoder Atribut dengan One Hot Encoding
1. Identifikasi atribut yang memerlukan one hot encoding, terutama jika terdapat atribut kategorikal yang perlu diubah menjadi bentuk numerik.
2. Gunakan encoder seperti `OneHotEncoder` dari scikit-learn untuk melakukan encoding.

### Langkah 4: Buat Model dengan Random Forest
1. Pisahkan data menjadi atribut (fitur) dan target.
2. Bagi data menjadi set pelatihan dan pengujian.
3. Buat model Random Forest menggunakan `RandomForestClassifier` dari scikit-learn.
4. Latih model menggunakan data pelatihan.
5. Evaluasi kinerja model menggunakan data pengujian.
6. Cek Feature Importance dari model yang terbentuk.
7. Simpan model dan encoder ke dalam folder model.

### Langkah 5: Buat Streamlit GUI untuk Klasifikasi Karyawan
1. Buat file Python baru untuk membuat aplikasi Streamlit.
2. Impor library yang diperlukan seperti pandas, joblib, numpy, dan streamlit.
3. Muat model dan encoder yang telah disimpan sebelumnya.
4. Buat antarmuka pengguna menggunakan elemen-elemen Streamlit.
5. Tentukan logika untuk mengklasifikasikan karyawan berdasarkan input pengguna.

### Langkah 6: Jalankan Streamlit
1. Jalankan perintah `streamlit run nama_file.py` di terminal atau command prompt, di mana `prediction.py` adalah nama file Python yang berisi kode Streamlit.
     ```bash
     streamlit run prediction.py
     ```

## Pembuatan Dasbor

- Manfaatkan [Looker Studio](https://lookerstudio.google.com/)
- Simpan tangkapan layar sebagai `<username>-dashboard.png`

## Dokumentasi

- Dokumentasikan proses dalam `readme.md`

## Dasbor Bisnis

Hasil pemodelan machine learning menunjukkan beberapa kolom yang memiliki dampak signifikan pada atrisi, ditampilkan dalam Looker Studio.

[Tautan ke Dasbor Bisnis](https://lookerstudio.google.com/reporting/b5f56f3b-291a-4b23-a80e-63af0621ef07)

Dasbor tersebut memperlihatkan hubungan antara beberapa kolom dan tingkat atrisi.

### Isi Dashboard

1. **Key Performance Indicators (KPIs)**
   
   KPIs merupakan metrik-metrik utama yang digunakan untuk mengukur kinerja dan efektivitas berbagai aspek yang berhubungan dengan karyawan. Berikut adalah penjelasan singkat mengenai beberapa KPI yang penting:

   - **Total Karyawan (Headcount)**
     - **Definisi**: Total jumlah karyawan yang saat ini bekerja di perusahaan.
     - **Fungsi**: Metrik ini memberikan gambaran tentang ukuran perusahaan dan sumber daya manusia yang tersedia. Hal ini penting untuk perencanaan sumber daya, pengaturan kerja, dan pengembangan karir.

   - **Rata-rata Usia (Average Age)**
     - **Definisi**: Usia rata-rata dari semua karyawan di perusahaan.
     - **Fungsi**: Informasi ini dapat membantu dalam memahami demografi tenaga kerja. Usia rata-rata dapat mempengaruhi dinamika tim, kebutuhan pelatihan, dan perencanaan suksesi.

   - **Tingkat Pergantian Karyawan (Attrition Rate)**
     - **Definisi**: Rasio jumlah karyawan yang keluar dibandingkan dengan total karyawan keseluruhan dalam periode tertentu.
     - **Fungsi**: Tingkat pergantian yang tinggi bisa menjadi indikasi masalah dalam manajemen sumber daya manusia seperti kepuasan kerja yang rendah, gaji yang tidak kompetitif, atau budaya kerja yang kurang baik. Mengelola tingkat attrisi penting untuk menjaga stabilitas dan kontinuitas operasional.

   - **Pendapatan Bulanan Rata-rata (Average Monthly Income)**
     - **Definisi**: Rata-rata penghasilan yang diterima karyawan per bulan.
     - **Fungsi**: Metrik ini memberikan wawasan tentang kompensasi yang diberikan kepada karyawan. Ini penting untuk memastikan bahwa perusahaan memberikan gaji yang kompetitif untuk menarik dan mempertahankan talenta.

   - **Kepuasan Lingkungan Kerja Rata-rata (Average Environment Satisfaction)**
     - **Definisi**: Tingkat rata-rata kepuasan karyawan terhadap lingkungan kerja mereka.
     - **Fungsi**: Kepuasan lingkungan kerja mencakup faktor-faktor seperti kondisi fisik tempat kerja, hubungan antar karyawan, dan keseimbangan kehidupan kerja. Kepuasan yang tinggi biasanya berhubungan dengan produktivitas yang lebih baik dan tingkat pergantian karyawan yang lebih rendah.

2. **Stacked Barchart: Monthly Income vs Attrition**

   Grafik ini menampilkan hubungan antara pendapatan bulanan dan tingkat pergantian karyawan. Data dibagi menjadi 20 rentang (bins) dengan rentang masing-masing 949.5, yang dihitung dari nilai maksimum dan minimum pendapatan bulanan karyawan dan dibagi menjadi 20 bagian.

3. **Age vs Attrition**

   Grafik ini membandingkan usia karyawan dengan tingkat pergantian (attrition). Mengetahui hubungan antara usia dan kecenderungan untuk meninggalkan pekerjaan dapat membantu dalam memahami pola dan faktor-faktor yang mempengaruhi keputusan karyawan untuk bertahan atau keluar.

4. **Years in Current Role vs Attrition**

   Grafik ini memperlihatkan hubungan antara jumlah tahun dalam peran saat ini dengan tingkat pergantian. Analisis ini membantu dalam mengevaluasi apakah lama berada dalam peran tertentu mempengaruhi kecenderungan karyawan untuk bertahan atau mencari peluang baru.

5. **Number of Companies Worked vs Attrition**

   Grafik ini menunjukkan hubungan antara jumlah perusahaan tempat karyawan sebelumnya bekerja dengan tingkat pergantian. Memahami sejarah kerja karyawan dapat memberikan wawasan tentang stabilitas pekerjaan mereka dan faktor-faktor yang memengaruhi keputusan mereka untuk tinggal atau pergi.

6. **Distance from Home vs Attrition**

   Grafik ini menggambarkan hubungan antara jarak tempuh dari rumah ke tempat kerja dengan tingkat pergantian. Memahami dampak jarak perjalanan terhadap kepuasan kerja dan keseimbangan kehidupan kerja dapat membantu dalam merancang kebijakan yang mendukung kesejahteraan karyawan.

7. **Percent Salary Hike vs Attrition**

   Grafik ini menampilkan hubungan antara persentase kenaikan gaji dengan tingkat pergantian. Kenaikan gaji yang lebih rendah dari harapan karyawan dapat menjadi faktor yang mempengaruhi keputusan mereka untuk mencari peluang lain.

8. **Overtime vs Attrition**

   Grafik ini membandingkan jumlah kerja lembur dengan tingkat pergantian. Pemahaman terhadap dampak kerja lembur terhadap kepuasan kerja dan keseimbangan kehidupan kerja karyawan dapat membantu dalam mengidentifikasi faktor-faktor yang menyebabkan tingkat attrisi yang tinggi.
## Kesimpulan

1. **Identifikasi Faktor Utama yang Mempengaruhi Tingkat Pergantian Karyawan:**
   - Faktor-faktor seperti usia (Age), lama bekerja dalam peran saat ini (Years in Current Role), jumlah perusahaan tempat bekerja sebelumnya (Number of Companies Worked), jarak dari rumah ke tempat kerja (Distance from Home), kenaikan persentase gaji (Percent Salary Hike), serta lembur (Overtime) telah diidentifikasi sebagai faktor-faktor yang berpengaruh terhadap tingkat pergantian karyawan.

2. **Model Prediksi:**
   - Sebuah model prediksi telah berhasil dikembangkan menggunakan algoritma Random Forest dengan akurasi sebesar 84%. Model ini dapat memprediksi kemungkinan atrisi karyawan berdasarkan atribut-atribut yang telah diidentifikasi.

3. **Business Dashboard:**
   - Dashboard bisnis telah dibuat untuk memberikan visibilitas yang jelas terhadap kinerja perusahaan dan faktor-faktor yang mempengaruhi atrisi karyawan. Dashboard ini mencakup Key Performance Indicators (KPIs) seperti Total Karyawan, Rata-rata Usia, Tingkat Pergantian Karyawan, Pendapatan Bulanan Rata-rata, serta Kepuasan Lingkungan Kerja Rata-rata. Selain itu, dashboard juga mencakup visualisasi lain seperti Stacked Barchart untuk membandingkan Monthly Income vs Attrition, serta grafik lainnya untuk memperoleh pemahaman yang lebih dalam tentang hubungan antara faktor-faktor tersebut dengan tingkat atrisi.

Dengan mengimplementasikan hasil-hasil ini, Jaya Jaya Maju dapat meningkatkan retensi karyawan, mengoptimalkan produktivitas, dan memperkuat stabilitas bisnisnya di masa depan.

## Rekomendasi Tindakan

Dari uraian masalah yang telah disajikan, kita dapat merumuskan dari rumusan masalah sebagai berikut:

1. **Strategi untuk Meningkatkan Kepuasan dan Retensi Karyawan:**
   - Meningkatkan kepuasan kerja dan lingkungan kerja dengan mendengarkan dan merespons masukan karyawan, serta menciptakan budaya kerja yang inklusif dan mendukung.
   - Menawarkan peluang pengembangan karir dan pelatihan yang jelas dan berkelanjutan bagi karyawan.
   - Memberikan kenaikan gaji yang kompetitif dan kebijakan insentif lainnya untuk meningkatkan motivasi dan loyalitas karyawan.
   - Mengurangi beban kerja yang berlebihan dan mengelola waktu kerja yang seimbang untuk mengurangi lembur dan kelelahan karyawan.

2. **Best Practice dalam Manajemen Sumber Daya Manusia:**
   - Melakukan survei dan analisis secara berkala terhadap kepuasan karyawan untuk mengidentifikasi masalah dan peluang perbaikan.
   - Menerapkan program-program kesejahteraan karyawan yang holistik, termasuk fleksibilitas kerja, dukungan kesehatan mental, dan program keseimbangan kehidupan kerja.
   - Membangun komunikasi yang terbuka dan transparan antara manajemen dan karyawan untuk meningkatkan keterlibatan dan kepercayaan.
   - Mendorong kolaborasi dan pertumbuhan profesional melalui pengembangan tim dan program mentorship.

Dengan memperhatikan faktor-faktor tersebut dan menerapkan strategi yang sesuai, Jaya Jaya Maju dapat mengurangi tingkat pergantian karyawan dan meningkatkan produktivitas, efisiensi operasional, serta stabilitas bisnisnya di masa depan.

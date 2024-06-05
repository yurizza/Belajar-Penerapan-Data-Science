# Proyek Akhir : Menyelesaikan Permasalahan Human Resources

## Pemahaman Bisnis

Jaya Jaya Maju merupakan perusahaan multinasional yang telah berdiri sejak tahun 2000. Perusahaan ini memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. Namun, meskipun menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih menghadapi kesulitan dalam mengelola karyawan, yang berdampak pada tingginya tingkat atrisi, mencapai lebih dari 16%.

Untuk mengatasi masalah ini, manajer departemen SDM meminta bantuan untuk mengidentifikasi faktor-faktor yang memengaruhi tingginya tingkat atrisi. Selain itu, mereka juga meminta pembuatan dasbor bisnis untuk memonitor faktor-faktor tersebut.

## Rumusan Masalah

Tingginya tingkat atrisi mencapai 16% memiliki dampak yang signifikan, termasuk terhadap produktivitas, kestabilan tim, dan biaya pelatihan karyawan baru.

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

- Pastikan Python terinstal
- Buat lingkungan virtual
- Pasang dependensi menggunakan `requirements.txt`

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

1. Buka Notebook Jupyter
2. Lakukan analisis data eksploratif dan pemodelan machine learning

## Pembuatan Dasbor

- Manfaatkan Looker Studio
- Simpan tangkapan layar sebagai `<username>-dashboard.png`

## Dokumentasi

- Dokumentasikan proses dalam `readme.md`

## Dasbor Bisnis

Hasil pemodelan machine learning menunjukkan beberapa kolom yang memiliki dampak signifikan pada atrisi, ditampilkan dalam Looker Studio.

[Tautan ke Dasbor Bisnis](https://lookerstudio.google.com/reporting/b5f56f3b-291a-4b23-a80e-63af0621ef07)

Dasbor tersebut memperlihatkan hubungan antara beberapa kolom dan tingkat atrisi.

## Kesimpulan

1. Sepuluh kolom teratas yang memengaruhi atrisi adalah MonthlyIncome, Age, DistanceFromHome,  YearsInCurrentRole, NumCompaniesWorked, PercentSalaryHike, OverTime_Yes, TrainingTimesLastYear, EnvironmentSatisfaction, JobSatisfaction
2. Model machine learning mencapai akurasi 84% menggunakan Random Forest.
3. Lakukan evaluasi dengan bertanya mengapa karyawan mengundurkan diri.
4. Usia muda, gaji rendah, pendidikan Sarjana, dan lembur cenderung menyebabkan atrisi.
5. Kenaikan gaji persentase rendah dan jarak dekat (< 9km) juga cenderung menyebabkan atrisi.

## Rekomendasi Tindakan

1. Mendekati karyawan dengan kemungkinan atrisi tinggi berdasarkan model ML.
2. Meningkatkan gaji.
3. Karyawan muda lebih suka mendapatkan penghargaan atas pencapaian.
4. Lakukan evaluasi bulanan terhadap karyawan untuk memungkinkan mereka mengungkapkan kekhawatiran/kesulitan.
5. Tingkatkan kenaikan gaji persentase.
6. Hindari lembur; jika perlu, berikan kompensasi yang cukup.

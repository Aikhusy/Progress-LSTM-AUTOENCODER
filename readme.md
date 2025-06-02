Progress 28/05/2025

untuk Feature ada 8 (masih uji coba)


fw_load_avg_1_min 
fw_load_avg_5_min
fw_load_avg_15_min
fw_cpu_used
mem_used
root_used
log_used
fw_total_alloc

untuk yang telah saya lakukan 

preprocessing
1. melakukan normalisasi data menjadi data scaled menggunakan minmax scaler
2. membagi data menjadi 10 sliding windows/ sequence

preprocessing training
1. untuk training data dibersihkan dari outlier
2. untuk testing data tidak dibersihkan dari outlier 
3. dibagi menjadi 80% training 20% testing

perubahan sedikit
1. sebelumnya menggunakan feature eng
2. sebelumnya data training dan testing masih mengandung data outlier

-SAVEMODEL.ipynb adalah file untuk training data (menggunakan data.csv)

-LOADMODEL.ipynb adalah file untuk testing data (menggunakan data300.csv)



untuk testing 300 data 
1. model saya menemukan bahwa [31, 34, 47, 48, 49, 50, 51, 57, 58, 59, 60, 61, 62, 63, 164, 165, 166, 167]
2. untuk isolation forest menemukan bahwa [ 57  58  59  60  61  62  63  64  65  66 202 204 205 206 207 208 277 278
 279]

3. irisannya adalah [57, 58, 59, 60, 61, 62, 63]
4. yang dimana index ke 57 mengandung data yang memang saya rubah menjadi data outlier [1,31;1,18;2,16;2;7836684;20076408;20258012;472676803;2025-10-03 12:07:02.830]

problem 
1. apakah ini sudah cukup baik, bagaimana menurut panjhennengan
2. apa yang harus saya lakukan supaya lebih baik?
--------------------------------------------------------------------
testing 29/05/2025

1. menambah fitur rx packet dan tx packet
2. Mencoba menyederhanakan model 
3. hasilnya ketika menggunakan data anomali dari testing 300
4. anomalinya terdeteksi dengan baik 

1. apakah ini sudah bagus?
--------------------------------------------------------------------
Final 02/06/2025

1. model LSTM sudah bisa mendeteksi anomali outlier
2. model LSTM sudah bisa mendeteksi anomali data random yang tidak melebihi outlier


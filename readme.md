Progress 28/05/2025

untuk Feature ada 7 (masih uji coba)
fw_load_avg_1_min;fw_load_avg_5_min;fw_load_avg_15_min;fw_cpu_used;mem_used;root_used;log_used;fw_total_alloc;

untuk yang telah saya lakukan 

preprocessing
1. penganganan missing value dengan interpolasi data
2. melakukan normalisasi data menjadi data scaled menggunakan minmax scaler
3. membagi data menjadi 5 sliding windows

preprocessing training
untuk training data dibersihkan dari outlier
untuk testing data tidak dibersihkan dari outlier 
dibagi menjadi 80% training 20% testing

perubahan sedikit
1. sebelumnya menggunakan feature eng
2. sebelumnya data training dan testing masih mengandung data outlier

problem 
1. apakah ini sudah cukup baik, bagaimana menurut panjhennengan
2. apa yang harus saya lakukan supaya lebih baik?
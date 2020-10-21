GETTING START
Untuk Windows.
Buat virtual environment :
1. python -m venv (project name)
2. (project name)\Scripts\activate.bat

Download libraries:
1. pip install -r requirements.txt

Start program :
1. python PPLJ_signup.py

PENGGUNAAN APLIKASI
Token TOTP :
1. Download aplikasi FreeOTP
2. Pilih logo kunci+ yang terdapat di pojok kanan aplikasi freeOTP
3. Bagian paling atas (jdoe@example.com) diisi dengan nama aplikasi, dalam hal ini 'Password Manager'.
4. Bagian kedua dari atas diisi nama akun password Manager.
5. Bagian 'secret' diisi dengan otp_secret yang diberikan oleh server.
6. Konfigurasi lain :
-Type 		: TOTP
-Digits		: 6
-Algorithm	: SHA1
-Interval	: 30

Telah disediakan akun kosong untuk uji coba :
Username	: ujicobaPPLJ
password	: 123
otp_secret	: NMSWIMFIJQS5KEAM
storage		: null

Petunjuk penggunaan aplikasi :
Registrasi dan Log in.
1. Registrasi bila ingin membuat akun baru.
2. Pilih menu login bila ingin menggunakan akun yang telah disediakan
3. Masukan data, tekan tombol login.

Menu utama.
1. Masukan kunci enkripsi dan pilih 'refresh/update table' untuk melihat data.
2. Masukkan kunci enkripsi dan data baru apabila database kosong. Pilih 'add password'.
3. Lakukan hal yang sama bila ingin memasukkan data baru.
4. Ganti row number sesuai dengan data yang ingin dihapus, pilih 'delete password'.
5. Penggantian username dan password pada 'change user profile' dapat dilakukan terpisah. Username baru harus tidak terdapat pada database. Pilih 'submit' untuk update.
6. Penggantian kunci enkripsi akan gagal bila kunci enkripsi lama gagal. 
7. Delete account untuk menghapus akun Password Manager.
8. Pilihan 'log out' dan 'about' ada di menu 'Account' di bagian kiri atas aplikasi.


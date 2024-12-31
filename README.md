**Penjelasan singkat arsitektur** :

Arsitektur ini memastikan bahwa semua autentikasi terpusat di SSO Server. Dengan JWT, aplikasi klien dapat memvalidasi token tanpa bergantung langsung pada server SSO untuk setiap permintaan, sehingga meningkatkan efisiensi. Dukungan untuk logout global memastikan bahwa sesi pengguna di seluruh aplikasi dapat ditutup secara bersamaan, meningkatkan keamanan sistem.

# irc-bootcamp-programming
<h2>Identitas Programmer</h2>
<p>Nama: Filzah Alexandra Athaillah</p>
<p>NIM: M0403241094</p>
<p>Departemen: Ilmu Komputer</p>

<h2>Resume Bootcamp</h2>
<h4>1. Serba-serbi Divisi Programming</h4>
Staf divisi programming berfungsi 'memberi otak' kepada robot sehingga robot dapat menjalankan task/tugasnya dengan semestinya. Robot diprogram agar bisa bergerak dengan baik, memproses input dari sensor, dan membuat keputusan yang benar. Anggota divisi Programming VTOL harus memfamiliarisasikan diri dengan bahasa pemrograman Python, serta tools seperti Roboflow; Yolo; MissionPlanner; dan DroneKit. Namun, juga perlu memiliki pemahaman yang baik tentang Arduino. 
<h4>2. Dasar Programming</h4>
Terdapat beberapa terminologi yang harus dikuasai sebagai dasar programming:
<ol>
  <li>Flowchart dan Pseudocode, yaitu representasi dari algoritma yang merupakan komponen penting dalam suatu pemrograman. Flowchart merepresentasikan algoritma dengan grafik dan simbol, sedangkan pseudocode merepresentasikan algoritma dengan penulisan yang mudah dipahami dan tidak terikat sintaks tertentu.</li>
  <li>Variabel dan Tipe Data, setiap variabel memiliki tipe data yang harus dideklarasikan sebelum digunakan. Di C/C++, tipe data yang digunakan harus dideklarasikan secara eksplisit, sedangkan Python lebih fleksibel.</li>
  <li>Operator, terdiri dari operator aritmatika; operator pembanding; operator boolean; dan operator kontrol. Operator merupakan komponen penting untuk mengoperasikan program.</li>
  <li>Tools dan IDE, yaitu pendukung tugas divisi programming. Contohnya Roboflow merupakan platform yang dapat membantu proses machine learning.</li>
</ol>
<h4>3. Demo: Object Detection</h4>
Tools yang digunakan: Roboflow, Google Collab, Ultralytics Yolo, Python IDE (Pycharm atau VSCode)
Alur demos:
<ol>
  <li>Latih model machine learning di Roboblow menggunakan gambar-gambar sampel,</li>
  <li>Konversi model Roboflow menjadi file Yolo menggunakan Google Collab,</li>
  <li>Import file Yolo yang sudah dilatih ke workspace Python, dan</li>
  <li>Gunakan library opencv-python dan ultralytics untuk membangun program object detector di python.</li>
</ol>
<h4>4. Demo: Arduino Prototype</h4>
Tools yang digunakan: Arduino IDE, Wowki, Platform IO, VSCode
Alur demos:
<ol>
  <li>Buat program .ino di Arduino IDE atau VSCode,</li>
  <li>Di VSCode, gunakan extension Platform IO untuk mensimulasikan program Arduino,</li>
  <li>Program juga bisa disimulasikan di platform Wowki,</li>
  <li>Di Wowki, pilih board yang akan digunakan dan rakit prototipe</li>
  <li>Tambahkan kode ke code editor agar protipe dapat tereksekusi</li>
</ol>
<h4>5. Version Control</h4>
Agar dapat berkolaborasi dengan efektif, penting bagi anggota divisi programming untuk memahami Git dan Github dengan baik. Github adalah platform yang memungkinkan satu orang untuk mempublikasi projeknya dan dapat dimodifikasi dan dikoreksi oleh anggota lainnya.
![WhatsApp Image 2025-05-12 at 19 58 44_0e48fb28](https://github.com/user-attachments/assets/7c24a629-fa51-4ea6-80a2-fbe4565129f8)
![WhatsApp Image 2025-05-12 at 19 58 44_289852cc](https://github.com/user-attachments/assets/7302fad3-fdd1-47e2-8370-8b0e11183298)
![WhatsApp Image 2025-05-12 at 19 58 44_883489fb](https://github.com/user-attachments/assets/bc15bc96-a040-4374-b4cf-33effe444d21)
![WhatsApp Image 2025-05-12 at 19 58 45_21ec7c2a](https://github.com/user-attachments/assets/563e5b55-2eed-4a8f-a133-fbf4cdf915e1)

<h2>Penjelasan Kode Arduino Uno</h2>
<p>Board yang digunakan dalam tugas ini adalah Arduino Uno. Pada board, dipasang tiga lampu LED dengan warna yang berbeda dan servo. Di atas fungsi void setup(), library servo diimport dan dideklarasikan variabel, yaitu masing-masing LED dihubungkan ke pin. LED berwarna merah dihubungkan ke pin 13, LED berwarna magenta dihubungkan ke pin 12, dan LED berwarna hijau dihubungkan ke pin 11. Di dalam fungsi void setup(), servo di-attach ke pin 6. Kemudian, semua pin yang dipakai dikonfigurasi sebagai output. Di dalam fungsi void loop(), ketiga LED diprogram agar menyala dengan fungsi digitalWrite(led1, HIGH) dan mati dengan fungsi digitalWrite(led1, LOW) setiap satu detik dengan fungsi delay(1000). Servo diprogram agar memutar sebanyak 180 derajat dan kembali masing-masing melalui fungsi servoku.write(180) dan servoku.write(0). Servo juga memiliki delay 1 detik. Link wowki: https://wokwi.com/projects/430652807592485889</p>
<p>Keterangan variabel:
led1 = merah;
led2 = magenta;
led 3 = hijau;
servoku = servo</p>

<h2>Penjelasan Kode OpenCV Python</h2>
<h3>OpenCV + DeepFace</h3>
Library yang digunakan pada projek ini adalah opencv-python dan deepface. Opencv-python memungkinkan program untuk membuka kamera dan menangkap gambar di webcam. Deepface adalah framework analisis wajah ringan yang mampu mengenali wajah. Program ini menggunakan fungsi dasar OpenCV untuk membuka kamera, menyalin frame, dan menampilkan teks di layar webcam. Library DeepFace digunakan untuk menyocokkan wajah yang muncul di webcam dengan gambar referensi.
<h3>OpenCV + Ultralytics Yolo11</h3>

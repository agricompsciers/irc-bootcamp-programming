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
  <li>Flowchart dan Pseudocode, yaitu</li>
</ol>

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
<h3>OpenCV + ultralytics Yolo11</h3>

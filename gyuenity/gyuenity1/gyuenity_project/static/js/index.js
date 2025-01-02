// Menunggu hingga seluruh konten halaman telah dimuat
document.addEventListener("DOMContentLoaded", function () {
    // Membuat array yang berisi ID dari semua tombol 'Tampilkan lebih banyak'
    const readMoreButtons = [
      "readMoreBtn1",
      "readMoreBtn2",
      "readMoreBtn3",
      "readMoreBtn4",
      "readMoreBtn5",
      "readMoreBtn6",
    ];
  
    // Melakukan iterasi atau perulangan pada setiap ID tombol di dalam array
    readMoreButtons.forEach((buttonId) => {
      // Mendapatkan elemen tombol berdasarkan ID-nya
      const button = document.getElementById(buttonId);
  
      // Menambahkan event listener untuk menangani klik pada tombol
      button.addEventListener("click", function () {
        // Mendapatkan elemen 'dots' (tiga titik yang menunjukkan teks terpotong)
        // 'dots' disesuaikan dengan angka terakhir dari ID tombol (misalnya, 'dots1', 'dots2', dll.)
        const dots = document.getElementById(
          `dots${buttonId.charAt(buttonId.length - 1)}`
        );
  
        // Mendapatkan elemen 'more' (teks yang akan ditampilkan lebih banyak)
        // 'more' disesuaikan dengan angka terakhir dari ID tombol
        const moreText = document.getElementById(
          `more${buttonId.charAt(buttonId.length - 1)}`
        );
  
        // Mengecek apakah teks 'more' sudah terlihat atau tidak (inline artinya terlihat)
        const isExpanded = moreText.style.display === "inline";
  
        // Jika teks lebih sudah terlihat, maka kita sembunyikan lagi
        if (isExpanded) {
          dots.style.display = "inline"; // Menampilkan kembali 'dots' (titik-titik)
          moreText.style.display = "none"; // Menyembunyikan teks lebih
          button.innerText = "Tampilkan lebih banyak"; // Mengubah teks tombol menjadi 'Tampilkan lebih banyak'
        }
        // Jika teks lebih belum terlihat, maka kita tampilkan
        else {
          dots.style.display = "none"; // Menyembunyikan 'dots'
          moreText.style.display = "inline"; // Menampilkan teks lebih
          button.innerText = "Sembunyikan"; // Mengubah teks tombol menjadi 'Sembunyikan'
        }
      });
    });
  });

  $(document).ready(function() {
    alert("Selamat datang!");

    $(window).on("scroll", function() {
        if ($(this).scrollTop() > 200) {
            $("#scroll-top").fadeIn(200);  
        } else {
            $("#scroll-top").fadeOut(200); 
        }
    });

    $("#scroll-top").on("click", function(event) {
        event.preventDefault();
        $("html, body").stop().animate({scrollTop: 0}, 50, 'linear'); 
    });
});

  
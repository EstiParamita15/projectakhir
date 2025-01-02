
    /* EFEK LOGO DIBAWAH TULISAN SIAPA KAMI  MEMPERBESAR DAN MEMPERKECIL*/
    function pulsateLogo() {
      $(".jumbotron img").animate({ scale: 1.1 }, 1000, function () {
        $(this).animate({ scale: 1 }, 1000, pulsateLogo);
      });
    }
    pulsateLogo();

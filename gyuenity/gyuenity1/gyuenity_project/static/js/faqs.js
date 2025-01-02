document.addEventListener("DOMContentLoaded", function () {
    const faqItems = document.querySelectorAll(".faq-item");
  
    faqItems.forEach((item) => {
        const question = item.querySelector(".faq-question");
        const answer = item.querySelector(".faq-answer");
  
        // Menampilkan jawaban FAQ saat pertanyaan diklik
        question.addEventListener("click", () => { 
            const isActive = question.classList.contains("active");
  
            // Menutup jawaban jika pertanyaan lain diklik
            faqItems.forEach((otherItem) => {
                if (otherItem !== item) {
                    otherItem.querySelector(".faq-question").classList.remove("active");
                    otherItem.querySelector(".faq-answer").classList.remove("active");
                }
            });
  
            // Toggle (beralih) status aktif
            question.classList.toggle("active", !isActive);
            answer.classList.toggle("active", !isActive);
        });
    });
  });
  
  // Pastikan jQuery sudah dimuat dan DOM siap
  $(document).ready(function () {
    // Form submission handler
    $("#contactForm").on("submit", function (e) {
        e.preventDefault();  // Mencegah form untuk melakukan submit default
  
        // Tampilkan alert setelah form disubmit
        alert("Thank you for your message. We will get back to you soon!");
  
        // Reset form setelah submit
        this.reset();
    });
  });
  
// Function to update class and price
function updateClassAndPrice() {
    const selectKelas = document.getElementById("selectKelas");
    const selectedOption = selectKelas.options[selectKelas.selectedIndex];
    const kelas = selectedOption.value;
    const price = selectedOption.getAttribute("data-price");

    // Update the input values for class and price
    document.getElementById("kelas").value = kelas;
    document.getElementById("harga").value = price;
}

// Function to simulate successful payment and show popup
function handlePayment(event) {
    event.preventDefault(); // Prevent the default form submission
    console.log("Form submitted and payment process initiated.");
    showPopup(); // Show the popup after payment
}

// Show the popup
function showPopup() {
    console.log("Popup should now be visible!");
    document.getElementById('popup').style.display = 'block';
    document.getElementById('overlay').style.display = 'block';
}

// Function to go to the class page (this is just an example, you can redirect to another page)
function goToClass() {
        // Mengirim permintaan POST ke server untuk memperbarui sesi
        const selectKelas = document.getElementById("selectKelas");
        fetch('set-session/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                 'X-CSRFToken': '{{ csrf_token }}'
            },
            body: JSON.stringify({ paymentStatus: 'success' , new_data: selectKelas}) // Data tambahan bisa ditambahkan jika diperlukan
        })
        .then(response => response.json())
        .then(data => {
            console.log(data.message); 
    
            const selectedClass = document.getElementById('selectKelas').value;
        
            // Buat URL dinamis berdasarkan kelas yang dipilih
            const url = `/gyu_app/class${selectedClass}`; 
            
            // Redirect ke URL yang sesuai
            window.location.href = url;
    
        })
        .catch(error => {
            console.error('Error:', error);
        });
    
    }
     // Panggil fungsi untuk menyetel sesi sebelum navigasi

    // Ambil nilai kelas yang dipilih dari dropdown
   


// Close the popup when clicking outside of it
document.getElementById('overlay').addEventListener('click', function() {
    document.getElementById('popup').style.display = 'none';
    document.getElementById('overlay').style.display = 'none';
});

// Add event listener to the form after the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function () {
    const paymentForm = document.getElementById('paymentForm');
    if (paymentForm) {
        paymentForm.addEventListener('submit', handlePayment);
    }
});

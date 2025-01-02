from django.shortcuts import render, redirect
from .forms import signupform, UserForm
from django.contrib.auth import authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from gyu_app.models import QuizResult
from django.utils import timezone
from .models import UserClass, Class, UserProfile, Progress
from django.contrib.auth.models import User
from .forms import ContactForm
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.db.models import Sum
import re

# Create your views here.
def index(request):
    return render(request, 'gyu_app/index.html')

# Fungsi untuk About
def about(request):
    return render(request, 'gyu_app/about.html')

# Fungsi untuk Course
def course(request):
    return render(request, 'gyu_app/course.html')

# Fungsi untuk Course
def faqs_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Thank you for your question!'}, status=200)
        else:
            return JsonResponse({'error': 'Invalid form submission'}, status=400)
    form = ContactForm()  # Form kosong untuk rendering di halaman
    return render(request, 'gyu_app/faqs.html', {'form': form})
# Fungsi untuk Courses
def courses(request):
    return render(request, 'gyu_app/courses.html')

# Fungsi untuk Class 1
def class1_view(request):
    return render(request, 'gyu_app/class1.html')


def pembayaran(request):
    return render(request, 'gyu_app/pembayaran.html')

@login_required
def payment_view(request, class_id):
    user_class = UserClass.objects.get(user=request.user, id=class_id)
    
    # Misalnya ini adalah pengecekan apakah pembayaran berhasil (ganti sesuai dengan logika pembayaranmu)
    payment_successful = check_payment_gateway_status()  # type: ignore # Implementasikan ini sesuai dengan gateway yang kamu pakai
    
    if payment_successful:
        # Pembayaran berhasil, update status di database
        user_class.is_paid = True
        user_class.save()

        # Simpan status pembayaran di session jika ingin mempermudah pengecekan status
        request.session['is_paid'] = True

        return redirect('class_detail', class_id=class_id)
    else:
        return render(request, 'payment_failed.html', {'user_class': user_class})

@login_required
def class_detail(request, class_id):
    # Ambil data kelas dan cek apakah pengguna sudah membayar
    user_class = UserClass.objects.get(user=request.user, id=class_id)

    if user_class.is_paid:
        # Jika sudah bayar, tampilkan kelas langsung tanpa modal
        return render(request, 'class_content.html', {'class': user_class})

    # Jika belum bayar, tampilkan modal untuk memilih bayar atau uji gratis
    return render(request, 'class_detail.html', {'class': user_class})

def check_payment_status(request):
    try:
        # Mendapatkan status pembayaran dari model UserClass
        user_class = UserClass.objects.get(user=request.user)
        return JsonResponse({
            "isPaid": user_class.is_paid,  # Menyediakan status pembayaran
            "trialUrl": reverse('gyu_app:class3'),  # URL untuk uji coba
            "payUrl": reverse('gyu_app:pembayaran'),  # URL untuk pembayaran
        })
    except UserClass.DoesNotExist:
        return JsonResponse({
            "isPaid": False,
            "trialUrl": reverse('gyu_app:class3'),
            "payUrl": reverse('gyu_app:pembayaran')
        })
    
def set_payment_session(request):
    if request.method == 'POST':
        # Perbarui sesi dengan status pembayaran
        print("POST request received")  # Verifikasi permintaan diterima
        print(request.body)  # Cek apakah ada data yang dikirim
        request.session['payment_status'] = 'success'
        print("Session set:", request.session.get('payment_status'))  # Cek sesi
        return JsonResponse({'message': 'Payment session updated successfully.'})
    return JsonResponse({'error': 'Invalid request method.'}, status=400)

def check_session(request):
    # Mengambil data dari sesi
    payment_status = request.session.get('payment_status', 'Not set')
    return JsonResponse({'payment_status': payment_status})

    
# Fungsi untuk Logout
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

# Fungsi untuk Signup
def signup(request):
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gyu_app:login')
    else:
        form = signupform()
    return render(request, 'gyu_app/signup.html', {'form': form})

# Fungsi untuk Login
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('gyu_app:dashboard')
        else:
            return render(request, 'gyu_app/login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'gyu_app/login.html')
    
# Fungsi untuk Logout
def logout_view(request):
    logout(request)
    return redirect('gyu_app:index')


# Fungsi untuk Dashboard
def dashboard(request):
    user_profile = request.user.profile  # Ambil profil pengguna
    return render(request, 'dashboard.html', {'user_profile': user_profile})

def profil(request):
    return render(request, 'gyu_app/profil.html')


@login_required
def profil(request):
    # Ambil atau buat profil pengguna jika belum ada
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('gyu_app:profil')  # Redirect setelah berhasil simpan
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=user_profile)

    return render(request, 'gyu_app/profil.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'user_profile': user_profile,  # Kirim user_profile ke template
    })


def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()  # Menyimpan foto profil
            return redirect('gyu_app:profil')  # Redirect ke halaman profil setelah penyimpanan
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.profile)

    return render(request, 'gyu_app/profil.html', {'user_form': user_form, 'profile_form': profile_form})

def dashboard(request):
     # Ambil profil pengguna yang sedang login, atau buat baru jika belum ada
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    # Kirim objek profile ke template
    return render(request, 'gyu_app/dashboard.html', {'profile': user_profile, 'user': request.user})

def get_youtube_id(url):
    """
    Fungsi untuk mengambil ID video dari URL YouTube
    """
    match = re.search(r'(youtu\.be/|youtube\.com/watch\?v=|youtube\.com/embed/)([a-zA-Z0-9_-]+)', url)
    if match:
        return match.group(2)  # ID video ada di grup kedua
    return None


def materi1class1(request):
    youtube_url = "https://youtu.be/qzMPvbL3GRQ?si=KuZzJ0p0ZkOXSdTV"  # URL YouTube
    video_id = get_youtube_id(youtube_url)  # Ambil ID video
    return render(request, 'gyu_app/materi1class1.html', {'video_id': video_id})


# Fungsi untuk Quiz Modul 1
def quizm1class1_view(request):
    return render(request, 'gyu_app/quizm1class1.html')



# Fungsi untuk Kuiz
def quizm1class1(request):
    user = request.user
    if request.method == 'POST':
        quiz_name = request.POST.get('quiz_name')
        correct_answers = {
            'question1': 'Browser',
            'question2': 'Mengolah dan menjaga informasi di database',
            'question3': 'Hyper Text Markup Language',
            'question4': 'Alamat IP',
            'question5': '<strong>',
            'question6': '<img>',
            'question7': '<br>',
            'question8': 'alt',
            'question9': 'Mengelompokkan elemen-elemen HTML',
            'question10': '<a>'
        }

        total_score = 0
        for question, correct_answer in correct_answers.items():
            user_answer = request.POST.get(question)
            if user_answer and user_answer.strip().lower() == correct_answer.strip().lower():
                total_score += 10  # Tambah skor  untuk jawaban yang benar

        # Tentukan class_number dan module_number sesuai dengan logika atau kebutuhan
        class_number = 1  # Misalnya, Kelas 1
        module_number = 1  # Misalnya, Modul 1

        # Update atau buat objek Progress untuk melacak progres kuis
        progress, created = Progress.objects.get_or_create(user=user, class_number=class_number, module_number=module_number)
        progress.completed = True  # Menandakan kuis sudah selesai
        progress.score = total_score  # Menyimpan total skor
        progress.save()

        # Simpan total skor di session
        request.session['total_score'] = total_score
        request.session['quiz_name'] = 'Modul 1 Front End Introduction'   # Simpan nama kuis di session
    
        return redirect('gyu_app:quizresultm1c1')  # Redirect ke halaman hasil kuis

    return render(request, 'gyu_app/quizm1class1.html')  # Render halaman kuis

# Fungsi untuk Kuiz
@login_required
def quizresultm1c1(request):
    user = request.user
    quiz_name = request.session.get('quiz_name', 'Default Quiz')
    score = request.session.get('total_score', 0)

    # Perbarui atau buat hasil baru
    quizresult, created = QuizResult.objects.update_or_create(
        user=user,
        quiz_name=quiz_name,
        defaults={
            'score': score,
            'submit_date': timezone.now()
        }
    )

    return render(request, 'gyu_app/quizresultm1c1.html', {
        'score': score,
        'quiz_name': quiz_name,
        'submit_date': timezone.localtime(quizresult.submit_date)
    })


def progressbelajar(request):
    user = request.user
    progress_data = {}

    for class_number in range(1, 4):  # Kelas 1 hingga Kelas 6
        completed_modules = Progress.objects.filter(user=user, class_number=class_number, completed=True).count()
        total_modules = 6  # Total modul per kelas
        percentage = (completed_modules / total_modules * 100) if total_modules > 0 else 0
        progress_data[class_number] = {
            'completed': completed_modules,
            'total': total_modules,
            'percentage': percentage,  # Hitung persentase di sini
        }

    return render(request, 'gyu_app/progressbelajar.html', {'progress_data': progress_data})


def progress_view(request):
    progress_data = {
        1: {"completed": 5, "total": 10, "percentage": 50},
        2: {"completed": 3, "total": 10, "percentage": 30},
    }
    return render(request, 'progressbelajar.html', {'progress_data': progress_data})

#fungsi untuk leaderboard
@login_required
def leaderboard(request):
    # mengelompokkan score berdasarkan pengguna, menghitung total score, dan mengurutkan secara global
    leaderboard_data = QuizResult.objects.values('user__username')\
        .annotate(total_score=Sum('score'))\
        .order_by('-total_score')[:5] #batasi hanya 10 teratas
    
    return render(request, 'gyu_app/leaderboard.html',{
        'leaderboard_data': leaderboard_data,
    })

@login_required
def hasilquiz(request):
    # Ambil hasil quiz terbaru
    latest_result = QuizResult.objects.filter(user=request.user).order_by('-submit_date').first()

    # Ambil semua hasil quiz untuk tabel
    all_results = QuizResult.objects.filter(user=request.user).order_by('-submit_date')

    return render(request, 'gyu_app/hasilquiz.html', {
        'latest_result': latest_result,
        'results': all_results
    })






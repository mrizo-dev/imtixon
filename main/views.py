from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Reja

# 1
def hamma_studentlar(request):
    talabalar = Student.objects.all()
    return render(request, 'talabalar.html', {'talabalar': talabalar})

# 2
def hamma_rejalar(request):
    rejalar = Reja.objects.all()
    return render(request, 'rejalar.html', {'rejalar': rejalar})

# 3
def bajarilmagan_rejalar(request):
    rejalar = Reja.objects.filter(bajarildi=False)
    return render(request, 'rejalar.html', {'rejalar': rejalar})

# 4
def bitiruvchilar(request):
    talabalar = Student.objects.filter(kurs__gte=3)
    return render(request, 'talabalar.html', {'talabalar': talabalar})

# 5
def katta_talabalar(request):
    talabalar = Student.objects.filter(yosh__gt=20)
    return render(request, 'talabalar.html', {'talabalar': talabalar})

# 6
def bitiruvchilar_rejalari(request):
    rejalar = Reja.objects.filter(student__kurs__gte=3)
    return render(request, 'rejalar.html', {'rejalar': rejalar})

# 7
def talaba_rejalari(request, talaba_id):
    talaba = get_object_or_404(Student, id=talaba_id)
    rejalar = talaba.rejalar.all()
    return render(request, 'rejalar.html', {'rejalar': rejalar, 'talaba': talaba})

# 8
def reja_ochirish(request, reja_id):
    reja = get_object_or_404(Reja, id=reja_id)
    reja.delete()
    return redirect('hamma_rejalar')

# 9
def reja_qoshish(request):
    if request.method == "POST":
        Reja.objects.create(
            sarlavha=request.POST.get('sarlavha'),
            batafsil=request.POST.get('batafsil'),
            sana=request.POST.get('sana'),
            student_id=request.POST.get('student_id')
        )
        return redirect('hamma_rejalar')
    talabalar = Student.objects.all()
    return render(request, 'reja_qoshish.html', {'talabalar': talabalar})
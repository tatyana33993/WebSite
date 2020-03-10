from django.shortcuts import render
from restaurant.models import Tables, Reservation
from restaurant.userform import UserForm

# Create your views here.


def index(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            tables = Tables.objects.in_bulk()
            request_name = userform.cleaned_data['name']
            request_number = userform.cleaned_data["number"]
            request_date = userform.cleaned_data["date"]
            request_time = userform.cleaned_data["time"]
            request_people = userform.cleaned_data["peoples"]
            request_comment = userform.cleaned_data["comment"]
            flag = False
            for id in tables:
                if int(request_people) <= tables[id].count_seats:
                    try:
                        Reservation.objects.get(date=request_date, table=tables[id].number)
                        continue
                    except Reservation.DoesNotExist:
                        reservation = Reservation(name=request_name, number=request_number,
                                                  date=request_date, time=request_time,
                                                  table=tables[id].number, comment=request_comment)
                        reservation.save()
                        message1 = "Столик успешно забронирован!!!"
                        message2 = "Ваш номер брони {0}.".format(reservation.id)
                        return render(request, "restaurant/contact.html", {"message1": message1, "message2": message2})
            if not flag:
                message1 = "Доступных столиков нет..."
                message2 = "Попробуйте забронировать столик на другой день."
                return render(request, "restaurant/contact.html", {"message1": message1, "message2": message2})
        else:
            return render(request, "restaurant/home.html", {"form": userform})
    else:
        userform = UserForm()
        return render(request, "restaurant/home.html", {"form": userform})

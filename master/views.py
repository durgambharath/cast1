from django.shortcuts import render, redirect

from master.models import CastDetails


def show_cast(request):
    return render(request, 'caste_master.html')


def cast_list(request):
    caste_name = request.POST.get("x")
    subcaste_name = request.POST.get("y")

    from pymongo import MongoClient
    client = MongoClient('mongodb://localhost:27017')
    db = client
    posts = db.sample
    d1 = {"cast_Name": caste_name, "subcast_name": subcaste_name}
    posts.sample.insert(d1)
    return render(request, "caste_master.html")


def edit(request, cast):
    caste_name = request.POST.get("x")
    subcaste_name = request.POST.get("y")
    from pymongo import MongoClient
    client = MongoClient()
    db = client
    d1 = {"cast_Name": caste_name, "subcast_name": subcaste_name}
    posts = db.sample
    posts.sample.edit(d1)
    master = CastDetails.objects.get(cast=cast)
    return render(request, 'caste_master.html')


def delete(request, cast):
    caste_name = request.POST.get("x")
    subcaste_name = request.POST.get("y")
    from pymongo import MongoClient
    client = MongoClient()
    db = client
    d1 = {"cast_Name": caste_name, "subcast_name": subcaste_name}
    posts = db.sample
    posts.sample.delete(d1)
    master = CastDetails.objects.get(cast=cast)
    master.delete()
    return redirect(request, "/caste_master.html")



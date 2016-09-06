from django.shortcuts import render
from pymongo import MongoClient
# Create your views here.

def error_view(request):
    return render(request, "404.html")
    

def sample_view(request):
    try:
        print request.method
        client = MongoClient()
        db = client["Writepad"]
        col = db["pad"]
        print col.name
        data = {}
        if col.name not in db.collection_names():
            print "here"
            col.insert({"note_id":"sample","name":"Sample","data":""})
        else:
            data = col.find_one({"note_id":"sample"},{"_id":0})
            print data
            
        return render(request, "sample.html", {"data":data})
    except Exception as e:
        return render(request, "404.html")
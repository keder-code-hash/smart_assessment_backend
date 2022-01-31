from re import sub
from django.shortcuts import render
import json

# importing Django modules
from django.http import HttpResponse
from users.views import is_authenticated_user, get_user
from django.contrib.staticfiles.storage import staticfiles_storage

# index page
def index(request):
    return HttpResponse("Landing Page")


# test page
def test(request):
    return HttpResponse("Test Page")


# test results
def test_results(request):
    exam_title = "Object Oriented Programming"
    total_marks = 100
    score = 80
    details = [
        {
            "q_no": 1,
            "qsn": "What is Inheritance",
            "stn_ans": "Inheritance in Java is a mechanism in which one object acquires all the properties and behaviors of a parent object. It is an important part of OOPs (Object Oriented programming system).",
            "std_ans": "Inheritance can be defined as the process where one class acquires the properties (methods and fields) of another.",
        },
        {
            "q_no": 2,
            "qsn": "What is Inheritance",
            "stn_ans": "Inheritance in Java is a mechanism in which one object acquires all the properties and behaviors of a parent object. It is an important part of OOPs (Object Oriented programming system).",
            "std_ans": "Inheritance can be defined as the process where one class acquires the properties (methods and fields) of another.",
        },
        {
            "q_no": 3,
            "qsn": "What is Inheritance",
            "stn_ans": "Inheritance in Java is a mechanism in which one object acquires all the properties and behaviors of a parent object. It is an important part of OOPs (Object Oriented programming system).",
            "std_ans": "Inheritance can be defined as the process where one class acquires the properties (methods and fields) of another.",
        },
        {
            "q_no": 4,
            "qsn": "What is Inheritance",
            "stn_ans": "Inheritance in Java is a mechanism in which one object acquires all the properties and behaviors of a parent object. It is an important part of OOPs (Object Oriented programming system).",
            "std_ans": "Inheritance can be defined as the process where one class acquires the properties (methods and fields) of another.",
        },
        {
            "q_no": 5,
            "qsn": "What is Inheritance",
            "stn_ans": "Inheritance in Java is a mechanism in which one object acquires all the properties and behaviors of a parent object. It is an important part of OOPs (Object Oriented programming system).",
            "std_ans": "Inheritance can be defined as the process where one class acquires the properties (methods and fields) of another.",
        },
        {
            "q_no": 5,
            "qsn": "What is Inheritance",
            "stn_ans": "Inheritance in Java is a mechanism in which one object acquires all the properties and behaviors of a parent object. It is an important part of OOPs (Object Oriented programming system).",
            "std_ans": "Inheritance can be defined as the process where one class acquires the properties (methods and fields) of another.",
        },
        {
            "q_no": 5,
            "qsn": "What is Inheritance",
            "stn_ans": "Inheritance in Java is a mechanism in which one object acquires all the properties and behaviors of a parent object. It is an important part of OOPs (Object Oriented programming system).",
            "std_ans": "Inheritance can be defined as the process where one class acquires the properties (methods and fields) of another.",
        },
        {
            "q_no": 5,
            "qsn": "What is Inheritance",
            "stn_ans": "Inheritance in Java is a mechanism in which one object acquires all the properties and behaviors of a parent object. It is an important part of OOPs (Object Oriented programming system).",
            "std_ans": "Inheritance can be defined as the process where one class acquires the properties (methods and fields) of another.",
        },
        {
            "q_no": 5,
            "qsn": "What is Inheritance",
            "stn_ans": "Inheritance in Java is a mechanism in which one object acquires all the properties and behaviors of a parent object. It is an important part of OOPs (Object Oriented programming system).",
            "std_ans": "Inheritance can be defined as the process where one class acquires the properties (methods and fields) of another.",
        },
        {
            "q_no": 5,
            "qsn": "What is Inheritance",
            "stn_ans": "Inheritance in Java is a mechanism in which one object acquires all the properties and behaviors of a parent object. It is an important part of OOPs (Object Oriented programming system).",
            "std_ans": "Inheritance can be defined as the process where one class acquires the properties (methods and fields) of another.",
        },
        {
            "q_no": 5,
            "qsn": "What is Inheritance",
            "stn_ans": "Inheritance in Java is a mechanism in which one object acquires all the properties and behaviors of a parent object. It is an important part of OOPs (Object Oriented programming system).",
            "std_ans": "Inheritance can be defined as the process where one class acquires the properties (methods and fields) of another.",
        },
        {
            "q_no": 5,
            "qsn": "What is Inheritance",
            "stn_ans": "Inheritance in Java is a mechanism in which one object acquires all the properties and behaviors of a parent object. It is an important part of OOPs (Object Oriented programming system).",
            "std_ans": "Inheritance can be defined as the process where one class acquires the properties (methods and fields) of another.",
        },
        {
            "q_no": 5,
            "qsn": "What is Inheritance",
            "stn_ans": "Inheritance in Java is a mechanism in which one object acquires all the properties and behaviors of a parent object. It is an important part of OOPs (Object Oriented programming system).",
            "std_ans": "Inheritance can be defined as the process where one class acquires the properties (methods and fields) of another.",
        },
    ]

    context = {
        "details": details,
        "score": score,
        "exam_title": exam_title,
        "total_marks": total_marks,
        "is_authenticated": is_authenticated_user(request),
    }

    return render(request, "StudentResult.html", context)


# view all results
def view_all_results(request):
    result = [
        {"name": "Arghya", "roll": 3685128, "marks": 60},
        {"name": "Purnadip", "roll": 6123465, "marks": 70},
        {"name": "Keder", "roll": 8541236, "marks": 80},
        {"name": "Random", "roll": 7845126, "marks": 90},
    ]
    subject = "OOP"

    context = {
        "details": result,
        "subject": subject,
        "is_authenticated": is_authenticated_user(request),
    }

    return render(request, "TeacherResult.html", context)


# self assessment
def self_assessment(request):
    return HttpResponse("Self Assessment")


# set questions for examination (accessible by teacher only)
def set_questions(request):
    user = get_user(request)
    file_url = staticfiles_storage.path('data/questions.json')
    data = ""
    with open(file_url, 'r+') as file:
        data = json.load(file).get(user.user_name)

    qno = list(range(1, len(data.get('qna'))+1))
    if qno == []:
        qno = [1]
    context = {
        "is_authenticated": is_authenticated_user(request),
        "user":user,
        "data":data,
        "qno" : qno
    }
    if context["is_authenticated"] and user.user_role == 't':
        return render(request, "Examset.html", context)
    else:
        err_log = {
            "msg" : "Are you logged in?"
        }
        return render(request, "Error.html", err_log)


# view results of all students (accessible by teacher only)
def view_results(request):
    return HttpResponse("View Results (accessible by Teacher)")

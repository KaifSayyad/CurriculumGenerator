from django.shortcuts import render
from django.http import HttpResponse
from .gpt import getSyllabus
import asyncio
from .forms import InputForm
import json
# Create your views here.
def home(request):
    context = {}
    context['form'] = InputForm()
    return render(request , 'base/home.html', context)

def output(request):
    if request.method == "POST":
        print("request",request)
        sem = request.POST['semester']
        dept = request.POST['department']
        subj = request.POST['subject']
        hrs = request.POST['numberOfHours']
        # print(sem)
        output =getSyllabus(subj, hrs,  dept, sem)

        # output = '{"courseOutcomes": "\\"1. Analyze and design object-oriented solutions to programming problems.\\\\n2. Implement and evaluate object-oriented programs using appropriate programming language.\\\\n3. Apply object-oriented concepts to design and develop software applications.\\\\n4. Understand and utilize inheritance, polymorphism, and encapsulation in object-oriented programming.\\\\n5. Develop reusable code using object-oriented techniques.\\"", "courseObjective": "\\"1. To introduce the basic concepts of object-oriented programming.\\\\n2. To familiarize students with the principles of object-oriented design and analysis.\\\\n3. To provide hands-on experience in implementing object-oriented programs.\\\\n4. To develop problem-solving skills using object-oriented approach.\\\\n5. To enhance students\' ability to design and develop software applications.\\"", "ModuleContent": "[\\" Introduction to Object-Oriented Programming\\\\n- Introduction to object-oriented programming\\\\n- Advantages and disadvantages of OOP\\\\n- Classes and objects\\\\n- Data members and member functions\\\\n- Constructors and destructors\\\\n- Access specifiers\\\\n- Inheritance and polymorphism\\\\n- Abstraction and encapsulation\\\\n- Introduction to UML (Unified Modeling Language)\\\\n\\\\n\\", \\" Classes and Objects\\\\n- Defining classes and objects\\\\n- Class members and access specifiers\\\\n- Constructors and destructors in detail\\\\n- Static data members and member functions\\\\n- Friend functions and friend classes\\\\n- Operator overloading\\\\n- Function overloading and default arguments\\\\n\\\\n\\", \\" Inheritance and Polymorphism\\\\n- Inheritance and its types\\\\n- Base and derived classes\\\\n- Single, multiple, and multilevel inheritance\\\\n- Virtual functions and polymorphism\\\\n- Abstract classes and pure virtual functions\\\\n- Function overriding\\\\n- Runtime polymorphism using virtual functions\\\\n\\\\n\\", \\" Advanced OOP Concepts\\\\n- Templates and generic programming\\\\n- Exception handling\\\\n- File handling in OOP\\\\n- Namespaces\\\\n- Object serialization\\\\n- Introduction to design patterns\\\\n\\\\n\\", \\" OOP Design and Development\\\\n- Object-oriented analysis and design\\\\n- UML diagrams: class diagram, use case diagram, sequence diagram\\\\n- Software development life cycle (SDLC)\\\\n- Test-driven development (TDD)\\\\n- Software testing and debugging in OOP\\\\n- Code reusability and modular programming\\\\n\\\\n\\"]", "ModuleHours": "[\\"8\\", \\"10\\", \\"10\\", \\"10\\", \\"8\\"]"}'
        finalOutput = json.loads(output)
        moduleCont = json.loads(finalOutput['ModuleContent'])
        moduleHrs = json.loads(finalOutput['ModuleHours'])
        courseOutcomes = json.loads(finalOutput['courseOutcomes'])
        courseObjectives = json.loads(finalOutput['courseObjective'])
        length = len(moduleCont)
        context = {'moduleCont' : moduleCont, 'moduleHrs':moduleHrs, 'courseOutcomes' : courseOutcomes, 'courseObjectives' : courseObjectives, 'len':length}
        return render(request, 'base/output.html', context)
    else:
        return HttpResponse("Error :(")


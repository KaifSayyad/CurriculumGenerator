import requests
import re
import json
from flask import Response

def getSyllabus(subject, numberOfHours=42,  department=None, semester=None):

	url = "https://chatgpt-api8.p.rapidapi.com/"


	payload = [
		{
			"content": " Give me the syllabus of "+subject+" subject for Semester-"+str(semester)+"  "+department+" course. Give the output in the well structured format of syllabus in form of modules and their content and also we have total "+ str(numberOfHours)+"  hours to finish this subject , allocate these 42 hours to each module in the syllabus according to its weightage. Also Provide with the references and structure the data in following manner.\n Course Outcomes\n Course Objectives \n Module 1 | It's Content | Number of hours allocated\n Module 2 | It's Content | Number of hours allocated.....\n References.",
			"role": "user"
		}
	]

	# This Header Should Be Changed According to Users API Key.
	headers = {
		"content-type": "application/json",
		"X-RapidAPI-Key": <Your API Key>,
		"X-RapidAPI-Host": "chatgpt-api8.p.rapidapi.com"
	}


	response = requests.post(url, json=payload, headers=headers)

	# print(response.json())

	prompt = response.json()

	text = prompt['text']

	# The text you provided
	# text = "Course Outcomes:\n1. Understand the fundamental principles of physics and their applications in computer science and engineering.\n2. Develop problem-solving and analytical skills by applying the principles of physics in real-world scenarios.\n3. Acquire knowledge of various concepts in mechanics, thermodynamics, and electromagnetism.\n4. Apply mathematical techniques to solve physics-related problems.\n5. Recognize the importance of physics in the field of computer science and engineering.\n\nCourse Objectives:\n1. To introduce students to the fundamental principles and laws of physics.\n2. To develop an understanding of the concepts of mechanics, thermodynamics, and electromagnetism.\n3. To enhance problem-solving and critical thinking skills.\n4. To provide practical applications of physics in computer science and engineering.\n\nModule 1: Mechanics\nContent:\n- Introduction to vectors and scalars\n- Kinematics: motion in one dimension\n- Kinematics: motion in two dimensions\n- Newton's laws of motion\n- Friction and circular motion\n- Work, energy, and power\n- Conservation laws: momentum and energy\n\nNumber of hours allocated: 12\n\nModule 2: Thermodynamics\nContent:\n- Temperature and heat\n- Laws of thermodynamics\n- Heat engines and refrigerators\n- Entropy and the second law of thermodynamics\n- Thermodynamic processes\n\nNumber of hours allocated: 8\n\nModule 3: Electromagnetism\nContent:\n- Electric charge and electric field\n- Gauss's law and electric potential\n- Capacitance and dielectrics\n- Electric current and resistance\n- Magnetic fields and forces\n- Electromagnetic induction\n\nNumber of hours allocated: 12\n\nModule 4: Mathematical Techniques in Physics\nContent:\n- Vector calculus\n- Differential equations\n- Complex numbers\n- Fourier series\n- Linear algebra\n\nNumber of hours allocated: 6\n\nReferences:\n1. Halliday, D., Resnick, R., & Walker, J. (2013). Fundamentals of Physics. John Wiley & Sons.\n2. Serway, R. A., & Jewett, J. W. (2017). Physics for Scientists and Engineers. Cengage Learning.\n3. Thornton, S. T., & Rex, A. F. (2012). Modern Physics for Scientists and Engineers. Cengage Learning.\n4. Aruldhas, G. (2010). Mathematical Physics. Prentice-Hall of India.\n5. Kreyszig, E. (2011). Advanced Engineering Mathematics. John Wiley & Sons."

	# Define regular expressions for extracting course outcomes, objectives, and modules
	course_outcomes_pattern = r'Course Outcomes:(.*?)Course Objectives:'
	course_objectives_pattern = r'Course Objectives:(.*?)Module 1:'
	module_pattern = r'Module (\d+):(.*?)Number of hours allocated: (\d+)'

	# Extract course outcomes and objectives
	course_outcomes_match = re.search(course_outcomes_pattern, text, re.DOTALL)
	course_objectives_match = re.search(course_objectives_pattern, text, re.DOTALL)

	if course_outcomes_match:
		course_outcomes = course_outcomes_match.group(1).strip()

	if course_objectives_match:
		course_objectives = course_objectives_match.group(1).strip()

	# Extract modules
	modules = re.findall(module_pattern, text, re.DOTALL)
	myDict = {'courseOutcomes':'', 'courseObjectives':'', 'moduleContent':[], 'moduleHours':[]}
	myDict["courseOutcomes"] = course_outcomes
	myDict['courseObjectives'] = course_objectives
	# Print extracted information
	# print("Course Outcomes:")
	# print(course_outcomes)

	# print("\nCourse Objectives:")
	# print(course_objectives)

	print("\nModules:")
	for module in modules:
		module_number, module_content, hours_allocated = module
		# print(f"Module {module_number}:")
		# print(module_content.strip())
		# print(f"Hours Allocated: {hours_allocated}\n")
		myDict['moduleContent'].append(module_content)
		myDict['moduleHours'].append(hours_allocated)
	

	ModuleContent = json.dumps(myDict['moduleContent'])
	ModuleHours = json.dumps(myDict['moduleHours'])
	newDict = {'courseOutcomes':json.dumps(myDict['courseOutcomes']), 'courseObjective': json.dumps(myDict['courseObjectives']), 'ModuleContent' : ModuleContent, 'ModuleHours' : ModuleHours}
	response = Response(
        response=json.dumps(newDict),
        status=200,
        mimetype='application/json'
    )
	return json.dumps(newDict)


def main():
	# department = input("Enter the name of the Deaprtment :")
	# semester = int(input("Enter the Semester No. (1-8):"))
	# subject = input("Enter the Subject :")
	# NumberOfHours = int(input("Enter the Number Of Hours Required to complete the course:"))
	# output = getSyllabus(subject, NumberOfHours, department, semester)
	output = '{"courseOutcomes": "\\"1. Analyze and design object-oriented solutions to programming problems.\\\\n2. Implement and evaluate object-oriented programs using appropriate programming language.\\\\n3. Apply object-oriented concepts to design and develop software applications.\\\\n4. Understand and utilize inheritance, polymorphism, and encapsulation in object-oriented programming.\\\\n5. Develop reusable code using object-oriented techniques.\\"", "courseObjective": "\\"1. To introduce the basic concepts of object-oriented programming.\\\\n2. To familiarize students with the principles of object-oriented design and analysis.\\\\n3. To provide hands-on experience in implementing object-oriented programs.\\\\n4. To develop problem-solving skills using object-oriented approach.\\\\n5. To enhance students\' ability to design and develop software applications.\\"", "ModuleContent": "[\\" Introduction to Object-Oriented Programming\\\\n- Introduction to object-oriented programming\\\\n- Advantages and disadvantages of OOP\\\\n- Classes and objects\\\\n- Data members and member functions\\\\n- Constructors and destructors\\\\n- Access specifiers\\\\n- Inheritance and polymorphism\\\\n- Abstraction and encapsulation\\\\n- Introduction to UML (Unified Modeling Language)\\\\n\\\\n\\", \\" Classes and Objects\\\\n- Defining classes and objects\\\\n- Class members and access specifiers\\\\n- Constructors and destructors in detail\\\\n- Static data members and member functions\\\\n- Friend functions and friend classes\\\\n- Operator overloading\\\\n- Function overloading and default arguments\\\\n\\\\n\\", \\" Inheritance and Polymorphism\\\\n- Inheritance and its types\\\\n- Base and derived classes\\\\n- Single, multiple, and multilevel inheritance\\\\n- Virtual functions and polymorphism\\\\n- Abstract classes and pure virtual functions\\\\n- Function overriding\\\\n- Runtime polymorphism using virtual functions\\\\n\\\\n\\", \\" Advanced OOP Concepts\\\\n- Templates and generic programming\\\\n- Exception handling\\\\n- File handling in OOP\\\\n- Namespaces\\\\n- Object serialization\\\\n- Introduction to design patterns\\\\n\\\\n\\", \\" OOP Design and Development\\\\n- Object-oriented analysis and design\\\\n- UML diagrams: class diagram, use case diagram, sequence diagram\\\\n- Software development life cycle (SDLC)\\\\n- Test-driven development (TDD)\\\\n- Software testing and debugging in OOP\\\\n- Code reusability and modular programming\\\\n\\\\n\\"]", "ModuleHours": "[\\"8\\", \\"10\\", \\"10\\", \\"10\\", \\"8\\"]"}'
	finalOutput = json.loads(output)
	moduleCont = json.loads(finalOutput['ModuleContent'])
	moduleHrs = json.loads(finalOutput['ModuleHours'])
	# print(finalOutput)
	for (i,j)  in zip(moduleCont,moduleHrs) :
		print(j+"\t"+i)
	


if __name__=="__main__":
    main()
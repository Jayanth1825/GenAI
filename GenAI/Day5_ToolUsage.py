def add_numbers(a, b):
    return a + b

def sub_numbers(x,y):
    return x - y

def resume_score(skills):
    return len(skills) * 10


query = input("Ask something: ").lower()


if "add" in query:

    result = add_numbers(25, 10)

    print("Tool used: Calculator")

    print("Result:", result)


elif "resume" in query:

    skills = ["Python", "SQL", "ML"]

    result = resume_score(skills)

    print("Tool used: Resume Scorer")

    print("Result:", result)


elif "sub" in query:
    result=sub_numbers(25,10)

    print("Tool used: Calculator")

    print("Result:", result)

else:
    print("No tool required.")
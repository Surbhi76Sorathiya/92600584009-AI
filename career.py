print("======================================")
print("        CAREER GUIDANCE SYSTEM        ")
print("======================================")
print("Answer the following question with yes and no.")

c1=input("\nDo you like coding? ").lower()
c2=input("Do you like mathemetics? ").lower()
c3=input("Do you like biology? ").lower()
c4=input("Do you like drawing? ").lower()


print("\n==========CAREER SUGGESTION===========")

if c1=="no" and c2=="no" and c3=="no" and c4=="no":
    print("Suggested Career : Explore your intrests and career options further.")
elif c1=="no" and c2=="no" and c3=="no" and c4=="yes":
    print("Suggested Career : Gaphic Designer / Animator")
elif c1=="no" and c2=="no" and c3=="yes" and c4=="no":
    print("Suggested Career : Pharmacist / Nurse")
elif c1=="no" and c2=="no" and c3=="yes" and c4=="yes":
    print("Suggested Career : Medical Illustrator / Healthcare Educator")
elif c1=="no" and c2=="yes" and c3=="no" and c4=="no":
    print("Suggested Career : Engineer / Data Analyst")
elif c1=="no" and c2=="yes" and c3=="no" and c4=="yes":
    print("Suggested Career : Architect")
elif c1=="no" and c2=="yes" and c3=="yes" and c4=="no":
    print("Suggested Career : Doctor")
elif c1=="no" and c2=="yes" and c3=="yes" and c4=="yes":
    print("Suggested Career : Medical Illustrator / Biomedical Designer")
elif c1=="yes" and c2=="no" and c3=="no" and c4=="no":
    print("Suggested Career : Programmer / Web Devloper")
elif c1=="yes" and c2=="no" and c3=="no" and c4=="yes":
    print("Suggested Career : Web Devloper / UI-UX Designer")
elif c1=="yes" and c2=="no" and c3=="yes" and c4=="no":
    print("Suggested Career : Medical Illustrator")
elif c1=="yes" and c2=="yes" and c3=="no" and c4=="no":
    print("Suggested Career : Software Engineer / Computer Scientist")
elif c1=="yes" and c2=="yes" and c3=="no" and c4=="yes":
    print("Suggested Career : Game Devloper / UI Engineer")
elif c1=="yes" and c2=="yes" and c3=="yes" and c4=="no":
    print("Suggested Career : Bioinformations Scientist")
elif c1=="yes" and c2=="yes" and c3=="yes" and c4=="yes":
    print("Suggested Career : Biomedical Software Engineer / Medical Technology Specialist")
else:
    print("Plese Answare in Yes or No.")


print("\nThank you for using the Career Guidance Expert System!")

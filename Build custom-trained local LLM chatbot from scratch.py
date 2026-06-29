# Read biodata from file

with open("biodata.txt", "r", encoding="utf-8") as file:
    biodata = file.read().lower()

print("=" * 40)
print("      Manthan AI Assistant")
print("=" * 40)
print("Ask me about my biodata.")
print("Type 'exit' to quit.\n")

while True:
    question = input("You: ").lower().strip()

    if question == "exit":
        print("Bot: Goodbye! Have a great day.")
        break

    elif "name" in question:
        print("Bot: My name is Manthan Belekar.")

    elif "age" in question:
        print("Bot: I am 21 years old.")

    elif "study" in question or "student" in question or "college" in question:
        print("Bot: I am an Engineering student.")

    elif "branch" in question or "department" in question:
        print("Bot: I belong to the Computer Engineering department.")

    elif "skills" in question or "skill" in question or "learned" in question:
        print("Bot: I have learned Python, C++, DBMS, Computer Networks, Artificial Intelligence, Machine Learning, and IoT.")

    elif "language" in question:
        print("Bot: I know Python, C++, C, SQL, HTML, CSS, and JavaScript.")

    elif "project" in question or "projects" in question:
        print("Bot: I have worked on Face Recognition, Traffic Signal Automation, DC Motor Control, LDR-based LED Control, Calculator App, Text File Reader, and IoT projects using ESP32.")

    elif "experience" in question:
        print("Bot: I have experience in embedded systems, Python programming, and AI projects.")

    elif "team eta" in question or "eta" in question:
        print("Bot: I worked as a Vehicle Dynamics Engineer in Team ETA.")

    elif "internship" in question:
        print("Bot: I have completed internships related to AI and Embedded Systems.")

    elif "hobbies" in question or "interest" in question:
        print("Bot: I enjoy sketching, football, working out, coding, and learning new technologies.")

    elif "goal" in question or "career" in question:
        print("Bot: My goal is to become an AI and Software Engineer.")

    elif "contact" in question or "email" in question:
        print("Bot: Please refer to my biodata for contact details.")

    elif "resume" in question or "cv" in question:
        print("Bot: My biodata contains my academic and project details.")

    elif "biodata" in question:
        print("\n----- Biodata -----")
        print(biodata)
        print("-------------------")

    else:
        print("Bot: Sorry, I don't know the answer yet.")
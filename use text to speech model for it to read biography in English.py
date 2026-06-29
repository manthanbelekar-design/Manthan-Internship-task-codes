import pyttsx3

engine = pyttsx3.init()

bio = """
My name is Manthan Belekar.

I am an Engineering student.

I have learned Python programming, DBMS, Computer Networks, and Artificial Intelligence.

I have worked on projects involving face recognition, traffic signal automation, and IoT using ESP32.

I enjoy learning new technologies and building practical projects.

I was a part of our college mega project team, 'Team ETA', where I worked as a Vehicle Dynamics Engineer.

Apart from academics, I love sketching, football, and working out.

I am eager to apply my technical knowledge to real-world challenges and continuously improve my skills in software development and emerging technologies.
"""

engine.save_to_file(bio, "manthan_introduction.wav")
engine.runAndWait()

print("Audio saved as manthan_introduction.wav")
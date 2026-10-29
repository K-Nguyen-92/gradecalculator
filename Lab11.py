import os

import matplotlib.pyplot as plt


def load_students():
    students = {}
    with open("data/students.txt", "r") as file:
        for line in file:
            line = line.strip()
            s_id = line[:3]
            s_name = line[3:]
            students[s_name] = s_id
    return students


def load_assignments():
    assignments = {}
    with open("data/assignments.txt", "r") as file:
        lines = [line.strip() for line in file]
    for i in range(0, len(lines), 3):
        a_name = lines[i]
        a_id = int(lines[i + 1])
        a_point = float(lines[i + 2])
        assignments[a_id] = {"name": a_name, "point": a_point}
    return assignments


def load_submissions():
    submissions = []
    folder_path = "data/submissions"
    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)
        with open(full_path, "r") as file:
            content = file.read()
            items = [i.strip() for i in content.split("|")]
            s_id, a_id, pct = int(items[0]), int(items[1]), float(items[2])
            submissions.append(
                {"student_id": s_id, "assignment_id": a_id, "percentage": pct}
            )
    return submissions


def main():
    print("1. Student grade\n2. Assignment statistics\n3. Assignment graph")
    choice = int(input("Enter your selection: "))
    students = load_students()
    assignments = load_assignments()
    submissions = load_submissions()
    if choice == 1:
        s_name = input("What is the student's name: ")
        if s_name not in students:
            print("Student not found")
            return
        s_id = int(students[s_name])
        total = 0.0
        for sub in submissions:
            if sub["student_id"] == s_id:
                for assignment in assignments:
                    if assignment == sub["assignment_id"]:
                        earn_percent = (
                            sub["percentage"] * assignments[assignment]["point"]
                        ) / 100
                        total += earn_percent
        print(f"{round(total / 10)}%")
    elif choice == 2:
        a_name = input("What is the assignment name: ")
        a_list = []
        a_id = int()
        for assignment in assignments:
            a_list.append(assignments[assignment]["name"])
            if a_name == assignments[assignment]["name"]:
                a_id = assignment
        if a_name not in a_list:
            print("Assignment not found")
            return
        score = [
            sub["percentage"] for sub in submissions if sub["assignment_id"] == a_id
        ]
        min_score = round(min(score))
        max_score = round(max(score))
        avg_score = round(sum(score) / len(score))
        print(f"Min: {min_score}%\nAvg: {avg_score}%\nMax: {max_score}%")
    elif choice == 3:
        a_name = input("What is the assignment name: ")
        a_list = []
        a_id = int()
        for assignment in assignments:
            a_list.append(assignments[assignment]["name"])
            if a_name == assignments[assignment]["name"]:
                a_id = assignment
        if a_name not in a_list:
            print("Assignment not found")
            return
        score = [
            sub["percentage"] for sub in submissions if sub["assignment_id"] == a_id
        ]
        min_score = round(min(score))
        max_score = round(max(score))
        avg_score = round(sum(score) / len(score))
        plt.hist(score, bins=[50, 60, 70, 80, 90, 100])
        plt.xlabel("Percentage")
        plt.ylabel("Quantities")
        plt.title(f"{a_name} Graph", fontweight="bold")
        plt.show()


if __name__ == "__main__":
    main()

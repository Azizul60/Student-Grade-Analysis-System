import matplotlib.pyplot as plt

def main():
    students = []

    while True:
        name = input("Enter student name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break
        subject = input("Enter subject: ")
        try:
            score = int(input(f"Enter your score in {subject}: "))
        except ValueError:
            print("Invalid input. Please enter a numerical score.")
            continue

        students.append({'name': name, 'subject': subject, 'score': score})

    # Calculate and display averages
    calculate_subject_averages(students)
    
    # Ask for a subject to display top performers
    subject = input("Enter a subject to see the top performers: ")
    top_performers(students, subject)
    
    # Plot subject averages
    plot_subject_averages(students)


def calculate_subject_averages(students):
    subject_totals = {}
    subject_counts = {}

    for student in students:
        subject = student['subject']
        score = student['score']

        if subject in subject_totals:
            subject_totals[subject] += score
            subject_counts[subject] += 1
        else:
            subject_totals[subject] = score
            subject_counts[subject] = 1

    for subject, total in subject_totals.items():
        print(f"Average score for {subject}: {total / subject_counts[subject]:.2f}")


def top_performers(students, subject):
    subject_students = [s for s in students if s['subject'].lower() == subject.lower()]
    if not subject_students:
        print(f"No records found for the subject: {subject}")
        return

    subject_students.sort(key=lambda x: x['score'], reverse=True)
    top_3 = subject_students[:3]

    print(f"Top 3 performers in {subject}:")
    for student in top_3:
        print(f"{student['name']} - {student['score']}")


def plot_subject_averages(students):
    subject_totals = {}
    subject_counts = {}

    for student in students:
        subject = student['subject']
        score = student['score']

        if subject in subject_totals:
            subject_totals[subject] += score
            subject_counts[subject] += 1
        else:
            subject_totals[subject] = score
            subject_counts[subject] = 1

    subjects = list(subject_totals.keys())
    averages = [subject_totals[subject] / subject_counts[subject] for subject in subjects]

    plt.bar(subjects, averages)
    plt.xlabel('Subjects')
    plt.ylabel('Average Scores')
    plt.title('Average Scores per Subject')
    plt.show()


if __name__ == "__main__":
    main()

def find_top(student_marks):
    max_avg = 0
    top_st = ""
    for student, marks in student_marks.items():
        av_mark = sum(marks) / len(marks)
        if av_mark > max_avg:
            max_avg = av_mark
            top_st = student
    return top_st, max_avg

students = {
    "Alex": [4, 5, 7, 10, 9],
    "Sasha": [3, 6, 7, 8, 9],
    "Mary": [5, 10, 9, 8, 7]
}

top_student, av_mark = find_top(students)
print(f"Top student: {top_student} with average mark: {av_mark:.2f}")
# Create tuples for student records
student1 = ("John Doe", 18, "Grade 12")
student2 = ("Jane Smith", 17, "Grade 11")
student3 = ("Mike Johnson", 16, "Grade 10")

# Create a tuple of student records
students = (student1, student2, student3)

# Use tuple methods
print(f"Number of students: {len(students)}")
print(f"Index of Jane Smith: {students.index(student2)}")

# Create sets for student IDs and courses
student_ids = {1001, 1002, 1003, 1004, 1005}
courses = {"Math", "Science", "English", "History"}

# Perform set operations
print(f"Student IDs: {student_ids}")
print(f"Courses: {courses}")

new_students = {1006, 1007}
student_ids.update(new_students)
print(f"Updated Student IDs: {student_ids}")

completed_courses = {"Math", "English"}
remaining_courses = courses - completed_courses
print(f"Remaining Courses: {remaining_courses}")

# Use frozen sets
frozen_courses = frozenset(["Math", "Science", "English", "History"])
print(f"Frozen Courses: {frozen_courses}")

# Attempt to modify a frozen set (will raise an error)
# frozen_courses.add("Art")  # Uncommenting this line will raise an AttributeError

# Create a frozen set of student data
frozen_student_data = frozenset(students)
print(f"Frozen Student Data: {frozen_student_data}")
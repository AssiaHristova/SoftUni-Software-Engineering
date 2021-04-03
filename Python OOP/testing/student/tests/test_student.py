import unittest
from student.project.student import Student


class StudentTests(unittest.TestCase):
    def setUp(self):
        self.student = Student('Assia', {})

    def test_student_init__expect_to_create_it(self):
        self.assertEqual('Assia', self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_student_enroll__when_course_name_exist__expect_to_update_notes(self):
        self.student.enroll('Python', ['OOP Module'])
        result = "Course already added. Notes have been updated."
        notes = ['OOP Module', 'updated']

        self.assertEqual(result, self.student.enroll('Python', ['updated']))
        self.assertListEqual(notes, self.student.courses['Python'])

    def test_student_enroll__when_course_name_exist_when_add_notes_is_None__expect_to_put_notes(self):
        result = "Course and course notes have been added."
        notes = ['OOP Module']

        self.assertEqual(result, self.student.enroll('Python_3', ['OOP Module'], ''))
        self.assertListEqual(notes, self.student.courses['Python_3'])

    def test_student_enroll__when_course_name_exist_when_add_notes_is_Y__expect_to_put_notes(self):
        result = "Course and course notes have been added."
        notes = ['OOP Module']

        self.assertEqual(result, self.student.enroll('Python_3', ['OOP Module'], 'Y'))
        self.assertListEqual(notes, self.student.courses['Python_3'])

    def test_student_enroll__when_course_name_do_not_exist__expect_to_add_course(self):
        result = "Course has been added."

        self.assertEqual(result, self.student.enroll('Python_2', [], 'note'))
        self.assertListEqual([], self.student.courses['Python_2'])

    def test_student_add_notes__when_course_name_exist__expect_to_update_notes(self):
        self.student.enroll('Python', ['OOP Module'], '')
        result = "Notes have been updated"
        notes = ['OOP Module', 'updated']

        self.assertEqual(result, self.student.add_notes('Python', 'updated'))
        self.assertListEqual(notes, self.student.courses['Python'])

    def test_student_add_notes__when_course_name_do_not_exist__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.student.add_notes('Java', 'updated')

        self.assertEqual("Cannot add notes. Course not found.", str(context.exception))

    def test_student_leave_course__when_course_name_exist__expect_to_remove_it(self):
        self.student.enroll('Python', ['OOP Module'], '')
        result = "Course has been removed"

        self.assertEqual(result, self.student.leave_course('Python'))
        self.assertDictEqual({}, self.student.courses)

    def test_student_leave_course__when_course_name_do_not_exist__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.student.leave_course('Java')

        self.assertEqual("Cannot remove course. Course not found.", str(context.exception))


if __name__ == '__main__':
    unittest.main()

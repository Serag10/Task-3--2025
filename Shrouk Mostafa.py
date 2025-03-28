'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

from collections import defaultdict
import heapq

class ExamScheduler:
    def __init__(self, conflict_table, level_table, num_courses_per_level, pattern):
        self.conflict_table = conflict_table
        self.level_table = level_table
        self.num_courses_per_level = num_courses_per_level
        self.pattern = pattern
        self.course_levels = {}
        self.conflicts = defaultdict(dict)
        self.schedule = defaultdict(list)
        self.build_data()

    def build_data(self):
        for course_id, level in self.level_table:
            self.course_levels[course_id] = level

        for course1, course2, weight in self.conflict_table:
            self.conflicts[course1][course2] = weight
            self.conflicts[course2][course1] = weight  

    def generate_day_sequence(self):
        pattern_1 = ["First", "Third", "Second"]
        pattern_2 = ["Third", "First", "Second"]
        pattern_cycle = pattern_1 if self.pattern == 1 else pattern_2

        total_courses = sum(self.num_courses_per_level.values())
        day_sequence = []
        i = 0
        while len(day_sequence) * 1 < total_courses:
            day_sequence.append(pattern_cycle[i % 3])
            i += 1
        return day_sequence

    def assign_courses(self):
        course_conflict_sum = {
            course: sum(self.conflicts[course].values()) for course in self.course_levels
        }
        sorted_courses = sorted(course_conflict_sum.items(), key=lambda x: -x[1])
        sorted_courses = [c[0] for c in sorted_courses]

        day_sequence = self.generate_day_sequence()
        assigned = {}
        for course in sorted_courses:
            course_level = self.course_levels[course]
            for day_index, level in enumerate(day_sequence):
                if level == course_level:
                    conflict_cost = 0
                    for scheduled_course in self.schedule[day_index]:
                        conflict_cost += self.conflicts[course].get(scheduled_course, 0)
                    if conflict_cost == 0:
                        self.schedule[day_index].append(course)
                        assigned[course] = day_index
                        break
            else:
                min_cost = float('inf')
                best_day = -1
                for day_index, level in enumerate(day_sequence):
                    if level == course_level:
                        conflict_cost = 0
                        for scheduled_course in self.schedule[day_index]:
                            conflict_cost += self.conflicts[course].get(scheduled_course, 0)
                        if conflict_cost < min_cost:
                            min_cost = conflict_cost
                            best_day = day_index
                self.schedule[best_day].append(course)
                assigned[course] = best_day

    def calculate_total_conflict_cost(self):
        total_cost = 0
        for day_courses in self.schedule.values():
            for i in range(len(day_courses)):
                for j in range(i + 1, len(day_courses)):
                    c1 = day_courses[i]
                    c2 = day_courses[j]
                    total_cost += self.conflicts[c1].get(c2, 0)
        return total_cost

    def print_schedule(self):
        print("\n📅 Final Exam Schedule:")
        for day, courses in sorted(self.schedule.items()):
            level = self.course_levels[courses[0]] if courses else "Unknown"
            print(f"Day {day+1} ({level}): {courses}")
        print("\n💰 Final Conflict Cost:", self.calculate_total_conflict_cost())


if __name__ == "__main__":
    conflict_table = [
        ("CS101", "CS102", 10),
        ("CS101", "CS201", 5),
        ("CS102", "CS202", 8),
        ("CS201", "CS301", 7),
        ("CS202", "CS301", 6),
        ("CS301", "CS302", 9)
    ]

    level_table = [
        ("CS101", "First"),
        ("CS102", "First"),
        ("CS201", "Second"),
        ("CS202", "Second"),
        ("CS301", "Third"),
        ("CS302", "Third")
    ]

    num_courses_per_level = {
        "First": 2,
        "Second": 2,
        "Third": 2
    }

    scheduler = ExamScheduler(conflict_table, level_table, num_courses_per_level, pattern=1)
    scheduler.assign_courses()
    scheduler.print_schedule()

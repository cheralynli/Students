def read_input_data():
    number_of_students= int(input().strip())
    students_db = []
    grade_records = []
    for i in range(number_of_students):
        student_info = input().strip().split(",")
        std_id = student_info[0].strip()
        std_name = student_info[1].strip()
        students_db.append({"student id": std_id, "student name": std_name})
    number_of_grades= int(input().strip())
    for i in range(number_of_grades):
        grade_info = input().strip().split(",")
        std_id= grade_info[0].strip()
        subject= grade_info[1].strip()
        grade= float(grade_info[2].strip())
        grade_records.append({"student id": std_id, "subject": subject, "score": grade})
    return students_db, grade_records

def calculate_subject_metrics(grade_records)
    subject_stats={}
    for record in grade_records:
        subject = record["subject"]
        score = record["score"]
        if subject not in subject_stats:
            subject_stats[subject] = {
                "total_score": 0,
                "count": 0, 
                "max_score": score, 
                "min_score": score,
                "passed_count": 0
                }
        subject_stats[subject]["count"] += 1
        subject_stats[subject]["total_score"] += score
        if score > subject_stats[subject]["max_score"]:
            subject_stats[subject]["max_score"] = score
        if score < subject_stats[subject]["min_score"]:
            subject_stats[subject]["min_score"] = score
        if score>=60:
            subject_stats[subject]["passed_count"] += 1
    final_res={}
    for subject, stats in subject_stats.items():
        final_res[subject] = {
            "avg": stats["total_score"]/stats["count"],
            "min": stats["min_score"],
            "max": stats["max_score"],
            "pass_rate": stats["passed_count"]/stats["count"]
        }
    return final_res

def calculate_student_total_scores(students_db, grade_records):
    student_scores=[]
    for student in students_db:
        std_id= student["student id"]
        std_name= student["student name"]
        total_score=0
        for record in grade_records:
            if record["student id"]==std_id:
                total_score += record["score"]
        student_scores.append({
            "id": std_id,
            "name": std_name,
            "total score": total_score
        })
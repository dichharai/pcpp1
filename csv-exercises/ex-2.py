import csv


with open('exam_results.csv', mode="r", newline='') as infile:
    fieldnames = ["Exam Name", "Candidate ID", "Score", "Grade"]
    reader = csv.DictReader(infile, fieldnames=fieldnames)
    
    math_dict = {"Exam Name": "Maths", "Number of Candidates": 0, "Number of Passed Exams": 0, "Number of Failed Exams": 0, "Best Score": 0, "Worst Score": 100}
    phys_dict = {"Exam Name": "Physics", "Number of Candidates": 0, "Number of Passed Exams": 0, "Number of Failed Exams": 0, "Best Score": 0, "Worst Score": 100}
    bio_dict = {"Exam Name": "Biology", "Number of Candidates": 0, "Number of Passed Exams": 0, "Number of Failed Exams": 0, "Best Score": 0, "Worst Score": 100}
    reader.__next__()

    for row in reader:
        subject = row["Exam Name"]
        candidate = row["Candidate ID"]
        score = int(row["Score"])
        grade = row["Grade"]

        if subject == "Maths":
            math_dict["Number of Candidates"] += 1
            if grade == "Pass":
               math_dict["Number of Passed Exams"] += 1
            else:
                math_dict["Number of Failed Exams"] += 1

            if score > math_dict["Best Score"]:
                math_dict["Best Score"] = score

            if score < math_dict["Worst Score"]:
                math_dict["Worst Score"] = score
        
        elif subject == "Biology":
            bio_dict["Number of Candidates"] += 1
            if grade == "Pass":
               bio_dict["Number of Passed Exams"] += 1
            else:
                bio_dict["Number of Failed Exams"] += 1
                
            if score > bio_dict["Best Score"]:
                bio_dict["Best Score"] = score

            if score < bio_dict["Worst Score"]:
                bio_dict["Worst Score"] = score
        
        elif  subject == "Physics":
            phys_dict["Number of Candidates"] += 1
            if grade == "Pass":
               phys_dict["Number of Passed Exams"] += 1
            else:
                phys_dict["Number of Failed Exams"] += 1
                
            if score > phys_dict["Best Score"]:
                phys_dict["Best Score"] = score

            if score < phys_dict["Worst Score"]:
                phys_dict["Worst Score"] = score
        
        else:
            print(f"Not a valid subject: {subject}")

    
    # print(bio_dict)
    # print(math_dict)
    # print(phys_dict)

    with open("exam-compre-result.csv", mode="w", newline="") as outfile:
        fieldnames=["Exam Name", "Number of Candidates", "Number of Passed Exams", "Number of Failed Exams", "Best Score", "Worst Score"]

        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        print(writer.fieldnames)
        writer.writerow(math_dict)

        writer.writerow(phys_dict)

        writer.writerow(bio_dict)
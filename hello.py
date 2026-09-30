import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# COLLEGE PLACEMENT ANALYSIS PROJECT
# ==========================================

# Sample student placement data
data = {
    "Student_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
                   111, 112, 113, 114, 115],
    
    "Name": ["Aarav", "Diya", "Riya", "Rahul", "Krisha",
             "Dev", "Meera", "Yash", "Ananya", "Harsh",
             "Pooja", "Karan", "Neha", "Vivek", "Jiya"],
    
    "Department": ["Computer", "Computer", "IT", "IT", "Computer",
                   "Mechanical", "Computer", "IT", "Civil", "Computer",
                   "IT", "Mechanical", "Civil", "Computer", "IT"],
    
    "CGPA": [8.7, 7.9, 8.5, 7.2, 9.1,
             6.8, 8.2, 7.5, 6.9, 8.8,
             7.7, 7.0, 7.4, 9.0, 8.1],
    
    "Skills": ["Python", "Java", "Python", "Java", "Python",
               "AutoCAD", "Python", "Java", "AutoCAD", "Python",
               "Java", "AutoCAD", "C++", "Python", "Java"],
    
    "Placement_Status": ["Placed", "Placed", "Placed", "Not Placed", "Placed",
                         "Not Placed", "Placed", "Placed", "Not Placed", "Placed",
                         "Placed", "Not Placed", "Placed", "Placed", "Placed"],
    
    "Package_LPA": [7.5, 6.2, 8.0, 0, 9.5,
                    0, 7.0, 6.8, 0, 8.5,
                    6.5, 0, 5.5, 9.0, 7.2]
}

# Create DataFrame
df = pd.DataFrame(data)

# ==========================================
# DISPLAY DATA
# ==========================================

print("\n========== COLLEGE PLACEMENT DATA ==========\n")
print(df.to_string(index=False))


# ==========================================
# BASIC INFORMATION
# ==========================================

print("\n========== BASIC INFORMATION ==========")

print("\nTotal Students:", len(df))

placed_students = (df["Placement_Status"] == "Placed").sum()
not_placed_students = (df["Placement_Status"] == "Not Placed").sum()

print("Placed Students:", placed_students)
print("Not Placed Students:", not_placed_students)


# ==========================================
# PLACEMENT PERCENTAGE
# ==========================================

placement_percentage = (placed_students / len(df)) * 100

print("\n========== PLACEMENT RESULT ==========")
print("Placement Percentage: {:.2f}%".format(placement_percentage))


# ==========================================
# SALARY ANALYSIS
# ==========================================

placed_df = df[df["Placement_Status"] == "Placed"]

average_package = placed_df["Package_LPA"].mean()
highest_package = placed_df["Package_LPA"].max()
lowest_package = placed_df["Package_LPA"].min()

print("\n========== PACKAGE ANALYSIS ==========")
print("Average Package: {:.2f} LPA".format(average_package))
print("Highest Package: {:.2f} LPA".format(highest_package))
print("Lowest Package: {:.2f} LPA".format(lowest_package))


# ==========================================
# DEPARTMENT-WISE ANALYSIS
# ==========================================

print("\n========== DEPARTMENT-WISE ANALYSIS ==========")

department_analysis = df.groupby("Department").agg(
    Total_Students=("Student_ID", "count"),
    Placed_Students=("Placement_Status",
                     lambda x: (x == "Placed").sum())
)

department_analysis["Placement_Percentage"] = (
    department_analysis["Placed_Students"] /
    department_analysis["Total_Students"] * 100
)

print(department_analysis)


# ==========================================
# DEPARTMENT-WISE AVERAGE PACKAGE
# ==========================================

print("\n========== DEPARTMENT-WISE AVERAGE PACKAGE ==========")

department_package = placed_df.groupby("Department")["Package_LPA"].mean()

print(department_package)


# ==========================================
# CGPA ANALYSIS
# ==========================================

print("\n========== CGPA ANALYSIS ==========")

average_cgpa = df["CGPA"].mean()

print("Average CGPA: {:.2f}".format(average_cgpa))

print("\nAverage CGPA of Placed Students:")

placed_cgpa = df[df["Placement_Status"] == "Placed"]["CGPA"].mean()

print("{:.2f}".format(placed_cgpa))


# ==========================================
# SKILL-WISE ANALYSIS
# ==========================================

print("\n========== SKILL-WISE ANALYSIS ==========")

skill_analysis = df.groupby("Skills")["Placement_Status"].apply(
    lambda x: (x == "Placed").sum()
)

print(skill_analysis)


# ==========================================
# GRAPH 1 - PLACED VS NOT PLACED
# ==========================================

plt.figure(figsize=(7, 5))

status_count = df["Placement_Status"].value_counts()

plt.bar(status_count.index, status_count.values)

plt.title("Placed vs Not Placed Students")
plt.xlabel("Placement Status")
plt.ylabel("Number of Students")

plt.tight_layout()
plt.show()


# ==========================================
# GRAPH 2 - DEPARTMENT-WISE STUDENTS
# ==========================================

plt.figure(figsize=(8, 5))

department_count = df["Department"].value_counts()

plt.bar(department_count.index, department_count.values)

plt.title("Department-wise Student Count")
plt.xlabel("Department")
plt.ylabel("Number of Students")

plt.tight_layout()
plt.show()


# ==========================================
# GRAPH 3 - DEPARTMENT-WISE PLACEMENT %
# ==========================================

plt.figure(figsize=(8, 5))

plt.bar(
    department_analysis.index,
    department_analysis["Placement_Percentage"]
)

plt.title("Department-wise Placement Percentage")
plt.xlabel("Department")
plt.ylabel("Placement Percentage (%)")

plt.ylim(0, 110)
plt.tight_layout()
plt.show()


# ==========================================
# GRAPH 4 - PACKAGE ANALYSIS
# ==========================================

plt.figure(figsize=(9, 5))

plt.bar(
    placed_df["Name"],
    placed_df["Package_LPA"]
)

plt.title("Student-wise Placement Package")
plt.xlabel("Student")
plt.ylabel("Package (LPA)")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ==========================================
# GRAPH 5 - CGPA VS PACKAGE
# ==========================================

plt.figure(figsize=(8, 5))

plt.scatter(
    placed_df["CGPA"],
    placed_df["Package_LPA"]
)

plt.title("CGPA vs Placement Package")
plt.xlabel("CGPA")
plt.ylabel("Package (LPA)")

plt.grid(True)
plt.tight_layout()
plt.show()


# ==========================================
# FINAL SUMMARY
# ==========================================

print("\n==========================================")
print("       COLLEGE PLACEMENT SUMMARY")
print("==========================================")

print("Total Students       :", len(df))
print("Placed Students      :", placed_students)
print("Not Placed Students  :", not_placed_students)
print("Placement Percentage :", "{:.2f}%".format(placement_percentage))
print("Average Package      :", "{:.2f} LPA".format(average_package))
print("Highest Package      :", "{:.2f} LPA".format(highest_package))
print("Lowest Package       :", "{:.2f} LPA".format(lowest_package))
print("Average CGPA         :", "{:.2f}".format(average_cgpa))

print("\n========== ANALYSIS COMPLETED ==========")
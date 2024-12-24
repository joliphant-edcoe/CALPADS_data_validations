import pandas as pd

# report 8.1 will give student list (be sure to select all grades)
# report 16.14 will give sped status for all students (select all grades)

CBEDS_DAY = "2024-10-02"


def check_infant_enrollments(student_list, sped_list):
    stu = (
        student_list.merge(sped_list, on="SSID", how="left")
        .assign(
            birthday=lambda df_: pd.to_datetime(df_.Student_Birth_Date),
            age_on_cbeds=lambda df_: (pd.to_datetime(CBEDS_DAY) - df_.birthday).dt.days
            / 365.25,
            enrollment_before_cbeds=lambda df_: pd.to_datetime(df_.Start_Date)
            < pd.to_datetime(CBEDS_DAY),
            dsea_edcoe=lambda df_: df_.DSEAName
            == "El Dorado County Office of Education",
            plan_type=lambda df_: df_.SpecialEdProgramType.isin(
                [
                    "300-Special Day Class (SDC)",
                    "100-Designated Instruction Services (DIS)",
                ]
            ),
            plan_effect_before_cbeds=lambda df_: pd.to_datetime(
                df_.PlanEffectiveStartdate
            )
            < pd.to_datetime(CBEDS_DAY),
        )
        .query("age_on_cbeds < 3")
        .sort_values("age_on_cbeds", ascending=True)
        .loc[
            :,
            [
                "SchoolName_x",
                "SSID",
                "StudentName_x",
                "LocalID",
                "Grade_Level_Code",
                "Student_Birth_Date",
                "Start_Date",
                "EnrollmentStatusName",
                "Exit_Date",
                "GeoRsdncDistName",
                "Special_Education",
                "DistrictofSpecialEducationAccountability",
                "DSEAName",
                "InitialServiceStartDate",
                "EligibleandParticipatingStatusStartDate",
                "PlanType",
                "PlanEffectiveStartdate",
                "ProgramSettingCode",
                "SpecialEdProgramType",
                "EnrollmentStatus",
                "EnrollmentStartDate",
                "EnrollmentExitDate",
                "birthday",
                "age_on_cbeds",
                "enrollment_before_cbeds",
                "dsea_edcoe",
                "plan_type",
                "plan_effect_before_cbeds",
            ],
        ]
    )
    return stu


file1 = "8.1_StudentProfileList.csv"
students = pd.read_csv(file1)
file2 = "16.14_StudentswithDisabilitiesPlanStudentList.csv"
sped = pd.read_csv(file2)

result = check_infant_enrollments(students, sped)

print(result)
result.to_csv("results.csv",index=False)

print(
    f"There are {len(result)} infants that were less than 3 on CBEDS day ({CBEDS_DAY})"
)
print(
    f"There are {result.enrollment_before_cbeds.sum()} infants that were enrolled on CBEDS day ({CBEDS_DAY})"
)
print(f"There are {result.dsea_edcoe.sum()} infants that have DSEA listed at EDCOE")
print(f"There are {result.plan_type.sum()} infants that had the correct plan type")
print(
    f"There are {result.plan_effect_before_cbeds.sum()} infants that had a plan effective on CBEDS day ({CBEDS_DAY})"
)

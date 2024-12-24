import os
import pandas as pd


def find_preschoolers(filename):

    df = pd.read_csv(
        filename,
        sep="^",
        parse_dates=["EnrollmentStartDate", "EnrollmentExitDate"],
        names=[
            "RecordTypeCode",
            "TransactionTypeCode",
            "LocalRecordID",
            "ReportingLEA",
            "SchoolofAttendance",
            "SchoolofAttendanceNPS",
            "AcademicYearID",
            "SSID",
            "LocalStudentID",
            "StudentLegalFirstName",
            "StudentLegalMiddleName",
            "StudentLegalLastName",
            "StudentLegalNameSuffix",
            "StudentAliasFirstName",
            "StudentAliasMiddleName",
            "StudentAliasLastName",
            "StudentBirthDate",
            "StudentGenderCode",
            "StudentBirthCity",
            "StudentBirthStateProvinceCode",
            "StudentBirthCountryCode",
            "EnrollmentStartDate",
            "EnrollmentStatusCode",
            "GradeLevelCode",
            "EnrollmentExitDate",
            "StudentExitReasonCode",
            "StudentSchoolCompletionStatus",
            "ExpectedReceiverSchoolofAttendance",
            "StudentMetallUCCSURequirementsIndicator",
            "StudentSchoolTransferCode",
            "DistrictofGeographicResidenceCode",
            "MeritDiplomaIndicator",
            "SealofBiliteracyIndicator",
            "AdultAgeStudentswithDisabilitiesinTransitionStatus",
            "GraduationExemptionIndicator",
            "a",
            "b",
        ],
    )

    return df.query('GradeLevelCode == "PS"').loc[
        :,
        [
            "ReportingLEA",
            "SchoolofAttendance",
            "SchoolofAttendanceNPS",
            "AcademicYearID",
            "SSID",
            "LocalStudentID",
            "StudentLegalFirstName",
            "StudentLegalLastName",
            "EnrollmentStartDate",
            "EnrollmentStatusCode",
            "GradeLevelCode",
            "EnrollmentExitDate",
            "StudentExitReasonCode",
        ],
    ]


## TODO: automate extraction of each district's SENR extract for CBEDS Day and check for preschoolers.
## buckeye (0961838) is expected to have some preschoolers because they do employee their own SLPs at William Brooks and Oak Meadow
## no need to check indian diggings, silver fork, or the high school district


files = os.listdir()

for f in files:
    _,ex = os.path.splitext(f)
    if ex == '.txt':
        result = find_preschoolers(f)
        print(f)
        if len(result) == 0:
            print('Empty DataFrame')
        else:
            
            print(result)

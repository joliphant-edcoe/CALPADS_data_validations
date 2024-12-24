import pandas as pd

# The snapshot report doesn't find the grade options, and the ods reports don't list 16.14 or 16.16. 
# For now we will have to download the reports manually...

# import sys
# import os

# current_dir = os.path.dirname(os.path.abspath(__file__))
# parent_dir = os.path.dirname(current_dir)
# sys.path.append(parent_dir)

# from calpads.client import CALPADSClient

# cc = CALPADSClient(username="fiscaldata@edcoe.org", password="FiscalData$11")


# dry = cc.download_report("0910090", "16.14", is_snapshot=False, dry_run=True)

# print(dry)

# form_input_2_14 = {
#     "AcademicYear": "2024-2025",
#     "LEAESIID": dry["LEAESIIDBySession"][0],
#     "Status": "Revised Uncertified",
#     "SELPA": {key: True for key, _ in dry["SELPA"].items()},
#     "Gender": {key: True for key, _ in dry["Gender"].items()},
#     "Race": {key: True for key, _ in dry["Race"].items()},
#     "SchoolTypeCodeValue": {key: True for key, _ in dry["SchoolTypeCodeValue"].items()},
#     "School": {key: True for key, _ in dry["School"].items()},
#     "Grade": {key: True for key, _ in dry["Grade"].items()},     ## this one is the problem....
#     "TitleIpartCMigrant": {key: True for key, _ in dry["TitleIpartCMigrant"].items()},
#     "Socioeconomicaldis": {key: True for key, _ in dry["Socioeconomicaldis"].items()},
#     "specialeducation": {key: True for key, _ in dry["specialeducation"].items()},
#     "GiftedandTalented": {key: True for key, _ in dry["GiftedandTalented"].items()},
#     "TitleIIIEligibleImmigrant": {
#         key: True for key, _ in dry["TitleIIIEligibleImmigrant"].items()
#     },
#     "EnglishLanguageAcquisitionstatus": {
#         key: True for key, _ in dry["EnglishLanguageAcquisitionstatus"].items()
#     },
# }


df1 = pd.read_csv("16.14_StudentswithDisabilitiesPlanStudentList.csv")
df2 = pd.read_csv("16.16_StudentswithDisabilitiesServiceStudentList.csv")

# Perform an outer merge to get all records
merged_df = pd.merge(df1, df2, on="SSID", how="outer", indicator=True)

# Filter for records only in df1
df1_only = merged_df[merged_df["_merge"] == "left_only"]

# Filter for records only in df2
df2_only = merged_df[merged_df["_merge"] == "right_only"]

print("Students that have a PLAN file but no SERVICES:")
print(df1_only[["SSID"]])  

print("Students that have a SERVICES file but no PLAN:")
print(df2_only[["SSID"]])  

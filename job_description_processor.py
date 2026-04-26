from text_preprocessing import clean_text

with open("job_description.txt", "r") as file:
    job_description = file.read()

cleaned_jd = clean_text(job_description)

print("\n--- CLEANED JOB DESCRIPTION ---\n")
print(cleaned_jd)

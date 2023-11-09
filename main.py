from LinkedIn import LinkedIn
linkedin_email = "hovdikruslan@gmail.com"
linkedin_password = "HondaRoyal0401!"
target_company_link = "https://www.linkedin.com/company/unilever/"
if __name__ == "__main__":
    connection = LinkedIn()
    login_state = connection.login(linkedin_email, linkedin_password)
    if login_state:
        print("Logged in to LinkedIn!")
        company_id = connection.getCompanyID(target_company_link)
        if company_id is not None:
            print("Collecting all company member profiles upto 10000!")
            profile_list, page_count = connection.listProfiles(company_id, 1, True)
            for page_no in range(2,page_count+1):
                profile_list.extend(connection.listProfiles(company_id, page_no))
            print("Profile list collected and saved! Extracting emails ...")
            all_emails = connection.bulkScan(profile_list)
            for email in all_emails:
                print(email)
                connection.saveEmail(email)
    else:
        print("Unable to login to LinkedIn!")
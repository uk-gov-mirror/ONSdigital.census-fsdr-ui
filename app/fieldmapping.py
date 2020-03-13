from app.tabutils import table_generation, format_to_uk_dates


def map_employee_history_table_headers(user_role, employee_history_table):
    employee_history_table_mapped = []
    for history in employee_history_table:
        employee_name = map_employee_name(history)

        if user_role != 'hr':
            employee_emergency_contact_name = map_emergency_contact_name(history)

        if user_role == 'fsss':
            employee_history_table_mapping = {'Ingest Date': history.pop('ingestDate'),
                                              'ID': history.pop('uniqueEmployeeId'),
                                              'Name': employee_name,
                                              'Preferred Name': history.pop('preferredName'),
                                              'ONS ID': history.pop('onsId'),
                                              'Personal Mobile Number': history.pop('telephoneNumberContact1'),
                                              'Home Phone Number': history.pop('telephoneNumberContact2'),
                                              'Status': history.pop('status'),
                                              'Badge ID': history.pop('idBadgeNo'),
                                              'Personal Email Address': history.pop('personalEmailAddress'),
                                              'Postcode': history.pop('postcode'),
                                              'Country': history.pop('country'),
                                              'Emergency Contact 1 Name': employee_emergency_contact_name[0],
                                              'Emergency Contact 1 Mobile Number': history.pop(
                                                  'emergencyContactMobileNo'),
                                              'Emergency Contact 2 Name': employee_emergency_contact_name[1],
                                              'Emergency Contact 2 Mobile Number': history.pop(
                                                  'emergencyContactMobileNo2'),
                                              'Weekly Hours': history.pop('weeklyHours'),
                                              'Mobility': history.pop('mobility'),
                                              'Mobile Staff': history.pop('mobileStaff')
                                              }
        if user_role == 'hr':
            employee_history_table_mapping = {'Ingest Date': history.pop('ingestDate'),
                                              'ID': history.pop('uniqueEmployeeId'),
                                              'Name': employee_name,
                                              'Preferred Name': history.pop('preferredName'),
                                              'ONS ID': history.pop('onsId'),
                                              'Personal Mobile Number': history.pop('telephoneNumberContact1'),
                                              'Status': history.pop('status'),
                                              'Personal Email Address': history.pop('personalEmailAddress'),
                                              'Country': history.pop('country'),
                                              'Date of Birth': history.pop('dob'),
                                              'Age': history.pop('age'),
                                              'Ethnicity': history.pop('ethnicity'),
                                              'Nationality': history.pop('nationality'),
                                              'Disability': history.pop('disability'),
                                              'Gender': history.pop('gender'),
                                              'Sexual Orientation': history.pop('sexualOrientation'),
                                              'Religion': history.pop('religion'),
                                              'Driving Information': history.pop('drivingInformation'),
                                              'Civil Service Pension Recipient': history.pop(
                                                  'civilServicePensionRecipient'),
                                              'Current Civil Servant': history.pop('currentCivilServant'),
                                              'Previous Civil Servant': history.pop('previousCivilServant')
                                              }
        if user_role == 'recruitment':
            history['address'] = history['address1'] + ' ' + history['address2']

            employee_history_table_mapping = {'Ingest Date': history.pop('ingestDate'),
                                              'ID': history.pop('uniqueEmployeeId'),
                                              'Name': employee_name,
                                              'Preferred Name': history.pop('preferredName'),
                                              'ONS ID': history.pop('onsId'),
                                              'Personal Mobile Number': history.pop('telephoneNumberContact1'),
                                              'Status': history.pop('status'),
                                              'Badge ID': history.pop('idBadgeNo'),
                                              'Personal Email Address': history.pop('personalEmailAddress'),
                                              'Address': history.pop('address'),
                                              'County': history.pop('county'),
                                              'Postcode': history.pop('postcode'),
                                              'Country': history.pop('country'),
                                              'Emergency Contact 1 Name': employee_emergency_contact_name[0],
                                              'Emergency Contact 1 Mobile Number': history.pop(
                                                  'emergencyContactMobileNo'),
                                              'Emergency Contact 2 Name': employee_emergency_contact_name[1],
                                              'Emergency Contact 2 Mobile Number': history.pop(
                                                  'emergencyContactMobileNo2'),
                                              'Date of Birth': history.pop('dob'),
                                              'Age': history.pop('age'),
                                              'Ethnicity': history.pop('ethnicity'),
                                              'Nationality': history.pop('nationality'),
                                              'Disability': history.pop('disability'),
                                              'Gender': history.pop('gender'),
                                              'Sexual Orientation': history.pop('sexualOrientation'),
                                              'Religion': history.pop('religion'),
                                              'Welsh Language Speaker': history.pop('welshLanguageSpeaker'),
                                              'Any Languages Spoken': history.pop('anyLanguagesSpoken'),
                                              'Work Restrictions': history.pop('workRestrictions'),
                                              'Weekly Hours': history.pop('weeklyHours'),
                                              'Reasonable Adjustments': history.pop('reasonableAdjustments'),
                                              'Mobility': history.pop('mobility'),
                                              'Mobile Staff': history.pop('mobileStaff')
                                              }

        employee_history_table_mapped.append(employee_history_table_mapping)

    full_table = table_generation(employee_history_table_mapped)

    return full_table


def map_employee_history_job_role_table_headers(employee_history_job_role_table):
    employee_history_job_role_table_mapped = []

    for job_roles in employee_history_job_role_table:
        employee_history_job_role_table_mapping = {'Operational Start Date': job_roles.pop('contractStartDate'),
                                                   'Operational End Date': job_roles.pop('operationalEndDate'),
                                                   'Job Role ID': job_roles.pop('uniqueRoleId'),
                                                   'Job Role': job_roles.pop('jobRole'),
                                                   'Area Location': job_roles.pop('areaLocation'),
                                                   'Assignment Status': job_roles.pop('assignmentStatus'),
                                                   'Active Job': job_roles.pop('active')}

        employee_history_job_role_table_mapping['Operational Start Date'] = format_to_uk_dates(
            employee_history_job_role_table_mapping['Operational Start Date'])
        employee_history_job_role_table_mapping['Operational End Date'] = format_to_uk_dates(
            employee_history_job_role_table_mapping['Operational End Date'])

        if employee_history_job_role_table_mapping['Active Job']:
            employee_history_job_role_table_mapping['Active Job'] = 'Yes'
        else:
            employee_history_job_role_table_mapping['Active Job'] = 'No'

        employee_history_job_role_table_mapped.append(employee_history_job_role_table_mapping)

    job_role_history_table = table_generation(employee_history_job_role_table_mapped)

    return job_role_history_table


def map_employee_name(employee_table):
    if employee_table['firstName'] is None and employee_table['surname'] is None:
        employee_name = '-'
    elif employee_table['firstName'] is None:
        employee_name = employee_table['surname']
    elif employee_table['surname'] is None:
        employee_name = employee_table['firstName']
    else:
        employee_name = employee_table['firstName'] + ' ' + employee_table['surname']

    if employee_name == '- -':
        employee_name = '-'

    return employee_name


def map_emergency_contact_name(employee_table):
    if employee_table['emergencyContactFirstName'] is None and employee_table['emergencyContactSurname'] is None:
        emergency_contact_1 = '-'
    elif employee_table['emergencyContactFirstName'] is None:
        emergency_contact_1 = employee_table['emergencyContactSurname']
    elif employee_table['emergencyContactSurname'] is None:
        emergency_contact_1 = employee_table['emergencyContactFirstName']
    else:
        emergency_contact_1 = employee_table['emergencyContactFirstName'] + ' ' + \
                              employee_table['emergencyContactSurname']

    if emergency_contact_1 == '- -':
        emergency_contact_1 = '-'

    if employee_table['emergencyContactFirstName2'] is None and employee_table['emergencyContactSurname2'] is None:
        emergency_contact_2 = '-'
    elif employee_table['emergencyContactFirstName2'] is None:
        emergency_contact_2 = employee_table['emergencyContactSurname2']
    elif employee_table['emergencyContactSurname2']is None:
        emergency_contact_2 = employee_table['emergencyContactFirstName2']
    else:
        emergency_contact_2 = employee_table['emergencyContactFirstName2'] + ' ' + \
                              employee_table['emergencyContactSurname2']

    if emergency_contact_2 == '- -':
        emergency_contact_2 = '-'

    emergency_contacts = [emergency_contact_1, emergency_contact_2]

    return emergency_contacts
from aiohttp_session import get_session


async def store_search_criteria(request, search_criteria):
    session = await get_session(request)
    if 'assignmentStatus' in search_criteria.keys():
        session['assignmentStatus'] = search_criteria.get('assignmentStatus')
    if 'jobRole' in search_criteria.keys():
        session['jobRole'] = search_criteria.get('jobRole')
    if 'area' in search_criteria.keys():
        session['area'] = search_criteria.get('area')
    if 'surname' in search_criteria.keys():
        session['surname'] = search_criteria.get('surname')
    if 'firstName' in search_criteria.keys():
        session['firstName'] = search_criteria.get('firstName')
    if 'badgeNumber' in search_criteria.keys():
        session['badgeNumber'] = search_criteria.get('badgeNumber')
    if 'jobRoleId' in search_criteria.keys():
        session['jobRoleId'] = search_criteria.get('jobRoleId')


async def clear_stored_search_criteria(session):
    if session.get('assignmentStatus'):
        del session['assignmentStatus']

    if session.get('jobRole'):
        del session['jobRole']

    if session.get('area'):
        del session['area']

    if session.get('surname'):
        del session['surname']

    if session.get('firstName'):
        del session['firstName']

    if session.get('badgeNumber'):
        del session['badgeNumber']

    if session.get('jobRoleId'):
        del session['jobRoleId']


def retrieve_job_roles(job_roles, previous_jobrole_selected):
    add_job_roles = []
    for job_roles in job_roles.json():
        add_job_roles.append({
            'value': job_roles,
            'text': job_roles
        }, )
    if previous_jobrole_selected:
        add_job_roles.append({
            "value": previous_jobrole_selected,
            "text": previous_jobrole_selected,
            "disabled": False,
            "selected": True
        })
    else:
        add_job_roles.append({
            "value": "",
            "text": "Select a job role",
            "disabled": True,
            "selected": True
        })

    return add_job_roles


def retrieve_assignment_statuses(assignment_statuses):
    add_assignment = []
    for assignments in assignment_statuses.json():
        add_assignment.append({
            'value': assignments,
            'text': assignments
        }, )
    add_assignment.append({
        "value": "",
        "text": "Select assignment status",
        "disabled": True,
        "selected": True
    })

    return add_assignment

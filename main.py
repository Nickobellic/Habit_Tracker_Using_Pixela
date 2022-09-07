import requests
from datetime import datetime
today = datetime.now()
kms = float(input('Enter the Km value(0 for No value):'))
pixela = "https://pixe.la/v1/users/<username>/graphs"

param = {
    'token': "<token>",
    'username': '<username>',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}


graph_params = {
    'id': '<id>',
    'name': '<graph_name>',
    'unit': '<unit_of_measurement>',
    'type': 'int',
    'color': 'sora'
}
cycle_pixel_param = {
    'date': f"{today.strftime('%Y%m%d')}",
    'quantity': str(kms)
}

cycling_params = {
    'id': '<graph_id>',
    'name': '<graph_name>',
    'unit': '<unit_of_measurement>',
    'type': 'float',
    'color': 'momiji'
}

header = {
    "X-USER-TOKEN": "<authentication-token>"
}

pixel_param = {
    'date': f"{today.strftime('%Y%m%d')}",
    'quantity': '1'
}

post_pixel = requests.post(url=f"{pixela}/gtaonline", headers=header, json=pixel_param)
# update_attendance = requests.put(url=f"{pixela}/gtaonline", headers=header,json=put_attendance_param)     #TESTING OF 'PUT' REQUEST
# requests.delete(url=f"{pixela}/bicycle/{today.strftime('%Y%m%d')}", headers=header)   TESTING 'DELETE' REQUEST


post_pixel_cycling = requests.post(url=f"{pixela}/bicycle", headers=header, json=cycle_pixel_param)
print(f"Attendance: <link of the graph1>\nCycling: <link of the graph2>")

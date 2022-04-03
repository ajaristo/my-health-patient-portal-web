from django.shortcuts import render
from . import fhir

# Create your views here.

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="cs-792-my-health-083c7ccd10ab.json"

def example_view(request):
    # my_app/templates/my_app/example.html
    return render(request, 'my_app/example.html')


def portal_view(request):

    my_var = {'first_name': 'Aris', 'last_name': 'ARISTORENAS',
              'some_list':[1, 2, 3], 'some_dict': {'inside_key': 'inside_value'},
              'user_logged_in': True
    }

    patient_resource = fhir.get_resource()
    
    fhir_var = {'address': str(patient_resource["address"][0]["line"][0]),
                'birthDate': str(patient_resource["birthDate"]),
                'givenName': str(''.join(i for i in patient_resource["name"][0]["given"][0] if not i.isdigit())),
                'familyName': str(''.join(i for i in patient_resource["name"][0]["family"] if not i.isdigit())),
                'id': str(patient_resource["identifier"][1]["value"]),
                'homePhone': str(patient_resource["telecom"][0]["value"]),
                'state': str(patient_resource["address"][0]["state"]),
                'country': str(patient_resource["address"][0]["country"]),
                'jsonPatient': str(patient_resource )
    }

    return render(request, 'my_app/portal.html', context=fhir_var)

def variable_view(request):
    patient_resource = fhir.get_resource()
    fhir_var = {'jsonPatient': str(patient_resource )
    }
    return render(request, 'my_app/variable.html', context=fhir_var)
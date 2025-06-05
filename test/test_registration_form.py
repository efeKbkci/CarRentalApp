import pytest
from datetime import datetime
from model import RegistrationFormDTO, Priority

def test_registration_form_dict():
    form = RegistrationFormDTO("Efe", "Kabakcı", 
                               "efkanefekabakcii@gmail.com", 
                               datetime.strptime("24.04.2004", "%d.%m.%Y"), 
                               Priority.NORMAL_USER,
                               "test_12345")
    
    form_dict = form.convert_dict() 
    assert type(form_dict["id"]) is str
    assert type(form_dict["name"]) is str
    assert type(form_dict["surname"]) is str
    assert type(form_dict["birth_date"]) is datetime
    assert type(form_dict["password"]) is str
    assert type(form_dict["priority"].value) is int
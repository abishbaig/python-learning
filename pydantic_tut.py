from pydantic import BaseModel, Field, EmailStr,field_validator, model_validator, computed_field
from typing import Annotated,List,Optional,Dict

# ---------------------------------------------
# Simple Example of Patient Model
# ---------------------------------------------
# Type + Data Validations using Annotations & Field
# Field Validator -> Validates a Specific Field
# Model Validator -> Validates different Fields at once
# Computed Field -> Compute some Result with pre-exisiting fields
# Nested Models -> A model used as an Field for another model
# ---------------------------------------------
class Address(BaseModel):
    city: Annotated[str, Field(
        ...,
        title="City Name",
        max_length=100,
        description="Enter name of the city for address",
        strict=True,
    )]

    country: Annotated[str, Field(
        ...,
        title="Counry Name",
        max_length=100,
        description="Enter name of the country for address",
        strict=True,
    )]

    pin_code: Annotated[int, Field(
        ...,
        title="Pin Code",
        description="Enter pin code of relevant area",
        examples=[1124, 54090, 110124629],
        strict=True,
    )]

    @field_validator("pin_code")
    @classmethod
    def validate_pinCode(cls, value: int):
        digits = len(str(abs(value)))
        if 12 < digits < 4:
            raise ValueError("Pin Code Should be in range of 4-12 Digits Only")
        else:
            return value


class Patient(BaseModel):
    name: Annotated[str, Field(
        ..., # Shows it is a required field
        title="Name",
        max_length=50,
        description="Enter name of the Patient with Max 50 Characters Allowed",
        examples=["Abish","Ali"],
        strict=True, # Defines that the Type Validation should be strictly performed and don't try to auto convert it
        )]
    
    age: Annotated[int, Field(
        ...,
        title="Age",
        gt=0,
        description="Enter age of Patient which is not a negative value",
        strict=True,
    )]

    allergies: Annotated[Optional[List[str]], Field(
        default=None,
        title="Allergies List",
        max_length=3,
        description="Enter atmost 3 Allergies of a Patient",
    )]

    contacts: Annotated[Dict[str,int], Field(
        ...,
        title="Contacts List",
        description="Enter Patients Contact Info.",
        examples=["+92-XXX-XXXXXXX"],
    )]

    email: Annotated[EmailStr, Field(
        ...,
        title="Email",
        description="Enter email of a Patient",
    )]

    height: Annotated[float, Field(
        ...,
        title="Height",
        gt= 0.55,
        description="Enter Patient Height in meters",
    )]

    
    weight: Annotated[float, Field(
        ...,
        title="Weight",
        gt= 2.5,
        description="Enter Patient Weight in Kg",
    )]

    address: Annotated[Address, Field(
        ...,
        title="Address",
        description="Enter Address of Patient according to given Address Model Format",
        examples=[{"city":"Lahore","country":"Pakistan","pin_code":54126}],        
    )]

    # "after" -> Mode to Validate Field after Type Checking & Coversion 
    # "before" -> Mode to Validate Field before Type Checking & Coversion 
    @field_validator("email", mode="after")
    @classmethod
    def validate_email(cls, value: str):
        valid_domains = ["baig.com","baig.in"]
        current_domain = value.split("@")[-1]
        if current_domain in valid_domains:
            return value
        else:
            raise ValueError("Email is not Valid according to Company Requirements")    

    @field_validator("name")
    @classmethod
    def transform_name(cls, value: str):
        return value.upper()

    @model_validator(mode="after")
    @classmethod
    def check_emergency_contact(cls, model):
        if model.age > 60 and "emergency_contact" not in model.contacts:
            raise ValueError("Patients Above 60 should provide their Emergency Contact Number")
        return model
    
    '''
    Use @property for regular Python classes or when you don't need the value in serialization.
    Use @computed_field + @property in Pydantic models when you want the computed value to be part 
    of the model's output and schema.
    '''
    @computed_field
    @property
    def bmi(self) -> float:
        return ((self.weight)/(self.height**2))


# ---------------------------------------------

        
def insert_patient(patient: Patient):
    print("Patient Record Inserted....")
    print(patient)
    # print(patient.address.city)


# ---------------------------------------------
patient_address = {
    "city":"Lahore",
    "country":"Pakistan",
    "pin_code":54129,
}
a1 = Address(**patient_address)

patient_record = {
    "name":"xyz",
    "age":65,
    "allergies":["allerg1","allerg2","allerg3"],
    "contacts":{"contact":"12345678","emergency_contact":"456789"},
    "email":"xyz123@baig.com",
    "weight": 62,
    "height": 1.73,
    "address":a1,
}
p1 = Patient(**patient_record)


# insert_patient(p1)

# ---------------------------------------------
# Serialization of Models
# ---------------------------------------------
# include=[] -> List of Fields to be include while exporting Model
# exclude=[] -> List of Fields or Fields within Fields (in case of Nested Models) to be excluded while maintaing rest of fields while exporting
# exclude_unset = True -> For Excluding Fields which are not set during object creation
# ---------------------------------------------

temp1 = p1.model_dump(include=["name","age"])
# temp1 = p1.model_dump(exclude={"address":["city"]})
# temp1 = p1.model_dump(exclude_unset=True)
# print(temp1)
print(type(temp1))

temp2 = p1.model_dump_json()
# print(temp2)
print(type(temp2))


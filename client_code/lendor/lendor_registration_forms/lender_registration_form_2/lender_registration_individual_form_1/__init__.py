from ._anvil_designer import lender_registration_individual_form_1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import re

class lender_registration_individual_form_1(lender_registration_individual_form_1Template):
  def __init__(self,user_id, **properties):
    self.userId = user_id
    user_id = int(user_id)
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    user_data=app_tables.fin_user_profile.get(customer_id=user_id)
    if user_data:
      self.text_box_1.text=user_data['company_name']
      self.drop_down_3.selected_value = user_data['occupation_type']
      self.drop_down_1.selected_value=user_data['employment_type']
      self.drop_down_2.selected_value=user_data['organization_type']
      user_data.update()

    
    # user_data = anvil.server.call('get_user_data', user_id)
        
    # if user_data:
    #         self.company_name = user_data.get('company_name', '')
    #         self.org_type = user_data.get('organization_type', '')
    #         self.emp_type = user_data.get('employment_type', '')
    #         self.com_type = user_data.get('occupation_type', '')
            
            
    # else:
    #     self.company_name = ''
    #     self.org_type = ''
    #     self.emp_type = ''
    #     self.com_type = ''
        

    #    #Restore previously entered data if available
    # if self.emp_type:
    #         self.drop_down_1.selected_value = self.emp_type
    # if self.org_type:
    #         self.drop_down_2.selected_value = self.org_type
    # if self.company_name:
    #         self.text_box_1.text= self.company_name
    # if self.com_type:
    #         self.drop_down_3.selected_value = self.com_type

    options = app_tables.fin_lendor_employee_type.search()
    options_string = [str(option['lendor_employee_type']) for option in options]
    self.drop_down_1.items = options_string

    options = app_tables.fin_lendor_organization_type.search()
    options_string = [str(option['lendor_organization_type']) for option in options]
    self.drop_down_2.items = options_string

    options = app_tables.fin_occupation_type.search()
    option_strings = [str(option['occupation_type']) for option in options]
    self.drop_down_3.items = option_strings
    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):      
      company_name = self.text_box_1.text
      org_type = self.drop_down_2.selected_value
      emp_type = self.drop_down_1.selected_value
      occupation_type = self.drop_down_3.selected_value
      user_id = int(self.userId)
      if not re.match(r'^[A-Za-z\s]+$', company_name):
        alert('enter valid college name')
      elif not company_name or not org_type or not emp_type or not occupation_type:
          Notification("Please fill in all required fields.").show()  
      else:
          anvil.server.call('add_lendor_individual_form_1', company_name,org_type,emp_type,occupation_type,user_id)
          open_form('lendor.lendor_registration_forms.lender_registration_form_2.lender_registration_individual_form_2', user_id=self.userId)
    
  def button_1_click(self, **event_args):
     user_id = self.userId
     open_form('lendor.lendor_registration_forms.lender_registration_form_2',user_id=self.userId)

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("bank_users.user_form")


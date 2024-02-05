from ._anvil_designer import RowTemplate18Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class RowTemplate18(RowTemplate18Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    value_to_pass = self.label_1.text
    open_form('admin.dashboard.loan_management.lapsed_loans.view_profile_8', value_to_pass)

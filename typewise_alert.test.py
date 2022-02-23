import unittest
import typewise_alert
import random

global CoolingTypes
CoolingTypes = {
  'PASSIVE_COOLING' :[0,35],
  'HI_ACTIVE_COOLING' : [0,45],
  'MED_ACTIVE_COOLING' : [0,40]
  }

class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    global CoolingTypes
    for cooling_type in CoolingTypes.keys():
      batteryChar= dict()
      batteryChar['coolingType'] = cooling_type

      lower_limit, upper_limit = CoolingTypes[cooling_type]
      
      self.assertTrue(typewise_alert.classify_temperature_breach(cooling_type, lower_limit-1) == 'TOO_LOW')
      self.assertTrue(typewise_alert.classify_temperature_breach(cooling_type, upper_limit+1) == 'TOO_HIGH')
      self.assertTrue(typewise_alert.classify_temperature_breach(cooling_type, lower_limit) == 'NORMAL')
      self.assertTrue(typewise_alert.classify_temperature_breach(cooling_type, upper_limit) == 'NORMAL')
      self.assertTrue(typewise_alert.classify_temperature_breach(cooling_type, random.randrange(lower_limit, upper_limit)) == 'NORMAL')

      self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', batteryChar, random.randrange(lower_limit, upper_limit )))
      self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL', batteryChar, random.randrange(lower_limit, upper_limit)))
      self.assertTrue(typewise_alert.check_and_alert('TO_Somewhere', batteryChar, random.randrange(lower_limit, upper_limit)) == 'Not Valid')
      
unittest.main()

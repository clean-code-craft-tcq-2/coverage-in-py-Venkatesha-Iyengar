coolingTypes ={
    'PASSIVE_COOLING' : [0, 35],
    'HI_ACTIVE_COOLING' : [0, 45],
    'MED_ACTIVE_COOLING' : [0, 40],
    }

email_content = {
    'TOO_LOW' : 'Hi, the temperature is too low',
    'TOO_HIGH' : 'Hi, the temperature is too high',
    }

def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'

def define_temperature_breach_limits(coolingType):
    return (coolingTypes.get(coolingType, [0,0]))
  
def classify_temperature_breach(coolingType, temperatureInC):
  lowerLimit, upperLimit = define_temperature_breach_limits(coolingType)
  return infer_breach(temperatureInC, lowerLimit, upperLimit)

def alertTargets(alertTarget, breachType):
    return {
        'TO_CONTROLLER': lambda: send_to_controller(breachType),
        'TO_EMAIL': lambda: send_to_email(breachType),
    }.get(alertTarget,lambda: 'Not Valid')()

def check_and_alert(alertTarget, batteryChar, temperatureInC):
  flag_alerted = False
  breachType =\
    classify_temperature_breach(batteryChar['coolingType'], temperatureInC)
  flag_alerted = alertTargets(alertTarget, breachType)
  return flag_alerted

def send_to_controller(breachType):
  header = 0xfeed
  print(f'{header}, {breachType}')
  return True

def email_body(breachType, recepient):
    return f'To: {recepient} \n{email_content.get(breachType, "Invalid Breach Type")}'

def send_to_email(breachType):
  recepient = "a.b@c.com"
  print(email_body(breachType, recepient))
  return True

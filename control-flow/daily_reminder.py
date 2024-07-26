def main():
  """Prompts user for task, priority, and time sensitivity, then displays a reminder."""

  # Get user input for task
  task = input("Enter your task: ")

  # Get user input for priority
  while True:
    priority = input("Priority (high/medium/low): ").lower()
    if priority in ("high", "medium", "low"):
      break
    else:
      print("Invalid priority. Please enter high, medium, or low.")

  # Get user input for time sensitivity
  while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    if time_bound in ("yes", "no"):
      break
    else:
      print("Invalid response. Please enter yes or no.")

  # Build reminder message
  reminder = f"Reminder: '{task}' is a "
  urgency = ""
  
  # Match case for priority
  match priority:
    case "high":
      reminder += "high priority task"
      if time_bound == "yes":
        urgency = " that requires immediate attention today!"
    case "medium":
      reminder += "medium priority task"
    case "low":
      reminder += "low priority task"

  # Add urgency based on time sensitivity
  reminder += urgency

  # Print reminder message
  print(reminder)

if __name__ == "__main__":
  main()

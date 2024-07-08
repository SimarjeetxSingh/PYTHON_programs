print("Custom affirmations generator to give the user a customized affirmation each day of the week.")
print()
username=input("Enter your Name: ")
dow=input("The current day of the week: ")
if dow=="Monday" or dow=="monday":
  print("Hey! ",username,"Your affirmation for ",dow,"\nI embrace the new week with enthusiasm and positivity. I am ready to conquer challenges and create opportunities for success.")
  
elif dow=="Tuesday" or dow=="tuesday" :
  print("Hey! ",username,"Your affirmation for ",dow,"\nI am focused and determined to achieve my goals. I trust in my abilities and know that I can handle whatever comes my way.")

elif dow=="Wednesday" or dow=="wednesday" :
  print("Hey! ",username,"Your affirmation for ",dow,"\nI am halfway through the week, and I am proud of my progress. I continue to grow and learn, and I am open to new possibilities.")
  
elif dow=="Thursday" or dow=="thursday" :
  print("Hey! ",username,"Your affirmation for ",dow,"\nI am grateful for all that I have accomplished so far this week. I approach each task with diligence and dedication.")

elif dow=="Friday" or dow=="friday" :
  print("Hey! ",username,"Your affirmation for ",dow,"\nToday is a day of joy and celebration. I am proud of my accomplishments, and I look forward to a rewarding weekend.")

elif dow=="Saturday" or dow=="saturday" :
  print("Hey! ",username,"Your affirmation for ",dow,"\nI take time for myself today to relax and rejuvenate. I deserve this break and will make the most of it.")

elif dow=="Sunday" or dow=="sunday" :
  print("Hey! ",username,"Your affirmation for ",dow,"\nI reflect on the past week with gratitude and positivity. I am ready to start a new week with a refreshed mind and a hopeful heart.")
else:
  print("--- INVALID")
  

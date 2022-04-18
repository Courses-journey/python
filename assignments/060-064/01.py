def get_score(**subjects):
  for key,value in subjects.items():
    print(f"{key} => {value}")

get_score(Math=90, Science=80, Language=70)

get_score(Logic=70, Problems=60)
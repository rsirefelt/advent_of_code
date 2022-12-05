def parse_line(line):
  choice, response = line.split(" ")
  response = response.split("\n")[0]
  return choice, response

def remap_p1(response):
  if response == "X":
    return "A"
  elif response == "Y":
    return "B"
  else:
    return "C"

def remap_p2(response, choice):
  lose = {"A": "C", "B": "A", "C": "B"}
  win = {"A": "B", "B": "C", "C": "A"}
  if response == "X":
    return lose[choice]
  elif response == "Y":
    return choice
  else:
    return win[choice]

def score_points(choice, response):
    scores = {"A": 1, "B": 2, "C": 3}
    win_loss_scores = scores[response]
    if choice == response:
      win_loss_scores += 3
    else:
      if scores[response] > scores[choice]:
        win_loss_scores += 6
      if response == "C" and choice == "A":
        win_loss_scores -= 6
      if response == "A" and choice == "C":
        win_loss_scores += 6
    return win_loss_scores

total_points_p1 = 0
total_points_p2 = 0
with open("input.txt", "r") as f:
  lines = f.readlines()
  for line in lines:
    choice, response = parse_line(line)
    total_points_p1 += score_points(choice, remap_p1(response))
    total_points_p2 += score_points(choice, remap_p2(response, choice))
print(total_points_p1)
print(total_points_p2)

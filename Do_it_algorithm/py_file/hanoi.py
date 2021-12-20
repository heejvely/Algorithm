# 하노이의 탑 구현하기

def move(no: int, x: int, y: int) -> None:
  """원반 no개를 x기둥에서 y기둥으로 옮김"""
  if no > 1:
    move(no - 1, x, 6 - x - y)

  print(f'원반 [{no}]을(를) {x}기둥에서 {y}기둥으로 옮깁니다.')

  if no > 1:
    move(no - 1, 6 - x - y, y)
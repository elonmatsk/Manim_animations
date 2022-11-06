from manim import *
 
class SieveEratosthenes(Scene):
  def construct(self):
    text = Text("Решето Эратосфена").scale(1.5)
    self.play(Write(text))
    self.wait(2)
    self.play(text.animate.shift(3 * UP).scale(0.5))

    W = 7
    H = 7
    N = W * H
    numbers = [[0 for _ in range(W)] for _ in range(H)]
    for i in range(N):
      numbers[i // W][i % W] = i + 1

    isprime = [True for i in range(N)]

    table = IntegerTable(numbers, include_outer_lines=True).scale(0.5).shift(3 * RIGHT)
    self.play(DrawBorderThenFill(table))
    self.wait()

    text = Text('Зелёным цветов выделяем простые числа,\nкрасным — составные.\nСначала \"выбрасываем\" все числа, делящиеся на 2,\nпотом — на 3 и так далее...', 
                 t2c={'[:7]': GREEN, '[39:47]': RED}, width=5, height=5).shift(3.5 * LEFT)
    self.play(Write(text))
    highlight = table.get_highlighted_cell((-6, -6), color=YELLOW).scale(0.5)
    self.play(FadeIn(highlight, run_time=0.3))
    self.play(FadeOut(table.get_cell((-6, -6), color=YELLOW).scale(0.5)))
    for i in range(2, N + 1):

      if not isprime[i - 1]:
        continue
      row, col = (i - 1) // W + 1, (i - 1) % W + 1
      cur_cell = table.get_cell((row, col), color=YELLOW).scale(0.5)
      self.play(FadeIn(cur_cell, run_time=0.3))
      highlight = table.get_highlighted_cell((row,col), color=GREEN).scale(0.5)
      self.play(FadeIn(highlight))
      for j in range(i * 2, N + 1, i):
        row, col = (j - 1) // W + 1, (j - 1) % W + 1
        cell = table.get_cell((row, col), color=YELLOW).scale(0.5)
        self.play(ReplacementTransform(cur_cell, cell, run_time=0.7))
        cur_cell = cell
        if isprime[j - 1]:
          highlight = table.get_highlighted_cell((row, col), color=RED).scale(0.5)
          self.play(FadeIn(highlight, run_time=0.3))
        else:
          self.wait(0.3)
        isprime[j - 1] = False
      self.play(FadeOut(cur_cell))
    self.wait(5)
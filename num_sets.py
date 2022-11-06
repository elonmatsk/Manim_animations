from manim import *
import numpy as mp

class MovingAndZoomingCamera(MovingCameraScene):
     def construct(self):
        ellipse1 = Ellipse(
            width=3.0, height=2.0, fill_opacity=0.3, color=ORANGE, stroke_width=10
        ).move_to(LEFT)
        self.play(FadeIn(ellipse1))
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.set(width = ellipse1.width).move_to(LEFT))
        textN_cyrillic = Text("Натуральные числа").scale(0.3).move_to(LEFT)
        textN = Tex("$\mathbb N$").scale(1.5).move_to(LEFT)
        textN_examples = Tex("$1, 2, 3, 4, \dots$").scale(0.7).move_to(LEFT)
        self.play(Write(textN_cyrillic))
        self.play(textN_cyrillic.animate.scale(0.0))
        self.play(Write(textN_examples))
        self.wait(0.5)
        self.play(textN_examples.animate.scale(0.0))
        self.play(Write(textN))
        self.wait(0.5)
        self.play(Restore(self.camera.frame))
        
        ellipse2 = Ellipse(
            width=5, height=4, fill_opacity=0.3, color=BLUE, stroke_width=10
        ).move_to(LEFT*0.5)
        self.play(FadeIn(ellipse2))
        self.play(self.camera.frame.animate.set(width = ellipse2.width).move_to(LEFT*0.5 + UP))
        textZ_cyrillic = Text("Целые числа").scale(0.6).move_to(1.5*UP + LEFT*0.5)
        textZ = Tex("$\mathbb Z$").scale(1.5).move_to(UP + RIGHT)
        textZ_examples = Tex("$-2,-1, 0, 1, 2, \dots$").scale(0.7).move_to(1.5*UP + LEFT*0.5)
        self.play(Write(textZ_cyrillic))
        self.play(textZ_cyrillic.animate.scale(0.0))
        self.play(Write(textZ_examples))
        self.wait(0.5)
        self.play(textZ_examples.animate.scale(0.0))
        self.play(Restore(self.camera.frame))
        self.play(Write(textZ))
        self.wait(0.5)
        
        ellipse3 = Ellipse(
            width=8, height=7, fill_opacity=0.3, color=YELLOW, stroke_width=10
        )
        self.play(FadeIn(ellipse3))
        self.play(self.camera.frame.animate.set(width = ellipse3.width).move_to(LEFT*0.5 + UP*1.5))
        textQ_cyrillic = Text("Рациональные числа").scale(0.6).move_to(2.5*UP)
        textQ = Tex("$\mathbb Q$").scale(1.5).move_to(UP*2 + RIGHT*2)
        textQ_examples = Tex("$-{5 \over 6}, -{1\over {37}}, {10 \over{11}}, {4 \over 3}, 3{7\over 8}, \dots$").scale(0.7).move_to(2.5*UP + LEFT*0.5)
        self.play(Write(textQ_cyrillic))
        self.play(textQ_cyrillic.animate.scale(0.0))
        self.play(Write(textQ_examples))
        self.wait(0.5)
        self.play(textQ_examples.animate.scale(0.0))
        self.play(Restore(self.camera.frame))
        self.play(Write(textQ))
        self.wait(0.5)
        

        ellipseZNQ_group = Group(textZ, textN, textQ, ellipse1, ellipse2, ellipse3)
        self.play(ellipseZNQ_group.animate.scale(0.5))
        
        ellipse4 = Ellipse(
            width=8, height=7, fill_opacity=0.3, color=RED, stroke_width=10
        )
        self.play(FadeIn(ellipse4))
        self.play(self.camera.frame.animate.set(width = ellipse4.width).move_to(LEFT*0.5 + UP*1.5))
        textI_cyrillic = Text("Вещественные числа").scale(0.6).move_to(2.5*UP)
        textI = Tex("$\mathbb R$").scale(1.5).move_to(UP*2 + RIGHT*2)
        textI_examples = Tex("$0.8(9),\pi, e, \sqrt 2, -\sqrt 3, \dots$").scale(0.7).move_to(2.5*UP + LEFT*0.5)
        self.play(Write(textI_cyrillic))
        self.play(textI_cyrillic.animate.scale(0.0))
        self.play(Write(textI_examples))
        self.wait(0.5)
        self.play(textI_examples.animate.scale(0.0))
        self.play(Restore(self.camera.frame))
        self.play(Write(textI))
        self.wait(0.5)
        
        self.play(FadeIn(ellipse4))
        self.play(Write(textI))
        self.play(FadeIn(ellipse3))
        self.play(Write(textQ))
        self.play(FadeIn(ellipse2))
        self.play(Write(textZ))
        self.play(FadeIn(ellipse1))
        self.play(Write(textN))
        
        
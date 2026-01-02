from manim import *

class BetaComparison(Scene):
    def construct(self):
        # 1. Setup the Axes
        # x-axis: Position (0 to L)
        # y-axis: Temperature (0 to Ts)
        axes = Axes(
            x_range=[0, 1.2, 1],
            y_range=[0, 1.2, 1],
            x_length=6,
            y_length=6,
            axis_config={
                "include_numbers": False, 
                "include_tip": True,
            },
        )

        # 2. Add Labels (0, L, Ts)
        # Origin 0 label
        zero_label = MathTex("0").next_to(axes.c2p(0, 0), DOWN + LEFT, buff=0.1)

        # L label at x=1
        l_label = MathTex("L").next_to(axes.c2p(1, 0), DOWN)
        l_tick = Line(UP*0.1, DOWN*0.1).move_to(axes.c2p(1, 0))

        # Ts label at y=1
        t_label = MathTex("T_s").next_to(axes.c2p(0, 1), LEFT)
        t_tick = Line(LEFT*0.1, RIGHT*0.1).move_to(axes.c2p(0, 1))

        # Axis Titles
        x_axis_label = axes.get_x_axis_label("x")
        y_axis_label = axes.get_y_axis_label("T")

        # 3. Define the Physics Function
        # Boundary Conditions: T(0)=0, T(L)=Ts
        # Formula: x(t) = [ t + (beta/2)*t^2 ] / [ 1 + beta/2 ]
        def get_curve(beta, color):
            return axes.plot_parametric_curve(
                lambda t: [
                    ((t) + (beta / 2) * (t**2)) / (1 + (beta / 2)), # x-coord
                    t,                                              # y-coord
                    0
                ],
                t_range=[0, 1],
                color=color,
                stroke_width=6
            )

        # 4. Create the Curves
        # Beta = 0 (Linear 45 deg)
        curve_linear = get_curve(0, WHITE)
        label_linear = MathTex(r"\beta = 0").move_to(axes.c2p(0.5, 0.4))
        
        # Beta > 0 (Conductivity rises with T -> Gradient starts steep, gets shallow)
        # Curve bows UP (Concave down)
        curve_pos = get_curve(2, RED)
        label_pos = MathTex(r"\beta > 0").set_color(RED).move_to(axes.c2p(0.3, 0.7))

        # Beta < 0 (Conductivity drops with T -> Gradient starts shallow, gets steep)
        # Curve bows DOWN (Concave up)
        curve_neg = get_curve(-0.5, BLUE)
        label_neg = MathTex(r"\beta < 0").set_color(BLUE).move_to(axes.c2p(0.7, 0.3))

        # 5. Animation Sequence
        self.play(
            Create(axes), 
            Write(x_axis_label), 
            Write(y_axis_label),
            Write(zero_label)
        )
        self.play(Create(l_tick), Write(l_label), Create(t_tick), Write(t_label))
        
        self.wait(0.5)

        # Draw curves starting from 0,0
        self.play(
            Create(curve_linear),
            Create(curve_pos),
            Create(curve_neg),
            run_time=3
        )
        
        self.play(
            Write(label_linear),
            Write(label_pos),
            Write(label_neg)
        )
        
        self.wait(2)
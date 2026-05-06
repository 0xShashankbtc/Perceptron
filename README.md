## Perceptron Algorithm

**Input vectors** $x \in \mathbb{R}^2$

**Labels** $y \in \\{-1, +1\\}$

**Prediction:** $\hat{y} = \text{sgn}(w^\top x + b)$

**Update rule** (only on mistake):

$$w \leftarrow w + yx, \quad b \leftarrow b + y$$

## Dataset

| Point | $x$ | $y$ |
|-------|-----|-----|
| $(x_1, y_1)$ | $(1, 1)$ | $+1$ |
| $(x_2, y_2)$ | $(-1, -2)$ | $-1$ |
| $(x_3, y_3)$ | $(2, -1)$ | $-1$ |
| $(x_4, y_4)$ | $(0, 2)$ | $+1$ |



## Output

Initial parameters: w = [0. 0.] , b = 0.0
Point 1: x=[1, 1], y=+1  --> Correct (y_hat=1), no update
  No change --> w = [0.0, 0.0], b = 0.0

Point 2: x=[-1, -2], y=-1 --> MISTAKE (y_hat=1)
  UPDATE --> w = [1.0, 2.0], b = -1.0

Point 3: x=[2, -1], y=-1 --> Correct (y_hat=-1), no update
  No change --> w = [1.0, 2.0], b = -1.0

Point 4: x=[0, 2], y=+1  --> Correct (y_hat=1), no update
  No change --> w = [1.0, 2.0], b = -1.0


Final w = [1.0, 2.0], b = -1.0

Points that caused updates: [2]










## **Output Screenshot in Issues**

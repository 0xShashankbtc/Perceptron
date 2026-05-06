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

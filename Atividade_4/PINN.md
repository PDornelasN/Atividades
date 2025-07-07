# PINN for 1D Heat Equation

Here we are going to implement a Physics-Informed Neural Network (PINN) to solve the 1D heat equation. 
As we know, PINNs work to minimize the loss function of the data that it is given and also to minimize the loss function of the differential equation that it is trying to solve.

## Loss function 

The loss function for the PINN is given by:
$$\mathcal{L} = \mathcal{L}_{data} + \mathcal{L}_{pde}$$
where $\mathcal{L}_{data}$ is the loss function for the data and $\mathcal{L}_{pde}$ is the loss function for the PDE.

Now, in addiction to that there is a little hidden detail. as we have these two parameters for the loss function we also have to define the weights for each of them.

$
\begin{equation}
\mathcal{L} = \lambda_{data} \mathcal{L}_{data} + \lambda_{pde} \mathcal{L}_{pde}
\end{equation}
$

And here is where it gets tricky, because if the weights of the data dominate the training process, our NN will be really bad at predicting the solution of the PDE. 
We could try to manuyally adjust the weights, but obviously that is not a efficient way to do it.

Another way is to try to learn the weights during the training process.

## Learning the Weights

To learn the weights, we can use a logarithmic transformation of the weights.
$$\lambda_{data} = e^{l_{data}}$$
$$\lambda_{pde} = e^{l_{pde}}$$

This is to asures that the weights are always positive.

So now we can start playing with some candidates for the loss function. One try it is to just implement the loss function as it is on equation (1) and see how it goes.

It dos not work.

 Why? Because this does not prevent one of the weights to dominate the other one, and one fo them go to zero.

 ### Trying to prevent the weights to go to zero

 You thought it was already getting complicated? That's not even the beggining. 

 One try is simple, we can just add a regularization term to the loss function, that is going to penalize the weights if they go to zero.

$$\mathcal{L} = \lambda_{data} \mathcal{L}_{data} + \lambda_{pde} \mathcal{L}_{pde} + \alpha (l_{data}^2 + l_{pde}^2)$$

This option seems to work, but it also does not attend the broblem of the zeros, so we can instead of using the jsu tthe weights, we can use the logarithm of the weights. The logarithm will penalize the weights if they go to zero.

$$\mathcal{L} = \lambda_{data} \mathcal{L}_{data} + \lambda_{pde} \mathcal{L}_{pde} + ln(\lambda_{data})^2 + ln(\lambda_{pde})^2 + (\lambda_{data} - \lambda_{pde})^2$$

This aproach also has its problems, it forces wights to be close to one and to themselfs, and this is not always the correct awswer.

One more try is to not use the weights just as multipliers, but to use them as a uncertainty measure of the data and the PDE. 

$$\mathcal{L} = \frac{1}{2\sigma_{data}^2} \mathcal{L}_{data} + \frac{1}{2\sigma_{pde}^2} \mathcal{L}_{pde} + \sigma_{data}^2 + \sigma_{pde}^2$$

Some parts of the literature advocate for this approach, but it is not a universal solution.

## What to do now?

It seems that every solution you try to improve one aspect, can lead to problems in another aspect. There are many approaches to solve this in the literature, but none of them are universal. Furthermore, I didn't even got to some other chalenges like the optimizer, NN architecture, NN size and other aspects that can influence the training process.



import torch

N, D_in, H, D_out = 64, 2, 2, 1

# creat data set
x = torch.randn(N, D_in)
y = torch.randn(N, D_out)

# define model
model = torch.nn.Sequential(
    torch.nn.Linear(D_in, H),
    torch.nn.ReLU(),
    torch.nn.Linear(H, D_out)
)

# torch.nn.init.normal_(model[0].weight)
# torch.nn.init.normal_(model[1].weight)

# start neural network training
# using optimizer for updating weights
learning_rate = 1e-6
loss_fn = torch.nn.MSELoss(reduction='sum')
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

for it in range(500):
    # propagating forward
    y_pred = model(x)

    # calculate loss
    loss = loss_fn(y_pred, y)
    print(it, loss.item())

    # clear zero-gradient, then propagating backward
    optimizer.zero_grad()
    loss.backward()
    # update parameters
    optimizer.step()

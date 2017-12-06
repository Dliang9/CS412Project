# read files
D_tr = readcsv("mushrooms.csv")
header = D_tr[1, :]
data = D_tr[2:end, 2:23]
result = D_tr[2:end, 1]
# construct x and y for training and testing
n = size(data, 1)
for i = 1:22
    myarray = Array{String,1}()
    for j = 1:n
        if size(myarray) == 0
            push!(myarray, data[j,i])
        elseif data[j,i] in myarray
        else
            push!(myarray, data[j,i])
        end
        f(x) = x == data[j,i]
        temp = find(f,myarray)
        data[j,i] = temp[1] - 0.5
    end
end

for j = 1:n
    if result[j] == "e"
        result[j] = 1
    else
        result[j] = 0
    end
end
X_tr = data[1:4000, :]
y_tr = result[1:4000, :]
X_ts = data[4001:end, :]
y_ts = result[4001:end,:]



# number of training / testing samples
n_tr = size(X_tr, 1)
n_ts = size(X_ts, 1)

# add 1 as a feature
X_tr = [ones(n_tr, 1) X_tr]
X_ts = [ones(n_ts, 1) X_ts]

# perform gradient descent :: logistic regression
n_vars = size(X_tr, 2)              # number of variables
lr = 1e-2                           # learning rate
w = zeros(n_vars)                   # initialize parameter w
a = zeros(n_tr)                     # initialize exp(wx)/(1+exp(wx))
tolerance = 1e-2                    # tolerance for stopping criteria
eta = 1e-6

iter = 0                            # iteration counter
max_iter = 1000                     # maximum iteration
accuracy_ts = ones(1000)
accuracy_tr = ones(1000)
for i=1:n_tr

    a[i] += dot(w, X_tr[i,:])

    if (a[i] > 700)
        a[i] = 1
    elseif (a[i] < -50)
        a[i] = 0
    else
        a[i] = exp(a[i]) / (1 + exp(a[i]))
    end

end

iter = 0
while iter < 1000
  iter = iter + 1               # start iteration
  # calculate gradient
  grad = zeros(n_vars)          # initialize gradient
  for j=1:n_vars
      for i=1:n_tr
          grad[j] += y_tr[i] * X_tr[i,j] - X_tr[i,j] * a[i]
      end
      w[j] = w[j] + eta * grad[j];
  end

  for i=1:n_tr
      #m = a[i] + dot(w,X_tr[i,1:n_vars])
      a[i] += dot(w, X_tr[i,:])
      if (a[i] > 700)
          a[i] = 1
      elseif (a[i] < -50)
          a[i] = 0
      else
          a[i] = exp(a[i]) / (1 + exp(a[i]))
      end
  end

end
pred = zeros(n_ts)                  # initialize prediction vector
for i = 1:n_ts
  wx = dot(w,X_ts[i,:])
  if (wx > 700)
    p1 = 1
  elseif (wx < -50)
    p1 = 0
  else
    p1 = 1 / (1 + exp(wx))
  end
  if(p1 > 0.5)
    pred[i] = 1.0
  end
end
count = 0
for i = 1:n_ts
  if (pred[i] != y_ts[i])
      count = count +1
  end
end
print(count)
print(n_ts)

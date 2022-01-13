


running_loss=0
correct=0
total=0
eval_losses=[]
eval_accu=[]
costs = []
for epoch in range(num_epochs):
    for (words, labels) in train_loader:
        words = words.to(device)
        labels = labels.to(dtype=torch.long).to(device)
        
        # Forward pass
        outputs = model(words)
        loss = criterion(outputs, labels)

        # Backward 
        optimizer.zero_grad()
        loss.backward()
        #update weight
        optimizer.step()
        running_loss += loss.item()
     
        _, predicted = outputs.max(1)
        total += labels.size(0)
        correct += predicted.eq(labels).sum().item()
        train_loss=running_loss/len(train_loader)
        accu=100.*correct/total
    eval_losses.append(train_loss)
    eval_accu.append(accu)

  
    if (epoch+1) % 100 == 0:
        print (f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')
        costs.append(loss)

print(f'final loss: {loss.item():.4f}')
print(f'training complete.')

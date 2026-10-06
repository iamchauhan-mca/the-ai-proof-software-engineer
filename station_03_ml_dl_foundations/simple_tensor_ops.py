"""
Station 3: PyTorch Tensor Foundations & Automatic Differentiation
The AI-Proof Software Engineer - Vivek Chauhan
"""

import torch

def run_tensor_lab():
    print("=" * 60)
    print("🧠 STATION 3: RUNNING PYTORCH TENSOR & AUTOMATIC GRADIENT LAB")
    print("=" * 60)

    # 1. Verify Hardware Acceleration Layer (CPU vs GPU Core Frameworks)
    # As discussed in Chapter 4, GPUs run matrix operations up to 100x faster
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"🖥️ Execution Compute Layer Target: [{device.upper()}]")

    # 2. Replicate the Core Input Architecture (Page 19)
    # Creating a tensor mock-up representing a student's technical metrics
    # Shape: [1, 3] -> 1 sample containing 3 discrete evaluation nodes
    inputs = torch.tensor([[0.5, 1.2, -0.3]], dtype=torch.float32, device=device)
    print(f"\n📥 Mock Ingestion Input Tensor (x):\n   -> {inputs}")
    print(f"   -> Structural Dimension Shape: {inputs.shape}")

    # 3. Initialize Modifiable Training Weights with Gradient Tracking
    # Setting requires_grad=True commands PyTorch to map calculus pipelines for backprop
    weights = torch.tensor([[0.5, 0.8, -0.1]], dtype=torch.float32, device=device, requires_grad=True)
    bias = torch.tensor([0.1], dtype=torch.float32, device=device, requires_grad=True)
    
    print(f"\n🏋️ Weight Coefficients Matrix (w):\n   -> {weights}")
    print(f"➕ System Offset Adjuster (bias):\n   -> {bias}")

    # 4. Phase 1: The Forward Pass Pipeline (Page 20)
    # Mathematical Equation: output = Activation(Inputs @ Weights_Transposed + Bias)
    # Performing matrix multiplication (@) to compute raw linear summation
    linear_sum = torch.matmul(inputs, weights.t()) + bias
    
    # Applying the Non-Linear Filter (Rectified Linear Unit - ReLU)
    # As noted in Section 4.3, without activation, layers compress into basic flat equations
    prediction = torch.relu(linear_sum)
    
    print(f"\n🔮 Step 1 (Forward Pass Outcome):")
    print(f"   -> Raw Combined Summation: {linear_sum.item():.4f}")
    print(f"   -> ReLU Activated Prediction (ŷ): {prediction.item():.4f}")

    # 5. Phase 2: Compute Loss / Tracking Divergence (Page 20)
    # Supplying a static target label value to determine programmatic error variance
    true_label = torch.tensor([[1.0]], dtype=torch.float32, device=device)
    
    # Standard Mean Squared Error (MSE) calculation mechanics
    loss = torch.mean((prediction - true_label) ** 2)
    print(f"\n📊 Step 2 (Loss / Divergence Scale):")
    print(f"   -> Quantified Task Error: {loss.item():.4f}")

    # 6. Phase 3 & 4: Automatic Backward Pass & Gradient Tracking (Page 20, 0.1.22)
    # This call commands PyTorch to instantly handle multi-layer calculus derivations
    loss.backward()
    
    print(f"\n⚡ Step 3 & 4 (Backward Propagation Calculations):")
    print(f"   -> Computed Derivation on Weights (dw):\n      {weights.grad}")
    print(f"   -> Computed Derivation on System Bias (db):\n      {bias.grad}")

    # 7. Simulated Optimization Loop Execution
    # Standard learning rate step size adjustment matrix logic
    learning_rate = 0.01
    
    print(f"\n🔄 Simulating Optimization Update Step (Learning Rate: {learning_rate}):")
    with torch.no_grad(): # Isolate state tracking to safely update static layers
        updated_weights = weights - learning_rate * weights.grad
        updated_bias = bias - learning_rate * bias.grad
        print(f"   -> New Optimized Weights Array:\n      {updated_weights}")
        print(f"   -> New Optimized System Bias: {updated_bias.item():.4f}")
        
    print("\n" + "=" * 60)
    print("✅ PyTorch Core Gradient Verification Complete.")
    print("=" * 60)

if __name__ == "__main__":
    run_tensor_lab()

---
title: B03_LLM_Fine_tuning_Guide
---

# LLM Fine-tuning Guide

---

## Tutorial Overview

<details>
<summary>Comprehensive Guide for Fine-tuning Large Language Models</summary>

---

- **Purpose**: Provide a detailed tutorial for fine-tuning LLMs, integrated with A01 (AWS Data Platform) and A04b (AppsFlyer) for marketing analytics.
- **Scope**: Cover strategies, technical specs, implementation, optimization, and troubleshooting for real-world use cases.
- **Target Audience**: Data scientists, ML engineers, AI researchers, marketing teams.
- **Key Outcomes**: Master fine-tuning techniques, implement on AWS, and optimize for AppsFlyer data.

#### Learning Objectives

- **Fundamentals**: Understand full, parameter-efficient, and quantization-aware fine-tuning.
- **Technical Depth**: Master quantization, data prep, and optimization for AWS.
- **Practical Skills**: Fine-tune LLMs for AppsFlyer campaign analysis.
- **Troubleshooting**: Resolve issues in AWS and marketing data processing.

---

#### Tutorial Structure

- **Strategies**: Compare fine-tuning approaches.
- **Specifications**: Quantization, data, optimization techniques.
- **Implementation**: Step-by-step fine-tuning on SageMaker.
- **Optimization**: Improve efficiency and quality.
- **Troubleshooting**: Address AWS and data-specific issues.

---

</details>

---

## Fine-tuning Strategies

<details>
<summary>Comparison of Different Approaches</summary>

---

- **Full Fine-tuning**:
  - **Description**: Update all model parameters (e.g., GPT-2's 124M parameters).
  - **Advantages**: High accuracy for complex tasks (e.g., AppsFlyer event classification).
  - **Disadvantages**: High compute (~8 GPUs, $10/hour on SageMaker).
  - **Use Case**: Customizing LLMs for campaign sentiment analysis.
- **Parameter-efficient (LoRA)**:
  - **Description**: Train small adapter layers (~1% parameters).
  - **Advantages**: Low compute (~1 GPU, $1/hour), fast training.
  - **Disadvantages**: Slightly lower accuracy.
  - **Use Case**: Fine-tuning for AppsFlyer event summarization.
- **Prompt Tuning**:
  - **Description**: Learn task-specific prompts, freeze model.
  - **Advantages**: Minimal compute (~$0.10/hour on Lambda), quick setup.
  - **Disadvantages**: Limited to simple tasks.
  - **Use Case**: Quick campaign description generation.
- **Quantization-aware Training**:
  - **Description**: Train with INT8/FP16 weights for efficiency.
  - **Advantages**: Reduces memory (~50%), latency (~30%).
  - **Disadvantages**: Needs careful tuning to avoid accuracy loss.
  - **Use Case**: Deploying models on resource-constrained AWS instances.

#### Selection Criteria

- **Task Complexity**: Full fine-tuning for sentiment analysis; LoRA for summarization.
- **Resources**: LoRA/prompt tuning for limited GPUs; full fine-tuning on SageMaker.
- **Deployment**: Quantization-aware for low-latency inference (e.g., ECS).
- **A04b**: LoRA for AppsFlyer event processing due to cost-efficiency.

#### Benchmarks (AWS SageMaker)

- **Full Fine-tuning**: ~10 hours, $80, 92% accuracy on AppsFlyer event classification.
- **LoRA**: ~2 hours, $2, 90% accuracy.
- **Prompt Tuning**: ~30 minutes, $0.10, 85% accuracy.
- **Quantization-aware**: ~3 hours, $3, 89% accuracy, 50% less memory.

---

</details>

---

## Technical Specifications

<details>
<summary>Quantization Methods, Data Requirements, and Optimization Techniques</summary>

---

- **Quantization Methods**:
  - **Post-training**: Apply INT8 after training, reduces model size (~50%).
  - **Quantization-aware**: Train with INT8/FP16, maintains accuracy better.
- **Data Requirements**:
  - **Size**: ~10K-100K labeled AppsFlyer events (e.g., installs, purchases).
  - **Quality**: Clean, task-specific (e.g., campaign descriptions).
  - **Preprocessing**: Tokenize, remove noise (e.g., invalid events).
- **Optimization Techniques**:
  - Learning rate: Warm-up (0 to 5e-5), decay (cosine schedule).
  - Gradient clipping: Norm &lt;1.0 to prevent explosions.
  - Regularization: Dropout (0.1), weight decay (0.01).
- **A01 Integration**: Store data on S3/EFS, train on SageMaker, auth with FreeIPA.

#### Quantization Example (LoRA + INT8)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from peft import LoraConfig, get_peft_model
model = AutoModelForCausalLM.from_pretrained("gpt2")
tokenizer = AutoTokenizer.from_pretrained("gpt2")
lora_config = LoraConfig(r=8, lora_alpha=16, target_modules=["c_attn"])
model = get_peft_model(model, lora_config)
model = torch.quantization.quantize_dynamic(model, {torch.nn.Linear}, dtype=torch.qint8)
```

#### Data Preprocessing (AppsFlyer)

```python
import pandas as pd
from datasets import Dataset
def preprocess_appsflyer_data():
    s3 = boto3.client('s3')
    data = s3.get_object(Bucket='data-platform-raw', Key='appsflyer/events.csv')['Body']
    df = pd.read_csv(data)
    df = df[df['event_type'].isin(['install', 'purchase'])][['event_type', 'campaign_id', 'user_id']]
    return Dataset.from_pandas(df)
```

---

</details>

---

## Implementation Steps

<details>
<summary>Chronological Fine-tuning Procedures</summary>

---

1. **Prepare Environment**:
   - Install: `pip install transformers datasets torch peft boto3`.
   - AWS SageMaker: Setup notebook instance (`ml.p3.2xlarge`).
2. **Load Model**:
   - Use `AutoModelForCausalLM` for GPT-2.
3. **Prepare Data**:
   - Load AppsFlyer events from S3, tokenize.
4. **Define Arguments**:
   - Learning rate: 5e-5, batch size: 8, epochs: 3.
5. **Train**:
   - Use SageMaker `Trainer` with LoRA.
6. **Evaluate**:
   - Measure accuracy on validation set.
7. **Deploy**:
   - Save to S3, deploy on ECS for inference.

#### SageMaker Training

```python
from sagemaker.pytorch import PyTorch
estimator = PyTorch(
    entry_point="train.py",
    role="SageMakerRole",
    instance_type="ml.p3.2xlarge",
    framework_version="2.0",
    py_version="py39",
    source_dir="scripts",
    hyperparameters={"epochs": 3, "learning_rate": 5e-5}
)
estimator.fit({"train": "s3://data-platform-raw/appsflyer"})
```

#### train.py

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments
def main():
    model = AutoModelForCausalLM.from_pretrained("gpt2")
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    dataset = preprocess_appsflyer_data()
    training_args = TrainingArguments(
        output_dir="/opt/ml/model",
        num_train_epochs=3,
        per_device_train_batch_size=8,
        learning_rate=5e-5
    )
    trainer = Trainer(model=model, args=training_args, train_dataset=dataset)
    trainer.train()
    model.save_pretrained("/opt/ml/model")
```

---

</details>

---

## Performance Optimization

<details>
<summary>Efficiency and Quality Improvement Techniques</summary>

---

- **Gradient Accumulation**: Simulate large batches (effective batch size: 32).
- **Mixed Precision (FP16)**: Reduce memory and speed up training.
- **Distributed Training**: Use SageMaker multi-GPU.
- **LoRA**: Train only 1% parameters for efficiency.
- **A01 Integration**: Monitor with CloudWatch, store on S3/EFS.

#### Mixed Precision + LoRA

```python
from torch.cuda.amp import GradScaler, autocast
from peft import LoraConfig, get_peft_model
scaler = GradScaler()
model = get_peft_model(model, LoraConfig(r=8, lora_alpha=16))
for batch in train_dataloader:
    with autocast():
        outputs = model(**batch)
        loss = outputs.loss
    scaler.scale(loss).backward()
    scaler.step(optimizer)
    scaler.update()
```

#### Benchmark

```python
import time
def measure_training_time():
    start = time.time()
    trainer.train()
    latency = time.time() - start
    cloudwatch.put_metric_data(
        Namespace="FineTuning",
        MetricData=[{"MetricName": "TrainingTime", "Value": latency, "Unit": "Seconds"}]
    )
    return latency
```

---

</details>

---

## Troubleshooting Guide

<details>
<summary>Common Issues and Solutions</summary>

---

- **Overfitting**:
  - **Solution**: Add dropout (0.1), early stopping after 3 epochs.
  - ```python
    trainer = Trainer(args=TrainingArguments(early_stopping_patience=3))
    ```
- **Exploding Gradients**:
  - **Solution**: Clip norm &lt;1.0, reduce learning rate to 1e-5.
  - ```python
    torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
    ```
- **Slow Training**:
  - **Solution**: Use FP16, increase batch size on SageMaker.
- **AWS Errors**:
  - **Quota Exceeded**: `aws service-quotas request-service-quota-increase`.
  - **S3 Permissions**: Check IAM role `SageMakerRole`.
- **AppsFlyer Data**:
  - **Noisy Data**: Filter invalid events in preprocessing.
  - ```python
    df = df.dropna(subset=['event_type'])
    ```

#### Logging

```python
cloudwatch = boto3.client('cloudwatch')
def log_error(error):
    cloudwatch.put_log_events(
        logGroupName="/aws/sagemaker/finetuning",
        logStreamName="errors",
        logEvents=[{"timestamp": int(time.time() * 1000), "message": str(error)}]
    )
```

---

</details>

---

## Conclusion

<details>
<summary>Summary and Next Steps</summary>

---

- **Key Learnings**: Full, LoRA, and quantization-aware fine-tuning optimized for AppsFlyer data on AWS.
- **Next Steps**:
  - Deploy SageMaker training job (1 week).
  - Test with AppsFlyer events (1 week).
  - Train team via Confluence.
- **Cost**: ~$80 for full fine-tuning, $2 for LoRA on SageMaker.

---

</details>

---
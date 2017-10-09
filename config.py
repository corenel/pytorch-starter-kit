"""Config for project."""

import os

# general
project_name = "project"
root = os.path.abspath(os.path.expanduser("."))
log_root = os.path.join(root, "log")

# params for dataset and data loader
data_root = os.path.join(root, "data")
dataset_split = os.path.join(data_root, "dataset_split.pt")
init_dataset = True  # split train/val/test split and save
dataset_mean = [0.485, 0.456, 0.406]
dataset_std = [0.229, 0.224, 0.225]
image_size = (224, 224)
batch_size = 50
num_workers = 1

# special for Domain Adaption
# src_dataset = "MNIST"
# tgt_dataset = "USPS"

# params for models
model_root = os.path.join(root, "snapshots")
model_restore = os.path.join(model_root, "model.pt")

# params for training network
eval_only = False
num_gpu = 1
num_epochs = 20000
log_step = 100
val_step = 400
save_step = 5000
manual_seed = None

# params for optimizing models
learning_rate = 1e-2
lr_decay_factor = 0.1
lr_decay_epoch = 30
beta1 = 0.9
beta2 = 0.999

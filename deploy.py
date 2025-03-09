import sagemaker, boto3, json 
from sagemaker import Session

# Instead of get_execution_role(), specify the ARN directly or use instance profile
aws_role = "arn:aws:iam::533267358966:role/service-role/AmazonSageMaker-ExecutionRole-20250205T165756"
aws_region = "ap-northeast-1" 
sess = sagemaker.Session() 

model_id = "tensorflow-tc-bert-multi-cased-L-12-H-768-A-12-2" 
from sagemaker.jumpstart.estimator import JumpStartEstimator 

training_data_prefix = "training-datasets/SST/" 
training_dataset_s3_path = f"s3://sagemaker-automated-execution-533267358966-ap-northeast-1/{training_data_prefix}" 

estimator = JumpStartEstimator( 
    model_id=model_id, 
    hyperparameters={"epochs": "1", "batch_size": "64", "use_fp16": "True", "train_only_top_layer":"True"}, 
    instance_type= "ml.m5.4xlarge",
    role=aws_role
	)

estimator.fit({"training": training_dataset_s3_path}, logs=True) 
predictor = estimator.deploy(instance_type="ml.m5.xlarge", initial_instance_count=1)
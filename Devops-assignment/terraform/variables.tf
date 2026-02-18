variable "aws_region"     { default = "us-east-1" }
variable "app_name"       { default = "healthpay" }
variable "ecr_image_uri"  { description = "ECR or GHCR image URI" }
variable "image_tag"      { default = "latest" }
variable "allowed_origins"{ default = "*" }
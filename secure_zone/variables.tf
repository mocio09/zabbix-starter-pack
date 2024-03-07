variable "region" {
  description = "eu-west-2"
  default     = "eu-west-2"
}

variable "environment" {
  description = "The Deployment environment"
  default = "dev"
}

//Networking
variable "vpc_cidr" {
  description = "The CIDR block of the vpc"
  default = "10.0.0.0/16"
}

variable "public_subnets_cidr" {
  type        = list
  description = "The CIDR block for the public subnet"
  default = ["10.0.1.0/24"]
}

variable "private_subnets_cidr" {
  type        = list
  description = "The CIDR block for the private subnet"
  default = ["10.0.10.0/24"]
}

